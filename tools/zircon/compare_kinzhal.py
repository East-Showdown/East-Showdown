"""Compare actual exported missiles using their entity scales and one camera fit."""
from pathlib import Path
import json
import re
import numpy as np
from PIL import Image,ImageDraw
from render_zircon import render,HERE,ROOT,font
from pdx_io import read


def main():
    models=[]
    for name in ('kinzhal','zircon'):
        asset=(ROOT/f'gfx/entities/rus_{name}.asset').read_text()
        scale=float(re.search(r'\bscale\s*=\s*([.\d]+)',asset).group(1))
        path=ROOT/f'gfx/models/units/missiles/{name}/{name}.mesh'
        mesh=read(path).child('object').children[0].child('mesh')
        p=np.array(mesh.get('p')).reshape(-1,3)*scale
        models.append((name,path,scale,p))
    # Side view projects Z to horizontal and Y to vertical. Both models use the
    # same projected bounds, so equal lengths occupy exactly the same pixels.
    points=np.concatenate([p for _,_,_,p in models])
    bounds=(points[:,[2,1]].min(0),points[:,[2,1]].max(0))
    sheet=Image.new('RGB',(1800,1240))
    stats={}
    for i,(name,path,scale,p) in enumerate(models):
        length=float(np.ptp(p[:,2]))
        label=f'{name.upper()} / LENGTH {length:.2f} / ENTITY SCALE {scale:.2f}'
        sheet.paste(render((-12,0,0),(1800,620),label,model=path,
                           world_scale=scale,frame_bounds=bounds),(0,i*620))
        stats[name]={'entity_scale':scale,'scaled_length':length,
                     'scaled_width_with_fins':float(np.ptp(p[:,0]))}
    draw=ImageDraw.Draw(sheet)
    for x in (70,1730):
        draw.line((x,65,x,1175),fill=(80,101,109),width=1)
    draw.text((900,618),'ОДИН МАСШТАБ • длина в игровых единицах',anchor='mm',
              font=font(20),fill=(215,228,230))
    sheet.save(HERE/'kinzhal_comparison.png')
    (HERE/'scale_comparison.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(stats)


if __name__=='__main__':
    main()
