"""Structured, symmetric external game-art surfaces; no engineering internals."""
import math
import numpy as np
from build import Geometry


class PchipInterpolator:
    # Monotone cubic Hermite interpolation, with no overshoot at shape stations.
    def __init__(self,x,y,axis=0):
        self.x=np.asarray(x);self.y=np.asarray(y)
        h=np.diff(self.x);shape=(-1,)+(1,)*(self.y.ndim-1)
        delta=np.diff(self.y,axis=0)/h.reshape(shape)
        self.m=np.zeros_like(self.y);self.m[0]=delta[0];self.m[-1]=delta[-1]
        for i in range(1,len(x)-1):
            a,b=delta[i-1],delta[i];same=a*b>0
            w1=2*h[i]+h[i-1];w2=h[i]+2*h[i-1]
            self.m[i]=np.where(same,(w1+w2)/(w1/np.where(same,a,1)+w2/np.where(same,b,1)),0)
    def __call__(self,z):
        z=np.asarray(z);i=np.clip(np.searchsorted(self.x,z)-1,0,len(self.x)-2)
        h=self.x[i+1]-self.x[i];t=(z-self.x[i])/h
        if self.y.ndim>1:t=t[...,None];h=h[...,None]
        return (2*t**3-3*t**2+1)*self.y[i]+(t**3-2*t**2+t)*h*self.m[i]+(-2*t**3+3*t**2)*self.y[i+1]+(t**3-t**2)*h*self.m[i+1]


def shell(g,rings,tile,part,cap=True):
    p=np.array(rings);count=len(p[0]);norm=np.zeros_like(p)
    faces=[];orientation=None
    for i in range(len(p)-1):
        for j in range(count):
            k=(j+1)%count
            for ids in [[(i,j),(i,k),(i+1,k)],[(i,j),(i+1,k),(i+1,j)]]:
                pts=np.array([p[a] for a in ids]);n=np.cross(pts[1]-pts[0],pts[2]-pts[0])
                radial=pts.mean(0)-(p[i].mean(0)+p[i+1].mean(0))/2
                if orientation is None:orientation=1 if np.dot(n,radial)>=0 else -1
                n*=orientation
                for a in ids:norm[a]+=n
                faces.append(ids)
    norm/=np.maximum(np.linalg.norm(norm,axis=2)[:,:,None],1e-12)
    for ids in faces:
        pts=np.array([p[a] for a in ids]);ns=np.array([norm[a] for a in ids])
        face=np.cross(pts[1]-pts[0],pts[2]-pts[0]);face/=np.linalg.norm(face)
        if np.dot(face,ns.mean(0))<0:face=-face
        # Keep the tight trailing-edge normals in the face hemisphere.
        ns[np.sum(ns*face,axis=1)<.05]=face
        g.triangle(pts,tile(pts.mean(0)) if callable(tile) else tile,ns,part=part)
    if cap:
        for i in (0,len(p)-1):
            center=p[i].mean(0)
            direction=center-p[1 if i==0 else -2].mean(0)
            for j in range(count):g.triangle([center,p[i,j],p[i,(j+1)%count]],tile(center) if callable(tile) else tile,[direction]*3,part=part)


# Shared shape stations keep surfaces, glazing and decals on the same contour.
BODY_KEYS=np.array([
    [-4.98,.018,.038,-.045],[-4.93,.105,.135,-.038],[-4.80,.235,.235,-.025],
    [-4.59,.300,.290,-.010],[-4.34,.320,.335,.010],[-4.07,.327,.357,.028],
    [-3.78,.327,.351,.022],[-3.40,.325,.335,.008],[-2.75,.325,.325,0],
    [-1.0,.325,.325,0],[.9,.325,.325,0],[1.8,.315,.315,0],
    [2.6,.275,.280,.015],[3.35,.215,.225,.035],[4.02,.15,.17,.055],
    [4.50,.11,.125,.065],[4.79,.10,.105,.065],[4.94,.025,.035,.065]])
BODY_SHAPE=PchipInterpolator(BODY_KEYS[:,0],BODY_KEYS[:,1:])


def body_point(z,a,offset=0):
    rx,ry,cy=BODY_SHAPE(z)
    return np.array([(rx+offset)*math.cos(a),cy+(ry+offset)*math.sin(a),z])


def fuselage(g):
    zs=np.unique(np.r_[np.linspace(-4.98,-3.4,19),np.linspace(-3.4,2.6,15),np.linspace(2.6,4.94,14),-4.50])
    angles=np.arange(48)*math.tau/48
    shell(g,[[body_point(z,a) for a in angles] for z in zs],
          lambda p:1 if p[2]<-4.50 and p[1]<BODY_SHAPE(p[2])[2]-.001 else 0,'fuselage')
    # A framed multi-pane cockpit follows the raised crown and the side contour.
    for side in (-1,1):
        for za,zb,aa,ab in [(-4.52,-4.32,.55,1.49),(-4.29,-4.07,.53,1.49),
                            (-4.04,-3.85,.40,1.25),(-3.82,-3.62,.30,.78)]:
            for z0,z1 in zip(np.linspace(za,zb,4)[:-1],np.linspace(za,zb,4)[1:]):
                for a0,a1 in zip(np.linspace(aa,ab,4)[:-1],np.linspace(aa,ab,4)[1:]):
                    pts=[body_point(z,a,.010)*[side,1,1] for z,a in ((z0,a0),(z1,a0),(z1,a1),(z0,a1))]
                    g.quad(pts,3,[side*.45,1,-.22],'cockpit_glazing')
    # Slim dorsal refuelling probe and rear rounded housing, visual only.
    g.lathe([(-5.43,.003),(-5.27,.010),(-4.70,.019)],4,center=(0,.105),segments=12,part='nose_probe')
    for z in (-3.38,-2.66,.95,2.5):
        for a in angles:
            g.quad([body_point(z-.004,a,.004),body_point(z+.004,a,.004),
                    body_point(z+.004,a+math.tau/48,.004),body_point(z-.004,a+math.tau/48,.004)],9,part='fuselage_seam')
    # Small lateral windows aft of the cockpit, with clean edges.
    for side in (-1,1):
        for z in (-3.18,-2.75):
            angle=.15
            g.quad([body_point(zz,a,.006)*[side,1,1] for zz,a in
                    ((z,.05),(z+.065,.05),(z+.065,.25),(z,.25))],3,[side,0,0],'side_window')


def foil_point(span,lead,chord,y,thickness,u,a,vertical=False):
    t=(1-math.cos(a))/2
    # Closed rounded leading edge, finite thin trailing edge.
    h=thickness*chord*.5*math.sin(a)*(1-.48*t)
    if vertical:return np.array([h,y+span*u,lead+chord*t])
    return np.array([span,y+h,lead+chord*t])


def wing(g,part,stations,vertical=False):
    rings=[]
    for span,lead,chord,y,thickness in stations:
        rings.append([foil_point(span,lead,chord,y,thickness,1,a,vertical) for a in np.arange(24)*math.tau/24])
    shell(g,rings,0,part)
    return rings


def loft(g,profile,center,tile,part,rings=19,segments=24):
    profile=np.array(profile);zs=np.unique(np.r_[np.linspace(profile[0,0],profile[-1,0],rings),profile[:,0]])
    rs=PchipInterpolator(profile[:,0],profile[:,1])(zs)
    shell(g,[[[center[0]+r*math.cos(a),center[1]+r*math.sin(a),z]
              for a in np.arange(segments)*math.tau/segments] for z,r in zip(zs,rs)],tile,part)


def prop_blade(g,pivot,angle,layer,part):
    radial=np.array([math.cos(angle),math.sin(angle),0.]);tangent=np.array([-math.sin(angle),math.cos(angle),0.])
    rows=[]
    for r,c,pitch in [(.08,.065,46),(.16,.12,38),(.29,.14,30),(.43,.14,24),(.56,.12,19),(.65,.095,16),(.68,.025,15)]:
        twist=math.radians(pitch)*(1 if layer==0 else -1)
        chord=tangent*math.cos(twist)+np.array([0,0,math.sin(twist)])
        normal=np.cross(radial,chord)
        rows.append([pivot+radial*r+tangent*(-.028*(r/.68)**2)+chord*(math.cos(a)*c/2)
                     +normal*(math.sin(a)*.009*(1-r)) for a in np.arange(8)*math.tau/8])
    shell(g,rows,5,part)
    tip=np.array(rows[-1]);inner=np.array(rows[-2]);start=inner*.32+tip*.68
    # Slight outward offset prevents coplanar flickering of the yellow tip.
    tip=tip+(tip-pivot)*.001;start=start+(start-pivot)*.001
    shell(g,[start,tip],8,part,cap=False)


def main_station(x):
    u=x/5.3
    return (x,-1.76+3.34*u,2.22-1.73*u,.18-.12*u,.115-.03*u)


def make_geometry(pivots):
    pivots.clear();g=Geometry();fuselage(g);half=Geometry()
    # Full center sections overlap inside the fuselage, eliminating wing gaps.
    wing(half,'main_wing',[main_station(x) for x in np.linspace(0,5.3,12)])
    wing(half,'tailplane',[(x,3.08+.63*x,1.20-.44*x,.16+.035*x,.10) for x in np.linspace(0,1.8,7)])
    for k,x in enumerate((1.43,2.97)):
        front=-2.12+k*.95;cy=.015-.025*k
        # Continuous inner nacelle incorporates its aft landing-gear fairing.
        profile=([(front,.115),(front+.16,.18),(front+.44,.193),(front+.90,.19),
                  (front+1.40,.18),(front+2.0,.215),(front+2.55,.22),(front+3.10,.14),(front+3.58,.007)]
                 if k==0 else
                 [(front,.115),(front+.16,.18),(front+.44,.193),(front+.90,.19),
                  (front+1.36,.165),(front+1.83,.12),(front+2.30,.007)])
        loft(half,profile,(x,cy),0,'inner_nacelle' if k==0 else 'outer_nacelle',rings=13,segments=28)
        for z in (front+.30,front+.68):
            half.lathe([(z-.012,.194),(z+.012,.194)],4,center=(x,cy),segments=28,part='nacelle_seam')
        # Spinner spans both hubs and joins the engine cowling without gaps.
        loft(half,[(front-.46,.006),(front-.40,.05),(front-.28,.09),(front-.10,.108),(front+.03,.116)],(x,cy),6,'spinner',rings=5,segments=20)
        for layer in range(2):
            pivot=np.array([x,cy,front-.07-layer*.17]);pivots.append(pivot);part=f'prop_{len(pivots)}'
            half.lathe([(pivot[2]-.038,.095),(pivot[2]+.038,.095)],6,center=(x,cy),segments=16,part=part)
            for j in range(4):prop_blade(half,pivot,j*math.pi/2+layer*math.pi/4+.12,layer,part)
        # Dark flush inlet at the front underside of each cowling.
        half.quad([[x-.058,cy-.116,front+.035],[x+.058,cy-.116,front+.035],
                   [x+.058,cy-.164,front+.17],[x-.058,cy-.164,front+.17]],11,[0,-.5,-1],'nacelle_inlet')
    # Subtle control-surface seams follow the actual wing profile.
    for x in (1.05,2.30,3.65,4.80):
        span,lead,c,y,t=main_station(x)
        for aa,ab in zip(np.linspace(.16,math.pi-.06,13)[:-1],np.linspace(.16,math.pi-.06,13)[1:]):
            pts=[]
            for xx,a in ((x-.007,aa),(x+.007,aa),(x+.007,ab),(x-.007,ab)):
                sp,le,ch,yy,th=main_station(xx);q=foil_point(sp,le,ch,yy,th,1,a);q[1]+=.003;pts.append(q)
            half.quad(pts,9,[0,1,0],'wing_panel_seam')
    for side in (1,-1):
        for t,part in enumerate(half.part):
            ids=half.tri[3*t:3*t+3];points=np.array([half.p[i] for i in ids]);normals=np.array([half.n[i] for i in ids])
            points[:,0]*=side;normals[:,0]*=side
            uv=np.array([half.uv[i] for i in ids]);tile=int(uv[0,0]*4)%4+4*int(uv[0,1]*4)
            local=(uv*4-[tile%4,tile//4]-.08)/.84
            if side<0 and part.startswith('prop_'):part=f'prop_{int(part.split("_")[1])+4}'
            g.triangle(points,tile,normals,local,part)
    pivots.extend([p*np.array([-1,1,1]) for p in pivots.copy()])
    # Swept fin with a thin rounded section, broad root and clipped tip.
    wing(g,'vertical_tail',[(h,2.67+1.18*u,1.98-1.36*u,.13,.08) for u,h in
         [(u,1.72*u) for u in np.linspace(0,1,10)]],vertical=True)
    # Markings are projected onto the fin and wing surfaces, not floating planes.
    for side in (-1,1):
        center=np.array([0,1.20,4.12]);pts=[]
        for i in range(10):
            a=math.pi/2+i*math.pi/5;r=.18 if i%2==0 else .075
            pts.append(center+[0,r*math.sin(a),r*math.cos(a)])
        def project(v):
            u=(v[1]-.13)/1.72;lead=2.67+1.18*u;c=1.98-1.36*u;t=(v[2]-lead)/c
            x=.08*c*.5*math.sqrt(max(0,1-(1-2*t)**2))*(1-.48*t)+.004
            return [side*x,v[1],v[2]]
        for i in range(10):g.triangle([project(center),project(pts[i]),project(pts[(i+1)%10])],7,[[side,0,0]]*3,part='tail_marking')
        center=np.array([4.18,0,1.32]);pts=[]
        for i in range(10):
            a=math.pi/2+i*math.pi/5;r=.20 if i%2==0 else .085
            pts.append(center+[r*math.cos(a),0,r*math.sin(a)])
        def project_wing(v):
            x,_,z=v;sp,lead,c,y,th=main_station(x);t=(z-lead)/c
            yy=y+th*c*.5*math.sqrt(max(0,1-(1-2*t)**2))*(1-.48*t)+.004
            return [side*x,yy,z]
        for i in range(10):g.triangle([project_wing(center),project_wing(pts[i]),project_wing(pts[(i+1)%10])],7,[[0,1,0]]*3,part='wing_marking')
    return g
