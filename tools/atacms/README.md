# ATACMS game model

External visual asset based on the supplied reference image. Y up, nose -Z; arbitrary art units.
3,476 triangles, one mesh/material, 512x512 DDS diffuse/normal/specular atlas with 10 mip levels.
Includes editable OBJ/MTL, deterministic Python generator, idle pose and independent entity states.

Rebuild from repository root:
```
python tools/atacms/build_atacms.py
python tools/atacms/render_atacms.py
python tools/validate_nto_missile_models.py
```

Equipment assignments:
- `nto_light_guided_missile_equipment_gmlrs`
- `nto_ballistic_missile_equipment_atacams`
- `nto_ballistic_missile_equipment_atacams_mod`
- `nto_ballistic_missile_equipment_atacams_2`
- `nto_ballistic_missile_equipment_atacams_2_mod`

Validated exported geometry, normals, tangent frames, UVs, bounds, textures, bone/pose data,
entity states and equipment bindings. Preview and four-view sheet render the actual game mesh.
In-game HOI4 appearance has not been tested. Equipment statistics are unchanged.
