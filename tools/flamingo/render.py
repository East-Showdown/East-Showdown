"""Render the exported mesh, using its actual diffuse texture and normals."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from pdx_io import read

HERE = Path(__file__).resolve().parent
MODEL = HERE.parents[1] / 'gfx/models/units/missiles/flamingo/flamingo.mesh'


def render(eye, size=(1400,900), label='FLAMINGO / UKRAINE', model=MODEL):
    model=Path(model)
    mesh=read(model).child('object').children[0].child('mesh')
    p=np.array(mesh.get('p')).reshape(-1,3)
    n=np.array(mesh.get('n')).reshape(-1,3)
    uv=np.array(mesh.get('u0')).reshape(-1,2)
    faces=np.array(mesh.get('tri')).reshape(-1,3)
    texture=np.array(Image.open(model.parent/mesh.child('material').get('diff')[0]).convert('RGB'))
    camera=np.array(eye,dtype=float);camera/=np.linalg.norm(camera)
    right=np.cross([0,1,0],camera);right/=np.linalg.norm(right)
    up=np.cross(camera,right);basis=np.array([right,up,camera]).T
    projected=p@basis
    low,high=projected[:,:2].min(0),projected[:,:2].max(0)
    w,h=size;scale=min((w-140)/(high[0]-low[0]),(h-200)/(high[1]-low[1]));center=(high+low)/2
    projected[:,0]=(projected[:,0]-center[0])*scale+w/2
    projected[:,1]=-(projected[:,1]-center[1])*scale+h/2+15
    # Ground shadow derived from the mesh silhouette, not a reference image.
    ground=p.copy();ground[:,1]=p[:,1].min()-.15
    ground=ground@basis
    ground[:,0]=(ground[:,0]-center[0])*scale+w/2
    ground[:,1]=-(ground[:,1]-center[1])*scale+h/2+15
    shadow=Image.new('L',size,0);draw=ImageDraw.Draw(shadow)
    if camera[1]>.15:
        for face in faces:draw.polygon([tuple(v) for v in ground[face,:2]],fill=30)
        shadow=shadow.filter(ImageFilter.GaussianBlur(15))
    canvas=np.full((h,w,3),[233,235,231],dtype=np.uint8)
    canvas=(canvas.astype(float)-np.array(shadow)[:,:,None]).clip(0,255).astype('uint8')
    depth=np.full((h,w),-np.inf)
    light=np.array([-.5,1.,-.7]);light/=np.linalg.norm(light)
    half=light+camera;half/=np.linalg.norm(half)
    for ids in faces:
        tri=projected[ids]
        x0,y0=np.maximum(np.floor(tri[:,:2].min(0)).astype(int),[0,0])
        x1,y1=np.minimum(np.ceil(tri[:,:2].max(0)).astype(int),[w-1,h-1])
        if x0>x1 or y0>y1:continue
        xx,yy=np.meshgrid(np.arange(x0,x1+1)+.5,np.arange(y0,y1+1)+.5)
        a,b,c=tri
        den=(b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1])
        if abs(den)<1e-10:continue
        w0=((b[1]-c[1])*(xx-c[0])+(c[0]-b[0])*(yy-c[1]))/den
        w1=((c[1]-a[1])*(xx-c[0])+(a[0]-c[0])*(yy-c[1]))/den
        w2=1-w0-w1;z=w0*a[2]+w1*b[2]+w2*c[2]
        zbuf=depth[y0:y1+1,x0:x1+1]
        mask=(w0>=0)&(w1>=0)&(w2>=0)&(z>zbuf)
        if not mask.any():continue
        weights=np.stack([w0[mask],w1[mask],w2[mask]],axis=1)
        coords=weights@uv[ids]
        tx=np.clip((coords[:,0]*texture.shape[1]).astype(int),0,texture.shape[1]-1)
        ty=np.clip((coords[:,1]*texture.shape[0]).astype(int),0,texture.shape[0]-1)
        normals=weights@n[ids];normals/=np.linalg.norm(normals,axis=1)[:,None]
        lambert=np.maximum(normals@light,0)
        spec=np.maximum(normals@half,0)**42
        colors=texture[ty,tx].astype(float)*(.62+.75*lambert[:,None])+spec[:,None]*48
        canvas[y0:y1+1,x0:x1+1][mask]=np.clip(colors,0,255).astype('uint8')
        zbuf[mask]=z[mask]
    result=Image.fromarray(canvas)
    draw=ImageDraw.Draw(result)
    draw.text((32,24),label,fill=(35,44,40),font_size=26)
    draw.text((32,h-36),f'EXPORTED GAME MESH / {len(faces):,} TRIANGLES',fill=(93,103,95),font_size=16)
    return result


if __name__ == '__main__':
    render((-10,6,-12)).save(HERE/'preview.png')
    views=[((-10,6,-12),'FRONT THREE-QUARTER'),((10,6,12),'REAR THREE-QUARTER'),
           ((-12,0,0),'SIDE'),((0,1,-18),'FRONT')]
    sheet=Image.new('RGB',(1600,1100))
    for i,(eye,label) in enumerate(views):
        sheet.paste(render(eye,(800,550),label),(i%2*800,i//2*550))
    sheet.save(HERE/'views.png')
