"""R-360 NEPTUNE visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/neptun'
EQUIPMENT=('ukr_sea_guided_missile_neptun',)
COLORS=[(204,211,211),(216,221,220),(198,205,205),(35,41,43),(141,151,151),(171,155,112),(124,132,134),(186,193,192),(137,120,76),(74,88,94),(219,223,219),(25,31,34),(204,211,211)]


def make_geometry():
    sys.path.insert(0,str(HERE.parent/'tu95'))
    from refined_geometry import shell,PchipInterpolator
    g=Geometry()
    # External proportions traced from the supplied R-360 renders, nose -Z.
    keys=np.array([[-4.0,.012],[-3.95,.105],[-3.83,.205],[-3.62,.295],
                   [-3.35,.358],[-3.0,.391],[-2.65,.40],[3.65,.40],[3.85,.38]])
    radius=PchipInterpolator(keys[:,0],keys[:,1])
    zs=np.unique(np.r_[np.linspace(-4,-2.65,23),keys[:,0],-1,0,1,2,3])
    g.lathe([(-4.002,0)]+[(z,float(radius(z))) for z in zs],0,segments=64,part='fuselage')
    # Four full-thickness wings and four smaller tail fins, all rooted inside skin.
    def fins(rootlead,rootchord,span,sweep,tipchord,name):
        for angle in (45,135,225,315):
            a=math.radians(angle);radial=np.array([math.cos(a),math.sin(a),0])
            normal=np.array([-math.sin(a),math.cos(a),0]);rows=[]
            for u in np.linspace(0,1,8):
                r=.34+span*u;lead=rootlead+sweep*u;chord=rootchord+(tipchord-rootchord)*u
                row=[]
                for t in np.arange(24)*math.tau/24:
                    v=(1-math.cos(t))/2
                    h=(.026-.014*u)*math.sin(t)*(1-.55*v)
                    row.append(radial*r+normal*h+[0,0,lead+chord*v])
                rows.append(row)
            shell(g,rows,2,name)
            # Hinge line follows the thin face at mid-span.
            for u in (.40,):
                r=.34+span*u;lead=rootlead+sweep*u;chord=rootchord+(tipchord-rootchord)*u
                pts=[radial*(r+d)+normal*.026+[0,0,lead+chord*v] for d,v in ((-.004,.12),(.004,.12),(.004,.87),(-.004,.87))]
                g.quad(pts,7,normal,name+'_hinge')
    fins(.05,1.13,.99,.58,.47,'main_wing')
    fins(2.84,.73,.54,.25,.36,'tail_fin')
    # Integrated belly fairing and forward-facing dark inlet, not a separate pod.
    profiles=[(.18,.13,.105,-.32),(.34,.20,.17,-.36),(.55,.22,.185,-.37),
              (1.15,.22,.17,-.37),(1.85,.18,.135,-.37),(2.6,.17,.125,-.37),
              (3.5,.16,.12,-.36),(3.80,.11,.09,-.34)]
    shell(g,[[[w*math.cos(a),cy+h*math.sin(a),z] for a in np.arange(32)*math.tau/32]
             for z,w,h,cy in profiles],2,'belly_fairing',cap=False)
    for z,w,h,cy,sign,tile in ((.181,.126,.10,-.32,-1,11),(3.801,.11,.09,-.34,1,2)):
        for i in range(32):
            a,b=i*math.tau/32,(i+1)*math.tau/32
            g.triangle([[0,cy,z],[w*math.cos(a),cy+h*math.sin(a),z],
                        [w*math.cos(b),cy+h*math.sin(b),z]],tile,[[0,0,sign]]*3,part='inlet' if sign<0 else 'belly_cap')
    # Recessed exhaust with a metal rim and shadowed center.
    g.lathe([(3.84,.38),(3.875,.373),(3.885,.30),(3.90,.29)],6,segments=48,part='nozzle_rim')
    g.lathe([(3.65,.225),(3.78,.26),(3.90,.29)],11,segments=48,inward=True,part='nozzle_recess')
    for i in range(48):
        a,b=i*math.tau/48,(i+1)*math.tau/48
        g.triangle([[0,0,3.65],[.225*math.cos(a),.225*math.sin(a),3.65],
                    [.225*math.cos(b),.225*math.sin(b),3.65]],11,[[0,0,1]]*3,part='exhaust_shadow')
    g.lathe([(3.64,.10),(3.73,.09),(3.82,.045),(3.84,0)],6,segments=24,part='exhaust_center')
    # Low longitudinal fairings on both sides and subtle panel joints.
    for side in (-1,1):
        rows=[]
        for z,w,h in ((-1.86,.012,.004),(-1.70,.042,.026),(-1.5,.043,.027),(.78,.043,.027),(1.03,.012,.004)):
            rows.append([[side*(.398+h*math.cos(a)),w*math.sin(a),z] for a in np.arange(16)*math.tau/16])
        shell(g,rows,1,'side_fairing')
        for z in np.linspace(-1.64,.80,8):
            x=side*.430
            g.quad([[x,-.010,z-.011],[x,.010,z-.011],[x,.010,z+.011],[x,-.010,z+.011]],8,[side,0,0],'fastener')
    for z in (-2.65,-.25,1.68,2.68,3.68):
        g.lathe([(z-.004,.401),(z+.004,.401)],7,segments=64,part='panel_joint')
    # Rear vent grilles curve with the upper hull.
    for ac in (math.pi/2,math.pi/2-.65,math.pi/2+.65):
        for z in np.linspace(1.89,2.15,9):
            pts=[[.405*math.cos(a),.405*math.sin(a),zz] for a,zz in
                 ((ac-.18,z),(ac+.18,z),(ac+.18,z+.016),(ac-.18,z+.016))]
            g.quad(pts,5,[math.cos(ac),math.sin(ac),0],'vent_slats')
    # Fine fastener rows remain subordinate to the missile silhouette.
    for ac in (math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4):
        radial=np.array([math.cos(ac),math.sin(ac),0]);tan=np.array([-math.sin(ac),math.cos(ac),0])
        for z in np.linspace(-.15,3.55,20):
            pts=[radial*.402+tan*d+[0,0,z+e] for d,e in ((-.008,-.008),(.008,-.008),(.008,.008),(-.008,.008))]
            g.quad(pts,8,radial,'skin_fastener')
    # A curved blue identifier tile follows the body, avoiding floating flat labels.
    for side in (-1,1):
        for j in range(10):
            vs=(j/10,(j+1)/10);pts=[];uv=[];ns=[]
            for u,v in ((0,vs[0]),(1,vs[0]),(1,vs[1]),(0,vs[1])):
                a=(.30-.60*v);z=(-2.48+.95*u) if side<0 else (-1.53-.95*u)
                pts.append([side*.402*math.cos(a),.402*math.sin(a),z])
                ns.append([side*math.cos(a),math.sin(a),0]);uv.append([u,v])
            for ids in ((0,1,2),(0,2,3)):
                g.triangle([pts[i] for i in ids],12,[ns[i] for i in ids],[uv[i] for i in ids],part='blue_marking')
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
    draw.text((64,64),'R-360',font=font,anchor='mm',fill=(53,72,139))
    diffuse[384:512,:128,:3]=np.array(label)
    for suffix,pixels in [('diffuse',diffuse),('normal',np.full((512,512,4),[128,128,0,128],dtype='uint8')),('specular',spec)]:
        im=Image.fromarray(pixels);path=OUT/f'neptun_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'neptun_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('neptun')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['neptun_diffuse.dds']),
             n=('s',['neptun_normal.dds']),spec=('s',['neptun_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,3.90]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'neptun.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'neptun_idle.anim').write_bytes(encode(anim))
    lines=['# R-360 NEPTUNE game art; Y up, nose -Z; arbitrary art units.','mtllib neptun.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl neptun');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'neptun.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'neptun.mtl').write_text('newmtl neptun\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd neptun_diffuse.png\n',encoding='utf-8')
    print(f'R-360 NEPTUNE: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
