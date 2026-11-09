# Ukrainian assault battalion icons

Generated with the built-in image generator, then fitted to the mod's existing
32×32 RGBA decision-icon canvas (28×28 content area, 2 px transparent padding).
The high-resolution PNGs in `sources/` retain transparency and can be opened in
Photoshop. No PSD or Photoshop execution is claimed.

Final runtime assets:

- `gfx/interface/decisions/UKR_assault_49_Karpatska_Sich.png`
- `gfx/interface/decisions/UKR_assault_48.png`
- `gfx/interface/decisions/UKR_assault_214_OPFOR.png`

`comparison-v2.png` shows 116, 117, 118 mechanized brigade references followed by
the new 49, 48 and 214 icons, enlarged with nearest-neighbour sampling.

## Current revision

The initial glossy metallic treatment was rejected. The current assets use
dark matte fields, muted ochre/olive symbols, restrained shading and thin dull
outlines matched against enlarged 116/117/118 references. Exact prompts for
this revision are saved in `prompts-v2.json`. `comparison.png` retains the
initial comparison; `sources/` contains the current high-resolution PNGs.

## Initial generation prompts (superseded)

Shared direction: one production-ready HOI4 decision icon, centered upright
shield on a transparent background. Use the supplied unit emblem for content
and `116th.png` / `117th.png` for the existing mod's style. Professional
Photoshop 2022 game UI treatment: clean silhouette, subtle metallic bevel,
restrained upper-left highlights, dark textured enamel, crisp colored insignia,
legible after reduction to 32×32. Preserve heraldic identity and colors. Remove
all MilitaryLand text and logos. No extra symbols, background or watermark.

- **49 / Karpatska Sich:** black shield, gold rim, sword integrated in the
  trident, exact title `КАРПАТСЬКА СІЧ`.
- **48 / Qırım:** black and gold shield, portrait wearing a fez, tamga, helmet,
  crossed swords, blue/yellow branches; `ОШБ 48` and `QIRIM BATALYONI`.
  Simplify fine border motifs for small-size legibility.
- **214 / OPFOR:** angular black shield, silver rim, gold boar with red mouth
  and white tusks, `214 ОШБ`, `OPFOR`, crossed gold arrows.

Targeted revisions: remove exterior glow from the 49 shield and retain a fully
transparent exterior; correct the first Cyrillic letter of the 214 inscription
to a plain oval `О`, not `Ф`, while preserving the remaining artwork.

## Unit behavior

The initial 49th infantry unit uses the shared `Pechotniy batalion` template
and retains unique ID `17802001`. The reform decision removes that ID before
spawning assault unit `17802002`. The dedicated infantry template is removed.
Both 48th spawn-location variants now start with experience factor 1.0; the
49th assault spawn already had 1.0. The mod's veteran threshold is 0.8.

These changes target newly created units; existing save-game templates and
already spawned units are not retroactively migrated.
