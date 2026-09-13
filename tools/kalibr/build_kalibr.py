"""Kalibr visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/kalibr'
EQUIPMENT=('rus_medium_guided_missile_kalibr',)
COLORS=[(193,201,199),(205,211,207),(168,181,181),(39,47,53),
        (111,122,126),(32,38,37),(139,148,146),(176,182,177),
        (152,72,38),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    # External visual model in art units, nose toward -Z.
    g.lathe([(-4.5,0),(-4.48,.09),(-4.41,.19),(-4.30,.28),
             (-4.16,.35),(-4.00,.386),(-3.85,.40)],3,segments=64,part='dark_radome')
    g.lathe([(-3.85,.40),(-3.4,.40),(-2.7,.40),(-1.8,.40),
             (-.8,.40),(.2,.40),(1.1,.40),(2.0,.397),(2.55,.38)],0,segments=64,part='fuselage')
    g.lathe([(2.55,.38),(2.8,.35),(3.1,.295),(3.35,.25),
             (3.7,.25),(4.0,.25)],1,segments=48,part='tail_fairing')
    g.lathe([(4.0,.25),(4.04,.27),(4.22,.27),(4.26,.25)],6,segments=48,part='exhaust_rim')
    g.lathe([(4.26,.25),(4.22,.21),(4.02,.19)],11,segments=48,inward=True,part='exhaust_recess')
    for i in range(48):
        a,b=math.tau*i/48,math.tau*(i+1)/48
        g.triangle([[0,0,4.01],[.19*math.cos(a),.19*math.sin(a),4.01],
                    [.19*math.cos(b),.19*math.sin(b),4.01]],11,[[0,0,1]]*3,part='exhaust_dark')
    foil=[(0,-.44),(.025,-.42),(.045,-.34),(.048,-.20),
          (.035,.0),(.012,.21),(0,.29),(-.015,.20),(-.028,0),(-.029,-.25),(-.016,-.40)]
    for side in (-1,1):
        rings=[]
        for span,sweep,taper in ((.32,0,1),(1.62,.11,.91),(1.94,.14,.82)):
            rings.append(np.array([[side*span,y*taper,z*taper+sweep] for y,z in foil]))
        for left,right in zip(rings,rings[1:]):
            center=(left.mean(0)+right.mean(0))/2
            for i in range(len(foil)):
                j=(i+1)%len(foil)
                pts=np.array([left[i],right[i],right[j],left[j]])
                n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
                if np.dot(n,pts.mean(0)-center)<0:n=-n
                g.quad(pts,1,n,'deployed_wing')
        for ring,sign in ((rings[0],-side),(rings[-1],side)):
            for i in range(1,len(ring)-1):
                g.triangle(ring[[0,i,i+1]],1,[[sign,0,0]]*3,part='wing_tip')
    for angle in (0,90,180,270):
        a=math.radians(angle);rad=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        outline=[(.24,3.15),(.66,3.30),(.69,3.72),(.60,3.81),(.24,3.72)]
        rings=[np.array([rad*r+[0,0,z]+normal*d for r,z in outline]) for d in (-.015,.015)]
        for ring,sign in zip(rings,(-1,1)):
            for i in range(1,len(ring)-1):
                g.triangle(ring[[0,i,i+1]],2,[normal*sign]*3,part='tail_fin')
        for i in range(len(outline)):
            j=(i+1)%len(outline)
            g.quad([rings[0][i],rings[1][i],rings[1][j],rings[0][j]],2,part='tail_edge')
    # Shallow ventral intake, visible from the lower reference view.
    g.prism([(-.34,1.55),(-.52,1.66),(-.50,2.48),(-.31,2.65)],-.18,.18,2,'ventral_fairing')
    g.quad([[-.15,-.48,1.64],[.15,-.48,1.64],[.15,-.35,1.57],[-.15,-.35,1.57]],11,[0,-.3,-1],'intake_shadow')
    for z,width in ((-3.83,.012),(-3.35,.018),(-3.18,.012),(-2.2,.008),(-1.5,.012),(.64,.014),(1.8,.012),(2.45,.009)):
        g.lathe([(z-width/2,.401),(z+width/2,.401)],4,segments=64,part='panel_seam')
    # Flush panel artwork on curved body; no protruding fine parts.
    for side in (-1,1):
        for z0,z1 in ((-2.95,-2.38),(-1.28,-.68),(.85,1.4)):
            for y0,y1 in ((-.085,-.078),(.078,.085)):
                x=side*math.sqrt(.402**2-y0**2)
                g.quad([[x,y0,z0],[x,y1,z0],[x,y1,z1],[x,y0,z1]],4,[side,0,0],'access_panel')
            for z in (z0,z1):
                g.quad([[side*.395,-.078,z],[side*.395,.078,z],
                        [side*.395,.078,z+.008],[side*.395,-.078,z+.008]],4,[side,0,0],'access_panel')
        for z in (-2.86,-2.60,-1.15,1.0):
            g.quad([[side*.403,-.025,z],[side*.403,.025,z],
                    [side*.403,.025,z+.04],[side*.403,-.025,z+.04]],9,[side,0,0],'stencil')
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
        im=Image.fromarray(pixels);path=OUT/f'kalibr_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'kalibr_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('kalibr')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['kalibr_diffuse.dds']),
             n=('s',['kalibr_normal.dds']),spec=('s',['kalibr_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,4.26]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'kalibr.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'kalibr_idle.anim').write_bytes(encode(anim))
    lines=['# Kalibr game art; Y up, nose -Z; arbitrary art units.','mtllib kalibr.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl kalibr');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'kalibr.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'kalibr.mtl').write_text('newmtl kalibr\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd kalibr_diffuse.png\n',encoding='utf-8')
    print(f'Kalibr: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
