"""Storm Shadow visual game asset from the user's reference images; arbitrary art units."""
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

OUT=ROOT/'gfx/models/units/missiles/stormshadow'
EQUIPMENT=('nto_light_guided_missile_equipment_shtormshadow',)
COLORS=[(108,119,127),(122,132,140),(89,101,112),(39,47,53),
        (65,76,84),(32,38,37),(139,148,146),(176,182,177),
        (222,201,55),(83,94,92),(214,218,211),(20,27,27)]


def make_geometry():
    g=Geometry()
    # Rounded rectangular sections; external art only, nose toward -Z.
    def section(z,w,h,cy=0):
        points=[]
        bevel=min(w,h)*.60
        for sx,sy,start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):
            for i in range(13):
                a=math.radians(start+i*7.5)
                points.append([sx*(w-bevel)+bevel*math.cos(a),
                               cy+sy*(h-bevel)+bevel*math.sin(a),z])
        return np.array(points)
    stations=[(-4.65,.003,.004,-.045),(-4.54,.052,.05,-.040),
              (-4.42,.112,.103,-.033),(-4.30,.17,.15,-.025),
              (-4.16,.227,.205,-.020),(-4.02,.28,.25,-.015),
              (-3.84,.34,.305,-.006),(-3.65,.39,.34,0),
              (-3.46,.427,.360,0),(-3.25,.45,.37,0),
              (-2.5,.45,.37,0),(-1.5,.45,.37,0),(-.5,.45,.37,0),
              (.5,.45,.37,0),(1.5,.445,.365,0),(2.1,.43,.35,0),
              (2.35,.42,.34,0),(2.6,.395,.325,0),(2.8,.37,.31,0),
              (3.08,.34,.295,0),(3.35,.32,.285,0),(3.55,.30,.275,0),(3.7,.29,.27,0)]
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
    loft(rings,lambda k:3 if stations[k][0]<-4.02 else 0,'smooth_fuselage')
    for ring,normal in ((rings[0],[0,0,-1]),(rings[-1],[0,0,1])):
        for i in range(1,len(ring)-1):
            g.triangle(ring[[0,i,i+1]],0,[normal]*3,part='body_cap')
    # Straight tapered wing pair with thin rounded profiles.
    # Rounded leading edge and thin trailing edge, with a continuous center.
    us=(1-np.cos(np.linspace(0,math.pi,17)))/2
    thick=lambda u: .085*(.2969*np.sqrt(u)-.126*u-.3516*u*u+.2843*u**3-.1036*u**4)
    foil=[(thick(u),u) for u in us]+[(-thick(u),u) for u in us[-2:0:-1]]
    for side in (-1,1):
        wingrings=[np.array([[side*x,.29+y*scale,lead+u*chord] for y,u in foil])
                   for x,lead,chord,scale in ((0.,-.06,.68,1.3),(.45,-.05,.67,1.3),
                       (1.5,.26,.48,1.0),(2.13,.44,.40,.7),(2.2,.48,.32,.5))]
        loft(wingrings,1,'main_wing')
        tip=wingrings[-1]
        for i in range(1,len(tip)-1):
            g.triangle(tip[[0,i,i+1]],1,[[side,0,0]]*3,part='wing_cap')
    # Reference tail: lateral stabilizers plus paired canted upper/lower fins.
    # Separate roots on the body shoulders replace the oversized central cross.
    for angle in (0,180,60,120,240,300):
        a=math.radians(angle)
        rad=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        lateral=angle in (0,180)
        stations_tail=(
            ((.24,3.00,.61,.022),(.61,3.16,.43,.017),(.77,3.31,.25,.007))
            if lateral else
            ((.26,2.87,.55,.020),(.48,3.01,.39,.014),(.67,3.13,.24,.006))
        )
        tailrings=[]
        for radius,lead,chord,t in stations_tail:
            tailrings.append(np.array([rad*radius+[0,0,lead+u*chord]+normal*y*t*35 for y,u in foil]))
        part='lateral_tailplane' if lateral else 'canted_tail_fin'
        loft(tailrings,1,part)
        tip=tailrings[-1]
        for i in range(1,len(tip)-1):
            g.triangle(tip[[0,i,i+1]],1,[rad]*3,part=part+'_tip')
    g.lathe([(3.68,.215),(3.74,.22),(3.81,.203)],6,segments=48,part='exhaust_lip')
    g.lathe([(3.81,.203),(3.75,.173),(3.705,.16)],11,segments=48,inward=True,part='exhaust_recess')
    for i in range(48):
        a,b=math.tau*i/48,math.tau*(i+1)/48
        g.triangle([[0,0,3.702],[.17*math.cos(a),.17*math.sin(a),3.702],
                    [.17*math.cos(b),.17*math.sin(b),3.702]],11,[[0,0,1]]*3,part='exhaust_dark')
    # Reference's yellow identification band.
    left,right=section(-3.18,.451,.371),section(-3.13,.451,.371)
    for i in range(len(left)):
        j=(i+1)%len(left)
        g.quad([left[i],right[i],right[j],left[j]],8,part='yellow_band')
    # Ventral intake and long shallow underside housing.
    g.prism([(-.30,-.15),(-.55,.05),(-.53,2.1),(-.30,2.55)],
            -.24,.24,2,'intake_fairing')
    g.quad([[-.20,-.34,-.13],[.20,-.34,-.13],[.20,-.53,.045],[-.20,-.53,.045]],
           11,[0,-.5,-1],'intake_opening')
    # Dorsal wing-root fairing overlaps both wings and the body.
    g.prism([(.34,-1.9),(.44,-1.45),(.44,.61),(.34,.85)],
            -.28,.28,1,'wing_root_fairing')
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
    for side in (-1,1):
        x=side*.452
        for z in (-2.98,-1.8):
            # Small warning triangle and a simple contrasting label.
            g.triangle([[x,.10,z],[x,.20,z+.07],[x,.10,z+.14]],8,
                       [[side,0,0]]*3,part='warning_mark')
            g.quad([[x,.02,z],[x,.045,z],[x,.045,z+.17],[x,.02,z+.17]],
                   10,[side,0,0],'white_label')
        for z in np.linspace(-2.45,1.4,16):
            g.quad([[x,-.07,z],[x,-.057,z],[x,-.057,z+.013],[x,-.07,z+.013]],
                   4,[side,0,0],'flush_fastener')
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
        im=Image.fromarray(pixels);path=OUT/f'stormshadow_{suffix}.dds';im.save(path);raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'stormshadow_diffuse.png')


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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('stormshadow')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['stormshadow_diffuse.dds']),
             n=('s',['stormshadow_normal.dds']),spec=('s',['stormshadow_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,0.,3.81]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'stormshadow.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(OUT/'stormshadow_idle.anim').write_bytes(encode(anim))
    lines=['# Storm Shadow game art; Y up, nose -Z; arbitrary art units.','mtllib stormshadow.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append('usemtl stormshadow');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'stormshadow.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'stormshadow.mtl').write_text('newmtl stormshadow\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd stormshadow_diffuse.png\n',encoding='utf-8')
    print(f'Storm Shadow: {len(g.tri)//3} triangles, {len(p)} vertices; mesh, textures, pose track and OBJ.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
