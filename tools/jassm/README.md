# JASSM game model

External visual asset based on the supplied reference image. Y up, nose -Z; arbitrary art units.
2,792 triangles, one mesh/material, 512x512 DDS diffuse/normal/specular atlas with 10 mip levels.
Includes editable OBJ/MTL, deterministic Python generator, idle pose and independent entity states.

Rebuild from repository root:
```
python tools/jassm/build_jassm.py
python tools/jassm/render_jassm.py
python tools/validate_nto_missile_models.py
```

Equipment assignments:
- `nto_medium_guided_missile_agm86`
- `nto_medium_guided_missile_129`
- `nto_medium_guided_missile_142`
- `nto_medium_guided_missile_158`
- `nto_medium_guided_missile_slam`
- `nto_sea_guided_missile_equipment_seaeagle`
- `nto_sea_guided_missile_equipment_seaskua`
- `nto_sea_guided_missile_equipment_harpoon`
- `nto_sea_guided_missile_equipment_agm158c`
- `nto_sea_guided_missile_equipment_exocet`
- `nto_sea_guided_missile_equipment_as15tt`
- `nto_sea_guided_missile_equipment_rbs15`

Validated exported geometry, normals, tangent frames, UVs, bounds, textures, bone/pose data,
entity states and equipment bindings. Preview and four-view sheet render the actual game mesh.
In-game HOI4 appearance has not been tested. Equipment statistics are unchanged.
