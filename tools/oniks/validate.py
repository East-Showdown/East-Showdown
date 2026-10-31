"""Validate the delivered binary geometry, textures, GLB, and resource bindings."""
from pathlib import Path
import json,math,struct
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"flamingo"))
from pdx_io import read,encode
ROOT=Path(__file__).resolve().parent
MOD=ROOT.parents[1]
GAME=MOD/'gfx/models/units/missiles/oniks'
root=read(GAME/'oniks_white.mesh');assert encode(root)==(GAME/'oniks_white.mesh').read_bytes()
obj=root.child('object').children[0];m=obj.child('mesh')
rows=lambda a,n:[a[i:i+n] for i in range(0,len(a),n)]
p=rows(m.get('p'),3);n=rows(m.get('n'),3);t=rows(m.get('ta'),4);uv=rows(m.get('u0'),2);faces=rows(m.get('tri'),3)
sub=lambda a,b:[x-y for x,y in zip(a,b)]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
cross=lambda a,b:[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
length=lambda a:math.sqrt(dot(a,a))
assert len(p)==len(n)==len(t)==len(uv) and len(faces)==6400
assert all(math.isfinite(v) for seq in (p,n,t,uv) for row in seq for v in row)
assert all(abs(length(row)-1)<1e-4 for row in n)
assert all(abs(length(row[:3])-1)<1e-4 and abs(row[3])==1 for row in t)
assert all(abs(dot(nn,tt[:3]))<1e-4 for nn,tt in zip(n,t))
areas=[];uv_areas=[]
for f in faces:
 assert len(set(f))==3 and all(0<=i<len(p) for i in f)
 a,b,c=[p[i] for i in f];area=length(cross(sub(b,a),sub(c,a)))/2;assert area>1e-12;areas.append(area)
 a,b,c=[uv[i] for i in f];e1=sub(b,a);e2=sub(c,a);ua=abs(e1[0]*e2[1]-e1[1]*e2[0]);assert ua>1e-12;uv_areas.append(ua)
assert all(0<=v<=1 for row in uv for v in row)
bounds=[[min(v[i] for v in p) for i in range(3)],[max(v[i] for v in p) for i in range(3)]]
for side,key in enumerate(('min','max')):assert all(abs(a-b)<1e-6 for a,b in zip(bounds[side],m.child('aabb').get(key)))
assert abs(bounds[1][2]-bounds[0][2]-10)<.001
assert obj.child('skeleton').child('root').get('ix')==[0]
assert m.child('skin').get('w')==[1.,0.,0.,0.]*len(p)
for suffix,pixel in [('diffuse',bytes((246,246,246,255))),('normal',bytes((0,128,128,128))),('specular',bytes((0,97,0,128)))]:
 path=GAME/f'oniks_white_{suffix}.dds';raw=path.read_bytes();assert raw[:4]==b'DDS '
 h=struct.unpack_from('<31I',raw,4);assert h[0]==124 and h[2:4]==(64,64) and h[6]==7
 assert len(raw)==128+4*sum((64>>i)**2 for i in range(7))
 assert raw[128:]==pixel*(len(raw[128:])//4)
mat=m.child('material')
for key in ('diff','n','spec'):assert (GAME/mat.get(key)[0]).is_file()
anim=read(GAME/'oniks_white_idle.anim');assert encode(anim)==(GAME/'oniks_white_idle.anim').read_bytes()
assert anim.child('info').get('j')==[1] and len(anim.child('samples').get('q'))==8
raw=(ROOT/'source/oniks_white.glb').read_bytes();magic,version,size=struct.unpack_from('<III',raw);assert magic==0x46546c67 and version==2 and size==len(raw)
size,kind=struct.unpack_from('<II',raw,12);gltf=json.loads(raw[20:20+size]);primitives=gltf['meshes'][0]['primitives']
assert sum(gltf['accessors'][v['indices']]['count']//3 for v in primitives)==len(faces)
assert 'images' not in gltf
assert gltf['materials'][0]['pbrMetallicRoughness']['baseColorFactor'][:3]==[0.9200000166893005]*3
gfx=(MOD/'gfx/entities/rus_oniks.gfx').read_text();asset=(MOD/'gfx/entities/rus_oniks.asset').read_text()
assert 'gfx/models/units/missiles/oniks/oniks_white.mesh' in gfx and 'rus_oniks_mesh' in asset
assert 'rus_oniks_pose_animation' in gfx and 'rus_oniks_pose_animation' in (GAME/'oniks_animations.asset').read_text()
report={'status':'PASS','triangles':len(faces),'export_vertices':len(p),'bounds':bounds,'minimum_triangle_area':min(areas),'checks':['binary mesh and animation roundtrip','finite positions, normals, UVs, tangents','unit normals and orthogonal tangent basis','nondegenerate mesh and UV triangles','index bounds, AABB, root skin weights','all DDS mip levels and uniform white diffuse','flat normal texture, no emissive channel','GLB triangle count and plain white material','mesh, texture, animation, entity references'],'visual_review':['perspective','side','rear','hoi4_scale'],'game_launched':False,'equipment':'rus_medium_guided_missile_oniks','entity':'rus_oniks_entity'}
import re
equipment=(MOD/'common/units/equipment/ES_rus_sea_guided_missile_equipment.txt').read_text(encoding='utf-8-sig')
block=re.search(r'\brus_medium_guided_missile_oniks\s*=\s*\{[^}]*\}',equipment).group()
assert 'sprite = rus_oniks' in block
technology=(MOD/'common/technologies/missiles_rus.txt').read_text(encoding='utf-8-sig')
technology=re.sub(r'#[^\r\n]*','',technology)
assert re.search(r'\bmissile_rus_3M55\s*=\s*\{\s*enable_equipments\s*=\s*\{\s*rus_medium_guided_missile_oniks\s*\}',technology)
assert 'name = "rus_oniks_entity"' in asset and 'default_state = "idle"' in asset
states=dict(re.findall(r'state\s*=\s*\{\s*name\s*=\s*"([^"]+)"\s+animation\s*=\s*"([^"]+)"',asset))
ids=set(re.findall(r'\bid\s*=\s*"([^"]+)"',gfx))
assert set(states.values())<=ids and {'idle','launch','move','bomb'}<=states.keys()
assert set(re.findall(r'next_state\s*=\s*"([^"]+)"',asset))<=states.keys()
for content in (asset,gfx,(GAME/'oniks_animations.asset').read_text()):
 assert content.count('{')==content.count('}')
all_assets='\n'.join(p.read_text(encoding='utf-8-sig',errors='replace') for p in (MOD/'gfx').rglob('*.asset'))
all_gfx='\n'.join(p.read_text(encoding='utf-8-sig',errors='replace') for p in (MOD/'gfx/entities').glob('*.gfx'))
assert len(re.findall(r'\bname\s*=\s*"rus_oniks_entity"',all_assets))==1
assert len(re.findall(r'\bname\s*=\s*"rus_oniks_pose_animation"',all_assets))==1
assert len(re.findall(r'\bname\s*=\s*"rus_oniks_mesh"',all_gfx))==1
report['checks'].extend(['Oniks equipment and technology binding','unique model/entity/animation registration','state and animation references'])
(ROOT/'validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
