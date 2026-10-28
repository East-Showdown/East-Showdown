"""Reference-based exterior game art, in arbitrary art units (not engineering data).

Build the HOI4 mesh and a portable OBJ/PBR source. No Blender/add-on required.
Requires Python 3, NumPy and Pillow. Run from any working directory.
"""
from pathlib import Path
from io import BytesIO
import json
import math
import struct
import sys

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from pdx_io import Node, encode, read

OUT = ROOT / 'gfx/models/units/missiles/geran5k5k'
SIZE = 1024
EQUIPMENT = ('rus_guided_uav_geranium5k5_k',)
# Pixel-space islands. Identical small symmetric surfaces reuse material patches.
REGIONS = {
    'body': (16, 16, 736, 1008),
    'fin': (768, 16, 1008, 464),
    'tail': (768, 496, 1008, 704),
    'metal': (768, 736, 1008, 816),
    'rim': (768, 848, 1008, 880),
    'inside': (768, 912, 1008, 944),
    'shadow': (768, 976, 1008, 1008),
}


class Geometry:
    def __init__(self):
        self.p, self.n, self.uv, self.tri, self.part = [], [], [], [], []

    def triangle(self, points, normals, uv, region, part):
        points, normals, uv = (np.asarray(a, dtype=float) for a in (points, normals, uv))
        cross = np.cross(points[1] - points[0], points[2] - points[0])
        if np.linalg.norm(cross) < 1e-10:
            return
        if np.dot(cross, normals.mean(0)) < 0:
            points, normals, uv = (a[[0, 2, 1]] for a in (points, normals, uv))
        normals /= np.linalg.norm(normals, axis=1)[:, None]
        x0, y0, x1, y1 = REGIONS[region]
        uv = (uv * [x1 - x0, y1 - y0] + [x0, y0]) / SIZE
        start = len(self.p)
        self.p.extend(points); self.n.extend(normals); self.uv.extend(uv)
        self.tri.extend([start, start + 1, start + 2]); self.part.append(part)

    def quad(self, points, region, part, normal=None, uv=None):
        points = np.asarray(points, dtype=float)
        if normal is None:
            normal = np.cross(points[1] - points[0], points[2] - points[0])
        uv = np.asarray(uv if uv is not None else [(0, 0), (1, 0), (1, 1), (0, 1)])
        for ids in ([0, 1, 2], [0, 2, 3]):
            self.triangle(points[ids], [normal] * 3, uv[ids], region, part)

    def lathe(self, profile, region, part, inward=False, segments=96):
        profile = np.asarray(profile, dtype=float)
        deriv = np.gradient(profile, axis=0)
        for j in range(len(profile) - 1):
            pts, ns, uvs = [], [], []
            for i in range(segments):
                pts.clear(); ns.clear(); uvs.clear()
                for k, step in ((j, i), (j, i + 1), (j + 1, i + 1), (j + 1, i)):
                    a = math.tau * step / segments
                    z, r = profile[k]; dz, dr = deriv[k]
                    pts.append([r * math.cos(a), r * math.sin(a), z])
                    normal = np.array([dz * math.cos(a), dz * math.sin(a), -dr])
                    if r == 0:
                        normal = np.array([0., 0., -1.])
                    ns.append(normal * (-1 if inward else 1))
                    v = (z + 5) / 10 if region == 'body' else k / (len(profile) - 1)
                    uvs.append([step / segments, v])
                for ids in ([0, 1, 2], [0, 2, 3]):
                    self.triangle(np.array(pts)[ids], np.array(ns)[ids],
                                  np.array(uvs)[ids], region, part)

    def prism(self, outline, angle, half_width, region, part, omit_root=False):
        """Extrude a convex (radius,z) outline with outward-facing hard edges."""
        a = math.radians(angle)
        radial = np.array([math.cos(a), math.sin(a), 0.])
        tangent = np.array([-math.sin(a), math.cos(a), 0.])
        outline = np.asarray(outline)
        uv = (outline - outline.min(0)) / np.maximum(np.ptp(outline, axis=0), 1e-8)
        rings = [np.array([radial * r + [0, 0, z] + tangent * t for r, z in outline])
                 for t in (-half_width, half_width)]
        for ring, sign in zip(rings, (-1, 1)):
            for i in range(1, len(ring) - 1):
                ids = [0, i, i + 1]
                self.triangle(ring[ids], [tangent * sign] * 3, uv[ids], region, part)
        center = np.concatenate(rings).mean(0)
        for i in range(len(outline)):
            j = (i + 1) % len(outline)
            # The closing edge is buried in the body; no invisible root cap.
            if omit_root and j == 0:
                continue
            points = np.array([rings[0][i], rings[1][i], rings[1][j], rings[0][j]])
            normal = np.cross(points[1] - points[0], points[2] - points[0])
            if np.dot(normal, points.mean(0) - center) < 0:
                normal *= -1
            self.quad(points, region, part, normal)


def make_geometry():
    from geometry_geran5k5k import build_geometry
    return build_geometry(Geometry)


def write_binary(path, data):
    """Publish complete exports atomically, including when Windows is indexing them."""
    staging=path.with_suffix(path.suffix+'.tmp')
    staging.write_bytes(data)
    staging.replace(path)


def save_dds(image, path):
    """Legacy BGRA8 DDS with a full mip chain, understood by HOI4's mesh shader."""
    image = image.convert('RGBA')
    stream=BytesIO()
    image.save(stream,format='DDS')
    raw = bytearray(stream.getvalue())
    levels = int(math.log2(image.width)) + 1
    struct.pack_into('<I', raw, 8, struct.unpack_from('<I', raw, 8)[0] | 0x20000)
    struct.pack_into('<I', raw, 28, levels)
    struct.pack_into('<I', raw, 108, 0x401008)
    for i in range(1, levels):
        raw.extend(image.resize((image.width >> i, image.height >> i),
                                Image.Resampling.BOX).tobytes('raw', 'BGRA'))
    write_binary(path,raw)


def make_textures():
    from texture_geran5k5k import make_textures as paint
    paint(HERE, OUT, REGIONS, SIZE, save_dds)


def export(g):
    # Weld vertices only when position, normal and UV match; retain hard edges/seams.
    lookup, positions, normals, uvs, indices = {}, [], [], [], []
    for p, n, uv in zip(g.p, g.n, g.uv):
        key = tuple(np.round(np.r_[p, n, uv], 7))
        if key not in lookup:
            lookup[key] = len(positions)
            positions.append(p); normals.append(n); uvs.append(uv)
        indices.append(lookup[key])
    p, n, uv = map(np.asarray, (positions, normals, uvs))
    faces = np.array(indices).reshape(-1, 3)
    ts, bs = np.zeros_like(p), np.zeros_like(p)
    for ids in faces:
        e1, e2 = p[ids[1]] - p[ids[0]], p[ids[2]] - p[ids[0]]
        a, b = uv[ids[1]] - uv[ids[0]], uv[ids[2]] - uv[ids[0]]
        det = a[0] * b[1] - a[1] * b[0]
        if abs(det) < 1e-12:
            raise ValueError('Degenerate UV triangle')
        ts[ids] += (e1 * b[1] - e2 * a[1]) / det
        bs[ids] += (-e1 * b[0] + e2 * a[0]) / det
    ts -= n * np.sum(n * ts, axis=1)[:, None]
    ts /= np.linalg.norm(ts, axis=1)[:, None]
    sign = np.where(np.sum(np.cross(n, ts) * bs, axis=1) >= 0, 1., -1.)
    tangents = np.column_stack((ts, sign))
    root = Node('File', pdxasset=('i', [1, 0]))
    obj = root.add('object').add('geran5k5k')
    mesh = obj.add('mesh', p=('f', p.ravel().tolist()), n=('f', n.ravel().tolist()),
                   ta=('f', tangents.ravel().tolist()), u0=('f', uv.ravel().tolist()), tri=('i', indices))
    mesh.add('aabb', min=('f', p.min(0).tolist()), max=('f', p.max(0).tolist()))
    mesh.add('material', shader=('s', ['PdxMeshAdvanced']), diff=('s', ['geran5k5k_diffuse.dds']),
             n=('s', ['geran5k5k_normal.dds']), spec=('s', ['geran5k5k_specular.dds']))
    mesh.add('skin', bones=('i', [4]), ix=('i', [0, -1, -1, -1] * len(p)),
             w=('f', [1., 0., 0., 0.] * len(p)))
    obj.add('skeleton').add('root', ix=('i', [0]), tx=('f', [1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.]))
    root.add('locator').add('engine_exhaust', p=('f', [0., 0., 5.]), q=('f', [1., 0., 0., 0.]), pa=('s', ['root']))
    path = OUT / 'geran5k5k.mesh'
    write_binary(path,encode(root))
    assert encode(read(path)) == path.read_bytes()
    anim = Node('File', pdxasset=('i', [1, 0]))
    info = anim.add('info', fps=('f', [30.]), sa=('i', [2]), j=('i', [1]))
    info.add('root', sa=('s', ['q']), t=('f', [0., 0., 0.]), q=('f', [0., 0., 0., 1.]), s=('f', [1.]))
    anim.add('samples', q=('f', [0., 0., 0., 1.] * 2))
    write_binary(OUT / 'geran5k5k_idle.anim',encode(anim))
    lines = ['# Geran-5K5-K exterior game art. Y up, nose -Z, arbitrary art units.', 'mtllib geran5k5k.mtl']
    lines += ['v ' + ' '.join(f'{v:.7f}' for v in row) for row in p]
    lines += [f'vt {u:.7f} {1-v:.7f}' for u, v in uv]
    lines += ['vn ' + ' '.join(f'{v:.7f}' for v in row) for row in n]
    lines.extend(['o Geran-5K5-K', 'g geran5k5k', 'usemtl geran5k5k'])
    for face in faces:
        lines.append('f ' + ' '.join(f'{i+1}/{i+1}/{i+1}' for i in face))
    (HERE / 'geran5k5k.obj').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (HERE / 'geran5k5k.mtl').write_text('newmtl geran5k5k\nKd 1 1 1\nKs 0.2 0.2 0.2\nNs 32\n'
        'Pr 0.57\nPm 0.12\nmap_Kd geran5k5k_basecolor.png\nmap_Pr geran5k5k_roughness.png\n'
        'map_Pm geran5k5k_metallic.png\nnorm geran5k5k_normal.png\n', encoding='utf-8')
    stats = dict(triangles=len(faces), vertices=len(p), texture_size=SIZE, mip_levels=11,
                 bounds=[p.min(0).tolist(), p.max(0).tolist()], equipment=list(EQUIPMENT),
                 parts={part: g.part.count(part) for part in dict.fromkeys(g.part)})
    (HERE / 'manifest.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(f'Geran-5K5-K: {len(faces):,} triangles, {len(p):,} indexed vertices, {SIZE}px DDS/PBR textures.')


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    make_textures()
    export(make_geometry())
