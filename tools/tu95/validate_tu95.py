"""Verify the revised exported asset, rig, symmetry and equipment bindings."""
from pathlib import Path
import sys,re,struct
import numpy as np
from PIL import Image
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent/'flamingo'))
from pdx_io import read,encode
BASE=ROOT/'gfx/models/units/planes/tu95'
r=read(BASE/'tu95ms.mesh');obj=r.child('object').children[0];m=obj.child('mesh')
assert encode(r)==(BASE/'tu95ms.mesh').read_bytes()
p=np.array(m.get('p')).reshape(-1,3);n=np.array(m.get('n')).reshape(-1,3)
tri=np.array(m.get('tri')).reshape(-1,3)
assert 15000<=len(tri)<=20000 and tri.min()==0 and tri.max()<len(p)
assert np.isfinite(p).all() and np.isfinite(n).all()
assert np.allclose(np.linalg.norm(n,axis=1),1,atol=1e-5)
points={tuple(v) for v in p.round(5)}
assert points=={(-x,y,z) for x,y,z in points},'Geometry is not symmetric'
area=np.linalg.norm(np.cross(p[tri[:,1]]-p[tri[:,0]],p[tri[:,2]]-p[tri[:,0]]),axis=1)
assert area.min()>1e-10
bones=obj.child('skeleton').children
weights=np.array(m.child('skin').get('w')).reshape(-1,4)
indices=np.array(m.child('skin').get('ix')).reshape(-1,4)
assert np.allclose(weights.sum(1),1) and set(indices[:,0])==set(range(9))
lo=np.array(m.child('aabb').get('min'));hi=np.array(m.child('aabb').get('max'))
anim=read(BASE/'tu95ms_fly.anim');info=anim.child('info')
assert [b.name for b in bones]==[b.name for b in info.children]
qs=np.array(anim.child('samples').get('q')).reshape(31,8,4)
assert np.allclose(np.linalg.norm(qs,axis=2),1)
assert np.allclose(abs((qs[0]*qs[-1]).sum(1)),1)
for i in range(1,9):
    pivot=np.array(info.children[i].get('t'))
    assert np.allclose(np.array(bones[i].get('tx'))[-3:],-pivot)
    local=p[indices[:,0]==i]-pivot
    for frame in range(31):
        q=qs[frame,i-1];a=2*np.arctan2(q[2],q[3]);c,s=np.cos(a),np.sin(a)
        rotated=local@np.array([[c,s,0],[-s,c,0],[0,0,1]])+pivot
        assert (rotated>=lo-1e-5).all() and (rotated<=hi+1e-5).all()
for key in ('diff','n','spec'):
    path=BASE/m.child('material').get(key)[0];raw=path.read_bytes()
    assert len(raw)==128+sum((512>>i)**2*4 for i in range(10))
    assert struct.unpack_from('<I',raw,28)[0]==10
    with Image.open(path) as im:im.load();assert im.size==(512,512)
s=(ROOT/'common/units/equipment/ES_planes_strat_bombers.txt').read_text()
targets=set(re.findall(r'(\w+)\s*=\s*\{\s*year\s*=\s*2022\s*sprite\s*=\s*rus_tu95',s))
assert targets=={'RUS_strat_bomber_equipment_tu95ms','RUS_strat_bomber_equipment_tu95msm'}
print(f'PASS: {len(tri)} triangles; bilateral symmetry; valid faces; 8 animated rotors within bounds; intact textures; both equipment bindings.')
