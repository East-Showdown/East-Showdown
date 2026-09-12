"""Original Shahed-style HOI4 game art based on the supplied visual reference.

Coordinates are arbitrary art units, not manufacturing dimensions.
Uses the existing Flamingo binary/primitive helpers; does not rebuild Flamingo.
"""
from pathlib import Path
import sys
import math
import struct
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from build import Geometry
from pdx_io import Node, read, encode

OUT = ROOT / 'gfx/models/units/missiles/shahed'
PIVOT = np.array([0., 0., 3.21])
COLORS = [(194,196,190), (206,208,202), (180,184,177), (23,28,101),
          (108,116,111), (63,69,65), (35,39,36), (151,154,146),
          (168,161,128), (42,45,42), (129,134,127), (209,210,201)]
EQUIPMENT = (
    'rus_irn_guided_uav_shahed131', 'rus_guided_uav_shahed131',
    'rus_guided_uav_geranium', 'rus_guided_uav_geranium_m',
    'rus_guided_uav_geranium3', 'rus_guided_uav_geranium4',
    'rus_guided_uav_geranium5',
)


def surface(g, points, tile, sign, part):
    """Smooth normals for a structured wing surface."""
    points = np.array(points)
    dx, dt = np.gradient(points, axis=(0, 1))
    normals = np.cross(dx, dt)
    normals *= np.where(normals[:, :, 1:2] * sign < 0, -1, 1)
    normals /= np.linalg.norm(normals, axis=2)[:, :, None]
    for i in range(len(points)-1):
        for j in range(len(points[0])-1):
            ids = [(i,j),(i+1,j),(i+1,j+1),(i,j+1)]
            for tri in ((0,1,2),(0,2,3)):
                g.triangle([points[ids[k]] for k in tri],tile,
                           [normals[ids[k]] for k in tri],part=part)


def box(g, center, size, tile, part):
    x,y,z=center;w,h,d=np.array(size)/2
    g.prism([(y-h,z-d),(y+h,z-d),(y+h,z+d),(y-h,z+d)],x-w,x+w,tile,part)


def line(g, a, b, width, tile=4, part='panel_line'):
    a,b=np.array(a),np.array(b)
    # Surface markings on the upper wing, offset perpendicular in the XZ plane.
    direction=b-a
    offset=np.cross(direction,[0,1,0]);offset*=width/(2*np.linalg.norm(offset))
    g.quad([a-offset,b-offset,b+offset,a+offset],tile,[0,1,0],part)


def make_geometry():
    g=Geometry()
    # Long rounded central body, with a broad delta wing behind its nose.
    g.lathe([(-3.48,.002),(-3.44,.08),(-3.34,.16),(-3.17,.225),
             (-2.93,.275),(-2.64,.302),(-1.94,.31)],1,segments=40,part='nose')
    g.lathe([(-1.94,.311),(-1.82,.311)],3,segments=40,part='blue_band')
    g.lathe([(-1.82,.31),(-1.2,.31),(.1,.31),(1.9,.30),(2.32,.263),
             (2.62,.218),(2.78,.15)],0,segments=40,part='fuselage')
    for side in (-1,1):
        rows=[]
        for u in (0,.12,.3,.5,.7,.87,1.):
            x=side*(.17+2.33*u)
            leading=-1.64+3.59*u
            thick=.128*(1-u)+.028*u
            row=[]
            for t in (0,.025,.08,.19,.36,.59,.81,.94,1.):
                shape=max(math.sin(math.pi*t),0)**.68
                row.append([x,thick*shape,leading+(2.82-leading)*t])
            rows.append(row)
        surface(g,rows,0,1,'delta_wing_top')
        lower=np.array(rows);lower[:,:,1]*=-.65
        surface(g,lower,2,-1,'delta_wing_bottom')
        # Close the thin end cap beneath the vertical winglet.
        for j in range(len(rows[-1])-1):
            g.quad([rows[-1][j],rows[-1][j+1],lower[-1,j+1],lower[-1,j]],2,part='wing_tip_cap')
        winglet=[(-.42,2.05),(.42,2.05),(.42,2.70),(0,2.94),(-.42,2.70)]
        x=2.50*side
        g.prism(winglet,x-.014,x+.014,1,'winglet')
        # Elevon hinge line near the broad straight trailing edge.
        line(g,[.34*side,.042,2.53],[2.45*side,.028,2.53],.010,4,'elevon_hinge')
        for x in (.78,1.70):
            line(g,[x*side,.037,2.55],[x*side,.004,2.80],.008,4,'elevon_joint')

    # Rear motor is represented by simple visual covers and cooling ribs.
    g.lathe([(2.65,.145),(2.76,.17),(2.99,.17),(3.08,.10)],5,segments=24,part='engine_case')
    for side in (-1,1):
        for z in (2.80,3.01):
            box(g,[side*.235,0,z],[.24,.23,.16],5,'cylinder_cover')
            for x in np.linspace(.17,.355,7):
                box(g,[side*x,0,z],[.013,.255,.18],7,'cooling_rib')
        box(g,[side*.13,-.18,2.92],[.10,.10,.20],6,'engine_detail')
    g.lathe([(3.06,.083),(3.17,.083),(3.20,.058)],8,segments=20,part='shaft')
    # Two decorative propeller blades on their own bone.
    blade=[(.055,-.026),(.22,-.067),(.55,-.10),(.73,-.060),(.79,-.012),
           (.73,.024),(.44,.063),(.18,.042)]
    for side in (-1,1):
        angle=math.radians(25)+(math.pi if side==-1 else 0)
        c,s=math.cos(angle),math.sin(angle)
        layers=[]
        for depth in (-.014,.014):
            layers.append(np.array([[c*x-s*y,s*x+c*y,PIVOT[2]+depth] for x,y in blade]))
        for layer,normal in zip(layers,([0,0,-1],[0,0,1])):
            for i in range(1,len(layer)-1):g.triangle(layer[[0,i,i+1]],7,[normal]*3,part='propeller')
        for i in range(len(blade)):
            j=(i+1)%len(blade)
            g.quad([layers[0][i],layers[0][j],layers[1][j],layers[1][i]],7,part='propeller')
    g.lathe([(3.19,.06),(3.23,.073),(3.27,.045),(3.28,.003)],7,segments=20,part='propeller')

    # Access panels on top of the central body and both wings.
    for z0,z1 in ((-1.73,-.85),(-.58,.20),(.46,1.25),(1.50,2.23)):
        y=.303 if z1<1.9 else .285
        for a,b in [([-.19,y,z0],[.19,y,z0]),([.19,y,z0],[.19,y,z1]),
                    ([.19,y,z1],[-.19,y,z1]),([-.19,y,z1],[-.19,y,z0])]:
            line(g,a,b,.008,10)
        for x in (-.16,.16):
            for z in (z0+.045,z1-.045):
                g.quad([[x-.008,y+.002,z-.008],[x+.008,y+.002,z-.008],
                        [x+.008,y+.002,z+.008],[x-.008,y+.002,z+.008]],5,[0,1,0],'fastener')
    for side in (-1,1):
        for x,z,w,d in ((.72,1.05,.37,.80),(1.26,2.10,.65,.39),(2.0,2.15,.46,.35)):
            # Sample the wing's visible upper surface so panels don't float.
            def height(xx,zz):
                u=(abs(xx)-.17)/2.33;leading=-1.64+3.59*u
                t=(zz-leading)/(2.82-leading)
                return (.128*(1-u)+.028*u)*max(math.sin(math.pi*t),0)**.68+.004
            corners=[(side*(x-w/2),z-d/2),(side*(x+w/2),z-d/2),
                     (side*(x+w/2),z+d/2),(side*(x-w/2),z+d/2)]
            for i in range(4):
                a,b=corners[i],corners[(i+1)%4]
                # Segment markings to follow the curved wing.
                for t in np.linspace(0,1,7)[:-1]:
                    aa=np.array(a)*(1-t)+np.array(b)*t
                    bb=np.array(a)*(1-t-1/6)+np.array(b)*(t+1/6)
                    line(g,[aa[0],height(*aa),aa[1]],[bb[0],height(*bb),bb[1]],.007,10)
        # Small hinge brackets and aerials from the reference silhouette.
        for x in (.42,1.42):box(g,[side*x,.05,2.51],[.035,.05,.085],5,'hinge_bracket')
        g.lathe([(.66,.005),(.69,.006)],5,center=(side*1.10,.23),segments=8,part='antenna_base')
    return g


def textures():
    diffuse=np.zeros((512,512,4),dtype='uint8');diffuse[:,:,3]=255
    spec=np.full((512,512,4),[0,58,25,95],dtype='uint8')
    rng=np.random.default_rng(136)
    for i,color in enumerate(COLORS):
        x,y=i%4*128,i//4*128
        diffuse[y:y+128,x:x+128,:3]=np.clip(np.array(color)+rng.normal(0,.45,(128,128,1)),0,255)
        if i in (5,7,8):spec[y:y+128,x:x+128]=[0,105,95,125]
    normal=np.full((512,512,4),[128,128,0,128],dtype='uint8')
    for suffix,pixels in [('diffuse',diffuse),('normal',normal),('specular',spec)]:
        im=Image.fromarray(pixels);path=OUT/f'shahed_{suffix}.dds';im.save(path)
        raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(im.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(HERE/'shahed_diffuse.png')


def export(g):
    p,n,uv=np.array(g.p),np.array(g.n),np.array(g.uv)
    tangents=[]
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
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add('shahed136')
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),
                 ta=('f',tangents),u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['shahed_diffuse.dds']),
             n=('s',['shahed_normal.dds']),spec=('s',['shahed_specular.dds']))
    indices=[]
    for part in g.part:indices.extend([1 if part=='propeller' else 0,-1,-1,-1]*3)
    mesh.add('skin',bones=('i',[4]),ix=('i',indices),w=('f',[1.,0.,0.,0.]*len(p)))
    skeleton=obj.add('skeleton')
    identity=[1.,0.,0.,0.,1.,0.,0.,0.,1.]
    skeleton.add('root',ix=('i',[0]),tx=('f',identity+[0.,0.,0.]))
    skeleton.add('propeller',ix=('i',[1]),pa=('i',[0]),tx=('f',identity+(-PIVOT).tolist()))
    root.add('locator').add('engine_exhaust',p=('f',[0.,-.18,2.94]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'shahed136.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[24.]),sa=('i',[25]),j=('i',[2]))
    info.add('root',sa=('s',['']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    info.add('propeller',sa=('s',['q']),t=('f',PIVOT.tolist()),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    samples=[]
    for i in range(25):
        angle=math.tau*i/24
        samples.extend([0.,0.,math.sin(angle/2),math.cos(angle/2)])
    anim.add('samples',q=('f',samples));(OUT/'shahed_fly.anim').write_bytes(encode(anim))
    lines=['# Shahed 136 / Geran-2 game art; Y up, nose -Z.','mtllib shahed136.mtl']
    lines.extend('v '+' '.join(f'{v:.7f}' for v in point) for point in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{v:.7f}' for v in point) for point in n)
    lines.append('usemtl shahed');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (HERE/'shahed136.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (HERE/'shahed136.mtl').write_text('newmtl shahed\nKd 1 1 1\nKs 0.1 0.1 0.1\nNs 24\nmap_Kd shahed_diffuse.png\n',encoding='utf-8')
    print(f'Shahed: {len(g.tri)//3} triangles; {len(p)} vertices; 2 bones; propeller animation.')


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    textures();export(make_geometry())
