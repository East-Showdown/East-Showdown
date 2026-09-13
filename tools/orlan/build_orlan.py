"""Orlan visual game asset from the user's reference images; arbitrary art units."""
from pathlib import Path
import sys
import math
import struct
import numpy as np
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent/'flamingo'))
from build import Geometry
from pdx_io import Node,encode,read

OUT=ROOT/'gfx/models/units/missiles/orlan'
EQUIPMENT=('rus_guided_uav_gerbera','rus_guided_uav_bm35','rus_guided_uav_molniya','rus_guided_uav_molniya2')
COLORS=[(193,201,199),(205,211,207),(168,181,181),(39,47,53),
        (111,122,126),(32,38,37),(139,148,146),(176,182,177),
        (152,72,38),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    g.lathe([(-2.5,.10),(-2.45,.23),(-2.30,.30),(-2.0,.33),(-1.4,.34),
             (-.8,.32),(-.2,.28),(.35,.22),(1.,.15),(1.8,.10),(2.5,.06),(2.8,0)],
            0,segments=48,part='fuselage')
    # Continuous center sections meet at X=0 without internal end caps.
    # Main wing is seated into the fuselage along its entire root chord.
    def wing(stations,cy,name):
        foil=[(0,0),(.07,.65),(.2,1),(.45,.8),(.75,.4),(1,0),
              (.75,-.3),(.45,-.5),(.2,-.6),(.07,-.4)]
        for side in (-1,1):
            rings=[np.array([[side*x,cy+t*v,lead+u*(trail-lead)] for u,v in foil])
                   for x,lead,trail,t in stations]
            for left,right in zip(rings,rings[1:]):
                center=(left.mean(0)+right.mean(0))/2
                for i in range(len(foil)):
                    j=(i+1)%len(foil);p=np.array([left[i],right[i],right[j],left[j]])
                    n=np.cross(p[1]-p[0],p[2]-p[0])
                    if np.dot(n,p.mean(0)-center)<0:n=-n
                    g.quad(p,1,n,name)
            for ring,sign in ((rings[-1],side),):
                for i in range(1,len(ring)-1):
                    g.triangle(ring[[0,i,i+1]],1,[[sign,0,0]]*3,part=name+'_tip')
    wing([(0.,-1.12,-.12,.075),(1.25,-1.12,-.12,.065),
          (3.6,-1.04,-.20,.047),(4.35,-.99,-.29,.035),
          (4.52,-.89,-.42,.021),(4.57,-.75,-.58,.012)],.24,'main_wing')
    wing([(0.,1.85,2.68,.035),(1.10,1.95,2.62,.023),
          (1.3,2.05,2.54,.012),(1.35,2.17,2.4,.008)],.035,'tailplane')
    g.prism([(.045,1.1),(.16,1.5),(.78,2.05),(1.0,2.27),
             (1.02,2.48),(.08,2.72)],-.028,.028,1,'vertical_fin')
    g.lathe([(-2.73,0),(-2.70,.07),(-2.6,.115),(-2.48,.115)],6,segments=32,part='spinner')
    # Two separate curved blades with thickness, rotating about the nose.
    for side in (-1,1):
        outline=[(.08,-.025),(.23,-.065),(.55,-.10),(.80,-.06),
                 (.88,0),(.79,.045),(.48,.07),(.20,.035)]
        rings=[np.array([[side*r,side*y,-2.56+d+side*y*.2] for r,y in outline])
               for d in (-.012,.012)]
        for ring,sign in zip(rings,(-1,1)):
            for i in range(1,len(ring)-1):
                g.triangle(ring[[0,i,i+1]],3,[[0,0,sign]]*3,part='propeller')
        for i in range(len(outline)):
            j=(i+1)%len(outline)
            g.quad([rings[0][i],rings[1][i],rings[1][j],rings[0][j]],3,part='propeller')
    # Small underside sensor fairing, simplified for the game camera.
    g.lathe([(-1.98,0),(-1.90,.11),(-1.72,.12),(-1.6,0)],2,
            center=(0,-.28),segments=24,part='sensor_housing')
    for side in (-1,1):
        x=side*.326
        g.quad([[x,-.12,-2.16],[x,-.02,-2.16],[x,-.02,-2.03],[x,-.12,-2.03]],
               5,[side,0,0],'engine_vent')
        for z in (-1.5,-.25):
            g.quad([[x,-.08,z],[x,.08,z],[x,.08,z+.012],[x,-.08,z+.012]],
                   4,[side,0,0],'hatch_seam')
    for side in (-1,1):
        x=side*1.24
        g.quad([[x,.307,-1.05],[x+side*.05,.307,-1.05],
                [x+side*.05,.26,-.15],[x,.26,-.15]],2,[0,1,0],'wing_joint')
    return g


def textures():
    diffuse=np.zeros((512,512,4),dtype='uint8');diffuse[:,:,3]=255
    spec=np.full((512,512,4),[0,78,38,100],dtype='uint8')
    rng=np.random.default_rng(55)
    for i,color in enumerate(COLORS):
        x,y=i%4*128,i//4*128
        diffuse[y:y+128,x:x+128,:3]=np.clip(np.array(color)+rng.normal(0,.45,(128,128,1)),0,255)
        if i in (2,6,7):spec[y:y+128,x:x+128]=[0,126,115,135]
    for suffix,pixels in [('diffuse',diffuse),('normal',np.full((512,512,4),[128,128,0,128],dtype='uint8')),('specular',spec)]:
        im=Image.fromarray(pixels);path=OUT/f'orlan_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'orlan_diffuse.png')


def export(g):
    p,n,uv=np.array(g.p),np.array(g.n),np.array(g.uv);tangents=[]
    for i in range(0,len(p),3):
        e1,e2=p[i+1]-p[i],p[i+2]-p[i];a,b=uv[i+1]-uv[i],uv[i+2]-uv[i]
        det=a[0]*b[1]-a[1]*b[0]
        t=(e1*b[1]-e2*a[1])/det if abs(det)>1e-10 else e1
        bitangent=(-e1*b[0]+e2*a[0])/det if abs(det)>1e-10 else e2
        for normal in n[i:i+3]:
            tangent=t-normal*np.dot(normal,t)
            if np.linalg.norm(tangent)<1e-9:tangent=np.cross(normal,[1,0,0] if abs(normal[0])<.9 else [0,1,0])
            tangent/=np.linalg.norm(tangent)
            tangents.extend([*tangent,1. if np.dot(np.cross(normal,tangent),bitangent)>=0 else -1.])
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('orlan')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['orlan_diffuse.dds']),
             n=('s',['orlan_normal.dds']),spec=('s',['orlan_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    path=OUT/'orlan.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'orlan_idle.anim').write_bytes(encode(anim))
    lines=['# Orlan game art; Y up, nose -Z; arbitrary art units.','mtllib orlan.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl orlan');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'orlan.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'orlan.mtl').write_text('newmtl orlan\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd orlan_diffuse.png\n',encoding='utf-8')
    print(f'Orlan: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


def animate_propeller(g):
    path=OUT/'orlan.mesh'
    tree=read(path);obj=tree.child('object').children[0]
    mesh=obj.child('mesh')
    # Rebuild skin node with a dedicated rigid propeller bone.
    mesh.children=[c for c in mesh.children if c.name!='skin']
    indices=[]
    for part in g.part:
        indices.extend(([1 if part=='propeller' else 0,-1,-1,-1])*3)
    mesh.add('skin',bones=('i',[4]),ix=('i',indices),w=('f',[1.,0.,0.,0.]*len(g.p)))
    obj.child('skeleton').add('propeller',ix=('i',[1]),pa=('i',[0]),
        tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,2.56]))
    path.write_bytes(encode(tree))
    anim=Node('File',pdxasset=('i',[1,0]))
    info=anim.add('info',fps=('f',[30.]),sa=('i',[13]),j=('i',[2]))
    info.add('root',sa=('s',['']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    info.add('propeller',sa=('s',['q']),t=('f',[0.,0.,-2.56]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    samples=[]
    for i in range(13):
        a=math.tau*i/12
        samples.extend([0.,0.,math.sin(a/2),math.cos(a/2)])
    anim.add('samples',q=('f',samples))
    (OUT/'orlan_idle.anim').write_bytes(encode(anim))

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();g=make_geometry();export(g);animate_propeller(g)
