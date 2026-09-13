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
from build_shahed import surface
from model_export import textures,export_rigid
from pdx_io import read,encode,Node
from render import render
OUT=ROOT/'gfx/models/units/planes/tu95'
COLORS=[(167,176,180),(199,203,200),(144,155,164),(31,47,55),
        (86,99,105),(41,43,42),(183,190,188),(156,45,40),
        (204,181,102),(102,114,119),(180,186,188),(69,77,78)]
PIVOTS=[]


def wing(g,side,span,lead,tip_lead,chord,tip_chord,y,part):
    rows=[]
    for u in (0,.15,.36,.62,.82,1):
        x=side*(.22+(span-.22)*u)
        z=lead+(tip_lead-lead)*u;c=chord+(tip_chord-chord)*u
        rows.append([[x,y-.07*u+.11*(1-u)*math.sin(math.pi*t),z+c*t]
                     for t in (0,.07,.24,.5,.76,1)])
    surface(g,rows,0,1,part)
    lower=np.array(rows);lower[:,:,1]=2*(y-.07*np.array([0,.15,.36,.62,.82,1])[:,None])-lower[:,:,1]-.015
    surface(g,lower,2,-1,part)
    for j in range(5):g.quad([rows[-1][j],rows[-1][j+1],lower[-1,j+1],lower[-1,j]],2,part=part)


def blade(g,pivot,angle,part):
    radial=np.array([math.cos(angle),math.sin(angle),0.])
    tangent=np.array([-math.sin(angle),math.cos(angle),0.])
    outline=[(.08,-.05),(.34,-.07),(.65,-.10),(.71,-.04),(.68,.015),(.22,.06)]
    layers=[np.array([pivot+radial*r+tangent*t+[0,0,z] for r,t in outline]) for z in (-.012,.012)]
    for pts,normal in zip(layers,([0,0,-1],[0,0,1])):
        for j in range(1,len(pts)-1):g.triangle(pts[[0,j,j+1]],5,[normal]*3,part=part)
    for j in range(6):g.quad([layers[0][j],layers[0][(j+1)%6],layers[1][(j+1)%6],layers[1][j]],5,part=part)
    for z,normal in [(-.014,[0,0,-1]),(.014,[0,0,1])]:
        pts=[pivot+radial*r+tangent*t+[0,0,z] for r,t in [(.63,-.091),(.68,-.099),(.71,-.04),(.68,.015),(.63,.02)]]
        for j in range(1,4):g.triangle([pts[0],pts[j],pts[j+1]],8,[normal]*3,part=part)


def geometry():
    PIVOTS.clear();g=Geometry()
    g.lathe([(-5.05,.006),(-4.97,.12),(-4.77,.25),(-4.48,.32)],1,segments=32,part='radome')
    g.lathe([(-4.48,.32),(-4.13,.355),(-3.5,.37),(-1.9,.37),(0,.37),(1.7,.35),
             (2.7,.29),(3.8,.21),(4.5,.13),(4.85,.025)],0,segments=32,part='fuselage')
    g.lathe([(-5.44,.004),(-5.08,.018),(-4.96,.035)],4,center=(0,.14),segments=10,part='nose_probe')
    # Cockpit glazing follows the upper fuselage. Narrow separators stay silver.
    for side in (-1,1):
        g.quad([[side*.045,.335,-4.39],[side*.21,.27,-4.38],[side*.29,.255,-4.06],[side*.05,.376,-4.06]],3,[side*.4,1,-.25],'cockpit')
        g.quad([[side*.22,.263,-4.35],[side*.315,.183,-4.19],[side*.344,.176,-3.85],[side*.293,.269,-4.02]],3,[side,1,0],'cockpit')
        wing(g,side,5.35,-1.3,1.6,2.25,.48,-.035,'main_wing')
        wing(g,side,1.8,3.18,4.29,1.36,.38,.2,'tailplane')
    g.prism([(.14,3.10),(.38,3.15),(1.91,4.04),(2.0,4.53),(.23,4.65)],-.06,.06,0,'vertical_tail')
    # Red star markings on both sides of the fin, as in the supplied photos.
    for side in (-1,1):
        center=np.array([side*.061,1.3,4.19]);points=[]
        for j in range(10):
            a=math.pi/2+j*math.pi/5;r=.20 if j%2==0 else .085
            points.append(center+[0,r*math.sin(a),r*math.cos(a)])
        for j in range(10):g.triangle([center,points[j],points[(j+1)%10]],7,[[side,0,0]]*3,part='tail_marking')
    for side in (-1,1):
        for k,x in enumerate((1.48,3.08)):
            x*=side;front=-1.88+k*.75;cy=-.14
            g.lathe([(front,.11),(front+.17,.23),(front+.42,.255),(front+1.15,.24),
                     (front+1.75,.18),(front+2.20,.08),(front+2.38,.006)],0,center=(x,cy),segments=24,part='nacelle')
            g.lathe([(front+.33,.257),(front+.45,.257)],4,center=(x,cy),segments=24,part='engine_band')
            for layer in range(2):
                pivot=np.array([x,cy,front-.12-layer*.13]);PIVOTS.append(pivot)
                part=f'prop_{len(PIVOTS)}'
                for j in range(4):blade(g,pivot,j*math.pi/2+layer*math.pi/4+.12,part)
            g.lathe([(front-.39,.006),(front-.33,.085),(front-.12,.105),(front+.04,.11)],6,center=(x,cy),segments=20,part='spinner')
    # Retracted landing gear: only the characteristic inner nacelle fairings.
    for side in (-1,1):
        g.lathe([(.0,.03),(.35,.15),(1.0,.16),(1.65,.09),(1.95,.003)],2,center=(side*1.48,-.27),segments=16,part='gear_fairing')
    return g


def export(g):
    if not all((OUT/f'tu95ms_{s}.dds').exists() for s in ('diffuse','normal','specular')):
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
