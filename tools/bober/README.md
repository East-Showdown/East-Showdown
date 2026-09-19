# Bober / Rubaka

Visual game model based on the five user-supplied references. 7,648 triangles,
one material, 512x512 DDS atlas with mipmaps. Original geometry and palette;
no reference-image pixels are embedded. Y up, nose -Z, arbitrary art units.

Rounded body, front canards, rear main wing, dorsal/ventral fins, external engine
covers, fixed three-wheel landing gear, and a two-blade animated pusher propeller.
Both wings and canards extend into the body so their roots are attached.
Two bones: body and propeller. OBJ is the editable static pose; the build script
recreates the game rig and the looping propeller animation.

Assignments:
- ukr_guided_uav_bober -> ukr_bober
- ukr_guided_uav_rubaka -> ukr_bober
- ukr_guided_uav_lut -> existing rus_orlan (shared mesh and animation)

Rebuild from the repository root (Python, NumPy, Pillow):
```
python tools/bober/build_bober.py
python tools/bober/render_bober.py
python tools/bober/validate_bober.py
```
File validation checks geometry, shading data, DDS, animation and bindings.
The complete propeller cycle is checked against the exported bounds.
HOI4 runtime rendering has not been tested.
