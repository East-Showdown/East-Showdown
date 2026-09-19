# Trembita / Ukraine

Original visual game asset from the two user-supplied references.
4,572 triangles, 13,716 vertices, one material; 512x512 DDS diffuse, normal
and specular atlases with 10 mip levels. Editable OBJ/MTL and PNG preview included.
Y up, nose -Z; arbitrary art units. External game artwork only.

Bevelled rectangular fuselage, pale nose and tail, tandem wings with curved yellow
winglets, dark dorsal engine on mounting saddles, lower tube and TREMBITA lettering.
Assigned only to `ukr_drone_missile_equipment_trembita`, using `ukr_trembita`.
Equipment statistics and other Ukrainian missile visuals are unchanged.

Rebuild from the repository root with Python, NumPy and Pillow:
```
python tools/trembita/build_trembita.py
python tools/trembita/render_trembita.py
python tools/trembita/validate_trembita.py
```
The generator uses shared Geometry and mesh helpers in tools/flamingo and tools/tu95.
An Arial Bold font from Windows supplies the locally generated label atlas tile.
Geometry, materials, animation states and binding are validated; HOI4 runtime display
has not been checked. Preview images show the actual exported mesh.
