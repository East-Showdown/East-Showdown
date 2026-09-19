"""Validate Neptune mesh, registration and requested equipment assignments."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from validate_missile_models import check_model,ROOT,block
check_model('neptun',('neptun.mesh','neptun_idle.anim','ukr_neptun',9910,
    ['ukr_sea_guided_missile_neptun']),technology_file='common/technologies/missiles_ukr.txt')
text=(ROOT/'common/units/equipment/ES_guided_missiles.txt').read_text(encoding='utf-8-sig')
assert 'sprite = rus_orlan' in block(text,'ukr_guided_uav_e300enterprise')
assert (ROOT/'gfx/entities/rus_orlan.asset').is_file()
assert (ROOT/'gfx/entities/rus_orlan.gfx').is_file()
assert (ROOT/'gfx/models/units/missiles/orlan/orlan.mesh').is_file()
print('PASS: E-300 Enterprise uses the existing Orlan model.')
