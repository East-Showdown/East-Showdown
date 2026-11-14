"""One unlit 1024px atlas. Panel detail is drawn, not sampled from photographs."""
import numpy as np
from PIL import Image, ImageDraw


def make_textures(source, directory, regions, size, save_dds):
    rng = np.random.default_rng(505)
    color = Image.new('RGB',(size,size),(39,43,47))
    height = Image.new('L',(size,size),128)
    rough = Image.new('L',(size,size),180)
    metal = Image.new('L',(size,size),20)
    d,h,r,m = [ImageDraw.Draw(im) for im in (color,height,rough,metal)]
    x0,y0,x1,y1 = regions['body']
    zpx = lambda z: round(y0+(z+5)/10*(y1-y0))
    upx = lambda u: round(x0+u*(x1-x0))
    # Variation is per physical panel; there are no directional gradients or AO.
    seams = [-4.78,-4.00,-2.65,-2.50,-.85,-.68,1.38,1.50,2.62,2.90,3.70,4.67]
    limits = [-5]+seams+[4.75]
    for i,(a,b) in enumerate(zip(limits,limits[1:])):
        shade = int(rng.integers(-1,2))
        d.rectangle((x0,zpx(a),x1,zpx(b)),fill=(39+shade,43+shade,47+shade))
    for z in seams:
        y = zpx(z)
        d.line((x0,y,x1,y),fill=(29,33,36))
        h.line((x0,y,x1,y),fill=115)
        if z in (-4.78,-2.50,-.68,1.50,3.70):
            for x in range(x0+9,x1,24):
                d.point((x,y+4),fill=(60,64,67)); h.point((x,y+4),fill=136)
    # Two clean longitudinal joints, away from the texture wrap.
    for u in (.25,.75):
        x = upx(u)
        d.line((x,zpx(-3.95),x,zpx(4.3)),fill=(34,38,42))
        h.line((x,zpx(-3.95),x,zpx(4.3)),fill=121)

    def panel(center,za,zb,half=.075,framed=False):
        # Draw across the wrapped seam too: both sides have the same clean cover.
        box = (upx(center-half),zpx(za),upx(center+half),zpx(zb))
        for im,fill,outline in ((color,(36,40,44),(66,70,72) if framed else (27,31,34)),
                                (height,127,115),(rough,183,160 if framed else 186),
                                (metal,20,78 if framed else 20)):
            patch = Image.new(im.mode,(size*3,size),0)
            # Crop after drawing allows the edge-side panel to wrap seamlessly.
            draw = ImageDraw.Draw(patch)
            shifted = (box[0]+size,box[1],box[2]+size,box[3])
            draw.rounded_rectangle(shifted,4,fill=fill,outline=outline,width=2 if framed else 1)
            # Copy only the bounded patch area; do not overwrite the body base.
            bx0,by0,bx1,by1 = box
            small=patch.crop((bx0+size,by0,bx1+size+1,by1+1))
            im.paste(small,(bx0,by0))
        if framed:
            inner = (box[0]+4,box[1]+4,box[2]-4,box[3]-4)
            d.rounded_rectangle(inner,3,outline=(25,29,33),width=1)
            for yy in (box[1]+7,box[3]-7):
                for xx in (box[0]+5,box[2]-5):
                    d.ellipse((xx-1,yy-1,xx+1,yy+1),fill=(73,76,78))
        else:
            for xx in (box[0]+3,box[2]-3):
                for yy in (box[1]+4,box[3]-4):
                    d.point((xx,yy),fill=(56,60,63))

    # Put flank panels at u=.5 and u=0/1 (the +X seam). Draw on a temporary
    # unclipped body tile so the wrapped portions stay inside the body island.
    originals=[im.copy() for im in (color,height,rough,metal)]
    for u in (0,.5,1):
        panel(u,-1.95,-.85,half=.09)
        panel(u,-.55,.25,half=.075)
        panel(u,1.72,2.51,half=.075,framed=True)
        panel(u,2.81,3.14,half=.037)
        panel(u,3.18,3.64,half=.075)
    for im,base in zip((color,height,rough,metal),originals):
        body=im.crop((x0,y0,x1+1,y1+1));im.paste(base);im.paste(body,(x0,y0))
    # Small nose markings represent external surface apertures, with no internals.
    for u in (.08,.42,.58,.92):
        xx,yy=upx(u),zpx(-4.96)
        d.ellipse((xx-2,yy-1,xx+2,yy+2),fill=(20,24,27))
        h.ellipse((xx-2,yy-1,xx+2,yy+2),fill=119)

    def fill(name,c,rr,mm):
        box=regions[name];d.rectangle(box,fill=c);r.rectangle(box,fill=rr);m.rectangle(box,fill=mm)
    for name in ('fin','tail'):
        fill(name,(33,37,40),182,22)
        fx,fy,fx1,fy1=regions[name]
        # Subtle trailing-panel joint; no high-contrast markings or decorative wear.
        xx=fx+int((fx1-fx)*.79)
        d.line((xx,fy+12,xx,fy1-12),fill=(28,32,35))
        h.line((xx,fy+12,xx,fy1-12),fill=119)
    fill('metal',(104,102,97),158,164)
    fill('rim',(119,119,114),148,170)
    fill('inside',(32,31,29),202,92)
    fill('shadow',(12,13,14),224,8)
    # Pad every island by eight pixels before generating mip levels.
    for im in (color,height,rough,metal):
        for ax,ay,bx,by in regions.values():
            tile=np.array(im)[ay:by+1,ax:bx+1]
            pads=((8,8),(8,8))+(((0,0),) if tile.ndim==3 else ())
            im.paste(Image.fromarray(np.pad(tile,pads,mode='edge')),(ax-8,ay-8))
    pixels=np.array(color,dtype=float)+rng.normal(0,.32,(size,size,1))
    color=Image.fromarray(np.clip(pixels,0,255).astype('uint8'))
    dy,dx=np.gradient(np.array(height,dtype=float)/255)
    normal=np.dstack((-dx*1.8,dy*1.8,np.ones_like(dx)))
    normal/=np.linalg.norm(normal,axis=2)[:,:,None]
    normal_rgb=np.clip((normal*.5+.5)*255,0,255).astype('uint8')
    for suffix,im in [('basecolor',color),('roughness',rough),('metallic',metal),
                      ('normal',Image.fromarray(normal_rgb))]:
        im.save(source/f'geran5k5k_{suffix}.png')
    packed=np.full((size,size,4),[128,128,0,128],dtype='uint8')
    packed[:,:,1]=normal_rgb[:,:,1];packed[:,:,3]=normal_rgb[:,:,0]
    spec=np.zeros((size,size,4),dtype='uint8')
    spec[:,:,1]=255-np.array(rough);spec[:,:,2]=np.array(metal);spec[:,:,3]=128
    for suffix,im in [('diffuse',color),('normal',Image.fromarray(packed)),
                      ('specular',Image.fromarray(spec))]:
        save_dds(im,directory/f'geran5k5k_{suffix}.dds')
