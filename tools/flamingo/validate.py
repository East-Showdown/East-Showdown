"""Check exported geometry, DDS mip chains, animation and equipment binding."""
from pathlib import Path
import re
import struct
import subprocess
import numpy as np
from PIL import Image
from pdx_io import read, encode

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'gfx/models/units/missiles/flamingo'


def validate():
    path=OUT/'flamingo.mesh';root=read(path)
    assert encode(root)==path.read_bytes()
    obj=root.child('object').children[0];mesh=obj.child('mesh')
    p=np.array(mesh.get('p')).reshape(-1,3)
    n=np.array(mesh.get('n')).reshape(-1,3)
    tangent=np.array(mesh.get('ta')).reshape(-1,4)
    uv=np.array(mesh.get('u0')).reshape(-1,2)
    faces=np.array(mesh.get('tri')).reshape(-1,3)
    assert p.shape==n.shape and len(uv)==len(p)==len(tangent)
    assert len(p)<65536 and len(faces)==3760
    assert all(np.isfinite(a).all() for a in (p,n,tangent,uv))
    assert (uv>=0).all() and (uv<=1).all()
    assert faces.min()>=0 and faces.max()<len(p)
    area=np.cross(p[faces[:,1]]-p[faces[:,0]],p[faces[:,2]]-p[faces[:,0]])
    assert (np.linalg.norm(area,axis=1)>1e-10).all()
    assert (np.sum(area*n[faces].mean(1),axis=1)>0).all(), 'Inverted faces'
    assert np.allclose(np.linalg.norm(n,axis=1),1,atol=1e-5)
    assert np.allclose(np.sum(n*tangent[:,:3],axis=1),0,atol=1e-5)
    assert np.allclose(p.min(0),mesh.child('aabb').get('min'))
    assert np.allclose(p.max(0),mesh.child('aabb').get('max'))
    weights=np.array(mesh.child('skin').get('w')).reshape(-1,4)
    indices=np.array(mesh.child('skin').get('ix')).reshape(-1,4)
    assert np.allclose(weights.sum(1),1) and (indices[weights>0]==0).all()
    assert [b.name for b in obj.child('skeleton').children]==['root']
    anim=read(OUT/'flamingo_idle.anim')
    assert [b.name for b in anim.child('info').children]==['root']
    assert len(anim.child('samples').get('q'))==4*anim.child('info').get('sa')[0]
    assert root.child('locator').child('engine_exhaust').get('pa')==['root']
    for key in ('diff','n','spec'):
        texture=OUT/mesh.child('material').get(key)[0]
        data=texture.read_bytes();assert data[:4]==b'DDS '
        assert Image.open(texture).size==(512,512)
        assert struct.unpack_from('<I',data,28)[0]==10
        assert len(data)==128+sum((512>>i)**2*4 for i in range(10))
    gfx=(ROOT/'gfx/entities/ukr_flamingo.gfx').read_text(encoding='utf-8-sig')
    asset=(ROOT/'gfx/entities/ukr_flamingo.asset').read_text(encoding='utf-8-sig')
    assert 'name = "ukr_flamingo_mesh"' in gfx and 'pdxmesh = "ukr_flamingo_mesh"' in asset
    assert 'name = "ukr_flamingo_entity"' in asset
    # Regression: an unresolved parent clone prevented entity registration in HOI4.
    active_asset = re.sub(r'#[^\n]*', '', asset)
    assert not re.search(r'\bclone\s*=', active_asset), 'Flamingo must not depend on the missing default missile entity'
    states = dict(re.findall(r'state\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s+animation\s*=\s*"([^"]+)"', active_asset))
    animation_ids = set(re.findall(r'\bid\s*=\s*"([^"]+)"', gfx))
    assert {'idle', 'launch', 'move', 'bomb', 'crash', 'explode'} <= states.keys()
    assert set(states.values()) <= animation_ids, 'Unbound entity animation'
    assert 'default_state = "idle"' in active_asset
    assert set(re.findall(r'next_state\s*=\s*"([^"]+)"', active_asset)) <= states.keys()
    assert 'name = "ukr_flamingo_pose_animation"' in (OUT/'flamingo_animations.asset').read_text(encoding='utf-8-sig')
    for text in (gfx,asset):assert text.count('{')==text.count('}')
    names={}
    for path in (ROOT/'gfx').rglob('*.asset'):
        for name in re.findall(r'name\s*=\s*"(ukr_flamingo[^\"]*)"',path.read_text(encoding='utf-8-sig',errors='replace')):
            names[name]=names.get(name,0)+1
    assert names=={'ukr_flamingo_entity':1,'ukr_flamingo_pose_animation':1}
    equipment=ROOT/'common/units/equipment/ES_guided_missiles.txt'
    text=equipment.read_bytes().replace(b'\r\n',b'\n')
    original=subprocess.check_output(['git','show','HEAD:common/units/equipment/ES_guided_missiles.txt'],cwd=ROOT).replace(b'\r\n',b'\n')
    start=original.index(b'\tukr_light_guided_missile_flamingo = {')
    end=original.index(b'\n\t}',start)
    expected=original[start:end].replace(b'sprite = missile_default',b'sprite = ukr_flamingo')
    current_start=text.index(b'\tukr_light_guided_missile_flamingo = {')
    current_end=text.index(b'\n\t}',current_start)
    assert text[current_start:current_end].replace(b'\r\n',b'\n')==expected.replace(b'\r\n',b'\n'), 'Flamingo equipment has changes beyond its sprite.'
    print('PASS: winding, tangents, UVs, skin, animation, DDS mipmaps, unique asset names and equipment references.')
    print('PASS: Flamingo equipment statistics preserved; other equipment is checked by its own validators.')


if __name__=='__main__':
    validate()
