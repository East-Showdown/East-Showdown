# Система боеприпасов

Справочник для авторов сабмодов, событий и фокусов. Hearts of Iron IV 1.19.3.

[English version](README.en.md)

## 1. Как это работает

Все расчёты идут раз в день для каждой страны (`on_daily`, эффект `ammunition_on_daily`).
Количества хранятся в тысячах единиц боеприпасов, потоки считаются за день.

### Уровень выделения

Уровень `ammunition_level` задаёт, какую долю нормы расхода войска получают. 1 = 100 %.

- Диапазон: от `level_min` до предела `cap`.
- `cap = clamp(level_max_base + ammunition_level_cap, level_min, level_max_abs)`.
  По умолчанию предел 1.25, абсолютный максимум 2.
- Игрок меняет уровень в окне шагами 1 / 10 / 100 % (клик, Ctrl, Shift; правая кнопка уменьшает).

### Расход

Расходуют боеприпасы только субюниты из таблицы. Бонусы и штрафы действуют на их снаряжение.

| Архетип снаряжения | Батальон | Рота поддержки |
| --- | --- | --- |
| `artillery_equipment` | `towed_art` | `artillery` |
| `sp_artillery_chassis` | `sp_art` | `support_spa` |
| `sp_heavy_artillery_chassis` | `sp_heavy_art` | `support_heavy_spa` |
| `sp_mlrs_chassis` | `MRLS` | `support_mlrs` |
| `sp_tos_chassis` | `TOS` | `support_tos` |
| `mortar_equipment` | | `mortar` |

Расход считается по генералам. Учитывается генерал, который назначен на армию, ведёт хотя бы одну дивизию
и не командует группой армий (фельдмаршал пропускается, его армии считаются через своих генералов).
Страна ИИ без войны не расходует ничего.

Расход генерала при уровне 1:

```
база = Σ n_X · k_X
расход = база · (factor_off · div_off + factor_def · div_def) / div_all
```

- `n_X` - число субюнитов `X` у генерала (`num_battalions_with_type@X`), роты поддержки тоже.
- `k_X` - расход одного субюнита за день, константа `k_<субюнит>`.
- `div_off`, `div_def` - дивизии генерала в наступательных и оборонительных боях; `div_all` - все его дивизии.
- `factor_off`, `factor_def` - множители атаки и обороны. Каждый умножается на множитель игрового правила
  и на `(1 + модификатор расхода стороны)`, не меньше 0.

Субюниты считаются распределёнными по дивизиям генерала поровну. Дивизии вне боя не расходуют.

Пример. У генерала 10 дивизий, в них 20 батальонов `towed_art` и 10 рот `artillery`.
База = 20 · 0.08 + 10 · 0.04 = 2.0 тыс. В атаке 4 дивизии, в обороне 3.
Расход = 2.0 · (2 · 4 + 1 · 3) / 10 = 2.2 тыс. в день при уровне 1, 2.75 тыс. при уровне 1.25.

Потребность дня: `need = level · Σ расходов генералов`.

### Покрытие и обеспеченность

- Доступно = склад до списания + приход дня.
- Списано = `min(need, доступно)`.
- Покрытие `cover = списано / need`. Без расхода `cover = 1`, если доступно больше 0, иначе 0.
- Обеспеченность `s = level · cover`. От неё зависят все эффекты.

### Эффекты: духи-ступени

`s` округляется до шага 5 %. Стране выдаётся один национальный дух `ammunition_<процент>`
(`ammunition_0` … `ammunition_200`). На ступени 100 % духа нет. Дух меняется, только когда меняется ступень.

Дух даёт `equipment_bonus` архетипам из таблицы выше:

| Стат | Кривая | s = 0 | s = 1 | s = 1.25 | s = 2 |
| --- | --- | --- | --- | --- | --- |
| `soft_attack`, `hard_attack` | `attack` | -70 % | 0 | +15 % | +30 % |
| `breakthrough` | `breakthrough` | -65 % | 0 | +20 % | +35 % |
| `defense` | `defense` | -15 % | 0 | +15 % | +25 % |

Между точками значение меняется линейно. Значения по умолчанию заданы в `tools/ammo/ammunition_curves.txt`.

Бонус действует на стат снаряжения. Поэтому вклад в дивизию пропорционален доле расходующих субюнитов.

Агрессивность ИИ (`ai_focus_aggressive_factor`) задаёт динамический модификатор `ammunition_effects` по кривой
`ai_aggressive`: -0.8 / 0.2 / 0.3 / 0.4 при `s` = 0 / 1 / 1.25 / 2.

### Автоматизация

Страна ИИ всегда на автоматизации. Игрок включает и выключает её кнопкой в окне.
Уровень автоматизации считается каждый день у каждой страны и хранится в `ammunition_level_auto`.
В `ammunition_level` он переходит только у ИИ и при включённой автоматизации.

Правило:

1. `need_ref` - потребность при уровне 1. Если она равна 0 (боёв нет), берётся расход всех расходующих
   субюнитов страны в обороне.
2. `L(D) = (склад / D + приход дня) / need_ref` - уровень, при котором склада с приходом хватит на `D` дней.
3. Если `L(ai_days_low) < 1`, уровень = `L(ai_days_low)`, но не ниже `ai_level_min`.
   Если `L(ai_days_low) > 1`, уровень = `L(ai_days_high)`, но не ниже 1. Иначе уровень = 1.
4. Прибавляется модификатор `ammunition_level_target`.
5. Результат ограничивается диапазоном `[level_min; cap]`.

С настройками по умолчанию: склада хватает меньше чем на 120 дней - уровень снижается; больше чем на 365 дней -
уровень растёт; между ними - 100 %. Если `need_ref` равна 0, уровень автоматизации = 1 + `ammunition_level_target`.

### Склад

- `ammunition_value_k` - готовые боеприпасы. Только они идут в расход.
- `ammunition_old_value_k` - боеприпасы, требующие восстановления.
- Мощность цехов: `daily_ammunition_gain / 1000 · (1 + ammunition_plants_efficiency_factor)` тыс. в день.
- Мощность делится ползунком на производство (доля `ammunition_produce_factor`, на старте `produce_share_start`)
  и восстановление (остаток до 1).
- Производство: мощность · доля · `(1 + ammunition_produce_efficiency_factor)`.
- Восстановление: мощность · доля · `(recovery_efficiency_base + ammunition_recovery_efficiency_factor)`.
  Оно переводит боеприпасы из `ammunition_old_value_k` в готовые. Если восстанавливать больше нечего,
  лишняя доля мощности уходит в производство.
- Вместимость = склады (`ammunition_capacity_k`) + полевые склады. Полевые склады = расход всех расходующих
  субюнитов страны при множителе 1 за `field_storage_days` дней.
- Излишек сверх вместимости сначала списывается из `ammunition_old_value_k`, затем из готовых.

Начальный склад (тыс.): у всех стран 5000 готовых и 3200 на восстановление; `NTO` 5900 и 400; `UKR` 2400 и 2520;
`RUS` 6800 и 3600 (`common/on_actions/ammo_on_actions.txt`).

## 2. Настройка

### `common/script_constants/ammo_constants.txt`

Блок `ammunition`. В скрипте константа читается как `constant:ammunition.<имя>`.

| Константа | Смысл | Единица | По умолчанию |
| --- | --- | --- | --- |
| `k_towed_art`, `k_sp_art`, `k_sp_heavy_art`, `k_MRLS` | расход батальона | тыс. в день | 0.08 |
| `k_TOS` | расход батальона ТОС | тыс. в день | 0.1 |
| `k_artillery`, `k_support_spa`, `k_support_heavy_spa`, `k_support_mlrs` | расход роты поддержки | тыс. в день | 0.04 |
| `k_support_tos` | расход роты ТОС | тыс. в день | 0.05 |
| `k_mortar` | расход роты миномётов | тыс. в день | 0.01 |
| `factor_off` | множитель расхода дивизий в атаке | множитель | 2 |
| `factor_def` | множитель расхода дивизий в обороне | множитель | 1 |
| `level_min` | нижняя граница уровня | доля | 0 |
| `level_max_base` | предел уровня без модификаторов | доля | 1.25 |
| `level_max_abs` | абсолютный максимум уровня и конец кривых | доля | 2 |
| `ai_days_low` | ниже этого запаса автоматизация снижает уровень | дни | 120 |
| `ai_days_high` | выше этого запаса автоматизация повышает уровень | дни | 365 |
| `ai_level_min` | нижняя граница уровня автоматизации до `ammunition_level_target` | доля | 0.2 |
| `field_storage_days` | вместимость полевых складов | дни расхода | 7 |
| `recovery_efficiency_base` | сколько единиц восстанавливает единица мощности | множитель | 2 |
| `produce_share_start` | начальная доля мощности на производство | доля | 0.7 |

`produce_share_start` действует только при инициализации страны.
После смены `level_max_abs` запустите генератор: кривые должны заканчиваться на новом значении.

### `tools/ammo/ammunition_curves.txt`

Кривая эффекта на строку: `имя = { s = значение s = значение … }`.

```
attack = { 0 = -0.7  1 = 0  1.25 = 0.15  2 = 0.3 }
```

Правила:

- Нужны все четыре кривые: `attack`, `breakthrough`, `defense`, `ai_aggressive`.
- Не меньше двух точек. Первая точка `0`, последняя `level_max_abs`. `s` строго растёт.
- Число точек любое. Между точками значение линейно.
- Значения - доли: -0.7 = -70 %. Для `ai_aggressive` - значение `ai_focus_aggressive_factor`.
- `#` начинает комментарий.

### Генератор

```
python3 tools/ammo/generate_ammunition_effects.py
```

Читает константы и кривые. При нарушении правил кривых выходит с ошибкой. Пишет:

| Файл | Содержимое |
| --- | --- |
| `common/ideas/ammo_ideas.txt` | духи-ступени `ammunition_<процент>` с `equipment_bonus` |
| `common/scripted_effects/ammo_idea_effects.txt` | `ammunition_update_idea`: выбор духа по `s` |
| `common/scripted_effects/ammo_curve_effects.txt` | `ammunition_calculate_effects`: значения кривых для окна и ИИ |
| `localisation/russian/ammo_ideas_l_russian.yml`, `localisation/english/ammo_ideas_l_english.yml` | названия и описания духов |

Эти файлы не правьте вручную. Меняйте `tools/ammo/ammunition_curves.txt`, константы или генератор и запускайте его заново.

### Игровое правило

`es_ammunition_consumption_factor` умножает `factor_off` и `factor_def`. Варианты 50-300 %
(`ES_AMMUNITION_CONSUMPTION_FACTOR_RULE_50` … `_300`), по умолчанию 100 %.
Значение хранится в `global.ammunition_consumption_rule_factor`.

## 3. API для событий и фокусов

### Модификаторы

Работают в любом блоке модификаторов страны: дух, динамический модификатор, советник и т. д.

| Модификатор | Действие | Единица |
| --- | --- | --- |
| `ammunition_level_cap` | сдвигает предел уровня `cap` | доля уровня: 0.25 = +25 % |
| `ammunition_level_target` | прибавляется к уровню автоматизации и ИИ; на ручной уровень не действует | доля уровня |
| `ammunition_consumption_offensive_factor` | расход в атаке · (1 + x), не меньше 0 | доля |
| `ammunition_consumption_defensive_factor` | расход в обороне · (1 + x), не меньше 0 | доля |
| `daily_ammunition_gain` | номинальная мощность цехов | единицы в день (не тысячи) |
| `ammunition_plants_efficiency_factor` | мощность цехов · (1 + x), не меньше 0 | доля |
| `ammunition_produce_efficiency_factor` | производство · (1 + x), не меньше 0 | доля |
| `ammunition_recovery_efficiency_factor` | прибавляется к `recovery_efficiency_base` | единицы на единицу мощности |
| `ammunition_capacity_k` | вместимость складов | тыс. |
| `ammunition_plants`, `ammunition_silos` | счётчики зданий для окна | штуки |

```
my_idea = {
	modifier = {
		ammunition_level_cap = 0.1
		ammunition_consumption_offensive_factor = -0.15
		ammunition_plants_efficiency_factor = 0.2
	}
}
```

### Эффекты

Оба эффекта берут вход из временной переменной `temp_delta` (доля уровня).

`ammunition_raise_level` - для событий. При ручном управлении у игрока: обновляет динамические модификаторы,
прибавляет `temp_delta` к уровню и ограничивает его пределом. Поэтому предел из модификатора, добавленного
тем же событием, действует сразу. При автоматизации и у ИИ ничего не делает: там уровень сдвигает
`ammunition_level_target`. Событие, меняющее уровень, должно задавать и модификатор цели.

`ammunition_change_level` - прибавляет `temp_delta` и ограничивает уровень. Проверок нет, его вызывают кнопки окна.
При автоматизации и у ИИ следующий день перезапишет уровень.

### Динамический модификатор `ammunition_war_mobilisation`

Пример: `ammunition_level_target = 0.25`, `ammunition_level_cap = 0.25`.

```
option = {
	name = my_event.1.a
	add_dynamic_modifier = { modifier = ammunition_war_mobilisation days = 60 }
	set_temp_variable = { temp_delta = 0.25 }
	ammunition_raise_level = yes
}
```

Модификатор поднимает цель автоматизации и предел. `ammunition_raise_level` поднимает ручной уровень.
Так событие действует при любом режиме.

### Флаги

| Флаг | Смысл |
| --- | --- |
| `ammunition_supply_factor_ai_disable` | флаг страны: стоит - автоматизация выключена, уровень ручной. У ИИ не действует. |
| `RUS_genstab_ammunition_supply_factor_limitation` | флаг страны с `original_tag = RUS`: включает динамический модификатор `ammunition_RUS_genstab_limitation` (`ammunition_level_cap = -0.75`, предел 0.5 при настройках по умолчанию). |

```
set_country_flag = ammunition_supply_factor_ai_disable   # ручное управление
clr_country_flag = ammunition_supply_factor_ai_disable   # автоматизация
```

### Переменные страны

Значения обновляются раз в день; до первого дня после старта часть переменных не задана.
Суффикс `_k` - тысячи единиц. Доля: 1 = 100 %.

| Переменная | Смысл | Единица |
| --- | --- | --- |
| `ammunition_value_k` | готовые боеприпасы на складе | тыс. |
| `ammunition_old_value_k` | боеприпасы на восстановление | тыс. |
| `sum_ammunition_value_k` | всего на складе | тыс. |
| `ammunition_max_storage_capacity_k` | вместимость всего | тыс. |
| `ammunition_silos_capacity_k` | вместимость складов-зданий | тыс. |
| `ammunition_field_storage_capacity_k` | вместимость полевых складов | тыс. |
| `ammunition_level` | уровень выделения | доля |
| `ammunition_level_auto` | уровень автоматизации | доля |
| `ammunition_level_max` | предел `cap` | доля |
| `ammunition_supply` | обеспеченность `s` | доля |
| `ammunition_cover` | покрытие `cover` | доля |
| `ammunition_need_k` | потребность дня | тыс. в день |
| `ammunition_need_level_1_k` | потребность при уровне 1 | тыс. в день |
| `ammunition_spent_k` | списано за день | тыс. в день |
| `ammunition_generation_value_k` | приход дня (производство + восстановление) | тыс. в день |
| `ammunition_delta_value_k` | приход минус списание | тыс. в день |
| `ammunition_days_at_level_1` | на сколько дней хватит готовых боеприпасов при `need_ref` с учётом прихода, не больше 1000 | дни |
| `ammunition_divisions` | дивизии учтённых генералов | штуки |
| `ammunition_divisions_off`, `ammunition_divisions_def` | из них в атаке, в обороне | штуки |

```
available = {
	check_variable = { ammunition_supply < 0.8 }
	check_variable = { ammunition_value_k > 1000 }
}
```

## 4. Новый расходующий субюнит или архетип

1. Добавьте константу `k_<субюнит>` в `common/script_constants/ammo_constants.txt`.
   Имя субюнита - как в `common/units`.
2. Добавьте строку в эффект `ammunition_calculate_base_consumption`
   (`common/scripted_effects/ammo_scripted_effects.txt`):

   ```
   add = { value = num_battalions_with_type@my_sub_unit multiply = constant:ammunition.k_my_sub_unit }
   ```

3. Если субюнит использует снаряжение нового архетипа, добавьте архетип в список `ARCHETYPES`
   в `tools/ammo/generate_ammunition_effects.py`. Описание духов в локализации задано там же.
4. Запустите `python3 tools/ammo/generate_ammunition_effects.py`.

Ключ бонуса - архетип: бонус получают все модели и варианты архетипа.

## 5. Здания

| Здание | Стоимость | Лимит в области | Модификаторы страны |
| --- | --- | --- | --- |
| `ammunition_plant` | 7200 | 3, общие слоты | `daily_ammunition_gain = 500` (0.5 тыс. в день), `ammunition_plants = 1` |
| `ammunition_silo` | 4200 | 5, общие слоты | `ammunition_capacity_k = 500` (500 тыс.), `ammunition_silos = 1` |

Скорость строительства обоих зависит от инфраструктуры.

## 6. Ограничения

- Дивизии без генерала не учитываются: ни в расходе, ни в числе дивизий.
- Субюниты генерала считаются распределёнными по его дивизиям поровну.
- Изменение духа доходит до дивизий при ежедневном пересчёте их статов, до 24 часов.
- Бонусы снаряжения складываются с другими бонусами того же стата, не перемножаются:
  `стат = база · (1 + Σ бонусов)`.
- Страны, появившиеся после старта игры, начинают с пустым складом.
