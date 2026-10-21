"""JASSM visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/jassm'
EQUIPMENT=('nto_medium_guided_missile_agm86', 'nto_medium_guided_missile_129', 'nto_medium_guided_missile_142', 'nto_medium_guided_missile_158', 'nto_medium_guided_missile_slam', 'nto_sea_guided_missile_equipment_seaeagle', 'nto_sea_guided_missile_equipment_seaskua', 'nto_sea_guided_missile_equipment_harpoon', 'nto_sea_guided_missile_equipment_agm158c', 'nto_sea_guided_missile_equipment_exocet', 'nto_sea_guided_missile_equipment_as15tt', 'nto_sea_guided_missile_equipment_rbs15')
COLORS=[(181, 191, 189), (195, 203, 200), (151, 164, 161), (48, 57, 58), (94, 111, 112), (32, 38, 37), (114, 127, 127), (176, 182, 177), (53, 103, 128), (83, 94, 92), (214, 218, 211), (17, 25, 27)]


def make_geometry():
    g=Geometry()
    # Faceted shoulder and broad flat underside; softened corners.
    def section(z,w,h,cy=0):
        shape=np.array([(1,.20),(.70,1),(-.70,1),(-1,.20),(-.84,-1),(.84,-1)])
        pts=[]
        for i,p in enumerate(shape):
            prev,nxt=shape[(i-1)%len(shape)],shape[(i+1)%len(shape)]
            a,b=p*.88+prev*.12,p*.88+nxt*.12
            for t in np.linspace(0,1,7):
                q=(1-t)**2*a+2*t*(1-t)*p+t*t*b
                pts.append([q[0]*w,cy+q[1]*h,z])
        return np.array(pts)
    stations=[(-4.3,.05,.09,-.03),(-4.2,.16,.15,-.02),(-4.04,.30,.22,0),
              (-3.8,.43,.29,0),(-3.5,.51,.36,0),(-3.2,.56,.39,0),
              (-2.8,.58,.4,0),(-2.2,.58,.4,0),(-1.4,.58,.4,0),
              (-.5,.58,.4,0),(.3,.57,.395,0),(1.1,.54,.38,0),
              (1.9,.49,.36,0),(2.5,.42,.33,0),(2.9,.35,.29,0),
              (3.2,.30,.26,0),(3.5,.255,.23,0),(3.65,.23,.21,0)]
    def loft(rings,tile,part):
        rings=np.array(rings)
        normals=np.zeros_like(rings)
        # Area-weighted shared vertex normals: smooth bevels, planar broad faces.
        for k in range(len(rings)-1):
            for i in range(rings.shape[1]):
                j=(i+1)%rings.shape[1]
                ids=[(k,i),(k,j),(k+1,j),(k+1,i)]
                pts=np.array([rings[t] for t in ids])
                n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
                center=(rings[k].mean(0)+rings[k+1].mean(0))/2
                if np.dot(n,pts.mean(0)-center)<0:n=-n
                for t in ids:normals[t]+=n
        normals/=np.linalg.norm(normals,axis=2)[:,:,None]
        for k in range(len(rings)-1):
            for i in range(rings.shape[1]):
                j=(i+1)%rings.shape[1]
                ids=[(k,i),(k,j),(k+1,j),(k+1,i)]
                color=tile(k) if callable(tile) else tile
                for tri in ((0,1,2),(0,2,3)):
                    g.triangle([rings[ids[t]] for t in tri],color,
                               [normals[ids[t]] for t in tri],part=part)
    rings=[section(*v) for v in stations]
    loft(rings,0,'faceted_fuselage')
    for ring,normal in ((rings[0],[0,0,-1]),(rings[-1],[0,0,1])):
        for i in range(1,len(ring)-1):g.triangle(ring[[0,i,i+1]],0,[normal]*3,part='body_cap')
    # Flush rectangular nose window on the lower forward face.
    g.quad([[-.085,-.173,-4.18],[.085,-.173,-4.18],
            [.15,-.253,-3.94],[-.15,-.253,-3.94]],11,[0,-1,-.4],'nose_window')
    us=(1-np.cos(np.linspace(0,math.pi,17)))/2
    thick=lambda u: .10*(.2969*np.sqrt(u)-.126*u-.3516*u*u+.2843*u**3-.1036*u**4)
    foil=[(thick(u),u) for u in us]+[(-thick(u),u) for u in us[-2:0:-1]]
    for side in (-1,1):
        wingrings=[np.array([[side*x,-.12+y,lead+u*chord] for y,u in foil])
                   for x,lead,chord in ((0,-.5,.70),(.52,-.5,.70),(1.5,-.27,.62),(2.65,0,.48),(2.72,.045,.40))]
        loft(wingrings,1,'deployed_wing')
        tip=wingrings[-1]
        for i in range(1,len(tip)-1):g.triangle(tip[[0,i,i+1]],1,[[side,0,0]]*3,part='wing_tip')
    # Single swept dorsal tail fin, matching the supplied display reference.
    g.prism([(.22,2.17),(.94,2.75),(.85,3.26),(.18,3.46)],-.035,.035,1,'vertical_tail')
    g.lathe([(3.60,.175),(3.69,.18),(3.73,.17)],6,segments=48,part='exhaust_lip')
    g.lathe([(3.73,.17),(3.66,.145),(3.61,.13)],11,segments=48,inward=True,part='exhaust_recess')
    for i in range(48):
        a,b=math.tau*i/48,math.tau*(i+1)/48
        g.triangle([[0,0,3.66],[.13*math.cos(a),.13*math.sin(a),3.66],
                    [.13*math.cos(b),.13*math.sin(b),3.66]],11,[[0,0,1]]*3,part='exhaust_shadow')
    # Compact belly fairing and dark intake mouth.
    g.prism([(-.32,-.08),(-.57,.18),(-.57,.65),(-.32,1.5)],-.28,.28,2,'belly_intake')
    g.quad([[-.24,-.34,-.055],[.24,-.34,-.055],[.24,-.55,.17],[-.24,-.55,.17]],11,[0,-.5,-1],'intake_opening')
    for z,width,tile in ((-2.8,.055,8),(-2.15,.013,4),(-1.4,.008,4)):
        left,right=section(z-width/2,.581,.401),section(z+width/2,.581,.401)
        for i in range(len(left)):
            j=(i+1)%len(left)
            g.quad([left[i],right[i],right[j],left[j]],tile,part='finish_band')
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
        im=Image.fromarray(pixels);path=OUT/f'jassm_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'jassm_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('jassm')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['jassm_diffuse.dds']),
             n=('s',['jassm_normal.dds']),spec=('s',['jassm_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,3.73]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'jassm.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'jassm_idle.anim').write_bytes(encode(anim))
    lines=['# JASSM game art; Y up, nose -Z; arbitrary art units.','mtllib jassm.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl jassm');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'jassm.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'jassm.mtl').write_text('newmtl jassm\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd jassm_diffuse.png\n',encoding='utf-8')
    print(f'JASSM: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
