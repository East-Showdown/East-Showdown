"""Software preview of the exported mesh and its actual DDS textures.

Neutral studio lighting is approximate; this is not an HOI4 screenshot.
"""
from pathlib import Path
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from pdx_io import read

MODEL = ROOT / 'gfx/models/units/missiles/geran5k5k/geran5k5k.mesh'


def font(size):
    p = Path('C:/Windows/Fonts/arial.ttf')
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default(size=size)


def render(eye, size=(1500, 850), label='GERAN-5K5-K', wire=False, tail_detail=False, focus=None,
           model=MODEL, world_scale=1.0, frame_bounds=None):
    model=Path(model)
    mesh = read(model).child('object').children[0].child('mesh')
    p = np.array(mesh.get('p')).reshape(-1, 3)*world_scale
    n = np.array(mesh.get('n')).reshape(-1, 3)
    t = np.array(mesh.get('ta')).reshape(-1, 4)
    uv = np.array(mesh.get('u0')).reshape(-1, 2)
    faces = np.array(mesh.get('tri')).reshape(-1, 3)
    material = mesh.child('material')
    diffuse = np.array(Image.open(model.parent / material.get('diff')[0]).convert('RGB'))
    normalmap = np.array(Image.open(model.parent / material.get('n')[0]).convert('RGBA'))
    specular = np.array(Image.open(model.parent / material.get('spec')[0]).convert('RGBA'))
    camera = np.array(eye, dtype=float); camera /= np.linalg.norm(camera)
    right = np.cross([0, 1, 0], camera); right /= np.linalg.norm(right)
    up = np.cross(camera, right)
    if abs(camera[1])>.98:
        right,up=up,-right
    projected = p @ np.array([right, up, camera]).T
    framing = projected[p[:, 2] >= 2.38] if tail_detail else projected
    if focus=='intake':
        framing=projected[(p[:,2]>-2.65)&(p[:,2]<-1.4)&(p[:,1]<-.18)]
    elif focus=='nose':
        framing=projected[p[:,2]<=-2.52+1e-5]
    low, high = framing[:, :2].min(0), framing[:, :2].max(0)
    if frame_bounds is not None:
        low,high=np.asarray(frame_bounds[0]),np.asarray(frame_bounds[1])
    w, h = size
    scale = min((w - 140) / (high[0] - low[0]), (h - 170) / (high[1] - low[1]))
    center = (high + low) / 2
    projected[:, 0] = (projected[:, 0] - center[0]) * scale + w / 2
    projected[:, 1] = -(projected[:, 1] - center[1]) * scale + h / 2 + 15
    canvas = np.full((h, w, 3), [224, 228, 229], dtype='uint8')
    depth = np.full((h, w), -np.inf)
    light = camera * .55 + up * .65 - right * .45; light /= np.linalg.norm(light)
    half = light + camera; half /= np.linalg.norm(half)
    for ids in faces:
        if n[ids].mean(0) @ camera < -.05:
            continue
        tri = projected[ids]
        x0, y0 = np.maximum(np.floor(tri[:, :2].min(0)).astype(int), [0, 0])
        x1, y1 = np.minimum(np.ceil(tri[:, :2].max(0)).astype(int), [w - 1, h - 1])
        if x0 > x1 or y0 > y1:
            continue
        xx, yy = np.meshgrid(np.arange(x0, x1 + 1) + .5, np.arange(y0, y1 + 1) + .5)
        a, b, c = tri
        den = (b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])
        if abs(den) < 1e-10:
            continue
        w0 = ((b[1] - c[1]) * (xx - c[0]) + (c[0] - b[0]) * (yy - c[1])) / den
        w1 = ((c[1] - a[1]) * (xx - c[0]) + (a[0] - c[0]) * (yy - c[1])) / den
        w2 = 1 - w0 - w1
        z = w0 * a[2] + w1 * b[2] + w2 * c[2]
        zbuffer = depth[y0:y1 + 1, x0:x1 + 1]
        mask = (w0 >= 0) & (w1 >= 0) & (w2 >= 0) & (z > zbuffer)
        if not mask.any():
            continue
        weights = np.stack([w0[mask], w1[mask], w2[mask]], axis=1)
        coords = weights @ uv[ids]
        tx = np.clip((coords[:, 0] * diffuse.shape[1]).astype(int), 0, diffuse.shape[1] - 1)
        ty = np.clip((coords[:, 1] * diffuse.shape[0]).astype(int), 0, diffuse.shape[0] - 1)
        normals = weights @ n[ids]; normals /= np.linalg.norm(normals, axis=1)[:, None]
        tangent = weights @ t[ids, :3]
        tangent -= normals * np.sum(tangent * normals, axis=1)[:, None]
        tangent /= np.linalg.norm(tangent, axis=1)[:, None]
        bitangent = np.cross(normals, tangent) * np.sign(weights @ t[ids, 3])[:, None]
        nx = normalmap[ty, tx, 3] / 255 * 2 - 1
        ny = normalmap[ty, tx, 1] / 255 * 2 - 1
        nz = np.sqrt(np.maximum(1 - nx * nx - ny * ny, 0))
        normals = tangent * nx[:, None] + bitangent * ny[:, None] + normals * nz[:, None]
        lambert = np.maximum(normals @ light, 0)
        gloss = specular[ty, tx, 1] / 255
        spec = np.maximum(normals @ half, 0) ** (18 + gloss * 80)
        colors = diffuse[ty, tx].astype(float) * (.62 + .72 * lambert[:, None])
        colors += spec[:, None] * (12 + gloss[:, None] * 32)
        if wire:
            edge = np.minimum(np.minimum(w0[mask], w1[mask]), w2[mask]) < .055
            colors[edge] = [122, 181, 184]
        canvas[y0:y1 + 1, x0:x1 + 1][mask] = np.clip(colors, 0, 255).astype('uint8')
        zbuffer[mask] = z[mask]
    result = Image.fromarray(canvas)
    d = ImageDraw.Draw(result)
    d.text((32, 24), label, fill=(36, 44, 50), font=font(24))
    d.text((32, h - 34), f'EXPORTED .MESH / {len(faces):,} TRIANGLES / 1024 PX',
           fill=(92, 106, 114), font=font(14))
    return result


if __name__ == '__main__':
    render((0,0,18),(1400,850),'REAR / LEVEL TOP-MOUNTED FINS / SLIGHT TAIL RISE').save(HERE/'rear_alignment.png')
    render((-12, 4.5, -5), (1800, 850)).save(HERE / 'preview.png')
    render((-12, 0, 0), (1800, 650), 'GERAN-5K5-K / SIDE').save(HERE / 'side.png')
    views = [((-12,0,0),'SIDE'),((0,12,-.001),'TOP'),
             ((8,5,13),'REAR THREE-QUARTER'),((0,.001,18),'REAR'),
             ((-12,-5,-5),'UNDERSIDE'),((-12,3,-4),'TOPOLOGY')]
    sheet=Image.new('RGB',(1800,1500))
    for i,(eye,label) in enumerate(views):
        sheet.paste(render(eye,(900,500),label,wire=i==5),(i%2*900,i//2*500))
    sheet.save(HERE/'views.png')
    render((4,1.8,12),(1300,850),'RECESSED EXHAUST',tail_detail=True).save(HERE/'nozzle.png')
    print('Rendered rear alignment, preview, side, six-view sheet and recessed exhaust.')
