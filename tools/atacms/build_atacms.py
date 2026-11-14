"""ATACMS visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/atacms'
EQUIPMENT=('nto_light_guided_missile_equipment_gmlrs', 'nto_ballistic_missile_equipment_atacams', 'nto_ballistic_missile_equipment_atacams_mod', 'nto_ballistic_missile_equipment_atacams_2', 'nto_ballistic_missile_equipment_atacams_2_mod')
COLORS=[(155, 151, 116), (172, 167, 133), (135, 133, 108), (47, 49, 45), (92, 94, 79), (32, 38, 37), (113, 116, 109), (176, 182, 177), (153, 148, 105), (83, 94, 92), (219, 218, 199), (20, 27, 27)]


def make_geometry():
    g=Geometry()
    # Smooth external silhouette in arbitrary game-art units, nose toward -Z.
    nose=[(-4.0,0),(-3.94,.045),(-3.8,.11),(-3.6,.19),(-3.35,.28),
          (-3.05,.375),(-2.7,.46),(-2.3,.535),(-1.9,.59),(-1.5,.625),(-1.1,.64)]
    g.lathe(nose,3,segments=64,part='ogive_radome')
    g.lathe([(-1.1,.64),(-.6,.64),(0,.64),(.8,.64),(1.6,.64),(2.3,.64),(3.2,.64),
             (3.6,.635),(3.75,.61)],0,segments=64,part='rear_body')
    g.lathe([(3.75,.61),(3.79,.60),(3.8,.48)],6,segments=64,part='nozzle_rim')
    g.lathe([(3.8,.48),(3.72,.43),(3.55,.39)],11,segments=64,inward=True,part='nozzle_recess')
    for i in range(64):
        a,b=math.tau*i/64,math.tau*(i+1)/64
        g.triangle([[0,0,3.55],[.39*math.cos(a),.39*math.sin(a),3.55],
                    [.39*math.cos(b),.39*math.sin(b),3.55]],11,[[0,0,1]]*3,part='nozzle_shadow')
    # Four thick, swept fins; buried roots ensure no floating components.
    for angle in (0,90,180,270):
        a=math.radians(angle);rad=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        outline=[(.57,2.22),(1.24,2.82),(1.36,3.37),(1.18,3.57),(.57,3.40)]
        rings=[np.array([rad*r+[0,0,z]+normal*t for r,z in outline]) for t in (-.025,.025)]
        for ring,sign in zip(rings,(-1,1)):
            for i in range(1,len(ring)-1):g.triangle(ring[[0,i,i+1]],1,[normal*sign]*3,part='tail_fin')
        for i in range(len(outline)):
            j=(i+1)%len(outline)
            g.quad([rings[0][i],rings[1][i],rings[1][j],rings[0][j]],1,part='fin_edge')
    for z in (-1.08,.35,2.35,3.53):
        g.lathe([(z-.008,.641),(z+.008,.641)],4,segments=64,part='body_seam')
    # Shallow dark dorsal strip as in the reference finish.
    for a0 in np.linspace(math.pi/2-.25,math.pi/2+.25,9)[:-1]:
        a1=a0+.0625
        g.quad([[.643*math.cos(a0),.643*math.sin(a0),-1.08],
                [.643*math.cos(a1),.643*math.sin(a1),-1.08],
                [.643*math.cos(a1),.643*math.sin(a1),3.2],
                [.643*math.cos(a0),.643*math.sin(a0),3.2]],3,part='dorsal_finish')
    for side in (-1,1):
        for z0 in (-.75,.75,2.5):
            for y0,y1 in ((-.14,-.132),(.132,.14)):
                x=side*math.sqrt(.644**2-y0*y0)
                g.quad([[x,y0,z0],[x,y1,z0],[x,y1,z0+.5],[x,y0,z0+.5]],4,[side,0,0],'panel_line')
            for z in (z0,z0+.5):
                g.quad([[side*.643,-.132,z],[side*.643,.132,z],[side*.643,.132,z+.008],[side*.643,-.132,z+.008]],4,[side,0,0],'panel_line')
        for z in (.05,.14,.23,1.6,1.69):
            g.quad([[side*.645,-.035,z],[side*.645,.035,z],[side*.645,.035,z+.04],[side*.645,-.035,z+.04]],10,[side,0,0],'small_stencil')
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
        im=Image.fromarray(pixels);path=OUT/f'atacms_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'atacms_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('atacms')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['atacms_diffuse.dds']),
             n=('s',['atacms_normal.dds']),spec=('s',['atacms_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,3.8]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'atacms.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'atacms_idle.anim').write_bytes(encode(anim))
    lines=['# ATACMS game art; Y up, nose -Z; arbitrary art units.','mtllib atacms.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl atacms');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'atacms.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'atacms.mtl').write_text('newmtl atacms\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd atacms_diffuse.png\n',encoding='utf-8')
    print(f'ATACMS: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
