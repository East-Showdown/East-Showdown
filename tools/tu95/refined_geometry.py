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
        g.triangle(pts,tile,ns,part=part)
    if cap:
        for i in (0,len(p)-1):
            center=p[i].mean(0)
            direction=center-p[1 if i==0 else -2].mean(0)
            for j in range(count):g.triangle([center,p[i,j],p[i,(j+1)%count]],tile,[direction]*3,part=part)


def fuselage(g):
    keys=[[-5.04,.015,-.045],[-4.96,.11,-.035],[-4.8,.225,-.015],[-4.56,.305,0],
          [-4.25,.345,.018],[-3.88,.355,.015],[-3.4,.36,0],[-2,.36,0],[0,.36,0],
          [1.6,.34,0],[2.7,.275,.015],[3.7,.195,.04],[4.35,.11,.065],[4.83,.024,.065]]
    keys=np.array(keys);f=PchipInterpolator(keys[:,0],keys[:,1:],axis=0)
    zs=np.unique(np.r_[np.linspace(-5.04,-3.4,15),np.linspace(-3.4,2.7,16),np.linspace(2.7,4.83,13)])
    angles=np.arange(48)*math.tau/48
    rings=[[[r*math.cos(a),cy+r*math.sin(a),z] for a in angles] for z,(r,cy) in zip(zs,f(zs))]
    shell(g,rings,0,'fuselage')
    # Glazing is split into individual curved panes on the actual fuselage.
    for side in (-1,1):
        for za,zb,aa,ab in [(-4.52,-4.27,.52,1.48),(-4.23,-3.98,.40,1.32),(-3.94,-3.72,.33,.76)]:
            for z0,z1 in zip(np.linspace(za,zb,4)[:-1],np.linspace(za,zb,4)[1:]):
                for a0,a1 in zip(np.linspace(aa,ab,4)[:-1],np.linspace(aa,ab,4)[1:]):
                    pts=[];ns=[]
                    for z,a in [(z0,a0),(z1,a0),(z1,a1),(z0,a1)]:
                        r,cy=f(z);n=np.array([side*math.cos(a),math.sin(a),0])
                        pts.append(n*(r+.008)+[0,cy,z]);ns.append(n)
                    for ids in [(0,1,2),(0,2,3)]:g.triangle([pts[i] for i in ids],3,[ns[i] for i in ids],part='cockpit_glazing')
    g.lathe([(-5.38,.004),(-5.10,.013),(-5.0,.018)],4,center=(0,.075),segments=12,part='probe')


def foil(g,span,lead,tip_lead,chord,tip_chord,y,part,vertical=False):
    rings=[]
    # Closed elliptical sampling concentrates vertices around the leading edge.
    for u in np.linspace(0,1,9):
        c=chord+(tip_chord-chord)*u;z=lead+(tip_lead-lead)*u
        row=[]
        for a in np.arange(24)*math.tau/24:
            t=(1-math.cos(a))/2
            thick=.065*c*math.sin(a)*(1-.45*t)
            if vertical:row.append([thick,y+span*u,z+c*t])
            else:row.append([.16+(span-.16)*u,y-.085*u+thick,z+c*t])
        rings.append(row)
    shell(g,rings,0,part)


def loft(g,profile,center,tile,part,rings=19,segments=28):
    profile=np.array(profile);zs=np.linspace(profile[0,0],profile[-1,0],rings)
    rs=PchipInterpolator(profile[:,0],profile[:,1])(zs)
    shell(g,[[[center[0]+r*math.cos(a),center[1]+r*math.sin(a),z]
              for a in np.arange(segments)*math.tau/segments] for z,r in zip(zs,rs)],tile,part)


def prop_blade(g,pivot,angle,layer,part):
    radial=np.array([math.cos(angle),math.sin(angle),0.]);tangent=np.array([-math.sin(angle),math.cos(angle),0.])
    rows=[]
    for r,c,pitch in [(.09,.075,48),(.17,.135,42),(.28,.145,34),(.40,.135,28),(.52,.116,23),(.63,.084,19),(.70,.035,16)]:
        twist=math.radians(pitch)*(1 if layer==0 else -1)
        chord=tangent*math.cos(twist)+np.array([0,0,math.sin(twist)])
        normal=np.cross(radial,chord)
        sweep=-.035*(r/.70)**2
        rows.append([pivot+radial*r+tangent*sweep+chord*(math.cos(a)*c/2)+normal*(math.sin(a)*.012*(1-r)) for a in np.arange(8)*math.tau/8])
    shell(g,rows,5,part)
    # Slim gold tip, following the actual pitched blade surface.
    tip=np.array(rows[-1]);inner=np.array(rows[-2]);start=inner*.22+tip*.78
    shell(g,[start,tip],8,part,cap=False)


def make_geometry(pivots):
    pivots.clear();g=Geometry();fuselage(g)
    # Build exactly one wing/engine half, then reflect positions AND normals.
    half=Geometry()
    foil(half,5.35,-1.27,1.72,1.95,.40,-.035,'main_wing')
    foil(half,1.72,3.17,4.12,1.25,.34,.22,'tailplane')
    # Broad shallow root glove blends the wing silhouette into the body.
    loft(half,[(-1.58,.025),(-1.22,.17),(-.4,.19),(.55,.16),(1.0,.018)],(.21,-.065),0,'wing_root_fairing',rings=12,segments=20)
    for k,x in enumerate((1.48,3.08)):
        front=-2.02+k*.84;cy=-.12
        loft(half,[(front,.12),(front+.19,.185),(front+.48,.205),(front+.95,.197),
                   (front+1.47,.17),(front+1.88,.11),(front+2.18,.012)],(x,cy),0,'nacelle')
        # One continuous inner nacelle extends aft for the retracted gear.
        if k==0:loft(half,[(front+1.1,.035),(front+1.55,.15),(front+2.05,.13),(front+2.70,.008)],(x,cy-.035),2,'gear_fairing',rings=12,segments=24)
        # Slender coaxial shafts and separated rotor hubs.
        for layer in range(2):
            pivot=np.array([x,cy,front-.12-layer*.17]);pivots.append(pivot)
            part=f'prop_{len(pivots)}'
            loft(half,[(pivot[2]-.065,.078),(pivot[2],.089),(pivot[2]+.06,.078)],(x,cy),6,part,rings=4,segments=16)
            for j in range(4):prop_blade(half,pivot,j*math.pi/2+layer*.48+.16,layer,part)
        loft(half,[(front-.52,.008),(front-.47,.046),(front-.38,.075),(front-.32,.078)],(x,cy),6,'spinner',rings=6,segments=20)
        # Lower intake is a recessed dark opening, not a thick external band.
        half.lathe([(front+.07,.055),(front+.24,.061)],4,center=(x,cy-.12),segments=16,part='intake_lip')
    for side in (1,-1):
        for t,part in enumerate(half.part):
            ids=half.tri[3*t:3*t+3];points=np.array([half.p[i] for i in ids]);normals=np.array([half.n[i] for i in ids])
            points[:,0]*=side;normals[:,0]*=side
            # Geometry helper remaps UV tiles, so preserve the original UVs here.
            uv=np.array([half.uv[i] for i in ids]);tile=int(uv[0,0]*4)%4+4*int(uv[0,1]*4)
            local=(uv*4-[tile%4,tile//4]-.08)/.84
            if side<0 and part.startswith('prop_'):part=f'prop_{int(part.split("_")[1])+4}'
            g.triangle(points,tile,normals,local,part)
    pivots.extend([p*np.array([-1,1,1]) for p in pivots.copy()])
    foil(g,1.64,3.0,4.04,1.62,.47,.18,'vertical_tail',vertical=True)
    loft(g,[(2.63,.01),(3.12,.11),(3.8,.10),(4.6,.015)],(0,.16),0,'tail_root',rings=10,segments=20)
    for side in (-1,1):
        center=np.array([side*.04,1.25,4.25]);pts=[]
        for i in range(10):
            a=math.pi/2+i*math.pi/5;r=.16 if i%2==0 else .067
            pts.append(center+[0,r*math.sin(a),r*math.cos(a)])
        for i in range(10):g.triangle([center,pts[i],pts[(i+1)%10]],7,[[side,0,0]]*3,part='tail_marking')
    return g
