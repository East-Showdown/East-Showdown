"""Geran-4 external game art from the supplied image; Y up, nose -Z."""
from pathlib import Path
import sys,math
import numpy as np
from PIL import Image
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(HERE.parent));sys.path.insert(0,str(HERE.parent/'flamingo'));sys.path.insert(0,str(HERE.parent/'shahed'))
from build import Geometry
from build_shahed import surface,box
from model_export import textures,export_rigid
from render import render
OUT=ROOT/'gfx/models/units/missiles/geran4'
COLORS=[(43,47,46),(33,37,37),(51,55,52),(17,21,22),(146,155,155),
        (191,196,184),(97,112,112),(76,85,83),(125,118,62),(25,29,29)]


def geometry():
    g=Geometry()
    g.lathe([(-3.45,.003),(-3.39,.10),(-3.25,.18),(-3.02,.22),(-2.6,.235),
             (-1.7,.235),(-.2,.245),(1.4,.24),(2.2,.20),(2.52,.12)],0,segments=40,part='body')
    for side in (-1,1):
        rows=[]
        for u in (0,.12,.28,.46,.65,.83,1.):
            x=side*(.16+2.29*u);lead=-1.7+3.55*u;end=2.65-.06*u
            rows.append([[x,.11*(1-u*.75)*math.sin(math.pi*t)**.7,lead+(end-lead)*t] for t in (0,.035,.12,.27,.48,.7,.89,1)])
        surface(g,rows,0,1,'wing_top');lower=np.array(rows);lower[:,:,1]*=-.7
        surface(g,lower,1,-1,'wing_bottom')
        for j in range(7):g.quad([rows[-1][j],rows[-1][j+1],lower[-1,j+1],lower[-1,j]],1,part='wing_tip')
        g.prism([(-.08,1.91),(.27,2.00),(.22,2.57),(-.08,2.63)],side*2.45-.015,side*2.45+.015,3,'winglet')
        # Muted rectangular surface patches from the supplied reference.
        for x,z,w,d in [(.64,.55,.34,.52),(.85,1.72,.59,.30),(1.45,2.15,.43,.23)]:
            def y(xx,zz):
                u=(abs(xx)-.16)/2.29;lead=-1.7+3.55*u;end=2.65-.06*u
                return .11*(1-u*.75)*max(math.sin(math.pi*(zz-lead)/(end-lead)),0)**.7+.004
            pts=[[side*xx,y(side*xx,zz),zz] for xx,zz in [(x-w/2,z-d/2),(x+w/2,z-d/2),(x+w/2,z+d/2),(x-w/2,z+d/2)]]
            g.quad(pts,7,[0,1,0],'surface_patch')
        box(g,(side*.13,-.11,2.47),(.06,.13,.45),4,'rear_mount')
    # Small exposed metallic rear pod, with dark nozzle; no propeller in reference.
    g.lathe([(2.42,.115),(2.51,.15),(2.70,.16),(2.91,.14),(3.02,.115)],5,center=(0,-.06),segments=32,part='rear_pod')
    g.lathe([(2.64,.164),(2.69,.164)],6,center=(0,-.06),segments=32,part='pod_band')
    g.lathe([(2.94,.096),(3.08,.096)],4,center=(0,-.06),segments=32,part='nozzle')
    for j in range(32):
        a,b=j*math.tau/32,(j+1)*math.tau/32
        g.triangle([[0,-.06,3.04],[.09*math.cos(a),-.06+.09*math.sin(a),3.04],[.09*math.cos(b),-.06+.09*math.sin(b),3.04]],3,[[0,0,1]]*3,part='nozzle_recess')
    return g


if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True);g=geometry()
    textures('geran4',OUT,HERE,COLORS);export_rigid(g,'geran4',OUT,HERE,(0,-.06,3.08))
    p=np.array(g.p);n=np.array(g.n);t=np.array(g.tri).reshape(-1,3)
    assert np.isfinite(p).all() and np.allclose(np.linalg.norm(n,axis=1),1)
    assert (np.sum(np.cross(p[t[:,1]]-p[t[:,0]],p[t[:,2]]-p[t[:,0]])*n[t[:,0]],axis=1)>0).all()
    model=OUT/'geran4.mesh'
    render((-8,8,-12),(1400,900),'GERAN-4',model).save(HERE/'preview.png')
    sheet=Image.new('RGB',(1600,1100))
    for i,(eye,label) in enumerate([((-8,8,-12),'FRONT'),((8,6,12),'REAR'),((0,14,-.01),'TOP'),((-12,0,0),'SIDE')]):
        sheet.paste(render(eye,(800,550),label,model),(i%2*800,i//2*550))
    sheet.save(HERE/'views.png');print('PASS: finite geometry, unit normals and face winding.')
