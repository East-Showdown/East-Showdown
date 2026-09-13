"""Kh-69 visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/kh69'
EQUIPMENT=('rus_aircraft_guided_missile_equipment_kh69',)
COLORS=[(193,201,199),(205,211,207),(168,181,181),(39,47,53),
        (111,122,126),(32,38,37),(139,148,146),(176,182,177),
        (152,72,38),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    # Rounded rectangular sections; external art only, nose toward -Z.
    def section(z,w,h,cy=0):
        points=[]
        bevel=min(w,h)*.30
        for sx,sy,start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):
            for i in range(5):
                a=math.radians(start+i*22.5)
                points.append([sx*(w-bevel)+bevel*math.cos(a),
                               cy+sy*(h-bevel)+bevel*math.sin(a),z])
        return np.array(points)
    stations=[(-4.45,.06,.075,-.08),(-4.30,.22,.17,-.045),
              (-4.02,.36,.285,-.015),(-3.65,.43,.355,0),
              (-3.25,.45,.37,0),(-2.5,.45,.37,0),(-1.5,.45,.37,0),
              (-.5,.45,.37,0),(.5,.45,.37,0),(1.5,.445,.365,0),
              (2.35,.42,.34,0),(2.8,.37,.31,0),(3.35,.32,.285,0),(3.7,.29,.27,0)]
    rings=[section(*s) for s in stations]
    for left,right in zip(rings,rings[1:]):
        for i in range(len(left)):
            j=(i+1)%len(left)
            pts=np.array([left[i],left[j],right[j],right[i]])
            n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
            center=(left.mean(0)+right.mean(0))/2
            if np.dot(n,pts.mean(0)-center)<0:n=-n
            g.quad(pts,0,n,'faceted_fuselage')
    for ring,normal in ((rings[0],[0,0,-1]),(rings[-1],[0,0,1])):
        for i in range(1,len(ring)-1):
            g.triangle(ring[[0,i,i+1]],0,[normal]*3,part='body_cap')
    # Straight tapered wing pair with thin rounded profiles.
    foil=[(0,-.36),(.025,-.32),(.038,-.22),(.032,0),(.012,.22),(0,.32),
          (-.014,.22),(-.023,0),(-.023,-.22),(-.014,-.32)]
    for side in (-1,1):
        root=np.array([[side*.35,.29+y,z+.3] for y,z in foil])
        tip=np.array([[side*2.2,.29+y*.55,z*.6+.69] for y,z in foil])
        center=(root.mean(0)+tip.mean(0))/2
        for i in range(len(foil)):
            j=(i+1)%len(foil);p=np.array([root[i],tip[i],tip[j],root[j]])
            n=np.cross(p[1]-p[0],p[2]-p[0])
            if np.dot(n,p.mean(0)-center)<0:n=-n
            g.quad(p,1,n,'main_wing')
        for ring,sign in ((root,-side),(tip,side)):
            for i in range(1,len(ring)-1):
                g.triangle(ring[[0,i,i+1]],1,[[sign,0,0]]*3,part='wing_cap')
    for angle in (45,135,225,315):
        a=math.radians(angle);rad=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        outline=[(.29,2.9),(.88,3.23),(.96,3.56),(.34,3.51)]
        rings=[np.array([rad*r+[0,0,z]+normal*t for r,z in outline]) for t in (-.017,.017)]
        for ring,sign in zip(rings,(-1,1)):
            g.quad(ring,1,normal*sign,'tail_fin')
        for i in range(4):
            j=(i+1)%4
            g.quad([rings[0][i],rings[1][i],rings[1][j],rings[0][j]],2,part='tail_edge')
    g.lathe([(3.68,.215),(3.74,.22),(3.81,.203)],6,segments=48,part='exhaust_lip')
    g.lathe([(3.81,.203),(3.75,.173),(3.705,.16)],11,segments=48,inward=True,part='exhaust_recess')
    for i in range(48):
        a,b=math.tau*i/48,math.tau*(i+1)/48
        g.triangle([[0,0,3.702],[.17*math.cos(a),.17*math.sin(a),3.702],
                    [.17*math.cos(b),.17*math.sin(b),3.702]],11,[[0,0,1]]*3,part='exhaust_dark')
    # Dark upper nose window follows the sloping upper face.
    g.quad([[-.14,.272,-4.02],[.14,.272,-4.02],[.14,.343,-3.73],[-.14,.343,-3.73]],
           3,[0,1,-.3],'nose_window')
    for z in (-2.7,-2.64,-1.35,1.5):
        left,right=section(z-.006,.451,.371),section(z+.006,.451,.371)
        for i in range(len(left)):
            j=(i+1)%len(left)
            g.quad([left[i],right[i],right[j],left[j]],4,part='panel_seam')
    for side in (-1,1):
        x=side*.451
        for z0 in (-2.4,-.9,.85):
            for y0,y1 in ((-.19,-.183),(.15,.157)):
                g.quad([[x,y0,z0],[x,y1,z0],[x,y1,z0+.58],[x,y0,z0+.58]],4,[side,0,0],'panel_outline')
            for z in (z0,z0+.58):
                g.quad([[x,-.19,z],[x,.15,z],[x,.15,z+.007],[x,-.19,z+.007]],4,[side,0,0],'panel_outline')
        for z in (-2.34,-.84,.91):
            g.quad([[x,-.04,z],[x,.015,z],[x,.015,z+.08],[x,-.04,z+.08]],9,[side,0,0],'stencil')
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
        im=Image.fromarray(pixels);path=OUT/f'kh69_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'kh69_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('kh69')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['kh69_diffuse.dds']),
             n=('s',['kh69_normal.dds']),spec=('s',['kh69_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,3.81]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'kh69.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'kh69_idle.anim').write_bytes(encode(anim))
    lines=['# Kh-69 game art; Y up, nose -Z; arbitrary art units.','mtllib kh69.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl kh69');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'kh69.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'kh69.mtl').write_text('newmtl kh69\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd kh69_diffuse.png\n',encoding='utf-8')
    print(f'Kh-69: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
