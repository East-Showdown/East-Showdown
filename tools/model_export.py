"""Shared export of rigid game-art meshes, DDS mip chains and editing OBJ files."""
from pathlib import Path
import sys
import struct
import numpy as np
from PIL import Image

sys.path.insert(0,str(Path(__file__).resolve().parent/'flamingo'))
from pdx_io import Node,encode,read


def textures(name,directory,source,colors):
    directory.mkdir(parents=True,exist_ok=True)
    diffuse=np.zeros((512,512,4),dtype='uint8');diffuse[:,:,3]=255
    spec=np.full((512,512,4),[0,75,32,95],dtype='uint8')
    rng=np.random.default_rng(5)
    for i,color in enumerate(colors):
        x,y=i%4*128,i//4*128
        diffuse[y:y+128,x:x+128,:3]=np.clip(np.array(color)+rng.normal(0,.22,(128,128,1)),0,255)
        if i in (5,6):spec[y:y+128,x:x+128]=[0,112,90,135]
    for suffix,pixels in [('diffuse',diffuse),('normal',np.full((512,512,4),[128,128,0,128],dtype='uint8')),('specular',spec)]:
        image=Image.fromarray(pixels);path=directory/f'{name}_{suffix}.dds';image.save(path)
        raw=bytearray(path.read_bytes())
        struct.pack_into('<I',raw,8,struct.unpack_from('<I',raw,8)[0]|0x20000)
        struct.pack_into('<I',raw,28,10);struct.pack_into('<I',raw,108,0x401008)
        for i in range(1,10):raw.extend(image.resize((512>>i,512>>i),Image.Resampling.BOX).tobytes('raw','BGRA'))
        path.write_bytes(raw)
    Image.fromarray(diffuse).save(source/f'{name}_diffuse.png')


def export_rigid(g,name,directory,source,exhaust):
    directory.mkdir(parents=True,exist_ok=True)
    p,n,uv=np.array(g.p),np.array(g.n),np.array(g.uv);tangents=[]
    for i in range(0,len(p),3):
        e1,e2=p[i+1]-p[i],p[i+2]-p[i];a,b=uv[i+1]-uv[i],uv[i+2]-uv[i]
        det=a[0]*b[1]-a[1]*b[0]
        tangent=(e1*b[1]-e2*a[1])/det if abs(det)>1e-10 else e1
        bitangent=(-e1*b[0]+e2*a[0])/det if abs(det)>1e-10 else e2
        for normal in n[i:i+3]:
            t=tangent-normal*np.dot(normal,tangent)
            if np.linalg.norm(t)<1e-9:t=np.cross(normal,[1,0,0] if abs(normal[0])<.9 else [0,1,0])
            t/=np.linalg.norm(t)
            tangents.extend([*t,1. if np.dot(np.cross(normal,t),bitangent)>=0 else -1.])
    root=Node('File',pdxasset=('i',[1,0]));obj=root.add('object').add(name)
    mesh=obj.add('mesh',p=('f',p.ravel().tolist()),n=('f',n.ravel().tolist()),ta=('f',tangents),
                 u0=('f',uv.ravel().tolist()),tri=('i',g.tri))
    mesh.add('aabb',min=('f',p.min(0).tolist()),max=('f',p.max(0).tolist()))
    mesh.add('material',shader=('s',['PdxMeshAdvanced']),diff=('s',[f'{name}_diffuse.dds']),
             n=('s',[f'{name}_normal.dds']),spec=('s',[f'{name}_specular.dds']))
    mesh.add('skin',bones=('i',[4]),ix=('i',[0,-1,-1,-1]*len(p)),w=('f',[1.,0.,0.,0.]*len(p)))
    obj.add('skeleton').add('root',ix=('i',[0]),tx=('f',[1.,0.,0.,0.,1.,0.,0.,0.,1.,0.,0.,0.]))
    root.add('locator').add('engine_exhaust',p=('f',list(exhaust)),q=('f',[1.,0.,0.,0.]),pa=('s',['root']))
    path=directory/f'{name}.mesh';path.write_bytes(encode(root));assert encode(read(path))==path.read_bytes()
    anim=Node('File',pdxasset=('i',[1,0]));info=anim.add('info',fps=('f',[30.]),sa=('i',[2]),j=('i',[1]))
    info.add('root',sa=('s',['q']),t=('f',[0.,0.,0.]),q=('f',[0.,0.,0.,1.]),s=('f',[1.]))
    anim.add('samples',q=('f',[0.,0.,0.,1.]*2));(directory/f'{name}_idle.anim').write_bytes(encode(anim))
    lines=[f'# {name} game art; Y up, nose -Z; arbitrary art units.',f'mtllib {name}.mtl']
    lines.extend('v '+' '.join(f'{x:.7f}' for x in row) for row in p)
    lines.extend(f'vt {u:.7f} {1-v:.7f}' for u,v in uv)
    lines.extend('vn '+' '.join(f'{x:.7f}' for x in row) for row in n)
    lines.append(f'usemtl {name}');previous=None
    for i,part in enumerate(g.part):
        if part!=previous:lines.append('g '+part);previous=part
        lines.append('f '+' '.join(f'{j+1}/{j+1}/{j+1}' for j in g.tri[i*3:i*3+3]))
    (source/f'{name}.obj').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    (source/f'{name}.mtl').write_text(f'newmtl {name}\nKd 1 1 1\nKs 0.15 0.15 0.15\nNs 32\nmap_Kd {name}_diffuse.png\n',encoding='utf-8')
    print(f'{name}: {len(g.tri)//3} triangles, {len(p)} vertices; exported mesh, DDS, pose and OBJ.')
