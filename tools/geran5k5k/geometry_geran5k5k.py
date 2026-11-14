"""Exterior art reconstructed from the supplied side reference, in art units.

The main pair is level and top-mounted. The tail pair sits slightly higher,
with only a three-degree rise. All roots share body edges.
"""
import math
import numpy as np

SEGMENTS = 48
# Half-cell phase provides symmetric root cells on the upper body shoulders.
ANGULAR_PHASE = math.pi / SEGMENTS
MAIN_HEIGHT = .420
TAIL_HEIGHT = .455
TAIL_RISE_DEGREES = 3.0
FIN_SHOULDER_X = .300
PROFILE = [
    (-5, 0), (-4.992, .045), (-4.970, .091), (-4.930, .140),
    (-4.870, .181), (-4.780, .217), (-4.640, .250), (-4.460, .282),
    (-4.220, .316), (-3.950, .349), (-3.650, .380), (-3.300, .403),
    (-2.900, .420), (-2.400, .430), (-1.800, .435), (-1.150, .435),
    (-.550, .435), (1.200, .435), (1.650, .433), (2.150, .431),
    (2.650, .426), (3.000, .420), (3.750, .384), (4.050, .352),
    (4.300, .316), (4.500, .276), (4.670, .232), (4.750, .208),
]
# Cell indices refer to angular intervals in the fuselage, not separate fins.
FIN_PATCHES = {
    (-.550, 9): ('main_right', 'fin', 1.440, .590, 1.270),
    (-.550, 13): ('main_left', 'fin', 1.440, .590, 1.270),
    (3.000, 9): ('tail_right', 'tail', 1.130, 3.500, 3.870),
    (3.000, 13): ('tail_left', 'tail', 1.130, 3.500, 3.870),
}


def attached_fin(g, corners, index, specification):
    """Join an upper-body root to a level swept surface, with a short fairing."""
    part, region, half_span, leading, trailing = specification
    side = 1 if part.endswith('right') else -1
    is_tail = part.startswith('tail_')
    height = TAIL_HEIGHT if is_tail else MAIN_HEIGHT
    slope = math.tan(math.radians(TAIL_RISE_DEGREES)) if is_tail else 0.0
    c,s = math.cos(ANGULAR_PHASE),math.sin(ANGULAR_PHASE)
    rotation = np.array([[c,-s,0],[s,c,0],[0,0,1]])
    # Work in the final Y-up frame: mounting height and surface slope are
    # independent of the angle of the cylindrical skin at the root.
    root = np.asarray(corners) @ rotation.T
    def ring(x, z_front, z_back):
        y = height + slope*(x-FIN_SHOULDER_X)
        return np.array([[side*x, y+side*t, z] for t,z in
                         [(-.008,z_front),(.008,z_front),
                          (.008,z_back),(-.008,z_back)]])
    front_z = root[0,2]*.88 + leading*.12
    rear_z = root[2,2]*.88 + trailing*.12
    shoulder = ring(FIN_SHOULDER_X,front_z,rear_z)
    tip = ring(half_span,leading,trailing)
    # Convert back to the cylinder lattice. The final shared rotation below
    # restores the level surfaces and retains exact common root positions.
    rings = [r @ rotation for r in (root,shoulder,tip)]
    for j in range(2):
        for k in range(4):
            next_k = (k+1)%4
            pts = np.array([rings[j][k], rings[j+1][k],
                            rings[j+1][next_k], rings[j][next_k]])
            # Root loop points outward from the skin. Bridge faces therefore
            # use the reverse winding; a centroid test fails on the concave
            # underside of the raised tail-root fairing.
            normal = -np.cross(pts[1]-pts[0], pts[2]-pts[0])
            # The two broad sides use matching islands. Thin edges use the same
            # dark material, with full-rank UVs even at the leading edge.
            uv = [(j*.5, 0), ((j+1)*.5, 0), ((j+1)*.5, 1), (j*.5, 1)]
            if k in (1,3):
                uv = [(0,j*.5),(0,(j+1)*.5),(1,(j+1)*.5),(1,j*.5)]
            g.quad(pts, region, part, normal, uv)
    g.quad(rings[-1], region, part, np.array([side,0,0]) @ rotation)


def build_geometry(Geometry):
    g = Geometry()
    profile = np.asarray(PROFILE)
    derivative = np.gradient(profile, axis=0)
    for j in range(len(profile)-1):
        for i in range(SEGMENTS):
            points, normals, uv = [], [], []
            for k,step in ((j,i),(j,i+1),(j+1,i+1),(j+1,i)):
                angle = math.tau*step/SEGMENTS
                z,r = profile[k]; dz,dr = derivative[k]
                points.append([r*math.cos(angle),r*math.sin(angle),z])
                normals.append([dz*math.cos(angle),dz*math.sin(angle),-dr]
                               if r else [0,0,-1])
                uv.append([step/SEGMENTS,(z+5)/10])
            patch = FIN_PATCHES.get((float(profile[j,0]),i))
            if patch:
                attached_fin(g,points,i,patch)
            else:
                for ids in ([0,1,2],[0,2,3]):
                    g.triangle(np.array(points)[ids], np.array(normals)[ids],
                               np.array(uv)[ids], 'body', 'fuselage')
    # Short integral housing, annular metal lip and real recessed inner wall.
    # Adjacent surfaces share position rings, leaving no sealed cap at z=5.
    g.lathe([(4.750,.208),(4.750,.182)],'metal','tail_shoulder',segments=SEGMENTS)
    g.lathe([(4.750,.182),(4.790,.181),(4.980,.158),(5.000,.158)],
            'metal','nozzle_outer',segments=SEGMENTS)
    g.lathe([(5.000,.158),(5.000,.132)],'rim','nozzle_rim',segments=SEGMENTS)
    g.lathe([(4.640,.111),(4.720,.122),(4.980,.132),(5.000,.132)],
            'inside','nozzle_inner',inward=True,segments=SEGMENTS)
    # Explicit disk triangulation with planar UVs, facing the exhaust aperture.
    for i in range(SEGMENTS):
        a,b = math.tau*i/SEGMENTS, math.tau*(i+1)/SEGMENTS
        pts = [[0,0,4.640],[.111*math.cos(a),.111*math.sin(a),4.640],
               [.111*math.cos(b),.111*math.sin(b),4.640]]
        uv = [[.5,.5],[.5+.49*math.cos(a),.5+.49*math.sin(a)],
              [.5+.49*math.cos(b),.5+.49*math.sin(b)]]
        g.triangle(pts,[[0,0,1]]*3,uv,'shadow','nozzle_recess')
    # Rotate the whole angular lattice, including the nozzle, so every shared
    # ring stays welded. Fin mounting heights are defined in the final frame.
    c,s = math.cos(ANGULAR_PHASE),math.sin(ANGULAR_PHASE)
    rotation = np.array([[c,-s,0],[s,c,0],[0,0,1]])
    g.p = (np.asarray(g.p) @ rotation.T).tolist()
    g.n = (np.asarray(g.n) @ rotation.T).tolist()
    return g
