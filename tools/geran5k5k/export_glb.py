"""Portable, single-object GLB with embedded PBR textures from the game export."""
from io import BytesIO
import json
from pathlib import Path
import struct
import sys
import numpy as np
from PIL import Image

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent/'flamingo'))
from pdx_io import read


def export():
    mesh=read(ROOT/'gfx/models/units/missiles/geran5k5k/geran5k5k.mesh').child('object').children[0].child('mesh')
    data=bytearray();views=[];accessors=[]
    def view(payload,target=None):
        while len(data)%4:data.append(0)
        entry=dict(buffer=0,byteOffset=len(data),byteLength=len(payload))
        if target:entry['target']=target
        views.append(entry);data.extend(payload)
        return len(views)-1
    def accessor(key,width,kind):
        array=np.array(mesh.get(key),dtype='<f4').reshape(-1,width)
        entry=dict(bufferView=view(array.tobytes(),34962),componentType=5126,
                   count=len(array),type=kind)
        if key=='p':entry.update(min=array.min(0).tolist(),max=array.max(0).tolist())
        accessors.append(entry)
        return len(accessors)-1
    attrs={name:accessor(key,width,kind) for name,key,width,kind in
           [('POSITION','p',3,'VEC3'),('NORMAL','n',3,'VEC3'),
            ('TEXCOORD_0','u0',2,'VEC2'),('TANGENT','ta',4,'VEC4')]}
    index=np.array(mesh.get('tri'),dtype='<u2')
    accessors.append(dict(bufferView=view(index.tobytes(),34963),componentType=5123,
                          count=len(index),type='SCALAR'))
    index_accessor=len(accessors)-1
    base=Image.open(HERE/'geran5k5k_basecolor.png').convert('RGB')
    normal=Image.open(HERE/'geran5k5k_normal.png').convert('RGB')
    packed=np.full((1024,1024,3),255,dtype=np.uint8)
    packed[:,:,1]=np.array(Image.open(HERE/'geran5k5k_roughness.png'))
    packed[:,:,2]=np.array(Image.open(HERE/'geran5k5k_metallic.png'))
    images=[]
    for image,name in [(base,'Base color'),(normal,'Tangent normal'),
                       (Image.fromarray(packed),'Metallic roughness')]:
        stream=BytesIO();image.save(stream,format='PNG')
        images.append(dict(bufferView=view(stream.getvalue()),mimeType='image/png',name=name))
    document={
        'asset':{'version':'2.0','generator':'Geran-5K5-K exterior game-art exporter'},
        'scene':0,'scenes':[{'nodes':[0]}],
        'nodes':[{'name':'Geran-5K5-K','mesh':0}],
        'meshes':[{'name':'Geran-5K5-K','primitives':[{'attributes':attrs,
                   'indices':index_accessor,'material':0,'mode':4}]}],
        'materials':[{'name':'geran5k5k','pbrMetallicRoughness':{
            'baseColorTexture':{'index':0},'metallicRoughnessTexture':{'index':2}},
            'normalTexture':{'index':1},'alphaMode':'OPAQUE','doubleSided':False}],
        'textures':[{'source':i,'sampler':0} for i in range(3)],
        'samplers':[{'magFilter':9729,'minFilter':9987,'wrapS':10497,'wrapT':10497}],
        'images':images,'accessors':accessors,'bufferViews':views,
        'buffers':[{'byteLength':len(data)}],
        'extras':{'purpose':'Exterior game art in arbitrary units; symmetric hidden-side reconstruction.'},
    }
    js=json.dumps(document,separators=(',',':')).encode()
    js+=b' '*((-len(js))%4);data+=b'\0'*((-len(data))%4)
    binary=struct.pack('<4sII',b'glTF',2,12+8+len(js)+8+len(data))
    binary+=struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(data),b'BIN\0')+data
    path=HERE/'geran5k5k.glb';path.write_bytes(binary)
    print(f'GLB: {len(index)//3} triangles, one object, one material, three embedded PBR maps.')


if __name__=='__main__':export()
