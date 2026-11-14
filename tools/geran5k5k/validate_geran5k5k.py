"""Validate geometry, texture packing, portable source and exact HOI4 binding."""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import numpy as np
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent))
sys.path.insert(0,str(HERE.parent/'flamingo'))
from pdx_io import read
from validate_missile_models import check_model,block
from build_geran5k5k import make_geometry

EQUIPMENT='rus_guided_uav_geranium5k5_k'
EQUIPMENT_FILE='common/units/equipment/ES_rus_guided_uav_equipment.txt'


def ray_z(x,y,p,faces):
    a,b,c=np.transpose(p[faces],(1,0,2))
    e1,e2=b-a,c-a;det=e1[:,0]*e2[:,1]-e1[:,1]*e2[:,0]
    valid=np.abs(det)>1e-12
    a,e1,e2,det=a[valid],e1[valid],e2[valid],det[valid]
    u=((x-a[:,0])*e2[:,1]-(y-a[:,1])*e2[:,0])/det
    v=(e1[:,0]*(y-a[:,1])-e1[:,1]*(x-a[:,0]))/det
    keep=(u>=-1e-7)&(v>=-1e-7)&(u+v<=1+1e-7)
    return (a[:,2]+u*e1[:,2]+v*e2[:,2])[keep]


def main():
    check_model('geran5k5k',('geran5k5k.mesh','geran5k5k_idle.anim','rus_geran5k5k',3424,[EQUIPMENT]),
                equipment_files=(EQUIPMENT_FILE,),texture_size=1024)
    tree=read(ROOT/'gfx/models/units/missiles/geran5k5k/geran5k5k.mesh')
    assert len(tree.child('object').children)==1
    obj=tree.child('object').children[0]
    assert sum(c.name=='mesh' for c in obj.children)==1
    mesh=obj.child('mesh')
    p=np.array(mesh.get('p')).reshape(-1,3);faces=np.array(mesh.get('tri')).reshape(-1,3)
    uv=np.array(mesh.get('u0')).reshape(-1,2);t=np.array(mesh.get('ta')).reshape(-1,4)
    assert 1500<=len(faces)<=5000
    assert np.allclose(np.linalg.norm(t[:,:3],axis=1),1,atol=1e-5)
    assert set(t[:,3])<={-1.,1.}
    a,b=uv[faces[:,1]]-uv[faces[:,0]],uv[faces[:,2]]-uv[faces[:,0]]
    assert (np.abs(a[:,0]*b[:,1]-a[:,1]*b[:,0])>1e-10).all()
    g=make_geometry();parts=np.array(g.part)
    assert np.allclose(p[faces].reshape(-1,3),g.p,atol=1e-6)
    assert set(parts)=={'fuselage','main_right','main_left','tail_right','tail_left',
                       'tail_shoulder','nozzle_outer','nozzle_rim','nozzle_inner','nozzle_recess'}
    # Collapse only normal/UV seam duplicates. The result must be one watertight
    # oriented component, including all four fins and the recessed nozzle.
    positions,ids=np.unique(np.round(p,6),axis=0,return_inverse=True)
    welded=ids[faces];edges=defaultdict(list);adj=defaultdict(set)
    for face in welded:
        for a,b in zip(face,np.roll(face,-1)):
            edges[tuple(sorted((int(a),int(b))))].append((int(a),int(b)))
            adj[int(a)].add(int(b));adj[int(b)].add(int(a))
    assert all(len(e)==2 and e[0]==e[1][::-1] for e in edges.values()),'Open/nonmanifold edge'
    assert len(positions)-len(edges)+len(faces)==2
    reached={0};pending=[0]
    while pending:
        for vertex in adj[pending.pop()]-reached:
            reached.add(vertex);pending.append(vertex)
    assert len(reached)==len(positions),'Detached component'
    assert len({tuple(sorted(f)) for f in welded})==len(faces),'Duplicate face'
    volume=np.einsum('ij,ij->',p[faces[:,0]],np.cross(p[faces[:,1]],p[faces[:,2]]))/6
    assert volume>0
    for pair in ('main','tail'):
        right=np.unique(np.round(p[faces[parts==pair+'_right']].reshape(-1,3),6),axis=0)
        left=np.unique(np.round(p[faces[parts==pair+'_left']].reshape(-1,3),6),axis=0)
        right[:,0]*=-1
        assert {tuple(x) for x in right}=={tuple(x) for x in left},'Asymmetric fin'
    main_points=p[faces[np.char.startswith(parts,'main_')]].reshape(-1,3)
    main_surface=main_points[np.abs(main_points[:,0])>.2999]
    assert np.max(np.abs(main_surface[:,1]-.420))<.00801,'Main pair must be level at the top of the body'
    assert main_points[:,1].min()>.400,'Main roots must be on the upper shoulders'
    for side in ('right','left'):
        points=np.unique(p[faces[parts=='tail_'+side]].reshape(-1,3),axis=0)
        shoulder=points[np.isclose(np.abs(points[:,0]),.300)].mean(0)
        tip=points[np.isclose(np.abs(points[:,0]),1.130)].mean(0)
        assert np.isclose(shoulder[1],.455),'Tail must sit slightly higher than the main pair'
        elevation=np.degrees(np.arctan2(tip[1]-shoulder[1],abs(tip[0]-shoulder[0])))
        assert abs(elevation-3.0)<.01,'Tail must be almost level, with only a small upward rise'
    # Aperture rays reach a recessed back wall, whereas rim rays hit the rear lip.
    for x,y in [(0,0),(.07,0),(-.07,0),(0,.07),(0,-.07)]:
        assert np.isclose(ray_z(x,y,p,faces).max(),4.64)
    assert np.isclose(ray_z(.145,0,p,faces).max(),5)
    outer=p[faces[parts=='nozzle_outer']].reshape(-1,3)
    assert np.ptp(outer[:,2])<=.251
    tip=outer[np.isclose(outer[:,2],5)]
    start=outer[np.isclose(outer[:,2],4.75)]
    assert np.linalg.norm(tip[:,:2],axis=1).max()<np.linalg.norm(start[:,:2],axis=1).min()
    print('PASS: one closed connected surface, welded fin roots, paired swept fins, recessed open nozzle.')
    print('PASS: level top-mounted main pair; tail mounts 0.035 units higher, with a 3-degree rise.')
    manifest=json.loads((HERE/'manifest.json').read_text())
    assert manifest['triangles']==len(faces) and manifest['vertices']==len(p)
    source=(HERE/'geran5k5k.obj').read_text()
    assert source.count('\no ')==source.count('\ng ')==source.count('\nusemtl ')==1
    assert source.count('\nf ')==len(faces)
    for name in ('basecolor','normal','roughness','metallic'):
        assert Image.open(HERE/f'geran5k5k_{name}.png').size==(1024,1024)
    # Verify embedded GLB geometry and PNGs against the actual game/source data.
    glb=(HERE/'geran5k5k.glb').read_bytes()
    assert struct.unpack_from('<4sII',glb)==(b'glTF',2,len(glb))
    jslen,kind=struct.unpack_from('<I4s',glb,12);assert kind==b'JSON'
    doc=json.loads(glb[20:20+jslen]);start=28+jslen
    assert glb[start-4:start]==b'BIN\0'
    assert len(doc['meshes'])==len(doc['materials'])==len(doc['nodes'])==1
    primitive=doc['meshes'][0]['primitives'][0]
    for key,expected in [('POSITION',p),('NORMAL',np.array(mesh.get('n')).reshape(-1,3)),
                         ('TANGENT',t),('TEXCOORD_0',uv)]:
        accessor=doc['accessors'][primitive['attributes'][key]]
        view=doc['bufferViews'][accessor['bufferView']]
        data=np.frombuffer(glb,dtype='<f4',count=expected.size,offset=start+view['byteOffset'])
        assert np.allclose(data.reshape(expected.shape),expected)
    for im in doc['images']:
        view=doc['bufferViews'][im['bufferView']];offset=start+view['byteOffset']
        assert glb[offset:offset+8]==b'\x89PNG\r\n\x1a\n'
    baseline=json.loads((HERE/'baseline.json').read_text())
    for name,digest in baseline.items():
        data=(ROOT/name).read_bytes()
        if name==EQUIPMENT_FILE:
            text=data.decode('utf-8-sig');before=block(text,EQUIPMENT)
            assert 'sprite = rus_geran5k5k' in before
            after=before.replace('sprite = rus_geran5k5k','sprite = rus_geran5')
            restored=text.replace(before,after,1).encode('utf-8')
            if data.startswith(b'\xef\xbb\xbf'):restored=b'\xef\xbb\xbf'+restored
            data=restored
        assert hashlib.sha256(data).hexdigest()==digest,f'Unrelated edit: {name}'
    registrations='\n'.join(p.read_text(encoding='utf-8-sig',errors='replace')
                              for p in (ROOT/'gfx/entities').glob('*.gfx'))
    assert len(re.findall(r'\bname\s*=\s*"rus_geran5k5k_mesh"',registrations))==1
    print('PASS: 1024px PNG/PBR and DDS mip chains, OBJ and embedded GLB, unique entity/mesh registration.')
    print('PASS: only the Geran-5K5-K sprite changed; original Geran-5 and Zircon assets preserved.')


if __name__=='__main__':main()
