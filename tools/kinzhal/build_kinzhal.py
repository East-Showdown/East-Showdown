"""Reference-based exterior game art, in arbitrary art units (not engineering data).

Build the HOI4 mesh and a portable OBJ/PBR source. No Blender/add-on required.
Requires Python 3, NumPy and Pillow. Run from any working directory.
"""
from pathlib import Path
import json
import math
import struct
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'flamingo'))
from pdx_io import Node, encode, read

OUT = ROOT / 'gfx/models/units/missiles/kinzhal'
SIZE = 1024
EQUIPMENT = ('rus_medium_guided_missile_kh47m2',)
# Pixel-space islands. Identical small symmetric surfaces reuse material patches.
REGIONS = {
    'body': (16, 16, 1008, 704),
    'fin': (16, 752, 464, 880),
    'rail': (496, 752, 752, 880),
    'bracket': (784, 752, 1008, 880),
    'rim': (16, 928, 240, 1008),
    'inside': (272, 928, 496, 1008),
    'shadow': (528, 928, 752, 1008),
    'dark': (784, 928, 1008, 1008),
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
    g = Geometry()
    # Smooth long ogive and cylindrical mid-body, traced from the supplied views.
    # Y is up; the nose points along -Z; overall length is ten arbitrary art units.
    nose_z = np.linspace(-5, -.65, 30)
    nose_r = .56 * np.sin((nose_z + 5) / 4.35 * math.pi / 2) ** .88
    body = list(zip(nose_z, nose_r))
    body += [(z, .56) for z in np.linspace(-.30, 3.55, 10)]
    # Preserve the complete nose/main fuselage. Only the aft section narrows;
    # its final run is linear so the small fin roots meet the skin without gaps.
    body += [(3.60, .559), (3.82, .540), (4.12, .510), (4.45, .477),
             (4.75, .447), (4.91, .431)]
    g.lathe(body, 'body', 'body_shell')
    # Short painted shoulder integrates a compact rim into the taper. The dark
    # metal lip occupies only the final .025 art units, not an external pipe.
    g.lathe([(4.91, .431), (4.975, .385)], 'body', 'nozzle_shoulder')
    g.lathe([(4.975, .385), (5., .375)], 'rim', 'nozzle_rim')
    g.lathe([(5., .375), (5., .340)], 'rim', 'nozzle_rim')
    # A single centered dark exterior recess; no engine or functional internals.
    g.lathe([(4.22, .275), (4.60, .290), (4.88, .310), (5., .340)],
            'inside', 'nozzle_recess', inward=True)
    for i in range(96):
        a, b = math.tau * i / 96, math.tau * (i + 1) / 96
        g.triangle([[0, 0, 4.22], [.275 * math.cos(a), .275 * math.sin(a), 4.22],
                    [.275 * math.cos(b), .275 * math.sin(b), 4.22]],
                   [[0, 0, 1]] * 3, [[.5, .5], [.5 + .49 * math.cos(a), .5 + .49 * math.sin(a)],
                   [.5 + .49 * math.cos(b), .5 + .49 * math.sin(b)]], 'shadow', 'recess_shadow')
    # Keep the original large fins and brackets. Clock only the small aft row
    # by 45 degrees: four cardinal main fins and four diagonal auxiliary fins.
    for angle in (0, 90, 180, 270):
        g.prism([(.54, 2.38), (1.02, 3.09), (1.025, 3.43), (.545, 3.55)],
                angle, .023, 'fin', 'main_fin', omit_root=True)
        # Match roots to the polygonal body surface at both thickness edges.
        # Fin tips, axial spacing and thickness retain their existing dimensions.
        root_offset = .016 * math.tan(math.pi / 96)
        g.prism([(.517 - root_offset, 4.05), (.79, 4.48), (.80, 4.82),
                 (.436 - root_offset, 4.86)],
                angle + 45, .016, 'fin', 'auxiliary_fin', omit_root=True)
        # Raised mounting lugs on each main fin root.
        for z in (3.43, 3.57):
            g.prism([(.54, z - .035), (.625, z - .035), (.625, z + .035), (.54, z + .035)],
                    angle, .075, 'bracket', 'fin_mount', omit_root=True)
        # Narrow bridge joins the two external lugs, leaving a visible small recess.
        g.prism([(.604, 3.43), (.630, 3.43), (.630, 3.57), (.604, 3.57)],
                angle, .075, 'bracket', 'mount_bridge')
    # Two low longitudinal fairings on opposite flanks, offset from the main fins.
    for angle in (35, 215):
        g.prism([(.551, -.28), (.597, -.20), (.605, -.08), (.605, 2.22),
                 (.590, 2.32), (.551, 2.37)], angle, .058, 'rail', 'longitudinal_fairing', omit_root=True)
        for z in (-.14, 2.24):
            g.prism([(.596, z - .026), (.609, z - .026), (.609, z + .026), (.596, z + .026)],
                    angle, .045, 'dark', 'fairing_end')
    return g


def save_dds(image, path):
    """Legacy BGRA8 DDS with a full mip chain, understood by HOI4's mesh shader."""
    image = image.convert('RGBA')
    image.save(path)
    raw = bytearray(path.read_bytes())
    levels = int(math.log2(image.width)) + 1
    struct.pack_into('<I', raw, 8, struct.unpack_from('<I', raw, 8)[0] | 0x20000)
    struct.pack_into('<I', raw, 28, levels)
    struct.pack_into('<I', raw, 108, 0x401008)
    for i in range(1, levels):
        raw.extend(image.resize((image.width >> i, image.height >> i),
                                Image.Resampling.BOX).tobytes('raw', 'BGRA'))
    path.write_bytes(raw)


def make_textures():
    rng = np.random.default_rng(47)
    color = Image.new('RGB', (SIZE, SIZE), (181, 191, 190))
    height = Image.new('L', (SIZE, SIZE), 128)
    rough = Image.new('L', (SIZE, SIZE), 146)
    metal = Image.new('L', (SIZE, SIZE), 32)
    d, h, r, m = (ImageDraw.Draw(im) for im in (color, height, rough, metal))
    x0, y0, x1, y1 = REGIONS['body']

    def zpix(z):
        return round(y0 + (z + 5) / 10 * (y1 - y0))

    for za, zb, c, roughness in [(-5, -3.70, (129, 140, 143), 163),
                                (-3.70, -.65, (196, 204, 201), 148),
                                (-.65, .35, (176, 187, 188), 142),
                                (.35, 3.55, (185, 196, 195), 145),
                                (3.55, 5, (162, 178, 181), 136)]:
        box = (x0, zpix(za), x1, zpix(zb))
        d.rectangle(box, fill=c); r.rectangle(box, fill=roughness)
    # Thin circumferential joints and highlights; never additional geometry.
    for z in (-3.70, -2.55, -.65, .35, 3.55, 4.91):
        y = zpix(z)
        d.line((x0, y, x1, y), fill=(99, 113, 116), width=1)
        d.line((x0, y + 1, x1, y + 1), fill=(204, 214, 211), width=1)
        h.line((x0, y, x1, y), fill=107)
    # Restrained access seams and rear rivet rows. All are painted/normal-map details.
    for sector in range(4):
        u = x0 + (sector + .5) / 4 * (x1 - x0)
        for za, zb in ((.85, 1.65), (2.10, 2.7)):
            box = (int(u - 28), zpix(za), int(u + 28), zpix(zb))
            d.rounded_rectangle(box, 3, outline=(149, 164, 166), width=1)
            h.rounded_rectangle(box, 3, outline=117, width=1)
        for row, z in enumerate(np.linspace(3.72, 4.72, 10)):
            for col in range(-3, 4):
                x, y = round(u + col * 12 + (row % 2) * 3), zpix(z)
                d.ellipse((x - 1, y - 1, x + 1, y + 1), fill=(115, 136, 141))
                d.point((x, y - 1), fill=(212, 221, 217))
                h.ellipse((x - 2, y - 2, x + 2, y + 2), fill=147)
                h.point((x, y), fill=163)
    # Only the clearly readable reference stencil is reproduced; no invented serials.
    font_paths = [Path('C:/Windows/Fonts/arial.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
    font = next((ImageFont.truetype(str(p), 15) for p in font_paths if p.exists()), None)
    if font is not None:
        for sector in (0, 2):
            u = int(x0 + (sector + .5) / 4 * (x1 - x0))
            for z in (-2.95, -1.85):
                y = zpix(z)
                d.line((u - 39, y - 4, u + 39, y - 4), fill=(58, 68, 68), width=2)
                d.text((u, y), 'БАНДАЖ', font=font, anchor='mt', fill=(50, 59, 60))
                d.line((u - 39, y + 19, u + 39, y + 19), fill=(58, 68, 68), width=1)
            d.rectangle((u + 46, zpix(-1.93), u + 70, zpix(-1.78)), fill=(163, 46, 40))
    for key, c, rr, mm in [('fin', (175, 189, 190), 137, 45),
                          ('rail', (198, 210, 207), 129, 48),
                          ('bracket', (172, 187, 188), 142, 55),
                          ('rim', (114, 131, 137), 115, 155),
                          ('inside', (43, 51, 56), 191, 85),
                          ('shadow', (10, 14, 18), 224, 0),
                          ('dark', (40, 49, 51), 180, 35)]:
        box = REGIONS[key]
        d.rectangle(box, fill=c); r.rectangle(box, fill=rr); m.rectangle(box, fill=mm)
    # Eight-pixel edge dilation prevents seams across atlas islands and mip levels.
    for im in (color, height, rough, metal):
        for x0, y0, x1, y1 in REGIONS.values():
            tile = np.array(im)[y0:y1 + 1, x0:x1 + 1]
            pads = ((8, 8), (8, 8)) + (((0, 0),) if tile.ndim == 3 else ())
            im.paste(Image.fromarray(np.pad(tile, pads, mode='edge')), (x0 - 8, y0 - 8))
    pixels = np.array(color, dtype=float)
    pixels += rng.normal(0, .40, (SIZE, SIZE, 1))
    color = Image.fromarray(np.clip(pixels, 0, 255).astype('uint8'))
    heights = np.array(height, dtype=float) / 255
    dy, dx = np.gradient(heights)
    normal = np.dstack((-dx * 2.0, dy * 2.0, np.ones_like(dx)))
    normal /= np.linalg.norm(normal, axis=2)[:, :, None]
    normal_rgb = ((normal * .5 + .5) * 255).clip(0, 255).astype('uint8')
    for suffix, im in [('basecolor', color), ('roughness', rough), ('metallic', metal),
                       ('normal', Image.fromarray(normal_rgb))]:
        im.save(HERE / f'kinzhal_{suffix}.png')
    # Clausewitz packed normal: X in alpha, Y in green; standard RGB retained above.
    packed = np.full((SIZE, SIZE, 4), [128, 128, 0, 128], dtype='uint8')
    packed[:, :, 1] = normal_rgb[:, :, 1]; packed[:, :, 3] = normal_rgb[:, :, 0]
    spec = np.zeros((SIZE, SIZE, 4), dtype='uint8')
    spec[:, :, 1] = 255 - np.array(rough)
    spec[:, :, 2] = np.array(metal)
    spec[:, :, 3] = 128
    for suffix, im in [('diffuse', color), ('normal', Image.fromarray(packed)),
                       ('specular', Image.fromarray(spec))]:
        save_dds(im, OUT / f'kinzhal_{suffix}.dds')


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
    obj = root.add('object').add('kinzhal')
    mesh = obj.add('mesh', p=('f', p.ravel().tolist()), n=('f', n.ravel().tolist()),
                   ta=('f', tangents.ravel().tolist()), u0=('f', uv.ravel().tolist()), tri=('i', indices))
    mesh.add('aabb', min=('f', p.min(0).tolist()), max=('f', p.max(0).tolist()))
    mesh.add('material', shader=('s', ['PdxMeshAdvanced']), diff=('s', ['kinzhal_diffuse.dds']),
             n=('s', ['kinzhal_normal.dds']), spec=('s', ['kinzhal_specular.dds']))
    mesh.add('skin', bones=('i', [4]), ix=('i', [0, -1, -1, -1] * len(p)),
             w=('f', [1., 0., 0., 0.] * len(p)))
    obj.add('skeleton').add('root', ix=('i', [0]), tx=('f', [1., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.]))
    root.add('locator').add('engine_exhaust', p=('f', [0., 0., 5.]), q=('f', [1., 0., 0., 0.]), pa=('s', ['root']))
    path = OUT / 'kinzhal.mesh'
    path.write_bytes(encode(root))
    assert encode(read(path)) == path.read_bytes()
    anim = Node('File', pdxasset=('i', [1, 0]))
    info = anim.add('info', fps=('f', [30.]), sa=('i', [2]), j=('i', [1]))
    info.add('root', sa=('s', ['q']), t=('f', [0., 0., 0.]), q=('f', [0., 0., 0., 1.]), s=('f', [1.]))
    anim.add('samples', q=('f', [0., 0., 0., 1.] * 2))
    (OUT / 'kinzhal_idle.anim').write_bytes(encode(anim))
    lines = ['# Kinzhal exterior game art. Y up, nose -Z, arbitrary art units.', 'mtllib kinzhal.mtl']
    lines += ['v ' + ' '.join(f'{v:.7f}' for v in row) for row in p]
    lines += [f'vt {u:.7f} {1-v:.7f}' for u, v in uv]
    lines += ['vn ' + ' '.join(f'{v:.7f}' for v in row) for row in n]
    lines.append('usemtl kinzhal')
    prev = None
    for face, part in zip(faces, g.part):
        if part != prev:
            lines.append('g ' + part); prev = part
        lines.append('f ' + ' '.join(f'{i+1}/{i+1}/{i+1}' for i in face))
    (HERE / 'kinzhal.obj').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (HERE / 'kinzhal.mtl').write_text('newmtl kinzhal\nKd 1 1 1\nKs 0.2 0.2 0.2\nNs 32\n'
        'Pr 0.57\nPm 0.12\nmap_Kd kinzhal_basecolor.png\nmap_Pr kinzhal_roughness.png\n'
        'map_Pm kinzhal_metallic.png\nnorm kinzhal_normal.png\n', encoding='utf-8')
    stats = dict(triangles=len(faces), vertices=len(p), texture_size=SIZE, mip_levels=11,
                 bounds=[p.min(0).tolist(), p.max(0).tolist()], equipment=list(EQUIPMENT),
                 parts={part: g.part.count(part) for part in dict.fromkeys(g.part)})
    (HERE / 'manifest.json').write_text(json.dumps(stats, indent=2) + '\n', encoding='utf-8')
    print(f'Kinzhal: {len(faces):,} triangles, {len(p):,} indexed vertices, {SIZE}px DDS/PBR textures.')


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    make_textures()
    export(make_geometry())
