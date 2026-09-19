"""Bober visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/bober'
EQUIPMENT=('ukr_guided_uav_bober','ukr_guided_uav_rubaka')
COLORS=[(129, 143, 146), (155, 165, 164), (107, 122, 126), (35, 40, 40), (91, 101, 103), (32, 38, 37), (151, 157, 153), (176, 182, 177), (166, 151, 95), (83, 94, 92), (214, 218, 211), (20, 27, 27)]


def make_geometry():
    sys.path.insert(0,str(HERE.parent/'tu95'))
    from refined_geometry import shell,PchipInterpolator
    g=Geometry()
    keys=np.array([[-3.25,.012,.025],[-3.1,.12,.12],[-2.8,.26,.23],[-2.3,.40,.34],
        [-1.6,.47,.40],[-.6,.48,.42],[.5,.47,.42],[1.5,.43,.38],[2.35,.35,.35],[2.65,.29,.32]])
    shape=PchipInterpolator(keys[:,0],keys[:,1:]);zs=np.unique(np.r_[np.linspace(-3.25,2.65,32),keys[:,0]])
    shell(g,[[[rx*math.cos(a),ry*math.sin(a),z] for a in np.arange(40)*math.tau/40]
             for z,(rx,ry) in zip(zs,shape(zs))],0,'fuselage')
    def wings(stations,name):
        for side in (-1,1):
            rows=[]
            for x,lead,c,y in stations:
                rows.append([[side*x,y+.055*c*math.sin(a)*(1-.45*(1-math.cos(a))/2),lead+c*(1-math.cos(a))/2]
                             for a in np.arange(24)*math.tau/24])
            shell(g,rows,0,name)
    wings([(x,.48+.25*x,1.72-.285*x,-.23) for x in np.linspace(0,3.8,9)],'main_wing')
    wings([(x,-2.97+.19*x,.77-.22*x,-.085) for x in np.linspace(0,1.62,6)],'canard')
    # Swept dorsal and ventral fins, with buried roots and a closed profile.
    for direction,span,lead,chord in ((1,.88,1.12,1.50),(-1,.72,1.68,.94)):
        rows=[]
        for u in np.linspace(0,1,8):
            c=chord*(1-.75*u);z=lead+.90*u
            rows.append([[.045*c*math.sin(a),direction*(.20+span*u),z+c*(1-math.cos(a))/2]
                         for a in np.arange(20)*math.tau/20])
        shell(g,rows,0,'dorsal_fin' if direction>0 else 'ventral_fin')
    g.lathe([(-3.58,.005),(-3.22,.012)],6,segments=12,part='nose_probe')
    # Simplified external engine casing and paired cylinder covers.
    g.lathe([(2.61,.20),(2.73,.22),(3.10,.19),(3.32,.10),(3.49,.07)],6,segments=32,part='engine_case')
    for side in (-1,1):
        cx=side*.24
        g.lathe([(2.73,.13),(2.80,.14),(3.10,.14),(3.16,.12)],6,center=(cx,.08),segments=20,part='cylinder_cover')
        for z in np.linspace(2.78,3.11,7):
            g.lathe([(z-.012,.147),(z+.012,.147)],4,center=(cx,.08),segments=16,part='cooling_rib')
        g.prism([(.13,2.8),(.59,2.8),(.59,2.88),(.13,2.88)],side*.24-.045,side*.24+.045,6,'exhaust_stub')
    # Two pitched blades, on a separate animated bone at the rear.
    for side in (-1,1):
        rows=[]
        for r,c in ((.055,.045),(.18,.12),(.40,.16),(.66,.13),(.86,.08),(.93,.018)):
            rows.append([[side*r,side*(.025*r+math.cos(a)*c/2),3.54+.32*math.cos(a)*c/2+.009*math.sin(a)]
                         for a in np.arange(10)*math.tau/10])
        shell(g,rows,3,'propeller')
    g.lathe([(3.45,.075),(3.57,.075),(3.63,.025)],6,segments=24,part='propeller_hub')
    # Fixed lightweight landing gear visible in the supplied references.
    def rod(p0,p1,r,tile,name):
        p0,p1=np.array(p0),np.array(p1);axis=p1-p0;axis/=np.linalg.norm(axis)
        v=np.cross(axis,[1,0,0] if abs(axis[0])<.9 else [0,1,0]);v/=np.linalg.norm(v);w=np.cross(axis,v)
        shell(g,[[p+r*(math.cos(a)*v+math.sin(a)*w) for a in np.arange(10)*math.tau/10] for p in (p0,p1)],tile,name)
    def wheel(cx,cy,cz):
        rows=[]
        for x,r in ((cx-.045,.115),(cx-.033,.15),(cx+.033,.15),(cx+.045,.115)):
            rows.append([[x,cy+r*math.cos(a),cz+r*math.sin(a)] for a in np.arange(20)*math.tau/20])
        shell(g,rows,3,'wheel')
        rod([cx-.05,cy,cz],[cx+.05,cy,cz],.058,6,'wheel_hub')
    rod([0,-.29,-1.74],[0,-.98,-1.66],.022,6,'nose_gear');wheel(0,-1.02,-1.66)
    for side in (-1,1):
        nodes=[[side*x,y,z] for x,y,z in ((.25,-.28,.83),(.48,-.47,.92),(.64,-.74,1.02),(.70,-1.01,1.06))]
        for a,b in zip(nodes,nodes[1:]):rod(a,b,.028,3,'main_gear')
        wheel(side*.70,-1.03,1.06)
    # Fine seams follow the actual body surface.
    for z in (-2.58,2.27):
        rx,ry=shape(z)
        for a in np.arange(40)*math.tau/40:
            g.quad([[(rx+.003)*math.cos(aa),(ry+.003)*math.sin(aa),zz] for zz,aa in
                    ((z-.004,a),(z+.004,a),(z+.004,a+math.tau/40),(z-.004,a+math.tau/40))],4,part='panel_seam')
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
        im=Image.fromarray(pixels);path=OUT/f'bober_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'bober_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('bober')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['bober_diffuse.dds']),
             n=('s',['bober_normal.dds']),spec=('s',['bober_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    path=OUT/'bober.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'bober_idle.anim').write_bytes(encode(anim))
    lines=['# Bober game art; Y up, nose -Z; arbitrary art units.','mtllib bober.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl bober');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'bober.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'bober.mtl').write_text('newmtl bober\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd bober_diffuse.png\n',encoding='utf-8')
    print(f'Bober: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


def animate_propeller(g):
    path=OUT/'bober.mesh'
    tree=read(path);obj=tree.child('object').children[0]
    mesh=obj.child('mesh')
    # Rebuild skin node with a dedicated rigid propeller bone.
    mesh.children=[c for c in mesh.children if c.name!='skin']
    indices=[]
    for part in g.part:
        indices.extend(([1 if part=='propeller' else 0,-1,-1,-1])*3)
    mesh.add('skin',bones=('i',[4]),ix=('i',indices),w=('f',[1.,0.,0.,0.]*len(g.p)))
    obj.child('skeleton').add('propeller',ix=('i',[1]),pa=('i',[0]),
        tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,-3.54]))
    path.write_bytes(encode(tree))
    anim=Node('File',pdxasset=('i',[1,0]))
    info=anim.add('info',fps=('f',[30.]),sa=('i',[13]),j=('i',[2]))
    info.add('root',sa=('s',['']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    info.add('propeller',sa=('s',['q']),t=('f',[0.,0.,3.54]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    samples=[]
    for i in range(13):
        a=math.tau*i/12
        samples.extend([0.,0.,math.sin(a/2),math.cos(a/2)])
    anim.add('samples',q=('f',samples))
    (OUT/'bober_idle.anim').write_bytes(encode(anim))

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();g=make_geometry();export(g);animate_propeller(g)
