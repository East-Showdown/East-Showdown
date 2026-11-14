"""Validate the exported game mesh and the exact 3M22 equipment binding."""
from pathlib import Path
import json
import hashlib
import re
import subprocess
import sys

import numpy as np
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent))
sys.path.insert(0,str(HERE.parent/'flamingo'))
from validate_missile_models import check_model, block
from pdx_io import read
from build_zircon import make_geometry

EQUIPMENT='rus_medium_guided_missile_3m22'
EQUIPMENT_FILE='common/units/equipment/ES_rus_heavy_guided_missile_equipment.txt'
OUT=ROOT/'gfx/models/units/missiles/zircon'


def ray_z(x,y,positions,faces):
    """All mesh intersections of a ray parallel to the Z axis."""
    triangles=positions[faces]
    a,b,c=triangles[:,0],triangles[:,1],triangles[:,2]
    e1,e2=b-a,c-a
    det=e1[:,0]*e2[:,1]-e1[:,1]*e2[:,0]
    valid=np.abs(det)>1e-12
    a,e1,e2,det=a[valid],e1[valid],e2[valid],det[valid]
    u=((x-a[:,0])*e2[:,1]-(y-a[:,1])*e2[:,0])/det
    v=(e1[:,0]*(y-a[:,1])-e1[:,1]*(x-a[:,0]))/det
    inside=(u>=-1e-7)&(v>=-1e-7)&(u+v<=1+1e-7)
    return (a[:,2]+u*e1[:,2]+v*e2[:,2])[inside]


def main():
    manifest=json.loads((HERE/'manifest.json').read_text())
    check_model('zircon',('zircon.mesh','zircon_idle.anim','rus_zircon',2112,[EQUIPMENT]),
                equipment_files=(EQUIPMENT_FILE,),texture_size=1024)
    mesh=read(OUT/'zircon.mesh').child('object').children[0].child('mesh')
    p=np.array(mesh.get('p')).reshape(-1,3)
    n=np.array(mesh.get('n')).reshape(-1,3)
    faces=np.array(mesh.get('tri')).reshape(-1,3)
    uv=np.array(mesh.get('u0')).reshape(-1,2)
    tangents=np.array(mesh.get('ta')).reshape(-1,4)
    assert len(faces)==manifest['triangles'] and len(p)==manifest['vertices']
    assert len(p)<len(faces) and 1500<=len(faces)<=5000
    assert np.allclose(np.linalg.norm(tangents[:,:3],axis=1),1,atol=1e-5)
    assert set(tangents[:,3])<={-1.,1.}
    assert np.isclose(p[:,2].min(),-5) and np.isclose(p[:,2].max(),5)
    keys=[tuple(sorted(tuple(v) for v in np.round(p[f],6))) for f in faces]
    assert len(set(keys))==len(keys),'Duplicate faces'
    a,b=uv[faces[:,1]]-uv[faces[:,0]],uv[faces[:,2]]-uv[faces[:,0]]
    assert (np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])>1e-10).all(),'Collapsed UVs'
    # Compare against editable source geometry, independent of export vertex indexing.
    g=make_geometry();parts=np.array(g.part)
    assert len(parts)==len(faces)
    assert np.allclose(p[faces].reshape(-1,3),np.array(g.p),atol=1e-6)
    assert np.allclose(n[faces].reshape(-1,3),np.array(g.n),atol=1e-6)
    assert manifest['parts']=={name:g.part.count(name) for name in dict.fromkeys(g.part)}
    # Six evenly spaced aft planes, no missing/mirrored fin or accidental asymmetry.
    fin=p[faces[parts=='tail_fin']].reshape(-1,3)
    angle=np.pi/3
    rotated=np.column_stack([fin[:,0]*np.cos(angle)-fin[:,1]*np.sin(angle),
                             fin[:,0]*np.sin(angle)+fin[:,1]*np.cos(angle),fin[:,2]])
    # Float32 and rotation may differ by one final decimal; compare nearest vertices.
    unique=np.unique(fin,axis=0)
    assert all(np.min(np.linalg.norm(unique-v,axis=1))<2e-6 for v in rotated)
    # Rear aperture is recessed, not a flat dark disc at the outer lip.
    for x,y in ((0,0),(.15,0),(-.15,0),(0,.15),(0,-.15)):
        assert np.isclose(ray_z(x,y,p,faces).max(),4.64)
    assert np.isclose(ray_z(.254,0,p,faces).max(),5.)
    outer=p[faces[parts=='nozzle_outer']].reshape(-1,3)
    radii=np.linalg.norm(outer[:,:2],axis=1)
    assert radii.max()/radii.min()<1.03, 'External nozzle flares like a trumpet'
    assert np.ptp(outer[:,2])<=.281, 'External nozzle is too long'
    # Below the forebody, the intake mouth is open up to its recessed back wall.
    for x in (-.17,0,.17):
        hits=ray_z(x,-.35,p,faces)
        assert len(hits) and np.isclose(hits.min(),-1.56)
    # Broad planar surfaces have real longitudinal creases; the nose never uses
    # circular rings. No separate side-pocket meshes or loose surface ornaments.
    assert not {'collar_recess','collar_crossbar','tail_mount','fin_hinge'} & set(parts)
    front=p[faces[(parts=='body_shell') & (p[faces][:,:,2].max(1)<1.4)]].reshape(-1,3)
    assert np.ptp(front[:,0])>.78
    assert np.ptp(front[:,1])<.57
    # A real broad transverse edge, not a pointed apex hidden by smoothing.
    leading=p[np.isclose(p[:,2],-5,atol=1e-6,rtol=0)]
    assert np.ptp(leading[:,0])>.43, 'Leading edge has collapsed to a central point'
    nose=p[faces[parts=='nose_cap']].reshape(-1,3)
    assert np.ptp(nose[:,0])>.61 and np.ptp(nose[:,1])<.027
    assert np.ptp(nose[:,0])/np.ptp(front[:,0])>.77, 'Nose narrows too much in plan view'
    shell=p[faces[parts=='body_shell']].reshape(-1,3)
    nose_sections=[]
    for z in (-4.94,-4.68,-4.32,-3.90,-3.45,-3.02,-2.52):
        section=shell[np.isclose(shell[:,2],z,atol=1e-6,rtol=0)]
        nose_sections.append((section[:,1].min(),section[:,1].max(),np.ptp(section[:,0])))
    sections=np.array(nose_sections)
    assert np.ptp(sections[:,0])<.004, 'Nose underside is not nearly flat'
    assert (np.diff(sections[:,1])>0).all(), 'Nose thickness must progressively increase rearward'
    assert sections[0,2]/sections[-1,2]>.80
    # Limit this revision to the nose: preserve other geometry, rear-body
    # attributes, all materials and the existing HOI4 registrations exactly.
    baseline=json.loads((HERE/'nose_refinement_baseline.json').read_text())
    arrays=[np.array(mesh.get(key),dtype='<f4').reshape(-1,width)
            for key,width in [('p',3),('n',3),('ta',4),('u0',2)]]
    def check_preserved(selected,expected):
        assert len(selected)==expected['triangles']
        assert hashlib.sha256(b''.join(a[selected].tobytes() for a in arrays)).hexdigest()==expected['sha256']
    for name,expected in baseline['protected_parts'].items():
        check_preserved(faces[parts==name],expected)
    check_preserved(faces[(parts=='body_shell') & (p[faces][:,:,2].min(1)>=-1.1-1e-6)],baseline['rear_body'])
    for path,expected in baseline['unchanged_files'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected,path
    for part in ('tail_fin','forward_fin'):
        pts=p[faces[parts==part]].reshape(-1,3)
        angles=np.arctan2(pts[:,1],pts[:,0])
        axes=np.round(angles/(np.pi/3))*np.pi/3
        transverse=-pts[:,0]*np.sin(axes)+pts[:,1]*np.cos(axes)
        assert np.max(np.abs(transverse))<=.00601, 'Thick fin edge'
    obj=(HERE/'zircon.obj').read_text()
    assert obj.count('\no ')==1 and obj.count('\ng ')==1 and obj.count('\nusemtl ')==1
    for suffix in ('basecolor','normal','roughness','metallic'):
        assert Image.open(HERE/f'zircon_{suffix}.png').size==(1024,1024)
    # No black rectangular strips in the light skin beside the lower chine.
    albedo=np.array(Image.open(HERE/'zircon_basecolor.png'))
    from build_zircon import REGIONS
    x0,y0,x1,y1=REGIONS['body'];middle=(y0+y1)//2
    xa=int(x0+.15*(x1-x0));xb=int(x0+.60*(x1-x0))
    assert albedo[y0:y0+5,xa:xb].min()>150
    assert albedo[middle-6:middle-2,xa:xb].min()>150
    x0,y0,x1,y1=REGIONS['panel']
    assert albedo[y0:y1,x0:x1].max()<110,'Underside panels are too bright'
    assert np.ptp(np.array(Image.open(HERE/'zircon_normal.png'))[:,:,0])>8
    assert 'norm zircon_normal.png' in (HERE/'zircon.mtl').read_text()
    gfx=(ROOT/'gfx/entities/rus_zircon.gfx').read_text()
    for path in re.findall(r'file\s*=\s*"([^"]+)"',gfx):
        assert (ROOT/path).is_file()
    registrations='\n'.join(path.read_text(encoding='utf-8-sig',errors='replace')
                            for path in (ROOT/'gfx').rglob('*.gfx'))
    assert len(re.findall(r'\bname\s*=\s*"rus_zircon_mesh"',registrations))==1
    current=(ROOT/EQUIPMENT_FILE).read_text(encoding='utf-8-sig')
    original=subprocess.check_output(['git','show',f'HEAD:{EQUIPMENT_FILE}'],cwd=ROOT).decode('utf-8-sig').replace('\r\n','\n')
    before=block(original,EQUIPMENT)
    expected=re.sub(r'\bsprite\s*=\s*\w+','sprite = rus_zircon',before)
    assert current==original.replace(before,expected,1),'Unrelated equipment fields changed'
    assert 'sprite = rus_kinzhal' in block(current,'rus_medium_guided_missile_kh47m2')
    print('PASS: up to 5000 triangles, single OBJ object/material, wedge silhouette and thin swept fins.')
    print('PASS: short cylindrical nozzle with geometric depth, recessed inlet, no separate pocket or mounting meshes.')
    print('PASS: continuous light-skin boundary and muted underside metal without gold strips.')
    print('PASS: broad transverse leading edge, gently tapering width, progressive thickness and nearly flat underside.')
    print('PASS: exact preservation of fins, intake, nozzle, rear body, textures and equipment registrations.')
    print('PASS: 1024px PBR sources, DDS mip chains, unique mesh registration and only 3M22 sprite changed.')


if __name__=='__main__':
    main()
