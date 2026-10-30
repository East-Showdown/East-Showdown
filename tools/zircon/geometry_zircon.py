"""Low-poly exterior: broad shovel nose, recessed intake, cylindrical nozzle."""
import math
import numpy as np


# z, half-width, crown, side chine, bottom, circular-section blend.
# Width stays broad at the leading edge; thickness alone tapers strongly forward.
STATIONS = np.array([
    [-4.988,.310,-.218,-.237,-.244,0],
    [-4.94,.318,-.207,-.235,-.244,0],
    [-4.68,.335,-.153,-.232,-.245,0],
    [-4.32,.352,-.055,-.228,-.246,0],
    [-3.90,.370,.067,-.221,-.247,0],
    [-3.45,.384,.177,-.216,-.247,0],
    [-3.02,.392,.260,-.212,-.247,0],
    [-2.52,.395,.310,-.210,-.247,0],
    [-1.10,.391,.312,-.212,-.250,0],
    [ .40,.374,.305,-.211,-.249,0],
    [1.38,.352,.300,-.205,-.245,0],
    [1.65,.350,.310,-.170,-.275,.16],
    [1.96,.350,.330,-.100,-.310,.50],
    [2.28,.350,.345,-.035,-.340,.84],
    [2.62,.350,.350,0,-.350,1],
    [3.20,.350,.350,0,-.350,1],
    [3.88,.350,.350,0,-.350,1],
    [4.18,.343,.343,0,-.343,1],
    [4.48,.326,.326,0,-.326,1],
    [4.70,.302,.302,0,-.302,1],
])
SEGMENTS = 32


def build_geometry(Geometry):
    g = Geometry()
    rings = []
    for z,w,top,chine,bottom,blend in STATIONS:
        # Eight corners with collinear subdivisions on the broad top and bottom.
        # Four samples per edge also give a clean 32-sided round rear section.
        polygon=np.array([[w,chine],[.55*w,top],[0,top],[-.55*w,top],
                          [-w,chine],[-.90*w,bottom],[0,bottom],[.90*w,bottom]])
        ring=[]
        for i in range(SEGMENTS):
            a,t=divmod(i,4);t/=4
            flat=polygon[a]*(1-t)+polygon[(a+1)%8]*t
            angle=math.tau*i/SEGMENTS
            # Broad crowned top and almost flat underside. The final shoulder
            # band gently blends back into the existing body by z=-2.52.
            nose=np.clip((-2.52-z)/1.25,0,1)
            xx=math.cos(angle);height=top-bottom
            if math.sin(angle)>=-1e-8:
                yy=bottom+height*(.12+.88*math.sqrt(max(1-xx**4,0)))
            else:
                yy=bottom+height*.12*(1-math.sqrt(max(1-xx**6,0)))
            flat=flat*(1-nose)+np.array([w*xx,yy])*nose
            circle=np.array([w*math.cos(angle),w*math.sin(angle)])
            point=flat*(1-blend)+circle*blend
            zz=z
            if z==STATIONS[0,0]:
                # Rounded lateral corners leave a long straight transverse edge.
                zz+=.050*max(0,(abs(point[0]/w)-.75)/.25)**2
            ring.append([*point,zz])
        rings.append(ring)
    rings=np.array(rings)
    dz=np.gradient(rings,STATIONS[:,0],axis=0)
    dtheta=np.roll(rings,-1,axis=1)-np.roll(rings,1,axis=1)
    smooth=np.cross(dtheta,dz)
    smooth/=np.linalg.norm(smooth,axis=2)[:,:,None]
    for k in range(len(rings)-1):
        for i in range(SEGMENTS):
            j=(i+1)%SEGMENTS
            ids=[(k,i),(k,j),(k+1,j),(k+1,i)]
            points=np.array([rings[a,b] for a,b in ids])
            normals=[]
            for a,b in ids:
                edge=rings[a,j]-rings[a,i]
                hard=np.cross(edge,dz[a,b]);hard/=np.linalg.norm(hard)
                blend=max(STATIONS[a,5],np.clip((-2.52-STATIONS[a,0])/1.25,0,1))
                normal=hard*(1-blend)+smooth[a,b]*blend
                normals.append(normal/np.linalg.norm(normal))
            uv=np.array([[(STATIONS[k,0]+5)/10,i/SEGMENTS],
                         [(STATIONS[k,0]+5)/10,(i+1)/SEGMENTS],
                         [(STATIONS[k+1,0]+5)/10,(i+1)/SEGMENTS],
                         [(STATIONS[k+1,0]+5)/10,i/SEGMENTS]])
            for ix in ([0,1,2],[0,2,3]):
                g.triangle(points[ix],np.array(normals)[ix],uv[ix],'body','body_shell')
    # A rounded transverse lip spans the full width. Multiple vertices along the
    # middle row share z=-5: there is no apex or central point. Its upper/lower
    # boundaries coincide with the first body ring, including the rounded corners.
    ring=rings[0]
    cap=[]
    for theta in np.linspace(-math.pi/2,math.pi/2,5):
        row=[]
        for i in range(SEGMENTS//2+1):
            upper,lower=ring[i],ring[(-i)%SEGMENTS]
            x=upper[0];middle=(upper[1]+lower[1])/2
            half=(upper[1]-lower[1])/2
            rounding=.012*min(1,max(0,(1-abs(x)/STATIONS[0,1])/.12))
            row.append([x,middle+half*math.sin(theta),upper[2]-rounding*math.cos(theta)])
        cap.append(row)
    cap=np.array(cap)
    ns=np.cross(np.gradient(cap,axis=1),np.gradient(cap,axis=0))
    lengths=np.linalg.norm(ns,axis=2)
    for k in range(5):
        for i in range(SEGMENTS//2+1):
            if lengths[k,i]<1e-12:
                ns[k,i]=[1 if cap[k,i,0]>0 else -1,0,0]
            else:
                ns[k,i]/=lengths[k,i]
    for k in range(4):
        for i in range(SEGMENTS//2):
            ids=[(k,i),(k,i+1),(k+1,i+1),(k+1,i)]
            points=np.array([cap[a,b] for a,b in ids])
            normals=np.array([ns[a,b] for a,b in ids])
            uv=np.array([[b/(SEGMENTS//2),a/4] for a,b in ids])
            for ix in ([0,1,2],[0,2,3]):
                g.triangle(points[ix],normals[ix],uv[ix],'rim','nose_cap')

    # Short cylindrical external housing. Radius varies by less than 3%; the
    # opening has an annular lip, recessed walls and a back surface 0.36 behind it.
    g.lathe([(4.70,.302),(4.72,.264)],'white','nozzle_shoulder',segments=32)
    g.lathe([(4.72,.264),(4.76,.270),(4.98,.270),(5.00,.266)],
            'rim','nozzle_outer',segments=32)
    g.lathe([(5.00,.266),(5.00,.241)],'metal','nozzle_lip',segments=32)
    g.lathe([(4.64,.208),(4.82,.224),(4.95,.239),(5.00,.241)],
            'inside','nozzle_recess',segments=32,inward=True)
    for i in range(32):
        a,b=math.tau*i/32,math.tau*(i+1)/32
        g.triangle([[0,0,4.64],[.208*math.cos(a),.208*math.sin(a),4.64],
                    [.208*math.cos(b),.208*math.sin(b),4.64]],[[0,0,1]]*3,
                   [[.5,.5],[.5+.49*math.cos(a),.5+.49*math.sin(a)],
                    [.5+.49*math.cos(b),.5+.49*math.sin(b)]],'shadow','nozzle_back')

    # Fins are thin closed-sided swept solids. Roots enter the body skin; there
    # are no loose plates, separate mounting blocks or geometric fasteners.
    for angle in range(0,360,60):
        g.prism([(.329,4.00),(.744,4.47),(.755,4.62),(.699,4.68),(.290,4.57)],
                angle,.006,'fin','tail_fin',omit_root=True)
    for angle in (0,60,120,180):
        g.prism([(.278,1.05),(.565,1.38),(.590,1.61),(.283,1.60)],
                angle,.006,'fin','forward_fin',omit_root=True)

    # An eight-sided ventral housing, inset mouth and actual shallow interior.
    # The swept opening is at the original reference position. Side panels are
    # bounded by upper and lower chamfers, never a thin isolated rectangular board.
    section=np.array([[.280,-.205],[-.280,-.205],[-.320,-.250],[-.320,-.405],
                      [-.250,-.485],[.250,-.485],[.320,-.405],[.320,-.250]])
    profiles=[]
    for z,width_scale,depth_scale in [(-2.40,1,1),(-1.52,1,1),(.68,1,1),
                                     (1.22,.88,.78),(1.65,.54,.19)]:
        xy=section.copy();xy[:,0]*=width_scale
        xy[:,1]=-.205+(xy[:,1]+.205)*depth_scale
        zz=np.full(8,z)
        if z==-2.40:
            zz+=(xy[:,1]+.485)/.280*.38
        profiles.append(np.column_stack([xy,zz]))
    profiles=np.array(profiles)
    for k in range(len(profiles)-1):
        for i in range(8):
            j=(i+1)%8
            pts=np.array([profiles[k,i],profiles[k,j],profiles[k+1,j],profiles[k+1,i]])
            normal=np.cross(pts[1]-pts[0],pts[2]-pts[0])
            center=(profiles[k].mean(0)+profiles[k+1].mean(0))/2
            if normal@(pts.mean(0)-center)<0:normal=-normal
            region='panel' if i in (2,6) else 'belly'
            uv=np.array([[(p[2]+2.4)/4.05,(p[1]+.485)/.28] for p in pts])
            # Horizontal/chamfer surfaces use circumferential V to avoid collapsed UVs.
            if abs(uv[0,1]-uv[1,1])<1e-6:
                uv=np.array([[(pts[0,2]+2.4)/4.05,i/8],[(pts[1,2]+2.4)/4.05,j/8],
                             [(pts[2,2]+2.4)/4.05,j/8],[(pts[3,2]+2.4)/4.05,i/8]])
            g.quad(pts,region,'intake_housing',normal,uv)
    outer=profiles[0]
    inner=outer.copy()
    inner[:,0]*=.88
    inner[:,1]=-.345+(inner[:,1]+.345)*.76
    inner[:,2]+=.014
    # The surrounding rim connects outer and inner skins around the full opening.
    for i in range(8):
        j=(i+1)%8
        g.quad([outer[i],outer[j],inner[j],inner[i]],'rim','intake_lip',[0,0,-1])
    back=inner.copy();back[:,2]=-1.56
    for i in range(8):
        j=(i+1)%8
        pts=np.array([inner[i],inner[j],back[j],back[i]])
        normal=np.cross(pts[1]-pts[0],pts[2]-pts[0])
        center=(inner.mean(0)+back.mean(0))/2
        if normal@(center-pts.mean(0))<0:normal=-normal
        g.quad(pts,'inside','intake_inner',normal)
    for i in range(1,7):
        ix=[0,i,i+1]
        uv=(back[ix,:2]-back[:,:2].min(0))/np.ptp(back[:,:2],axis=0)
        g.triangle(back[ix],[[0,0,-1]]*3,uv,'shadow','intake_back')
    # A small buried aft closure completes the housing where it meets the body.
    rear=profiles[-1]
    for i in range(1,7):
        ix=[0,i,i+1]
        uv=(rear[ix,:2]-rear[:,:2].min(0))/np.ptp(rear[:,:2],axis=0)
        g.triangle(rear[ix],[[0,0,1]]*3,uv,'belly','intake_aft_closure')
    return g
