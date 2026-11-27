# Очередь фокусов ES


## Как это работает
- В статический модификатор `gain_focus` (common/modifiers/00_static_modifiers.txt) добавлен `es_fq_active_marker = 1`. Игра применяет `gain_focus`, пока изучается фокус, поэтому триггер `es_fq_idle` может определить, что сейчас ни один фокус не изучается.
- Раз в день `on_daily` вызывает `es_fq_daily_update` для каждой страны под управлением игрока. Если фокус не изучается, `es_fq_tick` проходит по очереди сверху вниз:
  - убирает фокусы, которые уже выполнены, исключены взаимоисключающим фокусом или больше не входят в дерево страны;
  - пропускает фокусы с невыполненными требованиями: они становятся красными и остаются в очереди;
  - запускает первый доступный фокус через `load_oob = es_focus_queue/<id>`. Файл `history/units/es_focus_queue/<id>.txt` содержит только `focus = { current = <ФОКУС> }`.
- «Автоматические» фокусы никогда не попадают в очередь. Это фокусы, у которых в `available` используется `*_auto_focus_only_tt`: экономика Набиуллиной, фокусы УКР с таймером, беженцы НАТО, марш ЧВК. Не попадают в очередь и фокусы, у которых в `available` всегда стоит `always = no`. Цепочки событий таких фокусов продолжают работать параллельно с очередью.

## Файлы
Написаны вручную:
- common/scripted_effects/es_focus_queue_effects.txt
- common/scripted_triggers/es_focus_queue_triggers.txt
- common/scripted_guis/es_focus_queue_gui.txt
- common/scripted_localisation/es_focus_queue_static_loc.txt
- common/on_actions/es_focus_queue_on_actions.txt
- common/modifier_definitions/es_focus_queue_modifier_definitions.txt
- common/synchronized_dynamic_tokens/es_focus_queue_tokens.txt
- common/modifiers/00_static_modifiers.txt (одна строка в `gain_focus`)
- interface/es_focus_queue.gui и interface/es_focus_queue.gfx
- gfx/interface/focus_queue/es_focus_queue_buttons.png. 4 кадра по 30x30:
  1. «+»
  2. в очереди
  3. запущен очередью
  4. ждёт требований
- localisation/*/ES_focus_queue_l_*.yml

Создаются `generate.py`. Никогда не редактируйте их вручную:
- common/scripted_triggers/es_focus_queue_generated_triggers.txt
- common/scripted_effects/es_focus_queue_generated_effects.txt
- common/scripted_guis/es_focus_queue_tree_generated.txt
- interface/es_focus_queue_tree_generated.gui
- common/scripted_localisation/es_focus_queue_generated_loc.txt
- history/units/es_focus_queue/*.txt
- tools/focus_queue/report.txt

## После любого изменения дерева фокусов
```
python tools/focus_queue/generate.py
```
Затем проверьте `report.txt`, особенно список «Kept but REVIEW» и раздел «Warnings».

После каждого `mark_focus_tree_layout_dirty = yes` желательно ставить `add_to_variable = { es_fq_ui_revision = 1 }`. Отчёт покажет вызовы, где этой строки нет. Пока `TREE_GUI_DIRTY = False` (по умолчанию), кнопки на дереве и так обновляются каждый тик. Строка нужна, только если включить эту настройку.

`focus_ids.json` хранит постоянные номера фокусов, чтобы очереди в сохранениях не ломались после обновлений. Коммитьте этот файл и никогда не меняйте номера в нём.

## Добавление новых фокусов, веток и деревьев
Вручную ничего регистрировать не нужно. Пишите фокусы как обычно в `common/national_focus/` и запускайте генератор.
- **Новые фокусы или новая ветка:** каждый новый фокус получает следующий свободный номер. Старые номера не меняются, поэтому очереди в сохранениях остаются рабочими.
- **Новое дерево фокусов:** подхватывается автоматически, вместе с записью в `es_fq_supported`, кнопками и общими (shared) фокусами.
- **Ветки, скрытые через `allow_branch`:** кнопки подчиняются тому же условию. Если ветку открывает событие, поставьте `add_to_variable = { es_fq_ui_revision = 1 }` после `mark_focus_tree_layout_dirty = yes`. Отчёт отметит пропущенные места.
- **Смена этапов дерева:** собственное `allow_branch` начинает новое условие видимости. К нему не добавляются условия уже скрытых предыдущих этапов. Фокусы без собственного `allow_branch` наследуют видимость родительских веток.
- **Фокусы, которые выполняет скрипт («автоматические»):** дайте `available` блок `custom_override_tooltip` с ключом `*_auto_focus_only_tt` и `always = no`, как у фокусов Набиуллиной, УКР, НАТО и ЧВК. Тогда они не попадут в очередь. Фокус с простым `always = no` на верхнем уровне `available` тоже исключается.
- **Удалённые или переименованные фокусы:** старый номер остаётся зарезервированным. Очереди в сохранениях убирают такой фокус автоматически.
- **Условные блоки `offset`:** поддерживаются, для каждого варианта расположения создаётся своя кнопка. Максимум 4 условных смещения на цепочку фокусов.

## Обновление интерфейса
- У кнопок на дереве нет `dirty`. Игра пересчитывает их каждый тик, пока открыт экран фокусов, поэтому они правильные с первого часа игры. Ставьте `TREE_GUI_DIRTY = True` в `generate.py`, только если экран фокусов начнёт тормозить. Тогда кнопки будут обновляться раз в день, при нажатиях в очереди и при `mark_focus_tree_layout_dirty`.
- Панель очереди использует `dirty = es_fq_ui_revision`. Открытие панели всегда меняет эту переменную, поэтому она сразу показывает актуальное состояние.

## Калибровка
Если кнопки на дереве смещены относительно фокусов, поправьте `TREE_ORIGIN_X/Y`, `FOCUS_STEP_X/Y`, `TEXT_OFFSET_*` и `TEXT_FONT` в начале `generate.py` и перезапустите его. Если кнопка открытия очереди что-то перекрывает, её положение задаётся в `interface/es_focus_queue.gui` (`es_fq_open_window`).
