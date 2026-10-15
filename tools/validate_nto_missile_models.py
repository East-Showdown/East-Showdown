"""Validate both exported western missile meshes and all requested branch bindings."""
from pathlib import Path
import importlib.util
from validate_missile_models import check_model
ROOT=Path(__file__).resolve().parents[1]
for name,count in [('atacms',3476),('jassm',2792)]:
    spec=importlib.util.spec_from_file_location(name,ROOT/f'tools/{name}/build_{name}.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    check_model(name,(f'{name}.mesh',f'{name}_idle.anim',f'nto_{name}',count,module.EQUIPMENT),
                technology_file='common/technologies/missiles_nto.txt',
                equipment_files=('common/units/equipment/ES_guided_missiles.txt',
                                 'common/units/equipment/ES_ballistic_missiles.txt'))
