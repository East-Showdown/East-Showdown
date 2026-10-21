"""Geran-5 visual game model based on the supplied image; arbitrary art units."""
from pathlib import Path
import sys
import math
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent))
from model_export import textures,export_rigid
from build import Geometry

OUT=ROOT/'gfx/models/units/missiles/geran5'
COLORS=[(30,33,41),(34,37,45),(27,30,40),(20,23,29),
        (205,207,195),(131,139,135),(85,96,91),(16,20,20),
        (119,127,121),(43,48,53),(185,188,176),(23,26,34)]


def box(g,center,size,tile,part):
    x,y,z=center;w,h,d=np.array(size)/2
    g.prism([(y-h,z-d),(y+h,z-d),(y+h,z+d),(y-h,z+d)],x-w,x+w,tile,part)


def make_geometry():
    g=Geometry()
    g.lathe([(-4.98,.002),(-4.89,.063),(-4.73,.16),(-4.50,.249),
             (-4.22,.315),(-3.90,.348),(-3.5,.36)],1,segments=48,part='nose')
    g.lathe([(-3.5,.36),(-2.5,.36),(-1.25,.36),(0,.36),(1.5,.36),(2.80,.36),(3.70,.356)],0,segments=48,part='fuselage')
    g.lathe([(3.70,.356),(4.0,.348),(4.23,.30),(4.39,.222),(4.48,.111),(4.51,.002)],0,segments=40,part='rounded_tail')
    foil=[(-.13,-.34),(-.103,-.29),(-.088,-.14),(-.102,.19),(-.128,.60),
          (-.141,.66),(-.154,.30),(-.161,-.03),(-.15,-.25)]
    for side in (-1,1):
        x0,x1=sorted([side*.23,side*4.12])
        g.prism(foil,x0,x1,2,'straight_wing')
        # Long straight tailplane with upright end fins, as in the reference.
        tailfoil=[(0,3.35),(.034,3.43),(.018,4.20),(-.018,4.20),(-.034,3.43)]
        x0,x1=sorted([side*.22,side*1.32])
        g.prism(tailfoil,x0,x1,2,'tailplane')
        fin=[(-.12,3.43),(.61,3.67),(.69,4.13),(-.12,4.23)]
        x=side*1.32
        g.prism(fin,x-.020,x+.020,0,'twin_fin')
        # A thin hinge seam near the wing trailing edge.
        g.quad([[side*.47,-.119,.45],[side*4.08,-.119,.45],
                [side*4.08,-.121,.46],[side*.47,-.121,.46]],9,[0,1,0],'wing_hinge')
    # Compact pale dorsal engine cover with a recessed dark inlet.
    box(g,[0,.39,3.63],[.22,.15,.67],3,'engine_mount')
    cy=.60
    g.lathe([(3.06,.118),(3.14,.162),(3.29,.175),(3.75,.175),
             (3.91,.15),(3.98,.107)],4,center=(0,cy),segments=28,part='pale_engine')
    g.lathe([(3.06,.118),(3.12,.092),(3.27,.085)],7,center=(0,cy),segments=28,inward=True,part='intake')
    g.lathe([(3.98,.107),(4.08,.101),(4.12,.083)],5,center=(0,cy),segments=24,part='exhaust_ring')
    g.lathe([(4.00,.064),(4.12,.083)],7,center=(0,cy),segments=24,inward=True,part='exhaust_inside')
    for z,r,normal in ((3.28,.088,[0,0,-1]),(4.0,.066,[0,0,1])):
        for i in range(28):
            a,b=math.tau*i/28,math.tau*(i+1)/28
            g.triangle([[0,cy,z],[r*math.cos(a),cy+r*math.sin(a),z],
                        [r*math.cos(b),cy+r*math.sin(b),z]],7,[normal]*3,part='engine_recess')
    for side in (-1,1):
        box(g,[side*.151,.60,3.56],[.05,.17,.42],4,'engine_cover')
        for z in (3.32,3.71):box(g,[side*.184,.6,z],[.024,.040,.026],6,'engine_fastener')
    box(g,[0,.780,3.56],[.12,.050,.32],10,'engine_top_cover')
    for z in (3.25,3.80):
        g.lathe([(z-.006,.177),(z+.006,.177)],8,center=(0,cy),segments=28,part='engine_seam')
    # Pale underside fairing and dark attachment braces, visible in the reference.
    g.prism([(-.32,2.37),(-.43,2.35),(-.67,2.56),(-.71,3.11),(-.51,3.60),(-.31,3.65)],-.22,.22,8,'lower_fairing')
    for side in (-1,1):
        g.prism([(-.31,2.65),(-.31,2.70),(-.67,2.86),(-.69,2.82)],side*.25-.016,side*.25+.016,6,'attachment_brace')
    for z in (-3.50,-2.46,-1.20,.05,1.50,2.81):
        g.lathe([(z-.005,.361),(z+.005,.361)],11,segments=48,part='body_seam')
    # Discrete top access panels are laid on the curved upper surface.
    for z0,z1 in ((-2.35,-1.38),(-.99,-.02),(.28,1.28),(1.74,2.61)):
        x=.16;y=math.sqrt(.36**2-x*x)+.003
        for side in (-1,1):
            g.quad([[side*x,y,z0],[side*x,y,z1],[side*(x+.008),y-.003,z1],
                    [side*(x+.008),y-.003,z0]],9,[0,1,0],'access_seam')
        for z in (z0,z1):
            for i in range(12):
                xa=-x+2*x*i/12;xb=-x+2*x*(i+1)/12
                ya=math.sqrt(.36**2-xa*xa)+.003;yb=math.sqrt(.36**2-xb*xb)+.003
                g.quad([[xa,ya,z],[xb,yb,z],[xb,yb,z+.008],[xa,ya,z+.008]],9,[0,1,0],'access_seam')
    return g


if __name__=='__main__':
    textures('geran5',OUT,HERE,COLORS)
    export_rigid(make_geometry(),'geran5',OUT,HERE,[0.,.60,4.12])
