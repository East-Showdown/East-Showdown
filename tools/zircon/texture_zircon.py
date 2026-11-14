"""Procedural UV materials for the Zircon exterior; no reference photo sampling."""
import numpy as np
from PIL import Image, ImageDraw


def make_textures(source, directory, regions, size, save_dds):
    rng = np.random.default_rng(322)
    color = Image.new('RGB', (size, size), (177, 181, 180))
    height = Image.new('L', (size, size), 128)
    rough = Image.new('L', (size, size), 157)
    metal = Image.new('L', (size, size), 35)
    d, h, r, m = [ImageDraw.Draw(im) for im in (color, height, rough, metal)]

    def fill(name, c, rr, mm):
        box = regions[name]
        d.rectangle(box, fill=c); r.rectangle(box, fill=rr); m.rectangle(box, fill=mm)

    def panel_tiles(box, pitch_x=24, pitch_y=22):
        x0, y0, x1, y1 = box
        for row, y in enumerate(range(y0, y1, pitch_y)):
            for x in range(x0 - (pitch_x//2 if row % 2 else 0), x1, pitch_x):
                a, b = max(x0, x+1), min(x1, x+pitch_x-1)
                if b <= a:
                    continue
                shade = int(rng.integers(55, 63))
                c = (shade, shade+1, shade)
                bottom = min(y1, y+pitch_y-1)
                d.rectangle((a, y+1, b, bottom), fill=c)
                h.rectangle((a, y+1, b, bottom), fill=128)
                h.line((a, y, b, y), fill=121)
                if b-a > 10 and bottom-y > 10:
                    d.line((a+3,y+8,b-3,y+8), fill=(48,51,52))
                    for xx in (a+3,b-3):
                        d.point((xx,bottom-3), fill=(74,78,77))

    fill('body',(198,204,202),180,18)
    x0,y0,x1,y1 = regions['body']
    zpx = lambda z: int(round(x0+(z+5)/10*(x1-x0)))
    # Main UV island: horizontal axis along the missile, vertical axis around it.
    # The dark thermal-looking lower skin ends where the faceted body meets collar.
    lower = y0+(y1-y0)//2
    d.rectangle((x0,lower,zpx(1.38),y1),fill=(56,60,61))
    panel_tiles((x0,lower,zpx(1.38),y1),42,28)
    r.rectangle((x0,lower,zpx(1.43),y1),fill=194)
    m.rectangle((x0,lower,zpx(1.43),y1),fill=42)
    # Continuous boundary at the geometric chine: no stepped strips or notches.
    # Color is unlit albedo. There is no AO, directional shading or cast shadow.
    for za,zb,c,rr,mm in [(-5,-4.68,(75,83,87),166,85),
                         (1.38,2.62,(188,197,198),169,45),
                         (2.62,4.10,(194,202,201),182,22),
                         (4.10,4.70,(181,192,194),171,48)]:
        box=(zpx(za),y0,zpx(zb),y1)
        d.rectangle(box,fill=c);r.rectangle(box,fill=rr);m.rectangle(box,fill=mm)
    for z in (-4.68,-2.52,-1.1,.4,1.38,2.62,4.1,4.5):
        x=zpx(z)
        end=lower-1 if -4.6<z<1.38 else y1
        c=(183,190,188) if z<1.38 else (161,173,176)
        d.line((x,y0,x,end),fill=c,width=1)
        h.line((x,y0,x,end),fill=120,width=1)
    # Rear ring fasteners and access covers are pixels, not separate geometry.
    for z in (2.64,4.48):
        x=zpx(z)
        for y in range(y0+5,y1-3,24):
            d.point((x,y),fill=(142,155,158));h.point((x,y),fill=138)
    # Crisp shallow service panels. The +X panel wraps across the cylindrical UV
    # seam; all detail is painted/normal mapped on the unmodified transition skin.
    for image,panel_fill,outline in [(color,(175,186,189),(121,137,143)),
                               (height,126,116),(rough,173,180),(metal,40,45)]:
        patch=image.crop((x0,y0,x1+1,y1+1));draw=ImageDraw.Draw(patch)
        for v in (0,.5,1):
            cy=round(v*(y1-y0));half=round(.075*(y1-y0))
            box=(zpx(1.96)-x0,cy-half,zpx(2.43)-x0,cy+half)
            draw.rounded_rectangle(box,5,fill=panel_fill,outline=outline,width=2)
            if image is color:
                xx=box[0]+6
                for yy in range(box[1]+8,box[3]-7,13):
                    draw.point((xx,yy),fill=(142,155,158))
        image.paste(patch,(x0,y0))

    fill('belly',(56,60,61),194,26)
    panel_tiles(regions['belly'],55,35)
    bx,by,bx1,by1=regions['belly']
    fill('panel',(95,100,88),182,76)
    gx,gy,gx1,gy1=regions['panel']
    for x in range(gx,gx1,49):
        shade=int(rng.integers(-3,4))
        d.rectangle((x+2,gy+4,min(x+47,gx1),gy1-4),
                    fill=(95+shade,100+shade,88+shade))
        d.line((x,gy,x,gy1),fill=(80,86,78),width=1)
        h.line((x,gy,x,gy1),fill=120,width=1)
    for y in (gy+3,gy1-3):
        d.line((gx,y,gx1,y),fill=(82,88,79),width=1)

    fill('fin',(93,104,108),178,38)
    fx,fy,fx1,fy1=regions['fin']
    d.polygon([(fx+12,fy+20),(fx1-10,fy+20),(fx1-26,fy1-14),(fx+12,fy1-26)],
              fill=(84,95,99))
    d.line((fx+8,fy+8,fx1-8,fy+8),fill=(78,88,93),width=1)
    fill('metal',(125,139,146),153,115)
    fill('rim',(74,86,93),167,92)
    fill('inside',(34,41,46),201,40)
    fill('shadow',(9,12,15),225,0)
    fill('dark',(49,56,59),190,32)
    fill('white',(184,194,195),179,40)
    rx,ry,rx1,ry1=regions['rim']
    # Border dilation provides a safety margin around the packed UV islands.
    for im in (color,height,rough,metal):
        for x0,y0,x1,y1 in regions.values():
            tile=np.array(im)[y0:y1+1,x0:x1+1]
            pads=((8,8),(8,8))+(((0,0),) if tile.ndim==3 else ())
            im.paste(Image.fromarray(np.pad(tile,pads,mode='edge')),(x0-8,y0-8))
    pixels=np.array(color,dtype=float)
    pixels+=rng.normal(0,.40,(size,size,1))
    # Very slight grain survives close-ups without looking like heavy corrosion.
    color=Image.fromarray(np.clip(pixels,0,255).astype('uint8'))
    heights=np.array(height,dtype=float)/255
    dy,dx=np.gradient(heights)
    normal=np.dstack((-dx*1.2,dy*1.2,np.ones_like(dx)))
    normal/=np.linalg.norm(normal,axis=2)[:,:,None]
    normal_rgb=np.clip((normal*.5+.5)*255,0,255).astype('uint8')
    for suffix,im in [('basecolor',color),('roughness',rough),('metallic',metal),
                      ('normal',Image.fromarray(normal_rgb))]:
        im.save(source/f'zircon_{suffix}.png')
    packed=np.full((size,size,4),[128,128,0,128],dtype='uint8')
    packed[:,:,1]=normal_rgb[:,:,1];packed[:,:,3]=normal_rgb[:,:,0]
    spec=np.zeros((size,size,4),dtype='uint8')
    spec[:,:,1]=255-np.array(rough);spec[:,:,2]=np.array(metal);spec[:,:,3]=128
    for suffix,im in [('diffuse',color),('normal',Image.fromarray(packed)),
                      ('specular',Image.fromarray(spec))]:
        save_dds(im,directory/f'zircon_{suffix}.dds')
