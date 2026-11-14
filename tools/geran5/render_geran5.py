"""Preview actual Geran-5 game geometry."""
from pathlib import Path
import sys
from PIL import Image
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'flamingo'))
from render import render
MODEL=HERE.parents[1]/'gfx/models/units/missiles/geran5/geran5.mesh'

if __name__=='__main__':
    render((-8,10,-12),label='GERAN-5 / RUSSIA',model=MODEL).save(HERE/'preview.png')
    sheet=Image.new('RGB',(1600,1200))
    for i,(eye,label) in enumerate([((0,12,-.001),'TOP'),((9,6,10),'REAR'),((-12,0,0),'SIDE'),((0,1,-16),'FRONT')]):
        sheet.paste(render(eye,(800,600),label,model=MODEL),(i%2*800,i//2*600))
    sheet.save(HERE/'views.png')
