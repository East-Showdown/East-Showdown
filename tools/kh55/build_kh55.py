"""Kh-55 visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/kh55'
EQUIPMENT=('rus_medium_guided_missile_kh55','rus_medium_guided_missile_kh55cm',
           'rus_medium_guided_missile_kh555','rus_medium_guided_missile_kh101')
COLORS=[(193,201,199),(205,211,207),(168,181,181),(47,53,52),
        (116,126,126),(32,38,37),(139,148,146),(176,182,177),
        (152,72,38),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    g.lathe([(-4.52,.002),(-4.49,.09),(-4.40,.19),(-4.22,.29),
             (-4.00,.35),(-3.75,.383),(-3.47,.39)],1,segments=48,part='rounded_nose')
    g.lathe([(-3.47,.39),(-2.9,.39),(-1.6,.39),(0.,.39),(1.7,.39),(2.52,.383)],0,segments=48,part='fuselage')
    g.lathe([(2.52,.383),(2.91,.363),(3.35,.317),(3.75,.239),(4.06,.14),
             (4.32,.073),(4.38,.048)],2,segments=40,part='tail_body')
    # A shallow rounded airfoil and swept outer tips, copied visually from the views.
    foil=[(0.,-.55),(.035,-.51),(.059,-.40),(.052,-.20),(.026,.08),
          (0.,.30),(-.018,.08),(-.032,-.20),(-.033,-.40),(-.020,-.51)]
    for side in (-1,1):
        root=np.array([[side*.29,y,z] for y,z in foil])
        tip=np.array([[side*2.35,y*.68,z*.87+.17] for y,z in foil])
        for ring,normal in ((root,[-side,0,0]),(tip,[side,0,0])):
            for i in range(1,len(ring)-1):g.triangle(ring[[0,i,i+1]],0,[normal]*3,part='wing_cap')
        for i in range(len(foil)):
            j=(i+1)%len(foil)
            pts=np.array([root[i],tip[i],tip[j],root[j]])
            n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
            center=(root.mean(0)+tip.mean(0))/2
            if np.dot(n,pts.mean(0)-center)<0:n=-n
            g.quad(pts,0,n,'main_wing')
        # Visible folding joint on each wing root.
        x=side*.47
        g.quad([[x,.064,-.47],[x+side*.014,.064,-.47],
                [x+side*.014,.039,.10],[x,.039,.10]],4,[0,1,0],'wing_joint')
    # Three tapered tail surfaces around the narrowed rear body.
    for angle in (90,210,330):
        a=math.radians(angle);rad=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        outline=[(.21,3.20),(.83,3.66),(.92,3.83),(.89,3.99),(.15,4.03)]
        rings=[np.array([rad*r+[0,0,z]+normal*d for r,z in outline]) for d in (-.018,.018)]
        for ring,sign in zip(rings,(-1,1)):
            for i in range(1,len(ring)-1):g.triangle(ring[[0,i,i+1]],0,[sign*normal]*3,part='tail_fin')
        for i in range(len(outline)):
            j=(i+1)%len(outline)
            g.quad([rings[0][i],rings[1][i],rings[1][j],rings[0][j]],2,part='tail_fin_edge')
    # Deployed underbody engine and an open intake/nozzle; decorative game geometry.
    g.prism([(-.24,2.35),(-.24,3.52),(-.71,3.38),(-.71,2.64)],-.085,.085,4,'engine_pylon')
    cy=-.79
    g.lathe([(2.28,.155),(2.33,.195),(2.43,.218),(2.70,.225),(3.25,.216),
             (3.43,.18),(3.51,.134)],0,center=(0,cy),segments=32,part='engine_nacelle')
    g.lathe([(2.28,.155),(2.34,.14),(2.54,.132)],5,center=(0,cy),segments=32,inward=True,part='engine_intake')
    g.lathe([(3.51,.134),(3.64,.13),(3.71,.106)],6,center=(0,cy),segments=32,part='engine_nozzle')
    g.lathe([(3.52,.09),(3.71,.106)],11,center=(0,cy),segments=32,inward=True,part='nozzle_inside')
    for z,r,normal in ((2.55,.134,[0,0,-1]),(3.52,.092,[0,0,1])):
        for i in range(32):
            a,b=math.tau*i/32,math.tau*(i+1)/32
            g.triangle([[0,cy,z],[r*math.cos(a),cy+r*math.sin(a),z],
                        [r*math.cos(b),cy+r*math.sin(b),z]],11,[normal]*3,part='engine_recess')
    # Dark bands and fine panel seams, visible on the reference's pale fuselage.
    for z,width,tile in ((-3.44,.016,4),(-3.14,.073,3),(-2.69,.012,4),
                         (-1.34,.025,3),(1.82,.018,3),(2.54,.012,4)):
        r=.391 if z<2.52 else .384
        g.lathe([(z-width/2,r),(z+width/2,r)],tile,segments=48,part='body_band')
    for z in (2.6,3.20):g.lathe([(z-.006,.227),(z+.006,.227)],4,center=(0,cy),segments=32,part='pod_seam')
    for side in (-1,1):
        x=.391*side
        # Long side access rail; markings are artwork, not readable instructions.
        for y in (.02,.095):
            g.quad([[x,y,-.55],[x,y,1.68],[x,y+.009,1.68],[x,y+.009,-.55]],4,[side,0,0],'access_rail')
        for z in np.linspace(-.43,1.55,12):
            g.quad([[x,.04,z],[x,.06,z],[x,.06,z+.025],[x,.04,z+.025]],3,[side,0,0],'fastener')
        for z in (-2.37,.12):
            g.quad([[x,-.06,z],[x,.06,z],[x,.06,z+.06],[x,-.06,z+.06]],8,[side,0,0],'service_mark')
        for z in (-3.3,-2.75,1.85):
            g.quad([[x,-.03,z],[x,.04,z],[x,.04,z+.024],[x,-.03,z+.024]],7,[side,0,0],'small_label')
    # Rear ribbed fairing gives the pointed tail its characteristic finish.
    for z in np.linspace(4.07,4.30,7):
        r=.14-(z-4.06)*(.067/.26)
        g.lathe([(z-.006,r+.004),(z+.006,r+.004)],4,segments=24,part='tail_rib')
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
        im=Image.fromarray(pixels);path=OUT/f'kh55_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'kh55_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('kh55')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['kh55_diffuse.dds']),
             n=('s',['kh55_normal.dds']),spec=('s',['kh55_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,-.79,3.71]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'kh55.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'kh55_idle.anim').write_bytes(encode(anim))
    lines=['# Kh-55 game art; Y up, nose -Z; arbitrary art units.','mtllib kh55.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl kh55');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'kh55.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'kh55.mtl').write_text('newmtl kh55\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd kh55_diffuse.png\n',encoding='utf-8')
    print(f'Kh-55: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
