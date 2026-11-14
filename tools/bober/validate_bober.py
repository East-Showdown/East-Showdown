from pathlib import Path
import sys,re
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from validate_missile_models import check_model,ROOT,block,read
check_model('bober',('bober.mesh','bober_idle.anim','ukr_bober',7648,['ukr_guided_uav_bober','ukr_guided_uav_rubaka']),technology_file='common/technologies/missiles_ukr.txt')
for folder in ('bober','orlan'):
    base=ROOT/'gfx/models/units/missiles'/folder
    m=read(base/f'{folder}.mesh').child('object').children[0].child('mesh')
    a=read(base/f'{folder}_idle.anim');info=a.child('info')
    p=np.array(m.get('p')).reshape(-1,3)
    indices=np.array(m.child('skin').get('ix')).reshape(-1,4)
    pivot=np.array(info.child('propeller').get('t'))
    local=p[indices[:,0]==1]-pivot
    lo=np.array(m.child('aabb').get('min'));hi=np.array(m.child('aabb').get('max'))
    for q in np.array(a.child('samples').get('q')).reshape(-1,4):
        angle=2*np.arctan2(q[2],q[3]);c,s=np.cos(angle),np.sin(angle)
        points=local@np.array([[c,s,0],[-s,c,0],[0,0,1]])+pivot
        assert (points>=lo-1e-5).all() and (points<=hi+1e-5).all(),folder+' animated bounds'
text=(ROOT/'common/units/equipment/ES_guided_missiles.txt').read_text(encoding='utf-8-sig')
assert 'sprite = rus_orlan' in block(text,'ukr_guided_uav_lut')
assert (ROOT/'gfx/entities/rus_orlan.asset').exists()
assert (ROOT/'gfx/entities/rus_orlan.gfx').exists()
for name in ('rus_guided_uav_gerbera','rus_guided_uav_bm35','rus_guided_uav_molniya','rus_guided_uav_molniya2'):
    assert 'sprite = rus_orlan' in block(text,name)
print('PASS: Liutyi reuses Orlan; previous Orlan bindings preserved; propellers stay inside bounds.')
