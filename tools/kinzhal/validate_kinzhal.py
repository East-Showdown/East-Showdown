"""Validate the actual export, open rear recess and exact equipment registration."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from validate_missile_models import check_model, block
from pdx_io import read

EQUIPMENT_FILE = 'common/units/equipment/ES_rus_heavy_guided_missile_equipment.txt'
EQUIPMENT = 'rus_medium_guided_missile_kh47m2'
OUT = ROOT / 'gfx/models/units/missiles/kinzhal'


def rear_surface_at(x, y, p, faces):
    """Ray from behind the missile: return the first external surface's Z."""
    hits = []
    for ids in faces:
        a, b, c = p[ids]
        matrix = np.array([b[:2] - a[:2], c[:2] - a[:2]]).T
        if abs(np.linalg.det(matrix)) < 1e-12:
            continue
        u, v = np.linalg.solve(matrix, np.array([x, y]) - a[:2])
        if min(u, v) >= -1e-8 and u + v <= 1 + 1e-8:
            hits.append(a[2] + u * (b[2] - a[2]) + v * (c[2] - a[2]))
    assert hits
    return max(hits)


def main():
    check_model('kinzhal', ('kinzhal.mesh', 'kinzhal_idle.anim', 'rus_kinzhal', 10084, [EQUIPMENT]),
                equipment_files=(EQUIPMENT_FILE,), texture_size=1024)
    mesh = read(OUT / 'kinzhal.mesh').child('object').children[0].child('mesh')
    p = np.array(mesh.get('p')).reshape(-1, 3)
    faces = np.array(mesh.get('tri')).reshape(-1, 3)
    uv = np.array(mesh.get('u0')).reshape(-1, 2)
    tangents = np.array(mesh.get('ta')).reshape(-1, 4)
    assert 5000 <= len(faces) <= 15000
    assert len(p) == 6104 < len(faces)
    assert np.allclose(np.linalg.norm(tangents[:, :3], axis=1), 1, atol=1e-5)
    assert set(tangents[:, 3]) <= {-1., 1.}
    assert np.allclose((p.max(0) + p.min(0)) / 2, 0, atol=1e-6), 'Origin not centered'
    # No duplicate triangles, collapsed UVs, or flat sealed rear cap.
    keys = [tuple(sorted(tuple(v) for v in np.round(p[ids], 6))) for ids in faces]
    assert len(set(keys)) == len(keys)
    a = uv[faces[:, 1]] - uv[faces[:, 0]]
    b = uv[faces[:, 2]] - uv[faces[:, 0]]
    assert (np.abs(a[:, 0] * b[:, 1] - a[:, 1] * b[:, 0]) > 1e-10).all()
    assert abs(rear_surface_at(.01, .01, p, faces) - 4.22) < 1e-5
    assert abs(rear_surface_at(.355, .01, p, faces) - 5.0) < 1e-5
    assert 4.22 < rear_surface_at(.32, .01, p, faces) < 5.0
    # The large axial aperture stays unobstructed across its central cross-section.
    for x,y in ((.25,0),(-.25,0),(0,.25),(0,-.25)):
        assert abs(rear_surface_at(x,y,p,faces)-4.22)<1e-5
    manifest = json.loads((HERE / 'manifest.json').read_text())
    assert manifest['triangles'] == len(faces) and manifest['vertices'] == len(p)
    # Fin geometry is fourfold symmetric; small repeated details remain texture data.
    from build_kinzhal import make_geometry
    geometry = make_geometry()
    # New authorized scope includes aft-body taper and auxiliary-fin rotation.
    # Preserve the prior nozzle-only baseline as historical evidence; compare
    # this revision against the snapshot taken before the broader tail rework.
    baseline=json.loads((HERE/'tail_rework_baseline.json').read_text(encoding='utf-8'))
    parts=np.array(geometry.part)
    assert len(parts)==len(faces)
    arrays=[np.array(mesh.get(key),dtype='<f4').reshape(-1,width)
            for key,width in [('p',3),('n',3),('ta',4),('u0',2)]]
    for name,expected in baseline['protected_parts'].items():
        selected=faces[parts==name]
        assert len(selected)==expected['triangles'],f'{name}: topology changed'
        actual=hashlib.sha256(b''.join(a[selected].tobytes() for a in arrays)).hexdigest()
        assert actual==expected['sha256'],f'{name}: protected attributes changed'
    for name,cutoff,channels in [('front_body_attributes',3.55-1e-5,arrays),
                                  ('main_body_positions_uv',3.55+1e-5,[arrays[0],arrays[3]])]:
        selected=faces[(parts=='body_shell') & (arrays[0][faces][...,2].max(1)<cutoff)]
        expected=baseline[name]
        assert len(selected)==expected['triangles']
        actual=hashlib.sha256(b''.join(a[selected].tobytes() for a in channels)).hexdigest()
        assert actual==expected['sha256'],f'{name}: protected main body changed'
    for name,expected in baseline['unchanged_files'].items():
        data=(ROOT/name).read_bytes()
        if name==EQUIPMENT_FILE:
            # The later Zircon integration changes only its own sprite. Compare
            # the historical Kinzhal baseline after undoing that exact binding.
            data=data.replace(b'sprite = rus_zircon',b'sprite = missile_default')
        candidates=[data]
        if Path(name).suffix in ('.asset','.gfx','.txt'):
            # Git may check out text with CRLF; baselines contain both conventions.
            lf=data.replace(b'\r\n',b'\n')
            candidates.extend([lf,lf.replace(b'\n',b'\r\n')])
        assert any(hashlib.sha256(value).hexdigest()==expected for value in candidates),f'{name}: changed'
    rim=p[faces[parts=='nozzle_rim']].reshape(-1,3)
    mouth=rim[np.isclose(rim[:,2],5.)]
    radii=np.linalg.norm(mouth[:,:2],axis=1)
    assert np.all(np.isclose(radii,.340)|np.isclose(radii,.375))
    assert rim[:,2].min()>=4.975-1e-6 and np.linalg.norm(rim[:,:2],axis=1).max()<=.385001
    shell=p[faces[parts=='body_shell']].reshape(-1,3)
    z_values=np.unique(shell[:,2])
    radius_values=np.array([np.linalg.norm(shell[np.isclose(shell[:,2],z),:2],axis=1).mean()
                            for z in z_values])
    aft=radius_values[z_values>=3.55-1e-5]
    assert (np.diff(aft)<0).all(), 'Aft body does not taper continuously'
    assert np.isclose(aft[-1],.431) and np.isclose(aft[0],.56)
    # Small fins occupy diagonal radial planes, with their original tips and
    # thickness. Root edges coincide with the tapered polygonal body skin.
    auxiliary=np.unique(p[faces[parts=='auxiliary_fin']].reshape(-1,3),axis=0)
    angles=np.arctan2(auxiliary[:,1],auxiliary[:,0])
    centers=np.pi/4+np.round((angles-np.pi/4)/(np.pi/2))*np.pi/2
    assert len(set(np.round(centers%(2*np.pi),5)))==4
    radial=auxiliary[:,0]*np.cos(centers)+auxiliary[:,1]*np.sin(centers)
    lateral=-auxiliary[:,0]*np.sin(centers)+auxiliary[:,1]*np.cos(centers)
    assert np.allclose(np.abs(lateral),.016,atol=1e-6)
    assert np.isclose(radial.max(),.80)
    assert np.isclose(auxiliary[:,2].min(),4.05) and np.isclose(auxiliary[:,2].max(),4.86)
    roots=np.isclose(auxiliary[:,2],4.05)|np.isclose(auxiliary[:,2],4.86)
    skin=np.interp(auxiliary[roots,2],z_values,radius_values)
    assert np.allclose(radial[roots]+np.abs(lateral[roots])*np.tan(np.pi/96),skin,atol=1e-6)
    for name in ('main_fin', 'auxiliary_fin', 'fin_mount', 'mount_bridge'):
        indices = [i for i, part in enumerate(geometry.part) if part == name]
        points = np.array(geometry.p).reshape(-1, 3, 3)[indices].reshape(-1, 3)
        keys = set(map(tuple, np.round(points, 6)))
        rotated = np.column_stack((-points[:, 1], points[:, 0], points[:, 2]))
        assert keys == set(map(tuple, np.round(rotated, 6))), name
    for suffix in ('basecolor', 'roughness', 'metallic', 'normal'):
        im = Image.open(HERE / f'kinzhal_{suffix}.png')
        assert im.size == (1024, 1024)
    assert np.ptp(np.array(Image.open(HERE / 'kinzhal_normal.png'))[:, :, 0]) > 10
    assert 'norm kinzhal_normal.png' in (HERE / 'kinzhal.mtl').read_text()
    gfx = (ROOT / 'gfx/entities/rus_kinzhal.gfx').read_text()
    for path in re.findall(r'file\s*=\s*"([^"]+)"', gfx):
        assert (ROOT / path).is_file()
    all_gfx = '\n'.join(p.read_text(encoding='utf-8-sig', errors='replace')
                        for p in (ROOT / 'gfx').rglob('*.gfx'))
    assert len(re.findall(r'\bname\s*=\s*"rus_kinzhal_mesh"', all_gfx)) == 1
    text = (ROOT / EQUIPMENT_FILE).read_text(encoding='utf-8-sig')
    original = subprocess.check_output(['git', 'show', f'HEAD:{EQUIPMENT_FILE}'], cwd=ROOT)
    original = original.decode('utf-8-sig').replace('\r\n', '\n')
    before, after = block(original, EQUIPMENT), block(text, EQUIPMENT)
    # Works both before and after committing the integration.
    normalized = re.sub(r'\bsprite\s*=\s*\w+', 'sprite = rus_kinzhal', before)
    expected=original.replace(before,normalized,1)
    zircon=block(expected,'rus_medium_guided_missile_3m22')
    expected=expected.replace(zircon,re.sub(r'\bsprite\s*=\s*\w+','sprite = rus_zircon',zircon),1)
    assert text == expected, 'Unrelated equipment changed'
    assert 'sprite = rus_kinzhal' in after
    assert 'sprite = rus_zircon' in block(text, 'rus_medium_guided_missile_3m22')
    history = (ROOT / 'history/countries/RUS - Russia.txt').read_text(encoding='utf-8-sig')
    assert 'missile_rus_kh47 = 1' in history and f'type = {EQUIPMENT}' in history
    print('PASS: centered mesh, fourfold fins, open recessed nozzle, indexed vertices, PBR sources.')
    print('PASS: exact nose/main-body preservation, unchanged main fins/brackets/fairings and all textures.')
    print('PASS: continuous aft taper, compact centered nozzle, 45-degree staggered small fins with flush roots.')
    print('PASS: unique registration, researched Russian equipment and preserved Zircon sprite binding.')


if __name__ == '__main__':
    main()
