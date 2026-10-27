# -*- coding: utf-8 -*-
"""
East Showdown - balance settings

Used by balance_calc.py. Plain Python dicts - edit the numbers, rerun the calculator.

  build_cost_ic       = BASE + sum(stat * IC weight)              (+ sum(multiply_stat * MULT weight) for modules)
  supply_consumption  = sum(stat * SUPPLY weight)

Negative stats reduce the cost, except those listed in IC_IGNORE_NEGATIVE
(reliability by default), which never lower build_cost_ic.

=============================================================================
ИНСТРУКЦИЯ (RU)
=============================================================================
Этот файл - настройки калькулятора balance_calc.py. Он считает
build_cost_ic (стоимость в IC) и supply_consumption (расход снабжения)
для снаряжения из common/units/equipment и модулей из
common/units/equipment/modules.

ФОРМУЛЫ
  build_cost_ic      = base + сумма(стат * вес IC)
                       (+ сумма(multiply_stats * mult_weights) для модулей)
                       затем * ic_multiplier из правила (если задан)
  supply_consumption = сумма(стат * вес снабжения)

  Отрицательные статы уменьшают стоимость, КРОМЕ статов из списка
  IC_IGNORE_NEGATIVE (по умолчанию reliability) - их минус в IC не считается.
  Для модулей берутся статы из add_stats, для снаряжения - статы самого
  варианта (недостающие наследуются от архетипа).

ЗАПУСК (из корня репозитория)
  python tools/balance/balance_calc.py
      Пробный прогон: показывает, что изменится. Файлы НЕ меняются.
  python tools/balance/balance_calc.py --write
      Записать новые значения в файлы игры.
  python tools/balance/balance_calc.py --explain "*t72*"
      Показать расчёт по каждому стату для подходящих имён.
  python tools/balance/balance_calc.py --file "*art*"
      Только файлы, подходящие под маску.
  python tools/balance/balance_calc.py --name "sov_*"
      Только снаряжение/модули с подходящим именем.
  python tools/balance/balance_calc.py --profile hull --only ic
      Только один профиль; --only ic | supply - только одно поле.
  python tools/balance/balance_calc.py --unmapped
      Список того, к чему не подходит ни одно правило.
  python tools/balance/balance_calc.py --csv report.csv
      Полный отчёт в CSV (открывается в Excel).
  python tools/balance/balance_calc.py --all
      Показывать также значения, которые уже совпадают.

КАК МЕНЯТЬ НАСТРОЙКИ
  1. Цена/снабжение за стат - меняйте числа в weights нужного профиля
     (SUPPLY_PROFILES или IC_PROFILES).
     base  - фиксированная добавка к цене,
     round - сколько знаков после запятой записывать (0 = целое число).
  2. Какой профиль к чему применяется - EQUIPMENT_RULES (снаряжение) и
     MODULE_RULES (модули). Правила проверяются сверху вниз, срабатывает
     ПЕРВОЕ подходящее. Условия: file, archetype, type, category, name
     (можно маски с *). "ic"/"supply" = имя профиля или None (не трогать).
     "ic_multiplier": 1.5 = +50% к посчитанной цене.
  3. Чтобы калькулятор не трогал конкретные вещи - впишите имена в EXCLUDE.
  4. Сохраните файл, запустите пробный прогон, проверьте, затем --write.
     Перед --write лучше закоммитить изменения в git, чтобы легко откатить.
"""

# ---------------------------------------------------------------------------
# SUPPLY PROFILES  ->  supply_consumption
# RU: ПРОФИЛИ СНАБЖЕНИЯ - расход снабжения за 1 единицу стата.
# ---------------------------------------------------------------------------
SUPPLY_PROFILES = {
    # Infantry equipment (rifles, mortars, ATGM, MANPADS, grenade launchers)
    "infantry": {
        "round": 2,
        "weights": {
            "soft_attack": 0.002,
            "hard_attack": 0.003,
            "air_attack": 0.002,
            "ap_attack": 0.0001,
        },
    },
    # Vehicle modules ("add_stats") and towed artillery
    "vehicle": {
        "round": 2,
        "weights": {
            "soft_attack": 0.01,
            "hard_attack": 0.012,
            "air_attack": 0.002,
            "ap_attack": 0.0002,
        },
    },
}

# ---------------------------------------------------------------------------
# IC PROFILES  ->  build_cost_ic
#   base       : flat cost added on top
#   round      : decimals in the written value
#   weights    : IC per 1 point of a stat (equipment stats / module add_stats)
#   mult_weights (modules only): IC per 1.0 (=100%) of a multiply_stats entry
#
#   RU: ПРОФИЛИ IC - стоимость за 1 единицу стата.
#     base         - фиксированная добавка к цене
#     round        - знаков после запятой (0 = целое)
#     weights      - IC за 1 единицу стата (статы снаряжения / add_stats модуля)
#     mult_weights - только модули: IC за 1.0 (=100%) в multiply_stats
# ---------------------------------------------------------------------------
IC_PROFILES = {
    # ---- infantry -------------------------------------------------------
    "inf_weapons": {          # mortar, atgm, aa, grenade launchers
        "base": 0, "round": 2,
        "weights": {
            "soft_attack": 0.15,
            "hard_attack": 0.20,
            "ap_attack": 0.005,
            "air_attack": 0.40,
        },
    },
    "inf_gear": {             # guns, vests, uniform
        "base": 0, "round": 2,
        "weights": {
            "soft_attack": 0.03,
            "hard_attack": 0.04,
            "ap_attack": 0.001,
            "breakthrough": 0.02,
            "defense": 0.01,
        },
    },

    # ---- vehicles -------------------------------------------------------
    "hull": {
        "base": 0, "round": 2,
        "weights": {
            "breakthrough": 0.20,
            "defense": 0.10,
            "hardness": 3,
            "armor_value": 0.01,
            "reliability": 0.005,
        },
    },
    "engine": {
        "base": 0, "round": 2,
        "weights": {
            "breakthrough": 0.20,
            "reliability": 0.25,
            "maximum_speed": 0.10,
        },
    },
    "module": {
        "base": 0, "round": 2,
        "weights": {          # add_stats
            "breakthrough": 0.20,
            "defense": 0.10,
            "air_attack": 0.40,
            "soft_attack": 0.30,
            "hard_attack": 0.40,
            "ap_attack": 0.01,
            "armor_value": 0.01,
            "entrenchment": 4,
            "reliability": 2,
            "hardness": 3,
        },
        "mult_weights": {     # multiply_stats
            "breakthrough": 2,
            "defense": 1,
            "soft_attack": 4,
            "hard_attack": 6,
            "air_attack": 4,
            "ap_attack": 1,
            "armor_value": 2,
        },
    },

    # ---- air --------------------------------------------------------------
    "multirole": {
        "base": 50, "round": 2,
        "weights": {
            "air_attack": 0.3,
            "air_defence": 0.5,
            "air_agility": 0.2,
            "air_ground_attack": 2.0,
            "maximum_speed": 0.007,
        },
    },
    "drone": {
        "base": 1, "round": 2,
        "weights": {
            "air_attack": 0.1,
            "air_defence": 0.05,
            "air_agility": 0.1,
            "air_ground_attack": 2.0,
            "maximum_speed": 0.007,
        },
    },
    "helicopter": {
        "base": 30, "round": 2,
        "weights": {
            "air_attack": 0.05,
            "air_defence": 0.05,
            "air_agility": 0.1,
            "air_ground_attack": 2.0,
            "maximum_speed": 0.007,
        },
    },
    "plane_cas": {
        "base": 50, "round": 2,
        "weights": {
            "air_attack": 0.25,
            "air_defence": 0.3,
            "air_agility": 0.15,
            "air_ground_attack": 2.0,
            "maximum_speed": 0.02,
        },
    },
    "missile": {              # ballistic, SEAD and cruise missiles
        "base": 0, "round": 2,
        "weights": {
            "air_attack": 0.1,
            "air_agility": 0.15,
            "maximum_speed": 0.0001,
            "air_range": 0.0001,
            "air_bombing": 0.02,
        },
    },
    "aa_missile": {
        "base": 0, "round": 2,
        "weights": {
            "air_attack": 10,
            "air_agility": 0.01,
            "maximum_speed": 0.001,
            "air_range": 0.001,
            "air_bombing": 0.01,
        },
    },
}

# ---------------------------------------------------------------------------
# WHICH PROFILE APPLIES TO WHAT
#   Rules are checked top to bottom, first match wins.
#   Match keys (all optional, shell-style wildcards, all given keys must match):
#     file       - file name               e.g. "ES_tank_*_chassis.txt"
#     archetype  - equipment archetype     e.g. "fighter_equipment"
#     type       - archetype 'type'        e.g. "armor"
#     category   - module category         e.g. "*engine*"
#     name       - equipment / module name
#   Result keys: "ic" (IC profile name or None), "supply" (supply profile or None).
#   None = leave that field untouched.
#   Optional: "ic_multiplier" / "supply_multiplier" - scale the calculated value
#   (1.5 = +50%).
#
#   RU: ПРАВИЛА - какой профиль к чему применяется.
#   Проверяются сверху вниз, срабатывает первое подходящее правило.
#   Условия (все необязательные, маски с *, должны совпасть все указанные):
#     file       - имя файла                 напр. "ES_tank_*_chassis.txt"
#     archetype  - архетип снаряжения        напр. "fighter_equipment"
#     type       - type архетипа             напр. "armor"
#     category   - категория модуля          напр. "*engine*"
#     name       - имя снаряжения / модуля
#   Результат: "ic" - профиль IC, "supply" - профиль снабжения,
#   None = это поле не трогать.
#   "ic_multiplier" / "supply_multiplier" - множитель результата (1.5 = +50%).
#   Новое правило для конкретных вещей ставьте ВЫШЕ общих правил.
# ---------------------------------------------------------------------------
EQUIPMENT_RULES = [
    # infantry
    {"archetype": ["infantry_equipment", "body_armor_equipment", "uniform_equipment"],
     "ic": "inf_gear", "supply": "infantry"},
    {"archetype": ["mortar_equipment", "atgm_equipment", "aa_equipment", "grenade_launcher_equipment"],
     "ic": "inf_weapons", "supply": "infantry"},

    # towed artillery: priced like vehicle modules ("add_stats" weights), +50% IC
    {"archetype": ["artillery_equipment"], "ic": "module", "ic_multiplier": 1.5, "supply": "vehicle"},

    # air
    {"archetype": ["fighter_equipment"], "ic": "multirole", "supply": None},
    {"archetype": ["cas_equipment"], "ic": "plane_cas", "supply": None},
    {"archetype": ["hel_strike_equipment"], "ic": "helicopter", "supply": None},
    {"archetype": ["uav_strike_equipment", "uav_recon_equipment"], "ic": "drone", "supply": None},
    {"archetype": ["sam_missile_equipment"], "ic": "aa_missile", "supply": None},
    # missiles - one rule per group, so each has its own IC multiplier
    # RU: ракеты - отдельное правило на каждую группу, у каждой свой множитель IC
    {"archetype": ["ballistic_missile_equipment"],      "ic": "missile", "ic_multiplier": 1.25, "supply": None},
    {"archetype": ["*_guided_missile_equipment"],       "ic": "missile", "ic_multiplier": 1, "supply": None},
    {"archetype": ["*_anti_radar_missile_equipment"],   "ic": "missile", "ic_multiplier": 1, "supply": None},
    {"archetype": ["*_guided_uav_equipment"],           "ic": "missile", "ic_multiplier": 1, "supply": None},
    {"archetype": ["*_drone_missile_equipment"],        "ic": "missile", "ic_multiplier": 1, "supply": None},

    # vehicle hulls (every armor archetype; modules are priced separately)
    {"type": ["armor"], "ic": "hull", "supply": None},
]

MODULE_RULES = [
    {"category": ["*engine*"], "ic": "engine", "supply": None},
    # artillery / MLRS guns: +50% IC
    {"file": ["arty_guns_modules_ES.txt"], "ic": "module", "ic_multiplier": 1.5, "supply": "vehicle"},
    # missile guidance / bodies / warheads - not covered by the notes
    {"file": ["missile_modules_ES.txt", "rocket_warheads_ES.txt"], "ic": None, "supply": None},
    {"category": ["*"], "ic": "module", "supply": "vehicle"},
]

# Stats whose NEGATIVE values never reduce build_cost_ic (treated as 0).
# Positive values still add cost as usual.
# RU: статы, отрицательные значения которых НЕ уменьшают стоимость (считаются 0).
#     Положительные значения увеличивают стоимость как обычно.
IC_IGNORE_NEGATIVE = ["reliability"]

# Names (wildcards ok) that are never touched - hand-balanced items.
# RU: имена (можно с *), которые калькулятор никогда не меняет - ручной баланс.
EXCLUDE = [
    # "sov_tank_ad_*",
]

# Skip archetypes themselves (is_archetype = yes)?
# RU: не пересчитывать сами архетипы (is_archetype = yes).
SKIP_ARCHETYPES = True

# A variant inherits stats it does not define from its archetype (game behaviour).
# RU: вариант берёт недостающие статы у архетипа (как в игре).
INHERIT_FROM_ARCHETYPE = True

# RU: если у вещи нет ни одного стата из профиля (и base = 0), текущее значение
#     остаётся (напр. модули активной защиты: снабжение есть, атаки нет).
# If an item has none of the profile's stats (and base = 0) its current value is kept,
# e.g. active-defence modules with supply but no attack.
KEEP_IF_NO_STATS = True
