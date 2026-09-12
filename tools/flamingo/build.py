"""Build an original game-art Flamingo mesh from the user's four visual references.

All dimensions are arbitrary art units; this is not an engineering model.
Python 3, NumPy and Pillow are required. Run from any working directory.
"""
from pathlib import Path
import math
import numpy as np
from PIL import Image
from pdx_io import Node, encode, read

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent
OUT = ROOT / 'gfx/models/units/missiles/flamingo'
# Atlas tiles: body, radome, wing, nacelle, mounting fairing, intake,
# metal nozzle, panel seams, fasteners, stencil, fan, inner exhaust.
COLORS = [(51,53,52),(61,63,62),(48,51,50),(47,49,48),(43,46,45),
          (16,19,19),(156,162,163),(29,32,31),(99,103,100),(176,182,172),
          (30,34,33),(34,37,37)]


class Geometry:
    def __init__(self):
        self.p, self.n, self.uv, self.tri, self.part = [], [], [], [], []

    def triangle(self, points, tile, normals=None, uv=None, part='detail'):
        points = np.array(points, dtype=float)
        cross = np.cross(points[1]-points[0], points[2]-points[0])
        if np.linalg.norm(cross)<1e-10:
            return
        if normals is None:
            normals = np.tile(cross / np.linalg.norm(cross), (3,1))
        normals = np.array(normals, dtype=float)
        uv = np.array(uv if uv is not None else [[.2,.2],[.8,.2],[.8,.8]])
        if np.dot(cross, normals.mean(0))<0:
            points, normals, uv = points[[0,2,1]], normals[[0,2,1]], uv[[0,2,1]]
        normals /= np.linalg.norm(normals,axis=1)[:,None]
        index=len(self.p)
        self.p.extend(points.tolist()); self.n.extend(normals.tolist())
        # Insets prevent bleeding across atlas tiles in lower mip levels.
        self.uv.extend(((uv*.84+.08+[tile%4,tile//4])/4).tolist())
        self.tri.extend([index,index+1,index+2]); self.part.append(part)

    def quad(self, pts, tile, normal=None, part='detail'):
        for ids in ((0,1,2),(0,2,3)):
            self.triangle([pts[i] for i in ids],tile,
                          [normal]*3 if normal is not None else None,
                          [((0,0),(1,0),(1,1),(0,1))[i] for i in ids],part)

    def lathe(self, profile, tile, center=(0,0), segments=32, inward=False, part='body'):
        profile=np.array(profile,dtype=float)
        slopes=np.gradient(profile[:,1],profile[:,0])
        for j in range(len(profile)-1):
            for i in range(segments):
                pts=[]; norms=[];uv=[]
                for k,t in ((j,i),(j,i+1),(j+1,i+1),(j+1,i)):
                    a=2*math.pi*t/segments;z,r=profile[k]
                    pts.append([center[0]+r*math.cos(a),center[1]+r*math.sin(a),z])
                    n=np.array([math.cos(a),math.sin(a),-slopes[k]])
                    norms.append(n*(-1 if inward else 1))
                    uv.append([t/segments,k/(len(profile)-1)])
                for ids in ((0,1,2),(0,2,3)):
                    self.triangle([pts[t] for t in ids],tile,[norms[t] for t in ids],[uv[t] for t in ids],part)

    def prism(self, polygon, x0, x1, tile, part):
        # Polygon points are (y,z), extruded along X; orient faces outwards.
        rings=[np.array([[x,y,z] for y,z in polygon]) for x in (x0,x1)]
        center=np.concatenate(rings).mean(0)
        for ring in rings:
            normal=np.array([-1 if ring[0,0]==x0 else 1,0,0])
            for i in range(1,len(ring)-1):
                self.triangle(ring[[0,i,i+1]],tile,[normal]*3,part=part)
        for i in range(len(polygon)):
            j=(i+1)%len(polygon)
            pts=np.array([rings[0][i],rings[1][i],rings[1][j],rings[0][j]])
            n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
            if np.dot(n,pts.mean(0)-center)<0:n=-n
            self.quad(pts,tile,n,part)


def make_geometry():
    g=Geometry()
    g.lathe([(-4.8,.025),(-4.7,.105),(-4.52,.21),(-4.29,.30),(-4.04,.365),
             (-3.78,.407),(-3.52,.427),(-3.36,.43)],1,segments=48,part='radome')
    g.lathe([(-3.36,.43),(-3.33,.435),(-1.8,.435),(.5,.435),(2.4,.435),(3.32,.43)],0,segments=48,part='fuselage')
    g.lathe([(3.32,.43),(3.60,.408),(3.89,.35),(4.14,.258),(4.35,.14),(4.49,.008)],1,segments=40,part='tail_cone')
    # Pitot-like nose probe is a purely visual element from the references.
    g.lathe([(-5.38,.002),(-5.25,.026),(-5.15,.018),(-4.84,.018),(-4.78,.038)],6,segments=12,part='nose_probe')
    g.lathe([(-5.47,.001),(-5.37,.005)],8,segments=8,part='nose_probe')
    # Straight wings with a rounded leading edge and tapered trailing edge.
    foil=[(0,-.92),(.058,-.85),(.081,-.68),(.067,-.40),(.025,-.10),
          (0,.10),(-.018,-.10),(-.043,-.40),(-.05,-.68),(-.03,-.85)]
    for side in (-1,1):
        a,b=sorted([.30*side,2.93*side])
        g.prism(foil,a,b,2,'main_wing')
    # Four swept tail fins in an X around the rear fuselage.
    for angle in (25,155,225,315):
        a=math.radians(angle); radial=np.array([math.cos(a),math.sin(a),0.])
        normal=np.array([-math.sin(a),math.cos(a),0.])
        outline=[(.37,2.93),(.37,4.03),(1.42,4.0),(1.48,3.48)]
        rings=[np.array([radial*r+[0,0,z]+normal*thick for r,z in outline]) for thick in (-.022,.022)]
        for ring,sign in zip(rings,(-1,1)):g.quad(ring,2,normal*sign,'tail_fin')
        for j in range(4):
            k=(j+1)%4;g.quad([rings[0][j],rings[1][j],rings[1][k],rings[0][k]],2,part='tail_fin_edge')
    # Dorsal engine mount and open nacelle. No internal engineering is modeled.
    mount=[(.36,1.10),(.72,1.18),(1.13,1.38),(1.13,3.47),(.79,3.68),(.38,3.72)]
    g.prism(mount,-.25,.25,4,'engine_fairing')
    g.lathe([(.69,.282),(.76,.32),(.88,.357),(1.08,.373),(1.40,.38),
             (3.48,.38),(3.73,.358),(3.90,.306)],3,center=(0,1.08),segments=40,part='nacelle')
    # Rounded inlet lip leading into a dark recess; fan is decorative geometry.
    g.lathe([(.69,.282),(.73,.266),(.91,.251),(1.13,.24)],5,center=(0,1.08),segments=40,inward=True,part='inlet')
    g.lathe([(3.90,.306),(3.95,.31),(4.15,.292),(4.22,.276)],6,center=(0,1.08),segments=40,part='nozzle')
    g.lathe([(3.91,.242),(4.15,.255),(4.22,.276)],11,center=(0,1.08),segments=40,inward=True,part='exhaust_recess')
    for z,r,c in ((1.14,.247,5),(3.9,.244,5)):
        for i in range(40):
            a,b=2*math.pi*i/40,2*math.pi*(i+1)/40
            g.triangle([[0,1.08,z],[r*math.cos(a),1.08+r*math.sin(a),z],
                        [r*math.cos(b),1.08+r*math.sin(b),z]],c,
                       [[0,0,-1 if z<2 else 1]]*3,part='recess_back')
    for i in range(24):
        a=i*math.tau/24;b=a+.08
        g.quad([[.06*math.cos(a),1.08+.06*math.sin(a),1.10],
                [.23*math.cos(b),1.08+.23*math.sin(b),1.12],
                [.23*math.cos(b+.065),1.08+.23*math.sin(b+.065),1.13],
                [.06*math.cos(a+.08),1.08+.06*math.sin(a+.08),1.11]],10,[0,0,-1],'fan_blade')
    g.lathe([(.96,.002),(1.01,.045),(1.12,.072)],10,center=(0,1.08),segments=24,part='fan_hub')
    # Longitudinal rails and panel seams, readable at close inspection.
    for x in (-.26,.26):
        g.lathe([(-1.73,.012),(-1.65,.024),(.94,.024),(1.02,.012)],4,center=(x,.369),segments=8,part='dorsal_rail')
    for z,r in ((-3.345,.436),(3.325,.432)):
        g.lathe([(z-.009,r),(z+.009,r)],7,segments=48,part='panel_seam')
    # Flush rivets and stencils use small surface polygons, not separate textures.
    for side in (-1,1):
        for y in (.53,.82):
            for z in np.linspace(1.2,3.4,27):
                x=.251*side;d=.006
                g.quad([[x,y-d,z-d],[x,y+d,z-d],[x,y+d,z+d],[x,y-d,z+d]],8,[side,0,0],'fairing_rivet')
        for z in (1.36,2.13,2.90):
            x=.252*side;y=.91;d=.034
            g.quad([[x,y-d,z-d],[x,y+d,z-d],[x,y+d,z+d],[x,y-d,z+d]],9,[side,0,0],'fairing_stencil')
        x=.436*side;y=0.;z=-2.81
        for y0,y1,z0,z1 in ((-.10,.10,-.09,-.065),(-.10,.10,.065,.09),(-.10,-.072,-.065,.065),(.072,.10,-.065,.065)):
            g.quad([[x,y+y0,z+z0],[x,y+y1,z+z0],[x,y+y1,z+z1],[x,y+y0,z+z1]],9,[side,0,0],'body_stencil')
    return g


def make_textures():
    # Simple procedural game materials, without sampling the reference images.
    rng=np.random.default_rng(72)
    diffuse=np.zeros((512,512,4),dtype=np.uint8);diffuse[:,:,3]=255
    spec=np.full((512,512,4),[0,85,35,95],dtype=np.uint8)
    for tile,color in enumerate(COLORS):
        x,y=tile%4*128,tile//4*128
        noise=rng.normal(0,.8,(128,128,1))
        diffuse[y:y+128,x:x+128,:3]=np.clip(np.array(color)+noise,0,255).astype('uint8')
        if tile==6:spec[y:y+128,x:x+128]=[0,160,180,180]
        if tile in (5,11):spec[y:y+128,x:x+128]=[0,35,12,45]
    normal=np.full((512,512,4),[128,128,0,128],dtype=np.uint8)
    for name,pixels in (('diffuse',diffuse),('normal',normal),('specular',spec)):
        image=Image.fromarray(pixels)
        # Legacy uncompressed RGBA DDS with a complete mip chain.
        base=OUT/f'flamingo_{name}.dds';image.save(base)
        raw=bytearray(base.read_bytes())
        import struct
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10)
        struct.pack_into('<I',raw,108,0x401008)
        size=256
        while size:
            mip=image.resize((size,size),Image.Resampling.BOX)
            # Pillow's legacy RGBA DDS stores bytes in BGRA order.
            raw.extend(mip.tobytes('raw','BGRA'))
            size//=2
        base.write_bytes(raw)
    Image.fromarray(diffuse).save(SOURCE/'flamingo_diffuse.png')


def export(g):
    root=Node('File',pdxasset=('i',[1,0]))
    obj=root.add('object').add('flamingo')
    p,n,uv=np.array(g.p),np.array(g.n),np.array(g.uv)
    # Tangent basis from actual UVs, including atlas tile orientation.
    tangents=[]
    for i in range(0,len(p),3):
        e1,e2=p[i+1]-p[i],p[i+2]-p[i];a,b=uv[i+1]-uv[i],uv[i+2]-uv[i]
        det=a[0]*b[1]-a[1]*b[0]
        tangent=(e1*b[1]-e2*a[1])/det if abs(det)>1e-10 else e1
        bitangent=(-e1*b[0]+e2*a[0])/det if abs(det)>1e-10 else e2
        for normal in n[i:i+3]:
            t=tangent-normal*np.dot(normal,tangent)
            if np.linalg.norm(t)<1e-9:t=np.cross(normal,[1,0,0] if abs(normal[0])<.9 else [0,1,0])
            t/=np.linalg.norm(t)
            sign=1. if np.dot(np.cross(normal,t),bitangent)>=0 else -1.
            tangents.extend([*t,sign])
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),
                 ta=('f',tangents),u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',['flamingo_diffuse.dds']),
             n=('s',['flamingo_normal.dds']),spec=('s',['flamingo_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',[0.,1.08,4.22]),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=OUT/'flamingo.mesh';path.write_bytes(encode(root))
    assert encode(read(path))==path.read_bytes()
    # A constant pose track gives all game states a valid animation binding.
    anim=Node('File',pdxasset=('i',[1,0]))
    info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2))
    (OUT/'flamingo_idle.anim').write_bytes(encode(anim))
    lines=['# Flamingo game-art model. Y up, nose -Z; arbitrary art units.','mtllib flamingo.mtl']
    lines += ['v '+' '.join(f'{x:.7f}' for x in row) for row in p]
    lines += [f'vt {u:.7f} {1-v:.7f}' for u,v in uv]
    lines += ['vn '+' '.join(f'{x:.7f}' for x in row) for row in n]
    lines += ['usemtl flamingo']
    previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (SOURCE/'flamingo.obj').write_text('\n'.join(lines)+'\n')
    (SOURCE/'flamingo.mtl').write_text('newmtl flamingo\nKd 1 1 1\nKs 0.2 0.2 0.2\nNs 40\nmap_Kd flamingo_diffuse.png\n')
    print(f'Exported {len(g.tri)//3} triangles, {len(p)} vertices; mesh, DDS mipmaps, pose animation and OBJ.')


if __name__ == '__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    make_textures()
    export(make_geometry())
