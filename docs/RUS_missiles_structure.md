# Структура ракетных технологий РФ

Дата последнего обновления: 2026-01-22

## Файлы

- **Технологии:** `common/technologies/missiles_rus.txt`
- **Оборудование (управляемые ракеты):** `common/units/equipment/ES_guided_missiles.txt`
- **Оборудование (баллистические):** `common/units/equipment/ES_ballistic_missiles.txt`
- **Локализация (RU):** `localisation/russian/ES_equip_air_l_russian.yml`

---

## Древо технологий (missiles_folder)

### Координатная сетка

```
Y=2:  Х-22 ────────► Х-32
      (x=-6)         (x=-2)

Y=4:  Х-55 ────► Х-55СМ ────► Х-555 ────► Х-101 ────► Х-69
      (x=-6)    (x=-2)        (x=2)       (x=6)       (x=10)

Y=6:  Гранит ────► Калибр ────► Циркон
      (x=-6)       (x=-2)       (x=2)

Y=8:  Р-17 ────► Точка-У ────► Искандер-М ────► Искандер-1000
      (x=-6)     (x=-2)        (x=2)            (x=6)
                                    │
                                    ▼
Y=10:                          Кинжал
                               (x=2)

Y=12: Герань-2 ────► Герань-2М ────► Герань-3
      (x=-6)         (x=-2)          (x=2)

Y=14: 5B21 ────► 5В55Р ────► 48Н6Е3 ────► 40Н6Е ────► Прометей
      (x=-6)     (x=-2)      (x=2)        (x=6)       (x=10)
```

---

## Детали технологий

### Ветка 1: Х-серия лёгкая (y=2)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `missile_rus_kh22` | Х-22 | `rus_light_guided_missile_kh22` | x=-6, y=2 |
| `missile_rus_kh32` | Х-32 | `rus_light_guided_missile_kh32` | x=-2, y=2 |

### Ветка 2: Х-серия средняя (y=4)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `missile_rus_kh55` | Х-55 | `rus_medium_guided_missile_kh55` | x=-6, y=4 |
| `missile_rus_kh55cm` | Х-55СМ | `rus_medium_guided_missile_kh55cm` | x=-2, y=4 |
| `missile_rus_kh555` | Х-555 | `rus_medium_guided_missile_kh555` | x=2, y=4 |
| `missile_rus_kh101` | Х-101 | `rus_medium_guided_missile_kh101` | x=6, y=4 |
| `missile_rus_kh69` | Х-69 | `rus_aircraft_guided_missile_equipment_kh69` | x=10, y=4 |

### Ветка 3: Противокорабельные/гиперзвуковые (y=6)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `missile_rus_granit` | П-700 «Гранит» | `rus_medium_guided_missile_granit` | x=-6, y=6 |
| `missile_rus_kalibr` | 3М54 «Калибр» | `rus_medium_guided_missile_kalibr` | x=-2, y=6 |
| `missile_rus_3M22` | 3М22 Циркон | `rus_medium_guided_missile_3m22` | x=2, y=6 |

### Ветка 4: Баллистические (y=8, y=10)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `missile_rus_R17` | Р-17 | `rus_ballistic_missile_R17` | x=-6, y=8 |
| `missile_rus_9K79` | Точка-У | `rus_ballistic_missile_9K79` | x=-2, y=8 |
| `missile_rus_9M723` | Искандер-М | `rus_ballistic_missile_9M723` | x=2, y=8 |
| `missile_rus_iskander1000` | Искандер-1000 | `rus_ballistic_missile_iskander1000` | x=6, y=8 |
| `missile_rus_kh47` | Х-47М2 Кинжал | `rus_medium_guided_missile_kh47m2` | x=2, y=10 |

**Примечание:** Кинжал ответвляется ВНИЗ от Искандер-М, Искандер-1000 идёт ВПРАВО.

### Ветка 5: БПЛА (y=12)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `missile_rus_shahed136` | Герань-2 | `rus_guided_uav_geranium` | x=-6, y=12 |
| `missile_rus_shahed136M` | Герань-2М | `rus_guided_uav_geranium_m` | x=-2, y=12 |
| `missile_rus_geranium3` | Герань-3 | `rus_guided_uav_geranium3` | x=2, y=12 |

**Примечание:** `missile_rus_shahed136I` (Герань-2И) закомментирована.

### Ветка 6: ЗРК (y=14)
| Tech ID | Название | Оборудование | Позиция |
|---------|----------|--------------|---------|
| `rus_sam_5B21` | 5B21 | `rus_sam_5B21_equipment` | x=-6, y=14 |
| `rus_sam_5B55P` | 5В55Р | `rus_sam_5B55P_equipment` | x=-2, y=14 |
| `rus_sam_48Н6Е3` | 48Н6Е3 | `rus_sam_48H6E3_equipment` | x=2, y=14 |
| `rus_sam_40Н6Е` | 40Н6Е | `rus_sam_40H6E_equipment` | x=6, y=14 |
| `rus_sam_prometey` | Прометей | `rus_sam_prometey_equipment` | x=10, y=14 |

**Условия:**
- `rus_sam_5B21` требует `is_SOV_origin = yes`
- `rus_sam_48Н6Е3` требует `is_RUS_origin = yes`

---

## Архетипы оборудования

- **Лёгкие управляемые:** `rus_light_guided_missile_equipment` (в `00_ES_guided_missile_archetypes.txt`)
- **Средние управляемые:** `rus_medium_guided_missile_equipment`
- **Тяжёлые управляемые:** `rus_heavy_guided_missile_equipment`
- **БПЛА:** `rus_guided_uav_equipment`
- **Баллистические:** `ballistic_missile_equipment` (в `00_ES_ballistic_missile_archetypes.txt`)

---

## Закомментированные/неиспользуемые

- `missile_rus_kh101m` (Х-101М) - закомментирована в missiles_rus.txt
- `missile_rus_shahed136I` (Герань-2И) - закомментирована
- `rus_guided_uav_geranium_i` - оборудование осталось, но технология отключена

---

## Другие ракеты РФ (не в основном древе)

- `rus_ballistic_missile_oreshnik` - «Орешник» (есть в ES_ballistic_missiles.txt, нет технологии)
