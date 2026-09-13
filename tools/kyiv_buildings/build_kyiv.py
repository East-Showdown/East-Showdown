"""Reproducible Kyiv-inspired static building kit. Run from any working directory."""
from pathlib import Path
import json
import struct
import sys
import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / 'gfx/models/buildings/kyiv'
SRC = HERE / 'source'
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from pdx_io import Node, encode, read
from render import render

# Metres: width along X, depth along Z, eaves height along Y. Original generic art,
# inspired by common Kyiv building types, not replicas of specific addresses.
SPECS = [
    ('khrushchyovka_01', 'Khrushchyovka / cream', 48, 12, 15, 5, 'flat', (173,166,143)),
    ('khrushchyovka_02', 'Khrushchyovka / brick', 60, 12, 15, 5, 'flat', (151,119,94)),
    ('khrushchyovka_03', 'Khrushchyovka / pitched roof', 36, 11, 12, 4, 'gable', (171,174,160)),
    ('khrushchyovka_04', 'Khrushchyovka / long slab', 72, 12, 15, 5, 'flat', (164,159,147)),
    ('panel_09_01', 'Panel / 9 floors', 54, 14, 27, 9, 'flat', (168,173,169)),
    ('panel_09_02', 'Panel / 9 floors / ochre', 72, 14, 27, 9, 'flat', (179,163,132)),
    ('panel_09_03', 'Panel / 9 floors / stepped', 60, 14, 27, 9, 'step', (150,163,165)),
    ('panel_12_01', 'Panel / 12 floors', 42, 15, 36, 12, 'flat', (166,164,151)),
    ('panel_12_02', 'Panel / 12 floors / L plan', 48, 15, 36, 12, 'ell', (160,164,161)),
    ('tower_16_01', 'Tower / 16 floors', 21, 21, 48, 16, 'flat', (168,175,174)),
    ('tower_16_02', 'Tower / 16 floors / brick', 24, 18, 48, 16, 'flat', (158,128,106)),
    ('panel_16_01', 'Panel / 16 floors / slab', 48, 16, 48, 16, 'flat', (176,166,149)),
    ('private_01', 'Private house / one floor', 10, 8, 3.2, 1, 'gable', (183,176,148)),
    ('private_02', 'Private house / two floors', 12, 10, 6, 2, 'hip', (164,139,113)),
    ('private_03', 'Private house / cottage', 9, 8, 3.2, 1, 'hip', (170,177,166)),
    ('private_04', 'Private house / brick', 14, 9, 6, 2, 'gable', (153,111,91)),
    ('warehouse_01', 'Warehouse / metal', 42, 24, 7, 1, 'gable', (146,158,162)),
    ('warehouse_02', 'Warehouse / flat roof', 54, 30, 8, 1, 'flat', (167,161,145)),
    ('workshop_01', 'Workshop / brick', 36, 18, 8, 2, 'gable', (145,113,95)),
    ('factory_01', 'Factory / sawtooth roof', 48, 30, 9, 2, 'saw', (155,152,137)),
]


def rect_uv(tile, u=1., v=1.):
    x, y = tile % 4 * 256, tile // 4 * 128
    # Eight-pixel gutters. Sample only the inner rectangle; atlas V is image-down.
    a, b = (x+8)/1024, (y+8)/1024
    c, d = (x+8+240*u)/1024, (y+120)/1024
    b=d-(d-b)*v
    return [(a,d),(c,d),(c,b),(a,b)]


def save_dds(im, path):
    im.save(path)
    raw = bytearray(path.read_bytes())
    levels = 11
    struct.pack_into('<I', raw, 8, struct.unpack_from('<I', raw, 8)[0] | 0x20000)
    struct.pack_into('<I', raw, 28, levels)
    struct.pack_into('<I', raw, 108, 0x401008)
    for level in range(1, levels):
        raw.extend(im.resize((1024 >> level, 1024 >> level), Image.Resampling.BOX).tobytes('raw','BGRA'))
    path.write_bytes(raw)


def atlas():
    im = Image.new('RGBA', (1024,1024), (116,119,112,255))
    rng = np.random.default_rng(72)
    for index, (_, _, width, depth, height, floors, roof, color) in enumerate(SPECS):
        tile = Image.new('RGBA', (240,112), (*color,255)); d = ImageDraw.Draw(tile)
        cols = max(2, round(width / (5 if index >= 16 else 3)))
        fh, cw = 106/floors, 240/cols
        if index >= 16:
            for x in range(0,240,8):
                d.line((x,0,x,112), fill=tuple(max(0,c-12) for c in color))
        elif index in (1,10,15):
            for y in range(0,112,4):
                d.line((0,y,240,y), fill=tuple(max(0,c-15) for c in color))
                for x in range((y//4%2)*6,240,12):
                    d.line((x,y,x,y+4),fill=tuple(max(0,c-10) for c in color))
        else:
            for row in range(floors+1):
                y=3+row*fh
                d.line((0,y,240,y),fill=tuple(max(0,c-17) for c in color))
            for col in range(cols+1):
                x=col*cw
                d.line((x,0,x,112),fill=tuple(max(0,c-12) for c in color))
        for row in range(floors):
            y=3+row*fh+fh*.20
            for col in range(cols):
                x=col*cw+cw*.24
                ww, hh=cw*.49, fh*.49
                glass=(65,81,86) if rng.random()>.18 else (111,119,114)
                d.rectangle((x-1,y-1,x+ww+1,y+hh+1),fill=(194,193,179))
                d.rectangle((x,y,x+ww,y+hh),fill=glass)
                if ww>7: d.line((x+ww*.55,y,x+ww*.55,y+hh),fill=(175,181,173))
                if index < 12 and col%4 == 2:
                    d.rectangle((x-1,y+hh*.6,x+ww+1,y+hh+max(1,fh*.16)),fill=tuple(max(0,c-25) for c in color))
        d.rectangle((0,109,240,112),fill=(102,107,102))
        if index >= 16:
            for x in (25,125,195):
                d.rectangle((x,69,x+25,110),fill=(89,99,101))
                for y in range(73,109,5):d.line((x,y,x+25,y),fill=(114,122,121))
        elif index >= 12:
            d.rectangle((110,110-112*2.1/height,136,110),fill=(83,79,67))
        else:
            for x in range(30,240,60):
                d.rectangle((x,103,x+5,110),fill=(76,82,79))
        x,y=index%4*256,index//4*128
        # Extruded edge colors reduce bleeding through lower mip levels.
        im.paste(tile.resize((256,128)),(x,y))
        im.paste(tile,(x+8,y+8))
    palette=[(84,88,84),(112,73,59),(102,114,109),(78,88,97),(130,133,122),(65,82,89),(145,143,126),(99,103,98)]
    for j,color in enumerate(palette,20):
        x,y=j%4*256,j//4*128
        tile=Image.new('RGBA',(256,128),(*color,255)); d=ImageDraw.Draw(tile)
        for k in range(12,256,24):d.line((k,0,k,128),fill=tuple(max(0,c-10) for c in color))
        im.paste(tile,(x,y))
    im.save(SRC/'kyiv_diffuse.png')
    save_dds(im,OUT/'kyiv_diffuse.dds')
    save_dds(Image.new('RGBA',(1024,1024),(128,128,0,128)),OUT/'kyiv_normal.dds')
    save_dds(Image.new('RGBA',(1024,1024),(0,55,12,70)),OUT/'kyiv_specular.dds')


class Geometry:
    def __init__(self):
        self.p=[];self.n=[];self.uv=[];self.tri=[];self.ta=[]

    def face(self, points, tile, u=1., v=1.):
        points=np.asarray(points,dtype=float)
        normal=np.cross(points[1]-points[0],points[2]-points[0]);normal/=np.linalg.norm(normal)
        uv=np.asarray(rect_uv(tile,u,v)[:len(points)])
        e1,e2=points[1]-points[0],points[2]-points[0]
        a,b=uv[1]-uv[0],uv[2]-uv[0];det=a[0]*b[1]-a[1]*b[0]
        tangent=(e1*b[1]-e2*a[1])/det;tangent/=np.linalg.norm(tangent)
        bitangent=(-e1*b[0]+e2*a[0])/det
        handed=1 if np.dot(np.cross(normal,tangent),bitangent)>=0 else -1
        offset=len(self.p)
        self.p.extend(points.tolist());self.n.extend([normal.tolist()]*len(points))
        self.uv.extend(uv.tolist());self.ta.extend([[*tangent,handed]]*len(points))
        self.tri.extend([offset,offset+1,offset+2])
        if len(points)==4:self.tri.extend([offset,offset+2,offset+3])

    def box(self,x,z,w,d,h,tile,roof=20,base=0,ref=None,v=1.):
        a,b=x-w/2,x+w/2;c,e=z-d/2,z+d/2;y=base+h
        ref=ref or w
        self.face([(a,base,c),(a,base,e),(a,y,e),(a,y,c)],tile,min(d/ref,1),v)
        self.face([(b,base,e),(b,base,c),(b,y,c),(b,y,e)],tile,min(d/ref,1),v)
        self.face([(a,base,e),(b,base,e),(b,y,e),(a,y,e)],tile,min(w/ref,1),v)
        self.face([(b,base,c),(a,base,c),(a,y,c),(b,y,c)],tile,min(w/ref,1),v)
        self.face([(a,y,c),(a,y,e),(b,y,e),(b,y,c)],roof)
        self.face([(a,base,e),(a,base,c),(b,base,c),(b,base,e)],20)

    def roof(self,w,d,y,rise,style,tile):
        a,b=-w/2-.25,w/2+.25;c,e=-d/2-.25,d/2+.25
        inset=min(d*.5,w*.2) if style=='hip' else 0
        left,right=(a+inset,y+rise,0),(b-inset,y+rise,0)
        self.face([(a,y,c),left,right,(b,y,c)],tile)
        self.face([(b,y,e),right,left,(a,y,e)],tile)
        self.face([(a,y,e),left,(a,y,c)],tile)
        self.face([(b,y,c),right,(b,y,e)],tile)


def building(index,spec):
    name,label,w,d,h,floors,style,color=spec
    g=Geometry()
    if style=='step':
        g.box(-w/4,0,w/2,d,h,index,ref=w)
        g.box(w/4,2,w/2,d,h-6,index,ref=w,v=(h-6)/h)
    else:g.box(0,0,w,d,h,index)
    if style=='ell':g.box(-w/2+d/2,d, d,d,h,index,ref=w)
    if style in ('gable','hip'):
        g.roof(w,d,h,min(d*.27,3.6),style,21 if index%2 else 22)
    elif style=='saw':
        for k in range(5):
            z=-d/2+k*d/5;e=z+d/5
            g.face([(-w/2,h,z),(-w/2,h+2.2,e),(w/2,h+2.2,e),(w/2,h,z)],23)
            g.face([(w/2,h,e),(w/2,h+2.2,e),(-w/2,h+2.2,e),(-w/2,h,e)],25)
            g.face([(-w/2,h,z),(-w/2,h,e),(-w/2,h+2.2,e)],24)
            g.face([(w/2,h,e),(w/2,h,z),(w/2,h+2.2,e)],24)
    else:
        # Roof silhouette only: one plant-room block; no small vents/rails/pipes.
        g.box(-w*.15,0,max(3,w*.18),d*.4,1.7,24,20,base=h)
    if 12<=index<16:g.box(w*.19,0,.75,.85,2,24,20,base=h+1)
    # Recenter every footprint, including asymmetric variants, at ground level.
    p=np.array(g.p);shift=(p.min(0)+p.max(0))/2;shift[1]=0
    g.p=(p-shift).tolist()
    return g


def export(g,name,path,diff='kyiv_diffuse.dds'):
    p=np.array(g.p)
    root=Node('File',pdxasset=('i',[1,0]))
    mesh=root.add('object').add(name).add('mesh',**{key:('f',np.array(values).ravel().tolist()) for key,values in [('p',g.p),('n',g.n),('u0',g.uv),('ta',g.ta)]},tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvancedSnow']),diff=('s',[diff]),n=('s',['kyiv_normal.dds']),spec=('s',['kyiv_specular.dds']))
    root.add('locator')
    path.write_bytes(encode(root))


def obj(g,name):
    lines=['# Metres; Y up; ground-centred pivot.', 'mtllib kyiv.mtl',f'o {name}','usemtl kyiv']
    lines += ['v '+' '.join(f'{v:.6f}' for v in p) for p in g.p]
    lines += [f'vt {u:.7f} {1-v:.7f}' for u,v in g.uv]
    lines += ['vn '+' '.join(f'{v:.7f}' for v in n) for n in g.n]
    lines += ['f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i:i+3]) for i in range(0,len(g.tri),3)]
    (SRC/f'{name}.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def validate(records):
    assert len(records)==20 and len({r['name'] for r in records})==20
    for record in records:
        path=OUT/(record['name']+'.mesh');root=read(path)
        assert encode(root)==path.read_bytes()
        mesh=root.child('object').children[0].child('mesh')
        p=np.array(mesh.get('p')).reshape(-1,3);n=np.array(mesh.get('n')).reshape(-1,3)
        uv=np.array(mesh.get('u0')).reshape(-1,2);t=np.array(mesh.get('tri')).reshape(-1,3)
        assert np.isfinite(p).all() and t.min()>=0 and t.max()<len(p)
        assert np.allclose(np.linalg.norm(n,axis=1),1,atol=1e-5)
        assert uv.min()>=0 and uv.max()<=1 and p[:,1].min()==0
        cross=np.cross(p[t[:,1]]-p[t[:,0]],p[t[:,2]]-p[t[:,0]])
        assert (np.sum(cross*n[t[:,0]],axis=1)>1e-7).all()
        assert np.allclose((p.min(0)+p.max(0))[[0,2]],0,atol=1e-5)
        for prop in ['diff','n','spec']:assert (OUT/mesh.child('material').get(prop)[0]).exists()
    expected=128+sum((1024>>i)**2*4 for i in range(11))
    for path in OUT.glob('*.dds'):
        raw=path.read_bytes();assert len(raw)==expected and struct.unpack_from('<I',raw,28)[0]==11
    print('PASS: 20 static meshes; indices, winding, normals, UVs, pivots, material paths and full DDS mip chains.')


def main():
    OUT.mkdir(parents=True,exist_ok=True);SRC.mkdir(parents=True,exist_ok=True)
    atlas();records=[];geometries=[];gfx=['objectTypes = {'];entities=[]
    for i,spec in enumerate(SPECS):
        name='kyiv_'+spec[0];g=building(i,spec);geometries.append(g)
        export(g,name,OUT/f'{name}.mesh');obj(g,name)
        records.append(dict(name=name,label=spec[1],floors=spec[5],dimensions_m=np.ptp(g.p,axis=0).round(2).tolist(),triangles=len(g.tri)//3,vertices=len(g.p)))
        gfx.append(f'    pdxmesh = {{ name = "{name}_mesh" file = "gfx/models/buildings/kyiv/{name}.mesh" }}')
        entities.append(f'entity = {{ name = "{name}_entity" pdxmesh = "{name}_mesh" scale = 0.025 }}')
    gfx.append('}')
    (ROOT/'gfx/entities/kyiv_buildings.gfx').write_text('\n'.join(gfx)+'\n',encoding='utf-8')
    (ROOT/'gfx/entities/kyiv_buildings.asset').write_text('# Static kit: same conversion for every building; source units are metres.\n'+'\n'.join(entities)+'\n',encoding='utf-8')
    (SRC/'kyiv.mtl').write_text('newmtl kyiv\nKd 1 1 1\nKs 0 0 0\nmap_Kd kyiv_diffuse.png\n',encoding='utf-8')
    (HERE/'manifest.json').write_text(json.dumps(dict(units='metres',up_axis='Y',entity_scale=0.025,buildings=records),indent=2)+'\n',encoding='utf-8')
    validate(records)
    sheet=Image.new('RGB',(2000,2000),(233,235,231))
    for i,record in enumerate(records):
        thumb=render((-8,7,10),(500,400),f'{i+1:02} / {record["name"].removeprefix("kyiv_")}',OUT/(record['name']+'.mesh'))
        sheet.paste(thumb,(i%4*500,i//4*400))
    sheet.save(HERE/'catalog.png')
    # Same-scale neighborhood uses the exported geometry, with repeated instances.
    scene=Geometry()
    for row in range(6):
        for col in range(6):
            i=(row*6+col)%20;g=geometries[i];offset=len(scene.p)
            scene.p.extend((np.array(g.p)+[col*85,0,row*65]).tolist())
            scene.n.extend(g.n);scene.uv.extend(g.uv);scene.ta.extend(g.ta)
            scene.tri.extend([t+offset for t in g.tri])
    temp=HERE/'preview_scene.mesh'
    export(scene,'preview_only',temp,'../../gfx/models/buildings/kyiv/kyiv_diffuse.dds')
    render((-6,11,8),(1800,1300),'KYIV / 20 BUILDING TYPES / COMMON SCALE',temp).save(HERE/'neighborhood.png')
    temp.unlink()
    print(json.dumps(records,indent=2))


if __name__=='__main__':main()
