"""Validate missile game assets and their exact equipment assignments."""
from pathlib import Path
import sys
import re
import struct
import subprocess
import numpy as np
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools/flamingo'))
from pdx_io import read,encode

MODELS={
    'shahed': ('shahed136.mesh','shahed_fly.anim','rus_shahed',2736,
               ['rus_irn_guided_uav_shahed131','rus_guided_uav_shahed131','rus_guided_uav_geranium',
                'rus_guided_uav_geranium_m','rus_guided_uav_geranium3','rus_guided_uav_geranium4']),
    'geran5': ('geran5.mesh','geran5_idle.anim','rus_geran5',3304,['rus_guided_uav_geranium5']),
    'kh55': ('kh55.mesh','kh55_idle.anim','rus_kh55',3556,
             ['rus_medium_guided_missile_kh55','rus_medium_guided_missile_kh55cm',
              'rus_medium_guided_missile_kh555','rus_medium_guided_missile_kh101']),
}


def block(text,name):
    match=re.search(r'(?m)^\s*'+re.escape(name)+r'\s*=\s*\{',text)
    assert match,f'Missing equipment: {name}'
    start=match.start();pos=match.end();depth=1
    # Equipment blocks contain no quoted braces; strip line comments first.
    while depth:
        assert pos<len(text)
        depth+=(text[pos]=='{')-(text[pos]=='}');pos+=1
    return text[start:pos]


def check_model(folder,config):
    meshfile,animfile,sprite,triangles,equipment=config
    directory=ROOT/'gfx/models/units/missiles'/folder
    path=directory/meshfile;tree=read(path)
    assert encode(tree)==path.read_bytes()
    obj=tree.child('object').children[0];mesh=obj.child('mesh')
    p=np.array(mesh.get('p')).reshape(-1,3);n=np.array(mesh.get('n')).reshape(-1,3)
    uv=np.array(mesh.get('u0')).reshape(-1,2);t=np.array(mesh.get('ta')).reshape(-1,4)
    faces=np.array(mesh.get('tri')).reshape(-1,3)
    assert len(faces)==triangles and len(p)<65536
    assert len(p)==len(n)==len(uv)==len(t)
    assert all(np.isfinite(a).all() for a in (p,n,uv,t))
    assert faces.min()>=0 and faces.max()<len(p)
    area=np.cross(p[faces[:,1]]-p[faces[:,0]],p[faces[:,2]]-p[faces[:,0]])
    assert (np.linalg.norm(area,axis=1)>1e-10).all()
    assert (np.sum(area*n[faces].mean(1),axis=1)>0).all(),f'{folder}: inverted face'
    assert np.allclose(np.linalg.norm(n,axis=1),1,atol=1e-5)
    assert np.allclose(np.sum(n*t[:,:3],axis=1),0,atol=1e-5)
    assert (uv>=0).all() and (uv<=1).all()
    assert np.allclose(p.min(0),mesh.child('aabb').get('min'))
    assert np.allclose(p.max(0),mesh.child('aabb').get('max'))
    bones=obj.child('skeleton').children
    weights=np.array(mesh.child('skin').get('w')).reshape(-1,4)
    indices=np.array(mesh.child('skin').get('ix')).reshape(-1,4)
    assert len(weights)==len(p) and np.allclose(weights.sum(1),1)
    active=indices[weights>0];assert active.min()>=0 and active.max()<len(bones)
    animation=read(directory/animfile);info=animation.child('info')
    assert info.get('j')==[len(bones)]
    assert [b.name for b in bones]==[b.name for b in info.children]
    frame_count=info.get('sa')[0]
    tracks=[b for b in info.children if 'q' in b.get('sa')[0]]
    q=np.array(animation.child('samples').get('q')).reshape(frame_count,len(tracks),4)
    assert np.allclose(np.linalg.norm(q,axis=2),1,atol=1e-5)
    # Validate animated bone pivots against the inverse bind translation.
    for bone,pose in zip(bones,info.children):
        assert np.allclose(np.array(bone.get('tx')[-3:])+pose.get('t'),0)
    if folder=='shahed':
        assert len(bones)==2 and set(active)=={0,1}
        assert len(tracks)==1 and tracks[0].name=='propeller'
        assert np.allclose(q[0,0],[0,0,0,1]) and np.allclose(q[6,0],[0,0,2**-.5,2**-.5])
        prop=p[indices[:,0]==1];pivot=np.array(info.child('propeller').get('t'))
        assert np.ptp(prop[:,2])<.15
        relative=prop-pivot
        rotated=np.column_stack([-relative[:,1],relative[:,0],relative[:,2]])+pivot
        assert np.allclose(np.linalg.norm(prop-pivot,axis=1),np.linalg.norm(rotated-pivot,axis=1))
        assert np.max(np.abs(rotated-prop))>.5
    for name in ('diff','n','spec'):
        path=directory/mesh.child('material').get(name)[0];data=path.read_bytes()
        assert data[:4]==b'DDS ' and Image.open(path).size==(512,512)
        assert struct.unpack_from('<I',data,28)[0]==10
        assert len(data)==128+sum((512>>i)**2*4 for i in range(10))
    asset=(ROOT/f'gfx/entities/{sprite}.asset').read_text(encoding='utf-8-sig')
    gfx=(ROOT/f'gfx/entities/{sprite}.gfx').read_text(encoding='utf-8-sig')
    active_asset=re.sub(r'#[^\n]*','',asset)
    assert not re.search(r'\bclone\s*=',active_asset),'Missing default missile parent must not be reintroduced'
    assert f'name = "{sprite}_entity"' in asset and f'pdxmesh = "{sprite}_mesh"' in asset
    states=dict(re.findall(r'state\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s+animation\s*=\s*"([^"]+)"',asset))
    ids=set(re.findall(r'\bid\s*=\s*"([^"]+)"',gfx))
    assert set(states.values())<=ids and {'idle','launch','move','bomb'}<=states.keys()
    assert 'default_state = "idle"' in asset
    assert set(re.findall(r'next_state\s*=\s*"([^"]+)"',asset))<=states.keys()
    animations=(directory/f'{folder}_animations.asset').read_text(encoding='utf-8-sig')
    assert all(f'name = "{name}"' in animations for name in re.findall(r'\btype\s*=\s*"([^"]+)"',gfx))
    assert f'file = "{animfile}"' in animations
    for source in (asset,gfx,animations):assert source.count('{')==source.count('}')
    all_entities='\n'.join(path.read_text(encoding='utf-8-sig',errors='replace') for path in (ROOT/'gfx/entities').glob('*.asset'))
    assert len(re.findall(r'name\s*=\s*"'+sprite+r'_entity"',all_entities))==1
    text=(ROOT/'common/units/equipment/ES_guided_missiles.txt').read_text(encoding='utf-8-sig')
    technology=(ROOT/'common/technologies/missiles_rus.txt').read_text(encoding='utf-8-sig')
    for name in equipment:
        assert f'sprite = {sprite}' in block(text,name)
        assert re.search(r'\b'+re.escape(name)+r'\b',technology)
    print(f'PASS {folder}: {triangles} triangles, materials, states, {len(bones)} bones, animation and {len(equipment)} equipment bindings.')


if __name__=='__main__':
    for folder,config in MODELS.items():check_model(folder,config)
    text=(ROOT/'common/units/equipment/ES_guided_missiles.txt').read_text(encoding='utf-8-sig')
    original=subprocess.check_output(['git','show','HEAD:common/units/equipment/ES_guided_missiles.txt'],cwd=ROOT).decode('utf-8-sig').replace('\r\n','\n')
    expected=original
    for _,(_,_,sprite,_,equipment) in MODELS.items():
        for name in equipment:
            before=block(expected,name);after=re.sub(r'\bsprite\s*=\s*\w+',f'sprite = {sprite}',before)
            expected=expected.replace(before,after,1)
    assert text==expected,'Unexpected equipment changes outside the model sprite assignments'
    print('PASS: all other equipment fields and the previous Flamingo assignment preserved.')
