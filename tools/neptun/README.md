# R-360 Neptune game model

Original external game mesh based on the five user-supplied reference renders.
Y up, nose -Z; arbitrary art units. Rounded nose, four main wings and four tail
fins in an X arrangement, integrated belly fairing, recessed exhaust, side
fairings and blue R-360 marking. 9,910 triangles, one material and one pose bone.

Rebuild with `python tools/neptun/build_neptun.py`, render with
`python tools/neptun/render_neptun.py`, and validate with
`python tools/neptun/validate_neptun.py` (NumPy and Pillow required).

Equipment: `ukr_sea_guided_missile_neptun` uses `ukr_neptun`.
`ukr_guided_uav_e300enterprise` reuses the existing `rus_orlan` model.
Balance values and technology unlocks are unchanged. In-game visual verification
is still required; previews render the exported game mesh directly.
