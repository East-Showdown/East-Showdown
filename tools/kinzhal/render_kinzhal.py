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

MODEL = ROOT / 'gfx/models/units/missiles/kinzhal/kinzhal.mesh'


def font(size):
    p = Path('C:/Windows/Fonts/arial.ttf')
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default(size=size)


def render(eye, size=(1500, 850), label='KH-47M2 / KINZHAL', wire=False, tail_detail=False):
    mesh = read(MODEL).child('object').children[0].child('mesh')
    p = np.array(mesh.get('p')).reshape(-1, 3)
    n = np.array(mesh.get('n')).reshape(-1, 3)
    t = np.array(mesh.get('ta')).reshape(-1, 4)
    uv = np.array(mesh.get('u0')).reshape(-1, 2)
    faces = np.array(mesh.get('tri')).reshape(-1, 3)
    material = mesh.child('material')
    diffuse = np.array(Image.open(MODEL.parent / material.get('diff')[0]).convert('RGB'))
    normalmap = np.array(Image.open(MODEL.parent / material.get('n')[0]).convert('RGBA'))
    specular = np.array(Image.open(MODEL.parent / material.get('spec')[0]).convert('RGBA'))
    camera = np.array(eye, dtype=float); camera /= np.linalg.norm(camera)
    right = np.cross([0, 1, 0], camera); right /= np.linalg.norm(right)
    up = np.cross(camera, right)
    projected = p @ np.array([right, up, camera]).T
    framing = projected[p[:, 2] >= 2.38] if tail_detail else projected
    low, high = framing[:, :2].min(0), framing[:, :2].max(0)
    w, h = size
    scale = min((w - 140) / (high[0] - low[0]), (h - 170) / (high[1] - low[1]))
    center = (high + low) / 2
    projected[:, 0] = (projected[:, 0] - center[0]) * scale + w / 2
    projected[:, 1] = -(projected[:, 1] - center[1]) * scale + h / 2 + 15
    canvas = np.full((h, w, 3), [34, 42, 49], dtype='uint8')
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
        colors = diffuse[ty, tx].astype(float) * (.40 + .63 * lambert[:, None])
        colors += spec[:, None] * (12 + gloss[:, None] * 32)
        if wire:
            edge = np.minimum(np.minimum(w0[mask], w1[mask]), w2[mask]) < .055
            colors[edge] = [122, 181, 184]
        canvas[y0:y1 + 1, x0:x1 + 1][mask] = np.clip(colors, 0, 255).astype('uint8')
        zbuffer[mask] = z[mask]
    result = Image.fromarray(canvas)
    d = ImageDraw.Draw(result)
    d.text((32, 24), label, fill=(227, 236, 236), font=font(24))
    d.text((32, h - 34), f'EXPORTED .MESH / {len(faces):,} TRIANGLES / 1024 PX',
           fill=(147, 165, 174), font=font(14))
    return result


if __name__ == '__main__':
    render((-11, 5, -6), (1800, 1000)).save(HERE / 'preview.png')
    render((8, 5, 13), (1500, 900), 'REAR / OPEN EXHAUST').save(HERE / 'rear.png')
    views = [((-12, 0, 0), 'SIDE'), ((0, 12, -.001), 'TOP'),
             ((8, 5, 13), 'REAR THREE-QUARTER'), ((0, .001, 18), 'REAR / OPEN NOZZLE'),
             ((-10, 6, -11), 'FRONT THREE-QUARTER'), ((-12, 3, -4), 'TOPOLOGY')]
    sheet = Image.new('RGB', (1800, 1650))
    for i, (eye, label) in enumerate(views):
        sheet.paste(render(eye, (900, 550), label, wire=i == 5), (i % 2 * 900, i // 2 * 550))
    sheet.save(HERE / 'views.png')
    detail = Image.new('RGB', (1800, 700))
    for i,(eye,label) in enumerate([((8,5,13),'TAIL / THREE-QUARTER'),
                                     ((0,.001,18),'TAIL / REAR')]):
        detail.paste(render(eye,(900,700),label,tail_detail=True),(i*900,0))
    detail.save(HERE / 'tail_detail.png')
    print('Rendered exported mesh: preview.png, rear.png, views.png, tail_detail.png')
