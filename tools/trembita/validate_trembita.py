from pathlib import Path
import sys,re,subprocess
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from validate_missile_models import check_model,ROOT,block
check_model('trembita',('trembita.mesh','trembita_idle.anim','ukr_trembita',4572,['ukr_drone_missile_equipment_trembita']),technology_file='common/technologies/missiles_ukr.txt')
path='common/units/equipment/ES_guided_missiles.txt'
text=(ROOT/path).read_text(encoding='utf-8-sig')
original=subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT).decode('utf-8-sig').replace('\r\n','\n')
before=block(original,'ukr_drone_missile_equipment_trembita')
after=before.replace('sprite = missile_default','sprite = ukr_trembita')
assert text==original.replace(before,after,1),'Unexpected equipment change'
print('PASS: other missiles and all equipment statistics preserved.')
