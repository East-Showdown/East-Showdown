# Ammunition system

Reference for authors of submods, events and focuses. Hearts of Iron IV 1.19.3.

[Русская версия](README.md)

## 1. How it works

All calculations run once a day for each country (`on_daily`, effect `ammunition_on_daily`).
Amounts are stored in thousands of ammunition units; flows are per day.

### Supply level

The level `ammunition_level` sets the share of the consumption norm the troops receive. 1 = 100 %.

- Range: from `level_min` to the cap `cap`.
- `cap = clamp(level_max_base + ammunition_level_cap, level_min, level_max_abs)`.
  By default the cap is 1.25 and the absolute maximum is 2.
- The player changes the level in the window in steps of 1 / 10 / 100 % (click, Ctrl, Shift; right click lowers it).

### Consumption

Only the sub-units in the table consume ammunition. Bonuses and penalties apply to their equipment.

| Equipment archetype | Battalion | Support company |
| --- | --- | --- |
| `artillery_equipment` | `towed_art` | `artillery` |
| `sp_artillery_chassis` | `sp_art` | `support_spa` |
| `sp_heavy_artillery_chassis` | `sp_heavy_art` | `support_heavy_spa` |
| `sp_mlrs_chassis` | `MRLS` | `support_mlrs` |
| `sp_tos_chassis` | `TOS` | `support_tos` |
| `mortar_equipment` | | `mortar` |

Consumption is counted per general. A general counts if he is assigned to an army, leads at least one division
and does not lead an army group (a field marshal is skipped; his armies count through their own generals).
An AI country at peace consumes nothing.

A general's consumption at level 1:

```
base = Σ n_X · k_X
consumption = base · (factor_off · div_off + factor_def · div_def) / div_all
```

- `n_X` - the number of sub-units `X` under the general (`num_battalions_with_type@X`), support companies included.
- `k_X` - daily consumption of one sub-unit, constant `k_<sub_unit>`.
- `div_off`, `div_def` - the general's divisions in offensive and defensive combat; `div_all` - all his divisions.
- `factor_off`, `factor_def` - attack and defence multipliers. Each is multiplied by the game rule factor
  and by `(1 + that side's consumption modifier)`, floored at 0.

Sub-units are assumed to be spread evenly over the general's divisions. Divisions out of combat consume nothing.

Example. A general has 10 divisions with 20 `towed_art` battalions and 10 `artillery` companies.
Base = 20 · 0.08 + 10 · 0.04 = 2.0 k. 4 divisions attack, 3 defend.
Consumption = 2.0 · (2 · 4 + 1 · 3) / 10 = 2.2 k per day at level 1, 2.75 k at level 1.25.

Daily need: `need = level · Σ generals' consumption`.

### Cover and supply

- Available = stock before spending + the day's income.
- Spent = `min(need, available)`.
- Cover `cover = spent / need`. With no consumption, `cover = 1` if available is above 0, otherwise 0.
- Supply `s = level · cover`. All effects depend on it.

### Effects: idea steps

`s` is rounded to a 5 % step. The country gets one national idea `ammunition_<percent>`
(`ammunition_0` … `ammunition_200`). The 100 % step has no idea. The idea changes only when the step changes.

The idea gives `equipment_bonus` to the archetypes in the table above:

| Stat | Curve | s = 0 | s = 1 | s = 1.25 | s = 2 |
| --- | --- | --- | --- | --- | --- |
| `soft_attack`, `hard_attack` | `attack` | -70 % | 0 | +15 % | +30 % |
| `breakthrough` | `breakthrough` | -65 % | 0 | +20 % | +35 % |
| `defense` | `defense` | -15 % | 0 | +15 % | +25 % |
| `supply_consumption` | `supply_consumption` | -70 % | 0 | +15 % | +30 % |

Values are linear between points. The defaults are set in `tools/ammo/ammunition_curves.txt`.

The bonus applies to the equipment stat. So its share in a division is proportional to the share of consuming sub-units.

AI aggressiveness (`ai_focus_aggressive_factor`) comes from the dynamic modifier `ammunition_effects` along the curve
`ai_aggressive`: -0.8 / 0.2 / 0.3 / 0.4 at `s` = 0 / 1 / 1.25 / 2.

### Automation

An AI country is always automated. The player turns automation on and off with a button in the window.
The automation level is computed daily for every country and stored in `ammunition_level_auto`.
It is copied to `ammunition_level` only for the AI and when automation is on.

Rule:

1. `need_ref` - need at level 1. If it is 0 (no combat), the defensive consumption of all the country's consuming
   sub-units is used.
2. `L(D) = (stock / D + daily income) / need_ref` - the level at which stock plus income lasts `D` days.
3. If `L(ai_days_low) < 1`, level = `L(ai_days_low)`, but not below `ai_level_min`.
   If `L(ai_days_low) > 1`, level = `L(ai_days_high)`, but not below 1. Otherwise level = 1.
4. The modifier `ammunition_level_target` is added.
5. The result is clamped to `[level_min; cap]`.

With default settings: stock for less than 120 days lowers the level; more than 365 days raises it;
in between it is 100 %. If `need_ref` is 0, the automation level is 1 + `ammunition_level_target`.

### Storage

- `ammunition_value_k` - ready ammunition. Only it is spent.
- `ammunition_old_value_k` - ammunition that needs recovery.
- Plant capacity: `daily_ammunition_gain / 1000 · (1 + ammunition_plants_efficiency_factor)` k per day.
- A slider splits capacity between production (share `ammunition_produce_factor`, starts at `produce_share_start`)
  and recovery (the rest up to 1).
- Production: capacity · share · `(1 + ammunition_produce_efficiency_factor)`.
- Recovery: capacity · share · `(recovery_efficiency_base + ammunition_recovery_efficiency_factor)`.
  It moves ammunition from `ammunition_old_value_k` to ready. When there is nothing left to recover,
  the unused share of capacity goes to production.
- Capacity = silos (`ammunition_capacity_k`) + field depots. Field depots = consumption of all the country's
  consuming sub-units at multiplier 1 for `field_storage_days` days.
- Stock above capacity is removed from `ammunition_old_value_k` first, then from ready ammunition.

Starting stock (k): every country 5000 ready and 3200 to recover; `NTO` 5900 and 400; `UKR` 2400 and 2520;
`RUS` 6800 and 3600 (`common/on_actions/ammo_on_actions.txt`).

## 2. Configuration

### `common/script_constants/ammo_constants.txt`

Block `ammunition`. Script reads a constant as `constant:ammunition.<name>`.

| Constant | Meaning | Unit | Default |
| --- | --- | --- | --- |
| `k_towed_art`, `k_sp_art`, `k_sp_heavy_art`, `k_MRLS` | battalion consumption | k per day | 0.08 |
| `k_TOS` | TOS battalion consumption | k per day | 0.1 |
| `k_artillery`, `k_support_spa`, `k_support_heavy_spa`, `k_support_mlrs` | support company consumption | k per day | 0.04 |
| `k_support_tos` | TOS company consumption | k per day | 0.05 |
| `k_mortar` | mortar company consumption | k per day | 0.01 |
| `factor_off` | consumption multiplier of attacking divisions | multiplier | 2 |
| `factor_def` | consumption multiplier of defending divisions | multiplier | 1 |
| `level_min` | lower bound of the level | share | 0 |
| `level_max_base` | level cap without modifiers | share | 1.25 |
| `level_max_abs` | absolute level maximum and end of the curves | share | 2 |
| `ai_days_low` | below this stock automation lowers the level | days | 120 |
| `ai_days_high` | above this stock automation raises the level | days | 365 |
| `ai_level_min` | lower bound of the automation level before `ammunition_level_target` | share | 0.2 |
| `field_storage_days` | field depot capacity | days of consumption | 7 |
| `recovery_efficiency_base` | units recovered per unit of capacity | multiplier | 2 |
| `produce_share_start` | starting share of capacity for production | share | 0.7 |

`produce_share_start` applies only when a country is initialised.
After changing `level_max_abs`, run the generator: the curves must end at the new value.

### `tools/ammo/ammunition_curves.txt`

One effect curve per line: `name = { s = value s = value … }`.

```
attack = { 0 = -0.7  1 = 0  1.25 = 0.15  2 = 0.3 }
```

Rules:

- All five curves are required: `attack`, `breakthrough`, `defense`, `supply_consumption`, `ai_aggressive`.
- At least two points. The first point is `0`, the last is `level_max_abs`. `s` strictly increases.
- Any number of points. Values are linear between points.
- Values are fractions: -0.7 = -70 %. For `ai_aggressive` the value is `ai_focus_aggressive_factor`.
- `#` starts a comment.

### Generator

```
python3 tools/ammo/generate_ammunition_effects.py
```

Reads the constants and curves. Exits with an error if a curve breaks the rules. Writes:

| File | Content |
| --- | --- |
| `common/ideas/ammo_ideas.txt` | idea steps `ammunition_<percent>` with `equipment_bonus` |
| `common/scripted_effects/ammo_idea_effects.txt` | `ammunition_update_idea`: picks the idea from `s` |
| `common/scripted_effects/ammo_curve_effects.txt` | `ammunition_calculate_effects`: curve values for the window and the AI |
| `localisation/russian/ammo_ideas_l_russian.yml`, `localisation/english/ammo_ideas_l_english.yml` | idea names and descriptions |

Never edit these files by hand. Change `tools/ammo/ammunition_curves.txt`, the constants or the generator and run it again.

### Game rule

`es_ammunition_consumption_factor` multiplies `factor_off` and `factor_def`. Options 50-300 %
(`ES_AMMUNITION_CONSUMPTION_FACTOR_RULE_50` … `_300`), default 100 %.
The value is stored in `global.ammunition_consumption_rule_factor`.

## 3. API for events and focuses

### Modifiers

They work in any country modifier block: idea, dynamic modifier, advisor and so on.

| Modifier | Effect | Unit |
| --- | --- | --- |
| `ammunition_level_cap` | shifts the level cap `cap` | level share: 0.25 = +25 % |
| `ammunition_level_target` | added to the automation and AI level; no effect on a manual level | level share |
| `ammunition_consumption_offensive_factor` | attack consumption · (1 + x), floored at 0 | share |
| `ammunition_consumption_defensive_factor` | defence consumption · (1 + x), floored at 0 | share |
| `daily_ammunition_gain` | nominal plant capacity | units per day (not thousands) |
| `ammunition_plants_efficiency_factor` | plant capacity · (1 + x), floored at 0 | share |
| `ammunition_produce_efficiency_factor` | production · (1 + x), floored at 0 | share |
| `ammunition_recovery_efficiency_factor` | added to `recovery_efficiency_base` | units per unit of capacity |
| `ammunition_capacity_k` | silo capacity | k |
| `ammunition_plants`, `ammunition_silos` | building counters for the window | count |

```
my_idea = {
	modifier = {
		ammunition_level_cap = 0.1
		ammunition_consumption_offensive_factor = -0.15
		ammunition_plants_efficiency_factor = 0.2
	}
}
```

### Effects

Both effects take their input from the temporary variable `temp_delta` (level share).

`ammunition_raise_level` - for events. For a player on manual control it refreshes dynamic modifiers,
adds `temp_delta` to the level and clamps it to the cap. So the cap from a modifier added by the same event
applies at once. Under automation and for the AI it does nothing: there `ammunition_level_target` shifts the level.
An event that changes the level should also set a target modifier.

`ammunition_change_level` - adds `temp_delta` and clamps the level. It has no checks; the window buttons call it.
Under automation and for the AI the next day overwrites the level.

### Dynamic modifier `ammunition_war_mobilisation`

Example: `ammunition_level_target = 0.25`, `ammunition_level_cap = 0.25`.

```
option = {
	name = my_event.1.a
	add_dynamic_modifier = { modifier = ammunition_war_mobilisation days = 60 }
	set_temp_variable = { temp_delta = 0.25 }
	ammunition_raise_level = yes
}
```

The modifier raises the automation target and the cap. `ammunition_raise_level` raises the manual level.
So the event works in either mode.

### Flags

| Flag | Meaning |
| --- | --- |
| `ammunition_supply_factor_ai_disable` | country flag: set - automation is off, the level is manual. No effect on the AI. |
| `RUS_genstab_ammunition_supply_factor_limitation` | country flag for `original_tag = RUS`: enables the dynamic modifier `ammunition_RUS_genstab_limitation` (`ammunition_level_cap = -0.75`, cap 0.5 with default settings). |

```
set_country_flag = ammunition_supply_factor_ai_disable   # manual control
clr_country_flag = ammunition_supply_factor_ai_disable   # automation
```

### Country variables

Values update once a day; before the first day after the start some variables are not set.
Suffix `_k` - thousands of units. Share: 1 = 100 %.

| Variable | Meaning | Unit |
| --- | --- | --- |
| `ammunition_value_k` | ready ammunition in stock | k |
| `ammunition_old_value_k` | ammunition to recover | k |
| `sum_ammunition_value_k` | total in stock | k |
| `ammunition_max_storage_capacity_k` | total capacity | k |
| `ammunition_silos_capacity_k` | silo building capacity | k |
| `ammunition_field_storage_capacity_k` | field depot capacity | k |
| `ammunition_level` | supply level | share |
| `ammunition_level_auto` | automation level | share |
| `ammunition_level_max` | cap `cap` | share |
| `ammunition_supply` | supply `s` | share |
| `ammunition_cover` | cover `cover` | share |
| `ammunition_need_k` | daily need | k per day |
| `ammunition_need_level_1_k` | need at level 1 | k per day |
| `ammunition_spent_k` | spent today | k per day |
| `ammunition_generation_value_k` | daily income (production + recovery) | k per day |
| `ammunition_delta_value_k` | income minus spending | k per day |
| `ammunition_days_at_level_1` | days the ready stock lasts at `need_ref` with income, at most 1000 | days |
| `ammunition_divisions` | divisions of counted generals | count |
| `ammunition_divisions_off`, `ammunition_divisions_def` | of them in attack, in defence | count |

```
available = {
	check_variable = { ammunition_supply < 0.8 }
	check_variable = { ammunition_value_k > 1000 }
}
```

## 4. Adding a consuming sub-unit or archetype

1. Add the constant `k_<sub_unit>` to `common/script_constants/ammo_constants.txt`.
   The sub-unit name is as in `common/units`.
2. Add a line to the effect `ammunition_calculate_base_consumption`
   (`common/scripted_effects/ammo_scripted_effects.txt`):

   ```
   add = { value = num_battalions_with_type@my_sub_unit multiply = constant:ammunition.k_my_sub_unit }
   ```

3. If the sub-unit uses equipment of a new archetype, add the archetype to the `ARCHETYPES` list
   in `tools/ammo/generate_ammunition_effects.py`. The idea descriptions for localisation are set there too.
4. Run `python3 tools/ammo/generate_ammunition_effects.py`.

The bonus key is the archetype: every model and variant of the archetype gets the bonus.

## 5. Buildings

| Building | Cost | State limit | Country modifiers |
| --- | --- | --- | --- |
| `ammunition_plant` | 7200 | 3, shared slots | `daily_ammunition_gain = 500` (0.5 k per day), `ammunition_plants = 1` |
| `ammunition_silo` | 4200 | 5, shared slots | `ammunition_capacity_k = 500` (500 k), `ammunition_silos = 1` |

Infrastructure affects the construction speed of both.

## 6. Known limits

- Divisions without a general are not counted: neither in consumption nor in the division counts.
- A general's sub-units are assumed to be spread evenly over his divisions.
- An idea change reaches divisions at their daily stat recalculation, up to 24 hours.
- Equipment bonuses add up with other bonuses to the same stat; they do not multiply:
  `stat = base · (1 + Σ bonuses)`.
- Countries created after the game start begin with an empty stock.
