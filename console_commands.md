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
