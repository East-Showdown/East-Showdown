"""Render actual exported game geometry in four views."""
from pathlib import Path
import sys
from PIL import Image
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'flamingo'))
from render import render
MODEL=HERE.parents[1]/'gfx/models/units/missiles/kh69/kh69.mesh'

if __name__=='__main__':
    render((-10,6,-12),label='KH-69 / RUSSIA',model=MODEL).save(HERE/'preview.png')
    sheet=Image.new('RGB',(1600,1200))
    for i,(eye,label) in enumerate([((-12,0,0),'SIDE'),((0,12,-.001),'TOP'),((8,-6,10),'REAR / UNDERSIDE'),((0,1,-16),'FRONT')]):
        sheet.paste(render(eye,(800,600),label,model=MODEL),(i%2*800,i//2*600))
    sheet.save(HERE/'views.png')
