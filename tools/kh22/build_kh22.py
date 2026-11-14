"""Kh-22 visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/kh22'
EQUIPMENT=('rus_light_guided_missile_kh22','rus_light_guided_missile_kh32')
COLORS=[(193,201,199),(205,211,207),(168,181,181),(39,47,53),
        (111,122,126),(32,38,37),(139,148,146),(176,182,177),
        (152,72,38),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    # Reference-driven external game geometry in arbitrary art units.
    g.lathe([(-5.3,0),(-5.12,.045),(-4.82,.12),(-4.48,.195),
             (-4.10,.255),(-3.72,.302),(-3.35,.328),(-3.10,.335)],3,segments=64,part='ogive_radome')
    g.lathe([(-3.10,.335),(-2.9,.337),(-2.3,.34),(-1.6,.34),
             (-.8,.34),(0,.34),(.9,.34),(1.8,.337),(2.5,.325),
             (3.1,.31),(3.8,.31),(4.35,.30),(4.5,.295)],0,segments=64,part='fuselage')
    # Biconvex thin wing sections, with a strongly swept leading edge.
    def surface(angle,stations,name,tile):
        a=math.radians(angle)
        radial=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        foil=[(0,0),(.12,.65),(.35,1),(.7,.6),(1,0),(.7,-.6),(.35,-1),(.12,-.65)]
        rings=[np.array([radial*r+[0,0,lead+u*(trail-lead)]+normal*v*thick
                         for u,v in foil]) for r,lead,trail,thick in stations]
        for left,right in zip(rings,rings[1:]):
            center=(left.mean(0)+right.mean(0))/2
            for i in range(len(foil)):
                j=(i+1)%len(foil)
                p=np.array([left[i],right[i],right[j],left[j]])
                n=np.cross(p[1]-p[0],p[2]-p[0])
                if np.dot(n,p.mean(0)-center)<0:n=-n
                g.quad(p,tile,n,name)
        for ring,n in ((rings[0],-radial),(rings[-1],radial)):
            for i in range(1,len(ring)-1):
                g.triangle(ring[[0,i,i+1]],tile,[n]*3,part=name+'_cap')
    for angle in (0,180):
        surface(angle,[(.28,-1.65,1.93,.042),(.85,-.22,1.98,.034),
                       (1.5,1.47,2.01,.018)],'swept_main_wing',1)
        surface(angle,[(.25,2.60,4.39,.036),(.95,3.72,4.39,.018),
                       (1.0,3.86,4.37,.009)],'tailplane',1)
    for angle in (90,270):
        surface(angle,[(.26,2.57,4.18,.037),(.99,3.70,4.2,.015),
                       (1.08,3.97,4.2,.008)],'vertical_tail',1)
    # Shallow underside fairing visible in the side reference.
    g.prism([(-.29,-1.3),(-.48,-.1),(-.40,1.65),(-.30,1.84)],
            -.13,.13,2,'ventral_fairing')
    # Tail plate with two dark recessed exhaust openings.
    for i in range(64):
        a,b=math.tau*i/64,math.tau*(i+1)/64
        g.triangle([[0,0,4.5],[.295*math.cos(a),.295*math.sin(a),4.5],
                    [.295*math.cos(b),.295*math.sin(b),4.5]],6,[[0,0,1]]*3,part='tail_plate')
    for cy,r in ((.115,.125),(-.15,.087)):
        g.lathe([(4.501,r),(4.55,r*1.08),(4.59,r)],6,center=(0,cy),segments=32,part='nozzle_lip')
        g.lathe([(4.59,r),(4.56,r*.83),(4.515,r*.72)],11,center=(0,cy),segments=32,inward=True,part='nozzle_recess')
        for i in range(32):
            a,b=math.tau*i/32,math.tau*(i+1)/32
            g.triangle([[0,cy,4.512],[r*.73*math.cos(a),cy+r*.73*math.sin(a),4.512],
                        [r*.73*math.cos(b),cy+r*.73*math.sin(b),4.512]],11,[[0,0,1]]*3,part='nozzle_dark')
    for z,r in ((-3.08,.337),(-2.42,.341),(-1.25,.341),(-.35,.341),
                (.8,.341),(1.6,.339),(2.5,.326),(3.85,.311)):
        g.lathe([(z-.009,r),(z+.009,r)],4,segments=64,part='panel_seam')
    for angle in (0,90,180,270):
        a=math.radians(angle);rad=np.array([math.cos(a),math.sin(a),0.])
        tang=np.array([-math.sin(a),math.cos(a),0.])
        for z in (-2.7,-1.8,.45,1.25):
            c=rad*.342+np.array([0,0,z])
            g.quad([c-tang*.025,c+tang*.025,c+tang*.025+[0,0,.05],
                    c-tang*.025+[0,0,.05]],9,rad,'service_stencil')
    for side in (-1,1):
        for z0 in (-2.35,-1.15,2.75):
            r=.341 if z0<2 else .313
            # Thin access cover outline sitting on the curved surface.
            for y in (-.075,.075):
                x=side*math.sqrt(r*r-y*y)
                g.quad([[x,y,z0],[x,y+.006,z0],[x,y+.006,z0+.36],[x,y,z0+.36]],
                       4,[side,0,0],'access_cover')
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
        im=Image.fromarray(pixels);path=OUT/f'kh22_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'kh22_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('kh22')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['kh22_diffuse.dds']),
             n=('s',['kh22_normal.dds']),spec=('s',['kh22_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,4.59]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'kh22.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'kh22_idle.anim').write_bytes(encode(anim))
    lines=['# Kh-22 game art; Y up, nose -Z; arbitrary art units.','mtllib kh22.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl kh22');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'kh22.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'kh22.mtl').write_text('newmtl kh22\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd kh22_diffuse.png\n',encoding='utf-8')
    print(f'Kh-22: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
