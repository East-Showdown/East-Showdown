"""TREMBITA visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/trembita'
EQUIPMENT=('ukr_drone_missile_equipment_trembita',)
COLORS=[(108, 118, 123), (162, 169, 170), (126, 137, 140), (30, 42, 47), (76, 86, 88), (52, 55, 56), (130, 133, 130), (169, 171, 162), (224, 181, 28), (96, 105, 103), (217, 219, 208), (19, 24, 24), (108, 118, 123)]


def make_geometry():
    sys.path.insert(0,str(HERE.parent/'tu95'))
    from refined_geometry import shell
    g=Geometry()
    def section(z,w,h):
        points=[];r=min(w,h)*.18
        for sx,sy,start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):
            for i in range(7):
                a=math.radians(start+i*15)
                points.append([sx*(w-r)+r*math.cos(a),sy*(h-r)+r*math.sin(a),z])
        return points
    # Bevelled box body and rounded wedge end caps, matching the supplied render.
    profiles=[(-3.4,.025,.045),(-3.34,.10,.14),(-3.18,.23,.27),(-2.98,.34,.365),
              (-2.80,.38,.40),(-2.45,.38,.40),(-1.5,.38,.40),(0,.38,.40),
              (1.3,.38,.40),(2.4,.38,.40),(2.65,.37,.39),(2.85,.26,.30),
              (3.02,.12,.17),(3.08,.025,.065)]
    shell(g,[section(*row) for row in profiles],lambda p:1 if p[2]<-2.8 or p[2]>2.65 else 0,'fuselage')
    # Both tandem wings have volumetric profiles and roots buried in the body.
    for zbase,tipdir in ((-1.85,-1),(1.55,1)):
        for side in (-1,1):
            rows=[]
            for x,lift,bend in ((0,0,0),(.38,0,0),(1.0,0,0),(1.7,0,0),(2.13,0,0),(2.205,.020,30),(2.26,.075,60),(2.28,.15,90),(2.28,.27,90)):
                row=[]
                for a in np.arange(24)*math.tau/24:
                    u=(1-math.cos(a))/2
                    h=.042*math.sin(a)*(1-.42*u)
                    angle=math.radians(bend)
                    row.append([side*x-side*tipdir*math.sin(angle)*h,
                                -.025+tipdir*lift+math.cos(angle)*h,zbase+.60*u])
                rows.append(row)
            # Main panels stop before the smoothly bent yellow winglets.
            shell(g,rows[:5],0,'tandem_wing',cap=False)
            shell(g,rows[4:],8,'yellow_winglet',cap=False)
            tip=np.array(rows[-1]);center=tip.mean(0)
            for i in range(len(tip)):
                g.triangle([center,tip[i],tip[(i+1)%len(tip)]],8,[[0,tipdir,0]]*3,part='winglet_tip')
    # External dorsal engine silhouette: forward rounded chamber and rear tube.
    cy=.72
    g.lathe([(-.72,0),(-.70,.085),(-.62,.17),(-.47,.225),(-.25,.24),(.2,.24),
             (.45,.225),(.67,.17),(.83,.115),(1.2,.11),(1.8,.11),(2.6,.11),(3.25,.12),
             (3.55,.16),(3.65,.165)],5,center=(0,cy),segments=40,part='dorsal_engine')
    g.lathe([(3.65,.165),(3.62,.135),(3.42,.112)],11,center=(0,cy),segments=40,inward=True,part='engine_recess')
    for i in range(40):
        a,b=i*math.tau/40,(i+1)*math.tau/40
        g.triangle([[0,cy,3.41],[.112*math.cos(a),cy+.112*math.sin(a),3.41],
                    [.112*math.cos(b),cy+.112*math.sin(b),3.41]],11,[[0,0,1]]*3,part='engine_shadow')
    for z,r in ((-.21,.244),(.77,.132),(2.65,.116)):
        g.lathe([(z-.034,r),(z+.034,r)],6,center=(0,cy),segments=32,part='engine_band')
    # Small mounting saddles visibly connect the engine to the upper deck.
    for z,h in ((.7,.66),(2.62,.64)):
        g.prism([(.37,z-.13),(h,z-.045),(h,z+.045),(.37,z+.13)],-.045,.045,6,'engine_mount')
    # Compact external lower tube shown in the references, purely visual.
    g.lathe([(.78,0),(.83,.07),(.96,.115),(1.2,.12),(1.4,.095),(2.0,.095),
             (2.85,.095),(3.23,.13)],6,center=(0,-.65),segments=28,part='lower_tube')
    g.lathe([(3.23,.13),(3.22,.10),(3.10,.083)],11,center=(0,-.65),segments=28,inward=True,part='lower_tube_recess')
    g.prism([(-.35,1.20),(-.64,1.30),(-.64,1.55),(-.35,1.62)],-.075,.075,2,'lower_mount')
    for z in (-2.79,-.8,2.65):
        left,right=section(z-.005,.381,.401),section(z+.005,.381,.401)
        for i in range(len(left)):
            j=(i+1)%len(left);g.quad([left[i],right[i],right[j],left[j]],4,part='body_seam')
    for side in (-1,1):
        # Readable lettering uses a dedicated tile within the same material atlas.
        x=side*.382
        za,zb=(-.80,1.10) if side<0 else (1.10,-.80)
        pts=[[x,.17,za],[x,.17,zb],[x,-.10,zb],[x,-.10,za]]
        uv=[[0,.30],[1,.30],[1,.70],[0,.70]]
        for ids in ((0,1,2),(0,2,3)):
            g.triangle([pts[i] for i in ids],12,[[side,0,0]]*3,[uv[i] for i in ids],part='name_marking')
    return g


def textures():
    diffuse=np.zeros((512,512,4),dtype='uint8');diffuse[:,:,3]=255
    spec=np.full((512,512,4),[0,78,38,100],dtype='uint8')
    rng=np.random.default_rng(55)
    for i,color in enumerate(COLORS):
        x,y=i%4*128,i//4*128
        diffuse[y:y+128,x:x+128,:3]=np.clip(np.array(color)+rng.normal(0,.45,(128,128,1)),0,255)
        if i in (2,6,7):spec[y:y+128,x:x+128]=[0,126,115,135]
    from PIL import ImageDraw,ImageFont
    label=Image.new('RGB',(128,128),COLORS[12]);draw=ImageDraw.Draw(label)
    font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',20)
    draw.text((64,64),'TREMBITA',font=font,anchor='mm',fill=(223,224,216))
    diffuse[384:512,:128,:3]=np.array(label)
    for suffix,pixels in [('diffuse',diffuse),('normal',np.full((512,512,4),[128,128,0,128],dtype='uint8')),('specular',spec)]:
        im=Image.fromarray(pixels);path=OUT/f'trembita_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'trembita_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('trembita')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['trembita_diffuse.dds']),
             n=('s',['trembita_normal.dds']),spec=('s',['trembita_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,.72,3.65]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'trembita.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'trembita_idle.anim').write_bytes(encode(anim))
    lines=['# TREMBITA game art; Y up, nose -Z; arbitrary art units.','mtllib trembita.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl trembita');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'trembita.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'trembita.mtl').write_text('newmtl trembita\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd trembita_diffuse.png\n',encoding='utf-8')
    print(f'TREMBITA: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
