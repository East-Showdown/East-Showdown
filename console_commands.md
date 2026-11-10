start_smo - начинает СВО
add_ammunition <число> - добавляет готовые к применению боеприпасы

## Мосты и дамбы (тесты) / Bridges and dams (testing)
<обязательный>, [необязательный] / <required>, [optional].
Позиция <pos> = номер объекта 0-28 (как в рейдах и решениях). Вывод — в консоль и game.log.
<pos> = object position 0-28 (same as raids/decisions). Output goes to the console and game.log.

bridge_list - список всех мостов/дамб: HP, порог блокировки, заблокирован, разрушен, эрозия, владелец / list all objects
bridge_info <pos> - информация об одном объекте (позиция обязательна, напр. bridge_info 16) / one object (position required, e.g. bridge_info 16)
bridge_hp <pos> <hp> - задать HP и сразу применить блокировку/разрушение / set HP, apply blocking and destruction at once
bridge_damage <pos> <урон> - отнять HP как рейд (без немедленного обновления) / subtract HP like a raid, no immediate update
bridge_week [n] - прогнать еженедельное обновление n раз (по умолчанию 1) / run the weekly update n times (default 1)
bridge_reset <pos> - полное HP, снять отметку «разрушен», применить блокировку / full HP, clear destroyed mark, reapply blocking
bridge_unlock - открыть решения о подрыве мостов для игрока / unlock the blow-up decisions for the player

## Цели рейдов (тесты) / Raid targets (testing)
raid_state_info <state> - неповреждённые / все уровни каждого здания-цели рейдов в области / undamaged / total levels of every raid-target building in a state
raid_wreck <state> - полностью повредить все здания-цели рейдов в области / fully damage every raid-target building in a state

## Подстанции (тесты) / Substations (testing)
Вывод — в консоль и game.log, строки начинаются с SUBSTATION TEST. / Output goes to the console and game.log, lines start with SUBSTATION TEST.

round_test - проверить, как round_temp_variable округляет (формулы подстанций ждут округление к ближайшему) / check how round_temp_variable rounds (the substation formulas expect nearest)
substation_selftest [state] - прогнать расчёт подстанций на 10 значениях спроса и вывести PASS/FAIL, ничего не строит; по умолчанию — столица (нужны свободные слоты подстанций) / run the substation calculation for 10 demands and print PASS/FAIL, builds nothing; uses your capital by default (needs free substation slots)
substation_add <state> [amount] - настоящий вызов ESAPI_add_state_building: поставить в очередь [amount] военных заводов (по умолчанию 1) с учётом энергии; 1 завод = 0 больших + 1 малая подстанция / real ESAPI_add_state_building call: queue [amount] arms factories (default 1) with the energy check on; 1 factory = 0 big + 1 small substation

## Режим карты энергетики (тесты) / Energy map mode (testing)
Режим карты показывает energy_blackout_status области: 0 зелёный, 1 красный (локальный блэкаут), 2 жёлтый (глобальный). Еженедельный расчёт энергии перезаписывает значение. / The map mode shows a state's energy_blackout_status: 0 green, 1 red (local blackout), 2 yellow (global). The weekly energy calculation overwrites it.

blackout_set <state> <0|1|2> - задать статус блэкаута; после одного дня карта должна сменить цвет / set the blackout status; after one day the map should change color
blackout_info <state> - статус, обеспеченность энергией, потребление и пропускная способность подстанций / status, supply factor, consumption and substation capacity

## Удары по полевым складам (тесты) / Field depot strikes (testing)
Вывод — в консоль и game.log, строки начинаются с DEPOT TEST. / Output goes to the console and game.log, lines start with DEPOT TEST.

depot_mod_test <state> - повесить на область штраф 3 ступени (-15%) сразу для RUS, DPR, LPR и WGN на 30 дней и вывести, какие из них держатся / put the level 3 penalty (-15%) on the state for RUS, DPR, LPR and WGN at once for 30 days and print which ones stick
depot_mod_clear <state> - снять эти тестовые модификаторы / remove those test modifiers
depot_front_info - сколько областей помечено как линия фронта для ударов по полевым складам / how many states are flagged as front line for field depot strikes
depot_front_mark - пометить линию фронта сейчас и вывести число / mark the front line now and print the count
