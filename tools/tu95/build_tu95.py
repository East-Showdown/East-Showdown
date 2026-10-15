"""Original Tu-95MS game-art mesh from supplied photos; Y up, nose -Z.
Arbitrary art units, simplified external appearance only.
"""
from pathlib import Path
import sys, math
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent))
sys.path.insert(0,str(HERE.parent/'flamingo'))
sys.path.insert(0,str(HERE.parent/'shahed'))
from build import Geometry
from model_export import textures,export_rigid
from pdx_io import read,encode,Node
from render import render
OUT=ROOT/'gfx/models/units/planes/tu95'
COLORS=[(167,176,180),(199,203,200),(144,155,164),(31,47,55),
        (86,99,105),(41,43,42),(183,190,188),(156,45,40),
        (204,181,102),(102,114,119),(180,186,188),(69,77,78)]
PIVOTS=[]


def export(g):
    textures('tu95ms',OUT,HERE,COLORS)
    export_rigid(g,'tu95ms',OUT,HERE,(0,0,4.8))
    path=OUT/'tu95ms.mesh';root=read(path);obj=root.child('object').children[0]
    mesh=obj.child('mesh');skin=mesh.child('skin');indices=[]
    for part in g.part:
        bone=int(part.split('_')[1]) if part.startswith('prop_') else 0
        indices.extend([bone,-1,-1,-1]*3)
    skin.props['ix']=('i',indices)
    skeleton=obj.child('skeleton');identity=[1.,0.,0.,0.,1.,0.,0.,0.,1.]
    for i,pivot in enumerate(PIVOTS,1):skeleton.add(f'prop_{i}',ix=('i',[i]),pa=('i',[0]),tx=('f',identity+(-pivot).tolist()))
    # Bounds include all blade angles, not only the exported rest pose.
    p=np.array(g.p);lo=p.min(0);hi=p.max(0)
    for pivot in PIVOTS:lo=np.minimum(lo,pivot-[.73,.73,.02]);hi=np.maximum(hi,pivot+[.73,.73,.02])
    mesh.child('aabb').props=dict(min=('f',lo.tolist()),max=('f',hi.tolist()))
    path.write_bytes(encode(root))
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[31]),j=('i',[9]))
    info.add('root',sa=('s',['']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    for i,pivot in enumerate(PIVOTS,1):info.add(f'prop_{i}',sa=('s',['q']),t=('f',pivot.tolist()),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    samples=[]
    for frame in range(31):
        for i in range(8):
            a=math.tau*frame/30*(1 if i%2==0 else -1)
            samples.extend([0.,0.,math.sin(a/2),math.cos(a/2)])
    anim.add('samples',q=('f',samples));(OUT/'tu95ms_fly.anim').write_bytes(encode(anim))
    (OUT/'tu95ms_idle.anim').unlink()
    assert encode(read(path))==path.read_bytes()
    p=np.array(mesh.get('p')).reshape(-1,3);n=np.array(mesh.get('n')).reshape(-1,3)
    tri=np.array(mesh.get('tri')).reshape(-1,3);uv=np.array(mesh.get('u0'))
    assert 15000 <= len(tri) <= 20000
    assert np.isfinite(p).all() and uv.min()>=0 and uv.max()<=1
    assert np.allclose(np.linalg.norm(n,axis=1),1,atol=1e-5)
    assert (np.sum(np.cross(p[tri[:,1]]-p[tri[:,0]],p[tri[:,2]]-p[tri[:,0]])*n[tri[:,0]],axis=1)>0).all()
    assert set(indices)==set(range(9))|{-1} and len(indices)==len(p)*4
    q=np.array(samples).reshape(31,8,4);assert np.allclose(np.linalg.norm(q,axis=2),1)
    assert np.allclose(q[:,::2,2],-q[:,1::2,2])
    print(f'PASS: {len(tri)} triangles, 9 bones, 8 counter-rotating propellers, UVs/normals/winding/animation verified.')


if __name__=='__main__':
    from refined_geometry import make_geometry
    OUT.mkdir(parents=True,exist_ok=True);g=make_geometry(PIVOTS);export(g)
    model=OUT/'tu95ms.mesh'
    render((-9,7,-12),(1500,1000),'TU-95MS / TU-95MSM',model).save(HERE/'preview.png')
    from PIL import Image
    sheet=Image.new('RGB',(1600,1200))
    for i,(eye,label) in enumerate([((-9,7,-12),'THREE QUARTER'),((0,14,-.01),'TOP'),((-12,1,0),'SIDE'),((0,1,-14),'FRONT')]):
        sheet.paste(render(eye,(800,600),label,model),(i%2*800,i//2*600))
    sheet.save(HERE/'views.png')
