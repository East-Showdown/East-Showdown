# Аудит наземных 3D-моделей East Showdown

Проверены 840 записей техники и 87 типов наземных подразделений. Источники: текущий мод, установленная HOI4 и её DLC. Игровые файлы не изменялись.

Это статическая проверка ссылок, а не наблюдение в запущенной игре. Отсутствие отдельной модели шасси не означает невидимый батальон: он может использовать общую модель своего типа и страны.

Проверены sprite, parent/archetype, entity/clone, pdxmesh и наличие mesh. Варианты конструктора отдельно не перечислены: они используют соответствующее шасси. Поезда, самолёты, ракеты, БПЛА и предметы экипировки исключены. Доступность DLC в конкретной игровой сессии не проверялась.

## 1. Прямые ссылки на отсутствующие модели: 27 записей

Проверены как буквальные имена sprite, так и имена с суффиксом `_entity`. Эти ошибки относятся к записи техники; общая модель батальона всё ещё может отображаться.

| Техника | ID | Ссылка sprite | Файл |
|---|---|---|---|
| БТР на базе БМД-1 | `apc_afv_sov_bmd1_equipment` | `RUS_BMD_1` | [common/units/equipment/ES_afv_chassis_sov_bmd1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd1.txt) |
| БТР на базе БМД-2 | `apc_afv_sov_bmd2_equipment` | `RUS_BMD_1` | [common/units/equipment/ES_afv_chassis_sov_bmd2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd2.txt) |
| БТР на базе БМД-3 | `apc_afv_sov_bmd3_equipment` | `RUS_BMD_1` | [common/units/equipment/ES_afv_chassis_sov_bmd3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd3.txt) |
| БТР на базе БМД-4 | `apc_afv_rus_bmd4_equipment` | `RUS_BMD_1` | [common/units/equipment/ES_afv_chassis_sov_bmd4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd4.txt) |
| Шасси Borsuk | `ifv_pol_borsuk_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_pol_borsuk.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_pol_borsuk.txt) |
| Шасси БМП-1 | `ifv_sov_bmp1_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_sov_bmp1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp1.txt) |
| Шасси БМП-2 | `ifv_sov_bmp2_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_sov_bmp2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp2.txt) |
| Шасси БМП-3 | `ifv_sov_bmp3_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_sov_bmp3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp3.txt) |
| Шасси Курганец-25 | `ifv_rus_kurganetz25_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_sov_kurganetz25.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_kurganetz25.txt) |
| Шасси БМП-У | `ifv_ukr_bmpy_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_ukr_bmpy.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ukr_bmpy.txt) |
| Шасси Inguar-7 | `ifv_ukr_inguar7_equipment` | `RUS_BMP_1_entity` | [common/units/equipment/ES_ifv_chassis_ukr_inguar7.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ukr_inguar7.txt) |
| Шасси EMBT ADT140 | `tank_euro_EMBT_ADT140_equipment` | `tank_ger_leopard2_entity` | [common/units/equipment/ES_tank_chassis_embt.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_embt.txt) |
| Шасси Leopard 2 | `tank_ger_leopard2_equipment` | `tank_ger_leopard2_entity` | [common/units/equipment/ES_tank_chassis_ger_leopard2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ger_leopard2.txt) |
| Шасси Panther KF51 | `tank_ger_kf51_equipment` | `tank_ger_leopard2_entity` | [common/units/equipment/ES_tank_chassis_ger_leopard2_kf51.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ger_leopard2_kf51.txt) |
| Тяжелая БМП на базе Об.640 | `ifv_heavy_rus_obj640_equipment` | `UKR_T_64` | [common/units/equipment/ES_tank_chassis_sov_obj640.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_obj640.txt) |
| Тяжелая БМП на базе Т-14 | `ifv_heavy_rus_t14_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_sov_t14.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t14.txt) |
| Тяжелая БМП на базе Т-54/55 | `ifv_heavy_sov_t55_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_sov_t55.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t55.txt) |
| Тяжелая БМП на базе Т-62 | `ifv_heavy_sov_t62_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_sov_t62.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t62.txt) |
| Шасси Т-64 | `tank_sov_t64_equipment` | `t64` | [common/units/equipment/ES_tank_chassis_sov_t64.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t64.txt) |
| Тяжелая БМП на базе Т-64 | `ifv_heavy_sov_t64_equipment` | `UKR_T_64` | [common/units/equipment/ES_tank_chassis_sov_t64.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t64.txt) |
| Шасси Т-72 | `tank_sov_t72_equipment` | `t72_entity` | [common/units/equipment/ES_tank_chassis_sov_t72.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t72.txt) |
| Тяжелая БМП на базе Т-72 | `ifv_heavy_sov_t72_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_sov_t72.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t72.txt) |
| Тяжелая БМП на базе Т-80 | `ifv_heavy_sov_t80_equipment` | `UKR_T_64` | [common/units/equipment/ES_tank_chassis_sov_t80.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t80.txt) |
| БМП на базе Т-84 | `ifv_heavy_ukr_t84_equipment` | `UKR_T_64` | [common/units/equipment/ES_tank_chassis_sov_t84.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t84.txt) |
| Тяжелая БМП на базе Т-90 | `ifv_heavy_rus_t90_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_sov_t90.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t90.txt) |
| Тяжелая БМП на базе Объект 477 | `ifv_heavy_ukr_obj477_equipment` | `UKR_T_64` | [common/units/equipment/ES_tank_chassis_ukr_obj477.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ukr_obj477.txt) |
| Тяжелая БМП на базе M1 Abrams | `ifv_heavy_usa_abrams_equipment` | `RUS_BMP_1` | [common/units/equipment/ES_tank_chassis_usa_m60patton_abrams.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_usa_m60patton_abrams.txt) |

## 2. Не найдены модели типа батальона

- Рота итальянских БМП (`ifv_ita`): `ifv_ita_entity` — [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)
- Рота советских легких танков (`light_tank_sov`): `light_tank_sov_entity` — [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

## 3. Ванильная пехота и конфликтующие назначения

- В `gfx/entities/ec_flavor_pack.asset` есть `NTO_infantry_entity`, клонирующий `ROM_infantry_entity`: это ванильная румынская пехота из Death or Dishonor. В моде есть несколько определений `NTO_infantry_entity`, поэтому окончательный выбор требует проверки порядка загрузки/в игре.
- `POL_infantry_entity` в `gfx/entities/03_tanks_units.asset` клонирует отсутствующую `Stryker_entity`. Это сломанная ссылка, а не доказательство использования ванильной модели. Имя `POL_infantry_entity` также определено несколько раз.
- Общая `infantry_entity` остаётся ванильной. Она является запасным вариантом для стран без собственного подходящего определения. В России и Украине есть собственные модели пехоты; их нельзя целиком относить к ванильным.
- У Польши существует ванильная `POL_artillery_entity`. Она является кандидатом для подразделений со sprite `artillery`; общий `artillery_entity` в моде заменён на 2С1.

Подразделения, ссылающиеся на общую пехоту (наличие собственной модели по ID/стране указано в полном списке ниже):

- Рота поддержки на легких танках (`light_support_tank_sov`)
- Рота поддержки на легких танках (`light_support_tank_nto`)
- Средний ЗРК (`sp_aa`)
- Инженерный взвод (`engineer`)
- Тяжелый инженерный взвод (`engineer_heavy`)
- Полевой госпиталь (`field_hospital`)
- Взвод обеспечения (`logistics_company`)
- Ремонтный взвод (`maintenance_company`)
- Тяжелый ремонтный взвод (`heavy_maintenance_company`)
- Взвод связи (`signal_company`)
- Взвод снайперов (`sniper`)
- Отряд дроноводов (`fpv_team`)
- Взвод разведчиков на БРДМ (`recon`)
- Разведгруппа на советских БМП (`recon_ifv_sov`)
- Разведгруппа на американских БМП (`recon_ifv_usa`)
- Разведгруппа на тяжелых БМП (`recon_ifv_heavy_sov`)
- Разведгруппа на тяжелых БМП НАТО (`recon_ifv_heavy_nto`)
- Разведгруппа на БТР (`armored_recon`)
- Разведгруппа на БМД (`afv_recon`)
- Разведгруппа на ББМ (`imv_recon`)
- Разведгруппа на машинах (`imv_light_recon`)
- Военная полиция (`military_police`)
- command (`command`)
- Пехотная КШМ (`command_inf`)
- Артиллерийская КШМ (`command_spa`)
- Танковая КШМ (`command_tank`)
- lancet (`lancet`)
- Персонал штаба (`hq_support`)
- Персонал инженеров (`hq_engineer`)
- Разведывательный персонал БПЛА (`hq_drone_recon`)
- Персонал планового обслуживания (`hq_maintenance`)
- Медицинский персонал (`hq_field_hospital`)
- Персонал логистики и обслуживания (`hq_logistics`)
- Персонал сигнальщиков и разведчиков (`hq_signal`)
- Передовой авиадиспетчер (`hq_air_liaison`)
- Координация специальных операций (`hq_sso`)
- Координация ударов артиллерии (`hq_arty`)
- Координация применения танков (`hq_tank`)
- Пехотная охрана штаба на ББM (`hq_imv`)
- Рота советских БМД (`afv_sov`)
- Рота БМПТ (`bmpt`)
- Рота пехотинцев (`infantry`)
- Рота морских пехотинцев (`marine`)
- Рота горнострелков (`mountaineers`)
- Рота десантников (`paratrooper`)
- Рота ТРО (`opolchenie`)
- Рота заключённых (`prisoners`)
- Рота ЧВК Вагнер (`PMC_wagner`)
- Рота штурмовой пехоты (`assault_infantry`)
- Рота спецназа (`spetsnaz`)
- Пограничники (`border_guard`)
- Северокорейская Штурмовая пехота (`dprk_assault_infantry`)

Подразделения со sprite `artillery`:

- Артиллерийский дивизион поддержки (`artillery`)
- САУ Поддержки (`support_spa`)
- РСЗО Поддержки (`support_mlrs`)
- Тяжелая САУ Поддержки (`support_heavy_spa`)
- ТОС Поддержки (`support_tos`)
- Минометный расчет (`mortar`)
- Расчет ПТРК (`atgm`)

## 4. Без отдельной привязки техники: 783 записи

Ни sprite в цепочке parent/archetype, ни совпадающая entity техники не найдены. Это список для подключения отдельных моделей, а не список гарантированно невидимых юнитов. Производные САУ, ЗРК, БРЭМ и другие варианты перечислены вместе со своими шасси.

### ES_aa_equipments_nto

[common/units/equipment/ES_aa_equipments_nto.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_aa_equipments_nto.txt)

- ХM41 Redeye (`usa_xm41_redeye_equipment`)
- FIM-43 Redeye (Block 1) (`usa_fim43_redeye_equipment`)
- FIM-92 Stinger (`usa_fim92_stinger_equipment`)
- FIM-92 Stinger-POST (`usa_fim92_stinger_post_equipment`)
- FIM-92 Stinger RMP I (E) (`usa_fim92_stinger_rmp_e_equipment`)
- FIM-92 Stinger RMP Block II (F) (`usa_fim92_stinger_rmp_f_equipment`)
- FIM-92J Stinger (`usa_fim92j_stinger_equipment`)
- Blowpipe (`eng_blowpipe_equipment`)
- Javelin (`eng_javelin_equipment`)
- Starburst (`eng_starburst_equipment`)
- Starstreak (`eng_starstreak_equipment`)
- Martlet (`eng_martlet_equipment`)
- Mistral (`fra_mistral_equipment`)
- RBS 70 (`swe_rbs70_equipment`)
- RBS 70M (`swe_rbs70m_equipment`)
- RBS 90 (`swe_rbs90_equipment`)
- ПЗРК Grom (`pol_grom_equipment`)
- ПЗРК Piorun (`pol_piorun_equipment`)
### ES_aa_equipments_rus

[common/units/equipment/ES_aa_equipments_rus.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_aa_equipments_rus.txt)

- 9К338 \"Игла-С\" (`aa_9k338_igla_s_equipment`)
- 9К333 \"Верба\" (`aa_9k333_verba_equipment`)
- ПЗРК \"Метка\" (`aa_metka_equipment`)
### ES_aa_equipments_sov

[common/units/equipment/ES_aa_equipments_sov.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_aa_equipments_sov.txt)

- ПЗРК 9К32 \"Стрела-2\" (`aa_9k32_strela_2_equipment`)
- ПЗРК 9К34 \"Стрела-3\" (`aa_9k34_strela_3_equipment`)
- ПЗРК 9К38 \"Игла\" (`aa_9k38_igla_equipment`)
### ES_aa_equipments_ukr

[common/units/equipment/ES_aa_equipments_ukr.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_aa_equipments_ukr.txt)

- Игла-1 (`infantry_aa_igla1_equipment`)
- Игла-1М (`infantry_aa_igla1m_equipment`)
- РК-10 (`infantry_aa_rk10_equipment`)
### ES_afv_chassis_sov_bmd1

[common/units/equipment/ES_afv_chassis_sov_bmd1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd1.txt)

- ЛТ на базе БМД-1 (`light_tank_afv_sov_bmd1_equipment`)
- ЗРК на базе БМД-1 (`sp_aa_afv_sov_bmd1_equipment`)
- Мобильная установка с ПТУР на базе БМД-1 (`sp_atgm_afv_sov_bmd1_equipment`)
- ИМР на базе БМД-1 (`arv_afv_sov_bmd1_equipment`)
- САУ на базе БМД-1 (`sp_artillery_afv_sov_bmd1_equipment`)
- РСЗО на базе БМД-1 (`sp_mlrs_afv_sov_bmd1_equipment`)
### ES_afv_chassis_sov_bmd2

[common/units/equipment/ES_afv_chassis_sov_bmd2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd2.txt)

- ЛТ на базе БМД-2 (`light_tank_afv_sov_bmd2_equipment`)
- ЗРК на базе БМД-2 (`sp_aa_afv_sov_bmd2_equipment`)
- Мобильная установка с ПТУР на базе БМД-2 (`sp_atgm_afv_sov_bmd2_equipment`)
- ИМР на базе БМД-2 (`arv_afv_sov_bmd2_equipment`)
- САУ на базе БМД-2 (`sp_artillery_afv_sov_bmd2_equipment`)
- РСЗО на базе БМД-2 (`sp_mlrs_afv_sov_bmd2_equipment`)
### ES_afv_chassis_sov_bmd3

[common/units/equipment/ES_afv_chassis_sov_bmd3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd3.txt)

- ЛТ на базе БМД-3 (`light_tank_afv_sov_bmd3_equipment`)
- ЗРК на базе БМД-3 (`sp_aa_afv_sov_bmd3_equipment`)
- Мобильная установка с ПТУР на базе БМД-3 (`sp_atgm_afv_sov_bmd3_equipment`)
- ИМР на базе БМД-3 (`arv_afv_sov_bmd3_equipment`)
- САУ на базе БМД-3 (`sp_artillery_afv_sov_bmd3_equipment`)
- РСЗО на базе БМД-3 (`sp_mlrs_afv_sov_bmd3_equipment`)
### ES_afv_chassis_sov_bmd4

[common/units/equipment/ES_afv_chassis_sov_bmd4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_afv_chassis_sov_bmd4.txt)

- ЛТ на базе БМД-4 (`light_tank_afv_rus_bmd4_equipment`)
- ЗРК на базе БМД-4 (`sp_aa_afv_rus_bmd4_equipment`)
- Мобильная установка с ПТУР на базе БМД-4 (`sp_atgm_afv_rus_bmd4_equipment`)
- ИМР на базе БМД-4 (`arv_afv_rus_bmd4_equipment`)
- САУ на базе БМД-4 (`sp_artillery_afv_rus_bmd4_equipment`)
- РСЗО на базе БМД-4 (`sp_mlrs_afv_rus_bmd4_equipment`)
### ES_apc_chassis_eng_fv432

[common/units/equipment/ES_apc_chassis_eng_fv432.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_eng_fv432.txt)

- Шасси FV423 (`apc_eng_fv432_equipment`)
- ЛТ на базе FV423 (`light_tank_apc_eng_fv432_equipment`)
- ЗРК на базе FV423 (`sp_aa_apc_eng_fv432_equipment`)
- Мобильный ПТРК на базе FV423 (`sp_atgm_apc_eng_fv432_equipment`)
- ИМР на базе FV423 (`arv_apc_eng_fv432_equipment`)
- САУ на базе FV423 (`sp_artillery_apc_eng_fv432_equipment`)
### ES_apc_chassis_euro_CAVS

[common/units/equipment/ES_apc_chassis_euro_CAVS.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_euro_CAVS.txt)

- Шасси CAVS (`apc_euro_CAVS_equipment`)
- light_tank_apc_euro_CAVS_equipment (`light_tank_apc_euro_CAVS_equipment`)
- sp_aa_apc_euro_CAVS_equipment (`sp_aa_apc_euro_CAVS_equipment`)
- sp_atgm_apc_euro_CAVS_equipment (`sp_atgm_apc_euro_CAVS_equipment`)
- arv_apc_euro_CAVS_equipment (`arv_apc_euro_CAVS_equipment`)
- sp_artillery_apc_euro_CAVS_equipment (`sp_artillery_apc_euro_CAVS_equipment`)
### ES_apc_chassis_fra_VAB

[common/units/equipment/ES_apc_chassis_fra_VAB.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_fra_VAB.txt)

- Шасси VAB (`apc_fra_VAB_equipment`)
- ЛТ на базе VAB (`light_tank_apc_fra_VAB_equipment`)
- ЗРК на базе VAB (`sp_aa_apc_fra_VAB_equipment`)
- Мобильный ПТРК на базе VAB (`sp_atgm_apc_fra_VAB_equipment`)
- ИМР на базе VAB (`arv_apc_fra_VAB_equipment`)
- САУ на базе VAB (`sp_artillery_apc_fra_VAB_equipment`)
### ES_apc_chassis_ger_boxer

[common/units/equipment/ES_apc_chassis_ger_boxer.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_ger_boxer.txt)

- Шасси Boxer (`apc_ger_boxer_equipment`)
- ЛТ на базе Boxer (`light_tank_apc_ger_boxer_equipment`)
- ЗРК на базе Boxer (`sp_aa_apc_ger_boxer_equipment`)
- Мобильный ПТРК на базе Boxer (`sp_atgm_apc_ger_boxer_equipment`)
- ИМР на базе Boxer (`arv_apc_ger_boxer_equipment`)
- САУ на базе Boxer (`sp_artillery_apc_ger_boxer_equipment`)
### ES_apc_chassis_ger_fuchs

[common/units/equipment/ES_apc_chassis_ger_fuchs.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_ger_fuchs.txt)

- Шасси TPz 1 Fuchs (`apc_ger_fuchs_equipment`)
- ЛТ на базе TPz 1 Fuchs (`light_tank_apc_ger_fuchs_equipment`)
- ЗРК на базе TPz 1 Fuchs (`sp_aa_apc_ger_fuchs_equipment`)
- Мобильный ПТРК на базе TPz 1 Fuchs (`sp_atgm_apc_ger_fuchs_equipment`)
- ИМР на базе TPz 1 Fuchs (`arv_apc_ger_fuchs_equipment`)
- САУ на базе TPz 1 Fuchs (`sp_artillery_apc_ger_fuchs_equipment`)
### ES_apc_chassis_ita_freccia

[common/units/equipment/ES_apc_chassis_ita_freccia.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_ita_freccia.txt)

- Шасси Freccia (`apc_ita_freccia_equipment`)
- ЛТ на базе Freccia (`light_tank_apc_ita_freccia_equipment`)
- ЗРК на базе Freccia (`sp_aa_apc_ita_freccia_equipment`)
- Мобильный ПТРК на базе Freccia (`sp_atgm_apc_ita_freccia_equipment`)
- ИМР на базе Freccia (`arv_apc_ita_freccia_equipment`)
- САУ на базе Freccia (`sp_artillery_apc_ita_freccia_equipment`)
### ES_apc_chassis_pol_rosomak

[common/units/equipment/ES_apc_chassis_pol_rosomak.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_pol_rosomak.txt)

- Шасси Rosomak (`apc_pol_rosomak_equipment`)
- ЛТ на базе Rosomak (`light_tank_apc_pol_rosomak_equipment`)
- ЗРК на базе Rosomak (`sp_aa_apc_pol_rosomak_equipment`)
- Мобильная ПТРК на базе Rosomak (`sp_atgm_apc_pol_rosomak_equipment`)
- ИМР на базе Rosomak (`arv_apc_pol_rosomak_equipment`)
- САУ на базе Rosomak (`sp_artillery_apc_pol_rosomak_equipment`)
### ES_apc_chassis_sov

[common/units/equipment/ES_apc_chassis_sov.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_sov.txt)

- Шасси БТР-50 (`apc_sov_btr50_equipment`)
- ЛТ на базе БТР-50 (`light_tank_apc_sov_btr50_equipment`)
- ЗРК на базе БТР-50 (`sp_aa_apc_sov_btr50_equipment`)
- Мобильная установка с ПТУР на базе БТР-50 (`sp_atgm_apc_sov_btr50_equipment`)
- ИМР на базе БТР-50 (`arv_apc_sov_btr50_equipment`)
- САУ на базе БТР-50 (`sp_artillery_apc_sov_btr50_equipment`)
- Шасси МТ-ЛБ (`apc_sov_mtlb_equipment`)
- ЛТ на базе МТ-ЛБ (`light_tank_apc_sov_mtlb_equipment`)
- ЗРК на базе МТ-ЛБ (`sp_aa_apc_sov_mtlb_equipment`)
- Мобильная установка с ПТУР на базе МТ-ЛБ (`sp_atgm_apc_sov_mtlb_equipment`)
- ИМР на базе МТ-ЛБ (`arv_apc_sov_mtlb_equipment`)
- САУ на базе МТ-ЛБ (`sp_artillery_apc_sov_mtlb_equipment`)
- РСЗО на базе МТ-ЛБ (`sp_mlrs_apc_sov_mtlb_equipment`)
- ТОС на базе МТ-ЛБ (`sp_tos_apc_sov_mtlb_equipment`)
- Шасси БТР-60 (`apc_sov_btr60_equipment`)
- ЛТ на базе БТР-60 (`light_tank_apc_sov_btr60_equipment`)
- ЗРК на базе БТР-60 (`sp_aa_apc_sov_btr60_equipment`)
- Мобильная установка с ПТУР на базе БТР-60 (`sp_atgm_apc_sov_btr60_equipment`)
- ИМР на базе БТР-60 (`arv_apc_sov_btr60_equipment`)
- САУ на базе БТР-60 (`sp_artillery_apc_sov_btr60_equipment`)
- Шасси БТР-70 (`apc_sov_btr70_equipment`)
- ЛТ на базе БТР-70 (`light_tank_apc_sov_btr70_equipment`)
- ЗРК на базе БТР-70 (`sp_aa_apc_sov_btr70_equipment`)
- Мобильная установка с ПТУР на базе БТР-70 (`sp_atgm_apc_sov_btr70_equipment`)
- ИМР на базе БТР-70 (`arv_apc_sov_btr70_equipment`)
- САУ на базе БТР-70 (`sp_artillery_apc_sov_btr70_equipment`)
- Шасси БТР-80 (`apc_sov_btr80_equipment`)
- ЛТ на базе БТР-80 (`light_tank_apc_sov_btr80_equipment`)
- ЗРК на базе БТР-80 (`sp_aa_apc_sov_btr80_equipment`)
- Мобильная установка с ПТУР на базе БТР-80 (`sp_atgm_apc_sov_btr80_equipment`)
- ИМР на базе БТР-80 (`arv_apc_sov_btr80_equipment`)
- САУ на базе БТР-80 (`sp_artillery_apc_sov_btr80_equipment`)
- Шасси БТР-87 (`apc_rus_btr87_equipment`)
- ЛТ на базе БТР-87 (`light_tank_apc_rus_btr87_equipment`)
- ЗРК на базе БТР-87 (`sp_aa_apc_rus_btr87_equipment`)
- Мобильная установка с ПТУР на базе БТР-87 (`sp_atgm_apc_rus_btr87_equipment`)
- ИМР на базе БТР-87 (`arv_apc_rus_btr87_equipment`)
- САУ на базе БТР-87 (`sp_artillery_apc_rus_btr87_equipment`)
- Шасси БТР-3 (`apc_ukr_btr3_equipment`)
- ЛТ на базе БТР-3 (`light_tank_apc_ukr_btr3_equipment`)
- ЗРК на базе БТР-3 (`sp_aa_apc_ukr_btr3_equipment`)
- Мобильная установка с ПТУР на базе БТР-3 (`sp_atgm_apc_ukr_btr3_equipment`)
- ИМР на базе БТР-3 (`arv_apc_ukr_btr3_equipment`)
- САУ на базе БТР-3 (`sp_artillery_apc_ukr_btr3_equipment`)
- Шасси БТР-90 (`apc_rus_btr90_equipment`)
- ЛТ на базе БТР-90 (`light_tank_apc_rus_btr90_equipment`)
- ЗРК на базе БТР-90 (`sp_aa_apc_rus_btr90_equipment`)
- Мобильная установка с ПТУР на базе БТР-90 (`sp_atgm_apc_rus_btr90_equipment`)
- ИМР на базе БТР-90 (`arv_apc_rus_btr90_equipment`)
- САУ на базе БТР-90 (`sp_artillery_apc_rus_btr90_equipment`)
- Шасси БТР-4 (`apc_ukr_btr4_equipment`)
- ЛТ на базе БТР-4 (`light_tank_apc_ukr_btr4_equipment`)
- ЗРК на базе БТР-4 (`sp_aa_apc_ukr_btr4_equipment`)
- Мобильная установка с ПТУР на базе БТР-4 (`sp_atgm_apc_ukr_btr4_equipment`)
- ИМР на базе БТР-4 (`arv_apc_ukr_btr4_equipment`)
- САУ на базе БТР-4 (`sp_artillery_apc_ukr_btr4_equipment`)
- Шасси БТР-22 (`apc_rus_btr22_equipment`)
- ЛТ на базе БТР-22 (`light_tank_apc_rus_btr22_equipment`)
- ЗРК на базе БТР-22 (`sp_aa_apc_rus_btr22_equipment`)
- Мобильная установка с ПТУР на базе БТР-22 (`sp_atgm_apc_rus_btr22_equipment`)
- ИМР на базе БТР-22 (`arv_apc_rus_btr22_equipment`)
- САУ на базе БТР-22 (`sp_artillery_apc_rus_btr22_equipment`)
- Шасси БТР-16 (`apc_sov_btr16_equipment`)
- ЛТ на базе БТР-16 (`light_tank_apc_sov_btr16_equipment`)
- ЗРК на базе БТР-16 (`sp_aa_apc_sov_btr16_equipment`)
- Мобльная установка с ПТУР на базе БТР-16 (`sp_atgm_apc_sov_btr16_equipment`)
- ИМР на базе БТР-16 (`arv_apc_sov_btr16_equipment`)
- САУ на базе БТР-16 (`sp_artillery_apc_sov_btr16_equipment`)
### ES_apc_chassis_sov_volat2

[common/units/equipment/ES_apc_chassis_sov_volat2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_sov_volat2.txt)

- Шасси Volat V-2 (`apc_blr_volat2_equipment`)
- ЛТ на базе Volat V-2 (`light_tank_apc_blr_volat2_equipment`)
- ЗРК на базе Volat V-2 (`sp_aa_apc_blr_volat2_equipment`)
- Мобильная установка с ПТУР на базе Volat V-2 (`sp_atgm_apc_blr_volat2_equipment`)
- БРЭМ на базе Volat V-2 (`arv_apc_blr_volat2_equipment`)
- САУ на базе Volat V-2 (`sp_artillery_apc_blr_volat2_equipment`)
- РСЗО на базе Volat V-2 (`sp_mlrs_apc_blr_volat2_equipment`)
- ТОС на базе Volat V-2 (`sp_tos_apc_blr_volat2_equipment`)
### ES_apc_chassis_swe_pbv302

[common/units/equipment/ES_apc_chassis_swe_pbv302.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_swe_pbv302.txt)

- Шасси Pbv 302 (`apc_swe_pbv302_equipment`)
- ЛТ на базе Pbv 302 (`light_tank_apc_swe_pbv302_equipment`)
- ЗРК на базе Pbv 302 (`sp_aa_apc_swe_pbv302_equipment`)
- Мобильный ПТРК на базе Pbv 302 (`sp_atgm_apc_swe_pbv302_equipment`)
- ИМР на базе Pbv 302 (`arv_apc_swe_pbv302_equipment`)
- САУ на базе Pbv 302 (`sp_artillery_apc_swe_pbv302_equipment`)
### ES_apc_chassis_ukr_otaman

[common/units/equipment/ES_apc_chassis_ukr_otaman.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_ukr_otaman.txt)

- Шасси Отаман (`apc_ukr_otaman_equipment`)
- ЛТ на базе Отаман (`light_tank_apc_ukr_otaman_equipment`)
- ЗРК на базе Отаман (`sp_aa_apc_ukr_otaman_equipment`)
- обильная установка с ПТУР на базе Отаман (`sp_atgm_apc_ukr_otaman_equipment`)
- ИМР на базе Отаман (`arv_apc_ukr_otaman_equipment`)
- САУ на базе Отаман (`sp_artillery_apc_ukr_otaman_equipment`)
### ES_apc_chassis_usa_AAV

[common/units/equipment/ES_apc_chassis_usa_AAV.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_usa_AAV.txt)

- Шасси AAV7 (`apc_usa_aav7_equipment`)
- ЛТ на базе AAV7 (`light_tank_apc_usa_aav7_equipment`)
- ЗРК на базе AAV7 (`sp_aa_apc_usa_aav7_equipment`)
- Мобильный ПТРК на базе AAV7 (`sp_atgm_apc_usa_aav7_equipment`)
- ИМР на базе AAV7 (`arv_apc_usa_aav7_equipment`)
- САУ на базе AAV7 (`sp_artillery_apc_usa_aav7_equipment`)
### ES_apc_chassis_usa_ACV

[common/units/equipment/ES_apc_chassis_usa_ACV.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_usa_ACV.txt)

- Шасcи ACV (`apc_usa_ACV_equipment`)
- light_tank_apc_usa_ACV_equipment (`light_tank_apc_usa_ACV_equipment`)
- sp_aa_apc_usa_ACV_equipment (`sp_aa_apc_usa_ACV_equipment`)
- sp_atgm_apc_usa_ACV_equipment (`sp_atgm_apc_usa_ACV_equipment`)
- arv_apc_usa_ACV_equipment (`arv_apc_usa_ACV_equipment`)
- sp_artillery_apc_usa_ACV_equipment (`sp_artillery_apc_usa_ACV_equipment`)
### ES_apc_chassis_usa_lav25

[common/units/equipment/ES_apc_chassis_usa_lav25.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_usa_lav25.txt)

- Шасси LAV25 (`apc_usa_lav25_equipment`)
- ЛТ на базе LAV25 (`light_tank_apc_usa_lav25_equipment`)
- ЗРК на базе LAV25 (`sp_aa_apc_usa_lav25_equipment`)
- Мобильный ПТРК на базе LAV25 (`sp_atgm_apc_usa_lav25_equipment`)
- ИМР на базе LAV25 (`arv_apc_usa_lav25_equipment`)
- САУ на базе LAV25 (`sp_artillery_apc_usa_lav25_equipment`)
### ES_apc_chassis_usa_m113

[common/units/equipment/ES_apc_chassis_usa_m113.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_usa_m113.txt)

- Шасси M113 (`apc_usa_m113_equipment`)
- ЛТ на базе M113 (`light_tank_apc_usa_m113_equipment`)
- ЗРК на базе M113 (`sp_aa_apc_usa_m113_equipment`)
- Мобильный ПТРК на базе M113 (`sp_atgm_apc_usa_m113_equipment`)
- ИМР на базе M113 (`arv_apc_usa_m113_equipment`)
- САУ на базе M113 (`sp_artillery_apc_usa_m113_equipment`)
### ES_apc_chassis_usa_stryker

[common/units/equipment/ES_apc_chassis_usa_stryker.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_apc_chassis_usa_stryker.txt)

- Шасси Stryker (`apc_usa_stryker_equipment`)
- ЛТ на базе Stryker (`light_tank_apc_usa_stryker_equipment`)
- ЗРК на базе Stryker (`sp_aa_apc_usa_stryker_equipment`)
- Мобильный ПТРК на базе Stryker (`sp_atgm_apc_usa_stryker_equipment`)
- ИМР на базе Stryker (`arv_apc_usa_stryker_equipment`)
- САУ на базе Stryker (`sp_artillery_apc_usa_stryker_equipment`)
### ES_artillery_equipments_nto

[common/units/equipment/ES_artillery_equipments_nto.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_artillery_equipments_nto.txt)

- BL 5.5-inch Medium Gun (`eng_artillery_bl5inch_equipment`)
- L118 (`eng_artillery_l118_equipment`)
- 105 mm leFH 18/40 (`ger_artillery_leFH_equipment`)
- FH70 (`ger_artillery_FH70_equipment`)
- 105 mm Modèle 50 (`fra_artillery_modele50_equipment`)
- TRF1 (`fra_artillery_TRF1_equipment`)
- LG1 (`fra_artillery_TRF2_equipment`)
### ES_artillery_equipments_sov

[common/units/equipment/ES_artillery_equipments_sov.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_artillery_equipments_sov.txt)

- Д-1 (`sov_artillery_d1_equipment`)
- Д-74 (`sov_artillery_d74_equipment`)
- Д-20 (`sov_artillery_d20_equipment`)
- М-46 (`sov_artillery_m46_equipment`)
- Д-30 (`sov_artillery_d30_equipment`)
- 2а36 Гиацинт (`sov_artillery_2a36_equipment`)
- 2а65 Мста-Б (`sov_artillery_2a65_equipment`)
### ES_atgm_equipments_nto

[common/units/equipment/ES_atgm_equipments_nto.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_atgm_equipments_nto.txt)

- M47 Dragon (`usa_m47_dragon_equipment`)
- BGM-71 TOW (`usa_bgm71_tow_equipment`)
- BGM-71 TOW ІІ (`usa_bgm71_tow_ii_equipment`)
- BGM-71F TOW-2В (`usa_bgm71f_tow_2b_equipment`)
- FGM-148 Javelin (`usa_fgm148_javelin_atgm_equipment`)
- Javelin F-Model (`usa_javelin_f_model_equipment`)
- eng_vickers_vigilant_equipment (`eng_vickers_vigilant_equipment`)
- Swingfire (`eng_swingfire_equipment`)
- NLAW ATGM (`eng_nlaw_atgm_equipment`)
- ENTAC (`fra_entac_equipment`)
- Milan (`ger_fra_milan_equipment`)
- HOT (`ger_fra_hot_equipment`)
- Milan 2 (`ger_fra_milan2_equipment`)
- Milan 3 (`ger_fra_milan3_equipment`)
- ERYX (`ger_fra_eryx_equipment`)
- AKERON MP (`ger_fra_akeron_mp_equipment`)
- MMP (`ger_fra_mmp_equipment`)
### ES_brdm_chassis_sov_brdm1

[common/units/equipment/ES_brdm_chassis_sov_brdm1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_brdm_chassis_sov_brdm1.txt)

- Шасси БРДМ-1 (`sov_brdm1_equipment`)
- ЛТ на базе БРДМ-1 (`light_tank_sov_brdm1_equipment`)
- ЗРК на базе БРДМ-1 (`sp_aa_sov_brdm1_equipment`)
- Мобильная установка с ПТУР на базе БРДМ-1 (`sp_atgm_sov_brdm1_equipment`)
- ИМР на базе БРДМ-1 (`arv_sov_brdm1_equipment`)
### ES_brdm_chassis_sov_brdm2

[common/units/equipment/ES_brdm_chassis_sov_brdm2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_brdm_chassis_sov_brdm2.txt)

- Шасси БРДМ-2 (`sov_brdm2_equipment`)
- ЛТ на базе БРДМ-2 (`light_tank_sov_brdm2_equipment`)
- ЗРК на базе БРДМ-2 (`sp_aa_sov_brdm2_equipment`)
- Мобильная установка с ПТУР на базе БРДМ-2 (`sp_atgm_sov_brdm2_equipment`)
- ИМР на базе БРДМ-2 (`arv_sov_brdm2_equipment`)
### ES_ifv_chassis_eng_warrior

[common/units/equipment/ES_ifv_chassis_eng_warrior.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_eng_warrior.txt)

- Шасси Warrior (`ifv_eng_warrior_equipment`)
- ЛТ на базе Warrior (`light_tank_ifv_eng_warrior_equipment`)
- ЗРК на базе Warrior (`sp_aa_ifv_eng_warrior_equipment`)
- Мобильный ПТРК на базе Warrior (`sp_atgm_ifv_eng_warrior_equipment`)
- ИМР на базе Warrior (`arv_ifv_eng_warrior_equipment`)
- САУ на базе Warrior (`sp_artillery_ifv_eng_warrior_equipment`)
- РСЗО на базе Warrior (`sp_mlrs_ifv_eng_warrior_equipment`)
### ES_ifv_chassis_fra_amx10p

[common/units/equipment/ES_ifv_chassis_fra_amx10p.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_fra_amx10p.txt)

- Шасси AMX-10P (`ifv_fra_amx10p_equipment`)
- ЛТ на базе AMX-10P (`light_tank_ifv_fra_amx10p_equipment`)
- ЗРК на базе AMX-10P (`sp_aa_ifv_fra_amx10p_equipment`)
- Мобильный ПТРК на базе AMX-10P (`sp_atgm_ifv_fra_amx10p_equipment`)
- ИМР на базе AMX-10P (`arv_ifv_fra_amx10p_equipment`)
- САУ на базе AMX-10P (`sp_artillery_ifv_fra_amx10p_equipment`)
- РСЗО на базе AMX-10P (`sp_mlrs_ifv_fra_amx10p_equipment`)
### ES_ifv_chassis_fra_vbci

[common/units/equipment/ES_ifv_chassis_fra_vbci.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_fra_vbci.txt)

- Шасси VBCI (`ifv_fra_vbci_equipment`)
- ЛТ на базе VBCI (`light_tank_ifv_fra_vbci_equipment`)
- ЗРК на базе VBCI (`sp_aa_ifv_fra_vbci_equipment`)
- Мобильный ПТРК на базе VBCI (`sp_atgm_ifv_fra_vbci_equipment`)
- ИМР на базе VBCI (`arv_ifv_fra_vbci_equipment`)
- САУ на базе VBCI (`sp_artillery_ifv_fra_vbci_equipment`)
- РСЗО на базе VBCI (`sp_mlrs_ifv_fra_vbci_equipment`)
### ES_ifv_chassis_ger_kf41Lynx

[common/units/equipment/ES_ifv_chassis_ger_kf41Lynx.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ger_kf41Lynx.txt)

- Шасси KF-41 Lynx (`ifv_ger_kf41Lynx_equipment`)
- light_tank_ifv_ger_kf41Lynx_equipment (`light_tank_ifv_ger_kf41Lynx_equipment`)
- sp_aa_ifv_ger_kf41Lynx_equipment (`sp_aa_ifv_ger_kf41Lynx_equipment`)
- sp_atgm_ifv_ger_kf41Lynx_equipment (`sp_atgm_ifv_ger_kf41Lynx_equipment`)
- arv_ifv_ger_kf41Lynx_equipment (`arv_ifv_ger_kf41Lynx_equipment`)
- sp_artillery_ifv_ger_kf41Lynx_equipment (`sp_artillery_ifv_ger_kf41Lynx_equipment`)
- sp_mlrs_ifv_ger_kf41Lynx_equipment (`sp_mlrs_ifv_ger_kf41Lynx_equipment`)
### ES_ifv_chassis_ger_marder1

[common/units/equipment/ES_ifv_chassis_ger_marder1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ger_marder1.txt)

- Шасси Marder 1 (`ifv_ger_marder1_equipment`)
- ЛТ на базе Marder 1 (`light_tank_ifv_ger_marder1_equipment`)
- ЗРК на базе Marder 1 (`sp_aa_ifv_ger_marder1_equipment`)
- Мобильный ПТРК на базе Marder 1 (`sp_atgm_ifv_ger_marder1_equipment`)
- ИМР на базе Marder 1 (`arv_ifv_ger_marder1_equipment`)
- САУ на базе Marder 1 (`sp_artillery_ifv_ger_marder1_equipment`)
- РСЗО на базе Marder 1 (`sp_mlrs_ifv_ger_marder1_equipment`)
### ES_ifv_chassis_ger_puma

[common/units/equipment/ES_ifv_chassis_ger_puma.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ger_puma.txt)

- Шасси Puma (`ifv_ger_puma_equipment`)
- ЛТ на базе Puma (`light_tank_ifv_ger_puma_equipment`)
- ЗРК на базе Puma (`sp_aa_ifv_ger_puma_equipment`)
- Мобильный ПТРК на базе Puma (`sp_atgm_ifv_ger_puma_equipment`)
- ИМР на базе Puma (`arv_ifv_ger_puma_equipment`)
- САУ на базе Puma (`sp_artillery_ifv_ger_puma_equipment`)
- РСЗО на базе Puma (`sp_mlrs_ifv_ger_puma_equipment`)
### ES_ifv_chassis_ita_dardo

[common/units/equipment/ES_ifv_chassis_ita_dardo.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ita_dardo.txt)

- Шасси Dardo (`ifv_ita_dardo_equipment`)
- ЛТ на базе Dardo (`light_tank_ifv_ita_dardo_equipment`)
- ЗРК на базе Dardo (`sp_aa_ifv_ita_dardo_equipment`)
- Мобильный ПТРК на базе Dardo (`sp_atgm_ifv_ita_dardo_equipment`)
- ИМР на базе Dardo (`arv_ifv_ita_dardo_equipment`)
- САУ на базе Dardo (`sp_artillery_ifv_ita_dardo_equipment`)
- РСЗО на базе Dardo (`sp_mlrs_ifv_ita_dardo_equipment`)
### ES_ifv_chassis_pol_borsuk

[common/units/equipment/ES_ifv_chassis_pol_borsuk.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_pol_borsuk.txt)

- ЛТ на базе Borsuk (`light_tank_ifv_pol_borsuk_equipment`)
- ЗРК на базе Borsuk (`sp_aa_ifv_pol_borsuk_equipment`)
- Мобильная ПТРК на базе Borsuk (`sp_atgm_ifv_pol_borsuk_equipment`)
- ИМР на базе Borsuk (`arv_ifv_pol_borsuk_equipment`)
- САУ на базе Borsuk (`sp_artillery_ifv_pol_borsuk_equipment`)
- РСЗО на базе Borsuk (`sp_mlrs_ifv_pol_borsuk_equipment`)
### ES_ifv_chassis_sov_bmp1

[common/units/equipment/ES_ifv_chassis_sov_bmp1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp1.txt)

- ЛТ на базе БМП-1 (`light_tank_ifv_sov_bmp1_equipment`)
- ЗРК на базе БМП-1 (`sp_aa_ifv_sov_bmp1_equipment`)
- Мобильная установка с ПТУР на базе БМП-1 (`sp_atgm_ifv_sov_bmp1_equipment`)
- ИМР на базе БМП-1 (`arv_ifv_sov_bmp1_equipment`)
- САУ на базе БМП-1 (`sp_artillery_ifv_sov_bmp1_equipment`)
- РСЗО на базе БМП-1 (`sp_mlrs_ifv_sov_bmp1_equipment`)
### ES_ifv_chassis_sov_bmp2

[common/units/equipment/ES_ifv_chassis_sov_bmp2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp2.txt)

- ЛТ на базе БМП-2 (`light_tank_ifv_sov_bmp2_equipment`)
- ЗРК на базе БМП-2 (`sp_aa_ifv_sov_bmp2_equipment`)
- Мобильная установка с ПТУР на базе БМП-2 (`sp_atgm_ifv_sov_bmp2_equipment`)
- ИМР на базе БМП-2 (`arv_ifv_sov_bmp2_equipment`)
- САУ на базе БМП-2 (`sp_artillery_ifv_sov_bmp2_equipment`)
- РСЗО на базе БМП-2 (`sp_mlrs_ifv_sov_bmp2_equipment`)
### ES_ifv_chassis_sov_bmp3

[common/units/equipment/ES_ifv_chassis_sov_bmp3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_bmp3.txt)

- ЛТ на базе БМП-3 (`light_tank_ifv_sov_bmp3_equipment`)
- ЗРК на базе БМП-3 (`sp_aa_ifv_sov_bmp3_equipment`)
- Мобильная установка с ПТУР на базе БМП-3 (`sp_atgm_ifv_sov_bmp3_equipment`)
- ИМР на базе БМП-3 (`arv_ifv_sov_bmp3_equipment`)
- САУ на базе БМП-3 (`sp_artillery_ifv_sov_bmp3_equipment`)
- РСЗО на базе БМП-3 (`sp_mlrs_ifv_sov_bmp3_equipment`)
### ES_ifv_chassis_sov_kurganetz25

[common/units/equipment/ES_ifv_chassis_sov_kurganetz25.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_sov_kurganetz25.txt)

- ЛТ на базе Курганец-25 (`light_tank_ifv_rus_kurganetz25_equipment`)
- ЗРК на базе Курганец-25 (`sp_aa_ifv_rus_kurganetz25_equipment`)
- Мобильная установка с ПТУР на базе Курганец-25 (`sp_atgm_ifv_rus_kurganetz25_equipment`)
- ИМР на базе Курганец-25 (`arv_ifv_rus_kurganetz25_equipment`)
- САУ на базе Курганец-25 (`sp_artillery_ifv_rus_kurganetz25_equipment`)
- РСЗО на базе Курганец-25 (`sp_mlrs_ifv_rus_kurganetz25_equipment`)
### ES_ifv_chassis_swe_cv90

[common/units/equipment/ES_ifv_chassis_swe_cv90.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_swe_cv90.txt)

- Шасси CV90 (`ifv_swe_cv90_equipment`)
- ЛТ на базе CV90 (`light_tank_ifv_swe_cv90_equipment`)
- ЗРК на базе CV90 (`sp_aa_ifv_swe_cv90_equipment`)
- Мобильный ПТРК на базе CV90 (`sp_atgm_ifv_swe_cv90_equipment`)
- ИМР на базе CV90 (`arv_ifv_swe_cv90_equipment`)
- САУ на базе CV90 (`sp_artillery_ifv_swe_cv90_equipment`)
- РСЗО на базе CV90 (`sp_mlrs_ifv_swe_cv90_equipment`)
### ES_ifv_chassis_ukr_bmpy

[common/units/equipment/ES_ifv_chassis_ukr_bmpy.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ukr_bmpy.txt)

- light_tank_ifv_ukr_bmpy_equipment (`light_tank_ifv_ukr_bmpy_equipment`)
- sp_aa_ifv_ukr_bmpy_equipment (`sp_aa_ifv_ukr_bmpy_equipment`)
- sp_atgm_ifv_ukr_bmpy_equipment (`sp_atgm_ifv_ukr_bmpy_equipment`)
- arv_ifv_ukr_bmpy_equipment (`arv_ifv_ukr_bmpy_equipment`)
- sp_artillery_ifv_ukr_bmpy_equipment (`sp_artillery_ifv_ukr_bmpy_equipment`)
- sp_mlrs_ifv_ukr_bmpy_equipment (`sp_mlrs_ifv_ukr_bmpy_equipment`)
### ES_ifv_chassis_ukr_inguar7

[common/units/equipment/ES_ifv_chassis_ukr_inguar7.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_ukr_inguar7.txt)

- light_tank_ifv_ukr_inguar7_equipment (`light_tank_ifv_ukr_inguar7_equipment`)
- sp_aa_ifv_ukr_inguar7_equipment (`sp_aa_ifv_ukr_inguar7_equipment`)
- sp_atgm_ifv_ukr_inguar7_equipment (`sp_atgm_ifv_ukr_inguar7_equipment`)
- arv_ifv_ukr_inguar7_equipment (`arv_ifv_ukr_inguar7_equipment`)
- sp_artillery_ifv_ukr_inguar7_equipment (`sp_artillery_ifv_ukr_inguar7_equipment`)
- sp_mlrs_ifv_ukr_inguar7_equipment (`sp_mlrs_ifv_ukr_inguar7_equipment`)
### ES_ifv_chassis_usa_bradley

[common/units/equipment/ES_ifv_chassis_usa_bradley.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_ifv_chassis_usa_bradley.txt)

- Шасси M2 Bradley (`ifv_usa_bradley_equipment`)
- ЛТ на базе M2 Bradley (`light_tank_ifv_usa_bradley_equipment`)
- ЗРК на базе M2 Bradley (`sp_aa_ifv_usa_bradley_equipment`)
- Мобильный ПТРК на базе M2 Bradley (`sp_atgm_ifv_usa_bradley_equipment`)
- ИМР на базе M2 Bradley (`arv_ifv_usa_bradley_equipment`)
- САУ на базе M2 Bradley (`sp_artillery_ifv_usa_bradley_equipment`)
- РСЗО на базе M2 Bradley (`sp_mlrs_ifv_usa_bradley_equipment`)
### ES_imv_chassis_civil_0

[common/units/equipment/ES_imv_chassis_civil_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_civil_0.txt)

- Гражданская машина 1 (`imv_civil_0_equipment`)
- ЗРК на базе гражданской машины 1 (`sp_aa_imv_civil_0_equipment`)
- Мобильная установка с ПТУР на базе гражданской машины 1 (`sp_atgm_imv_civil_0_equipment`)
- САУ на базе гражданской машины 1 (`sp_artillery_imv_civil_0_equipment`)
- РСЗО на базе гражданской машины 1 (`sp_mlrs_imv_civil_0_equipment`)
- ТОС на базе гражданской машины 1 (`sp_tos_imv_civil_0_equipment`)
### ES_imv_chassis_civil_1

[common/units/equipment/ES_imv_chassis_civil_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_civil_1.txt)

- Гражданская машина 2 (`imv_civil_1_equipment`)
- ЗРК на базе гражданской машины 2 (`sp_aa_imv_civil_1_equipment`)
- Мобильная установка с ПТУР на базе гражданской машины 2 (`sp_atgm_imv_civil_1_equipment`)
- САУ на базе гражданской машины 2 (`sp_artillery_imv_civil_1_equipment`)
- РСЗО на базе гражданской машины 2 (`sp_mlrs_imv_civil_1_equipment`)
- ТОС на базе гражданской машины 2 (`sp_tos_imv_civil_1_equipment`)
### ES_imv_chassis_civil_2

[common/units/equipment/ES_imv_chassis_civil_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_civil_2.txt)

- Гражданская машина 3 (`imv_civil_2_equipment`)
- ЗРК на базе гражданской машины 3 (`sp_aa_imv_civil_2_equipment`)
- Мобильная установка с ПТУР на базе гражданской машины 3 (`sp_atgm_imv_civil_2_equipment`)
- САУ на базе гражданской машины 3 (`sp_artillery_imv_civil_2_equipment`)
- РСЗО на базе гражданской машины 3 (`sp_mlrs_imv_civil_2_equipment`)
- ТОС на базе гражданской машины 3 (`sp_tos_imv_civil_2_equipment`)
### ES_imv_chassis_civil_3

[common/units/equipment/ES_imv_chassis_civil_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_civil_3.txt)

- Гражданская машина 4 (`imv_civil_3_equipment`)
- ЗРК на базе гражданской машины 4 (`sp_aa_imv_civil_3_equipment`)
- Мобильная установка с ПТУР на базе гражданской машины 4 (`sp_atgm_imv_civil_3_equipment`)
- САУ на базе гражданской машины 4 (`sp_artillery_imv_civil_3_equipment`)
- РСЗО на базе гражданской машины 4 (`sp_mlrs_imv_civil_3_equipment`)
- ТОС на базе гражданской машины 4 (`sp_tos_imv_civil_3_equipment`)
### ES_imv_chassis_civil_4

[common/units/equipment/ES_imv_chassis_civil_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_civil_4.txt)

- Гражданская машина 5 (`imv_civil_4_equipment`)
- ЗРК на базе гражданской машины 5 (`sp_aa_imv_civil_4_equipment`)
- Мобильная установка с ПТУР на базе гражданской машины 5 (`sp_atgm_imv_civil_4_equipment`)
- САУ на базе гражданской машины 5 (`sp_artillery_imv_civil_4_equipment`)
- РСЗО на базе гражданской машины 5 (`sp_mlrs_imv_civil_4_equipment`)
- ТОС на базе гражданской машины 5 (`sp_tos_imv_civil_4_equipment`)
### ES_imv_chassis_heavy_0

[common/units/equipment/ES_imv_chassis_heavy_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_heavy_0.txt)

- Тяжёлая бронемашина 1 (`imv_heavy_0_equipment`)
- ЗРК на базе тяжелой бронемашины 1 (`sp_aa_imv_heavy_0_equipment`)
- Мобильная установка с ПТУР на базе тяжелой бронемашины 1 (`sp_atgm_imv_heavy_0_equipment`)
- САУ на базе тяжелой бронемашины 1 (`sp_artillery_imv_heavy_0_equipment`)
- РСЗО на базе тяжелой бронемашины 1 (`sp_mlrs_imv_heavy_0_equipment`)
- ТОС на базе тяжелой бронемашины 1 (`sp_tos_imv_heavy_0_equipment`)
### ES_imv_chassis_heavy_1

[common/units/equipment/ES_imv_chassis_heavy_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_heavy_1.txt)

- Тяжёлая бронемашина 2 (`imv_heavy_1_equipment`)
- ЗРК на базе тяжелой бронемашины 2 (`sp_aa_imv_heavy_1_equipment`)
- Мобильная установка с ПТУР на базе тяжелой бронемашины 2 (`sp_atgm_imv_heavy_1_equipment`)
- САУ на базе тяжелой бронемашины 2 (`sp_artillery_imv_heavy_1_equipment`)
- РСЗО на базе тяжелой бронемашины 2 (`sp_mlrs_imv_heavy_1_equipment`)
- ТОС на базе тяжелой бронемашины 2 (`sp_tos_imv_heavy_1_equipment`)
### ES_imv_chassis_heavy_2

[common/units/equipment/ES_imv_chassis_heavy_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_heavy_2.txt)

- Тяжёлая бронемашина 3 (`imv_heavy_2_equipment`)
- ЗРК на базе тяжелой бронемашины 3 (`sp_aa_imv_heavy_2_equipment`)
- Мобильная установка с ПТУР на базе тяжелой бронемашины 3 (`sp_atgm_imv_heavy_2_equipment`)
- САУ на базе тяжелой бронемашины 3 (`sp_artillery_imv_heavy_2_equipment`)
- РСЗО на базе тяжелой бронемашины 3 (`sp_mlrs_imv_heavy_2_equipment`)
- ТОС на базе тяжелой бронемашины 3 (`sp_tos_imv_heavy_2_equipment`)
### ES_imv_chassis_heavy_3

[common/units/equipment/ES_imv_chassis_heavy_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_heavy_3.txt)

- Тяжёлая бронемашина 4 (`imv_heavy_3_equipment`)
- ЗРК на базе тяжелой бронемашины 4 (`sp_aa_imv_heavy_3_equipment`)
- Мобильная установка с ПТУР на базе тяжелой бронемашины 4 (`sp_atgm_imv_heavy_3_equipment`)
- САУ на базе тяжелой бронемашины 4 (`sp_artillery_imv_heavy_3_equipment`)
- РСЗО на базе тяжелой бронемашины 4 (`sp_mlrs_imv_heavy_3_equipment`)
- ТОС на базе тяжелой бронемашины 4 (`sp_tos_imv_heavy_3_equipment`)
### ES_imv_chassis_heavy_4

[common/units/equipment/ES_imv_chassis_heavy_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_heavy_4.txt)

- Тяжёлая бронемашина 5 (`imv_heavy_4_equipment`)
- ЗРК на базе тяжелой бронемашины 5 (`sp_aa_imv_heavy_4_equipment`)
- Мобильная установка с ПТУР на базе тяжелой бронемашины 5 (`sp_atgm_imv_heavy_4_equipment`)
- САУ на базе тяжелой бронемашины 5 (`sp_artillery_imv_heavy_4_equipment`)
- РСЗО на базе тяжелой бронемашины 5 (`sp_mlrs_imv_heavy_4_equipment`)
- ТОС на базе тяжелой бронемашины 5 (`sp_tos_imv_heavy_4_equipment`)
### ES_imv_chassis_light_0

[common/units/equipment/ES_imv_chassis_light_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_light_0.txt)

- Лёгкая бронемашина 1 (`imv_light_0_equipment`)
- ЗРК на базе легкой бронемашины 1 (`sp_aa_imv_light_0_equipment`)
- Мобильная установка с ПТУР на базе легкой бронемашины 1 (`sp_atgm_imv_light_0_equipment`)
- САУ на базе легкой бронемашины 1 (`sp_artillery_imv_light_0_equipment`)
- РСЗО на базе легкой бронемашины 1 (`sp_mlrs_imv_light_0_equipment`)
- ТОС на базе легкой бронемашины 1 (`sp_tos_imv_light_0_equipment`)
### ES_imv_chassis_light_1

[common/units/equipment/ES_imv_chassis_light_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_light_1.txt)

- Лёгкая бронемашина 2 (`imv_light_1_equipment`)
- ЗРК на базе легкой бронемашины 2 (`sp_aa_imv_light_1_equipment`)
- Мобильная установка с ПТУР на базе легкой бронемашины 2 (`sp_atgm_imv_light_1_equipment`)
- САУ на базе легкой бронемашины 2 (`sp_artillery_imv_light_1_equipment`)
- РСЗО на базе легкой бронемашины 2 (`sp_mlrs_imv_light_1_equipment`)
- ТОС на базе легкой бронемашины 2 (`sp_tos_imv_light_1_equipment`)
### ES_imv_chassis_light_2

[common/units/equipment/ES_imv_chassis_light_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_light_2.txt)

- Лёгкая бронемашина 3 (`imv_light_2_equipment`)
- ЗРК на базе легкой бронемашины 3 (`sp_aa_imv_light_2_equipment`)
- Мобильная установка с ПТУР на базе легкой бронемашины 3 (`sp_atgm_imv_light_2_equipment`)
- САУ на базе легкой бронемашины 3 (`sp_artillery_imv_light_2_equipment`)
- РСЗО на базе легкой бронемашины 3 (`sp_mlrs_imv_light_2_equipment`)
- ТОС на базе легкой бронемашины 3 (`sp_tos_imv_light_2_equipment`)
### ES_imv_chassis_light_3

[common/units/equipment/ES_imv_chassis_light_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_light_3.txt)

- Лёгкая бронемашина 4 (`imv_light_3_equipment`)
- ЗРК на базе легкой бронемашины 4 (`sp_aa_imv_light_3_equipment`)
- Мобильная установка с ПТУР на базе легкой бронемашины 4 (`sp_atgm_imv_light_3_equipment`)
- САУ на базе легкой бронемашины 4 (`sp_artillery_imv_light_3_equipment`)
- РСЗО на базе легкой бронемашины 4 (`sp_mlrs_imv_light_3_equipment`)
- ТОС на базе легкой бронемашины 4 (`sp_tos_imv_light_3_equipment`)
### ES_imv_chassis_light_4

[common/units/equipment/ES_imv_chassis_light_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_light_4.txt)

- Лёгкая бронемашина 5 (`imv_light_4_equipment`)
- ЗРК на базе легкой бронемашины 5 (`sp_aa_imv_light_4_equipment`)
- Мобильная установка с ПТУР на базе легкой бронемашины 5 (`sp_atgm_imv_light_4_equipment`)
- САУ на базе легкой бронемашины 5 (`sp_artillery_imv_light_4_equipment`)
- РСЗО на базе легкой бронемашины 5 (`sp_mlrs_imv_light_4_equipment`)
- ТОС на базе легкой бронемашины 5 (`sp_tos_imv_light_4_equipment`)
### ES_imv_chassis_medium_0

[common/units/equipment/ES_imv_chassis_medium_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_medium_0.txt)

- Бронемашина 1 (`imv_medium_0_equipment`)
- ЗРК на базе бронемашины 1 (`sp_aa_imv_medium_0_equipment`)
- Мобильная установка с ПТУР на базе бронемашины 1 (`sp_atgm_imv_medium_0_equipment`)
- САУ на базе легкой бронемашины 1 (`sp_artillery_imv_medium_0_equipment`)
- РСЗО на базе бронемашины 1 (`sp_mlrs_imv_medium_0_equipment`)
- ТОС на базе бронемашины 1 (`sp_tos_imv_medium_0_equipment`)
### ES_imv_chassis_medium_1

[common/units/equipment/ES_imv_chassis_medium_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_medium_1.txt)

- Бронемашина 2 (`imv_medium_1_equipment`)
- ЗРК на базе бронемашины 2 (`sp_aa_imv_medium_1_equipment`)
- Мобильная установка с ПТУР на базе бронемашины 2 (`sp_atgm_imv_medium_1_equipment`)
- САУ на базе легкой бронемашины 2 (`sp_artillery_imv_medium_1_equipment`)
- РСЗО на базе бронемашины 2 (`sp_mlrs_imv_medium_1_equipment`)
- ТОС на базе бронемашины 2 (`sp_tos_imv_medium_1_equipment`)
### ES_imv_chassis_medium_2

[common/units/equipment/ES_imv_chassis_medium_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_medium_2.txt)

- Бронемашина 3 (`imv_medium_2_equipment`)
- ЗРК на базе бронемашины 3 (`sp_aa_imv_medium_2_equipment`)
- Мобильная установка с ПТУР на базе бронемашины 3 (`sp_atgm_imv_medium_2_equipment`)
- САУ на базе легкой бронемашины 3 (`sp_artillery_imv_medium_2_equipment`)
- РСЗО на базе бронемашины 3 (`sp_mlrs_imv_medium_2_equipment`)
- ТОС на базе бронемашины 3 (`sp_tos_imv_medium_2_equipment`)
### ES_imv_chassis_medium_3

[common/units/equipment/ES_imv_chassis_medium_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_medium_3.txt)

- Бронемашина 4 (`imv_medium_3_equipment`)
- ЗРК на базе бронемашины 4 (`sp_aa_imv_medium_3_equipment`)
- Мобильная установка с ПТУР на базе бронемашины 4 (`sp_atgm_imv_medium_3_equipment`)
- САУ на базе легкой бронемашины 4 (`sp_artillery_imv_medium_3_equipment`)
- РСЗО на базе бронемашины 4 (`sp_mlrs_imv_medium_3_equipment`)
- ТОС на базе бронемашины 4 (`sp_tos_imv_medium_3_equipment`)
### ES_imv_chassis_medium_4

[common/units/equipment/ES_imv_chassis_medium_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_imv_chassis_medium_4.txt)

- Бронемашина 5 (`imv_medium_4_equipment`)
- ЗРК на базе бронемашины 5 (`sp_aa_imv_medium_4_equipment`)
- Мобильная установка с ПТУР на базе бронемашины 5 (`sp_atgm_imv_medium_4_equipment`)
- САУ на базе легкой бронемашины 5 (`sp_artillery_imv_medium_4_equipment`)
- РСЗО на базе бронемашины 5 (`sp_mlrs_imv_medium_4_equipment`)
- ТОС на базе бронемашины 5 (`sp_tos_imv_medium_4_equipment`)
### ES_mortar_equipments_nto

[common/units/equipment/ES_mortar_equipments_nto.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mortar_equipments_nto.txt)

- M19 (`usa_m19_equipment`)
- M29 (`usa_m29_equipment`)
- M224 (`usa_m224_equipment`)
- M120 (`usa_m120_equipment`)
- Ordnance SBML 2-inch mortar (`eng_sbml2inch_equipment`)
- L16 (`eng_l16_equipment`)
- 8-cm s.Gr.W.34 (`ger_grw34_equipment`)
- 120 Krh/40 (`ger_120krh40_equipment`)
- RSG60 (`ger_rsg60_equipment`)
- Brandt Mle 27/31 (`fra_brandt2731_equipment`)
- MO-120-RT (`fra_mo120rt_equipment`)
### ES_mortar_equipments_pol

[common/units/equipment/ES_mortar_equipments_pol.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mortar_equipments_pol.txt)

- M-98 (`mortar_M98_equipment`)
- LM-60 (`mortar_LM60_equipment`)
- LMP-2017 (`mortar_LMP2017_equipment`)
### ES_mortar_equipments_sov

[common/units/equipment/ES_mortar_equipments_sov.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mortar_equipments_sov.txt)

- Миномёт ВМВ (`mortar_sov_ww2_equipment`)
- 2Б9 Василёк (`mortar_2b9_vasilyok_equipment`)
- 2Б11 (`mortar_2b11_equipment`)
- 2Б14 Поднос (`mortar_2b14_podnos_equipment`)
- 2Б24 Поднос (`mortar_2b24_podnos_equipment`)
- 2Б25 \"Галл\" (`mortar_2b25_gall_equipment`)
### ES_mortar_equipments_ukr

[common/units/equipment/ES_mortar_equipments_ukr.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mortar_equipments_ukr.txt)

- М120-15 «Молот» (`infantry_mortar_m12015molot_equipment`)
- УПИК-82 (`infantry_mortar_ypik82_equipment`)
- МП-120 (`infantry_mortar_mp120_equipment`)
### ES_motorized

[common/units/equipment/ES_motorized.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_motorized.txt)

- Моторизованное снаряжение (`motorized_equipment_1`)
### ES_mrv_chassis_tracked_0

[common/units/equipment/ES_mrv_chassis_tracked_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_tracked_0.txt)

- Гусеничная машина 1 (`mrv_tracked_0_equipment`)
- ЗРК на базе гусенечной машины 1 (`sp_aa_mrv_tracked_0_equipment`)
- Мобильная установка с ПТУР на базе гусенечной машины 1 (`sp_atgm_mrv_tracked_0_equipment`)
- САУ на базе гусенечной машины 1 (`sp_artillery_mrv_tracked_0_equipment`)
- Тяжелая САУ на базе гусенечной машины 1 (`sp_heavy_artillery_mrv_tracked_0_equipment`)
- РСЗО на базе гусенечной машины 1 (`sp_mlrs_mrv_tracked_0_equipment`)
- ТОС на базе гусенечной машины 1 (`sp_tos_mrv_tracked_0_equipment`)
### ES_mrv_chassis_tracked_1

[common/units/equipment/ES_mrv_chassis_tracked_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_tracked_1.txt)

- Гусеничная машина 2 (`mrv_tracked_1_equipment`)
- ЗРК на базе гусенечной машины 2 (`sp_aa_mrv_tracked_1_equipment`)
- Мобильная установка с ПТУР на базе гусенечной машины 2 (`sp_atgm_mrv_tracked_1_equipment`)
- САУ на базе гусенечной машины 2 (`sp_artillery_mrv_tracked_1_equipment`)
- Тяжелая САУ на базе гусенечной машины 2 (`sp_heavy_artillery_mrv_tracked_1_equipment`)
- РСЗО на базе гусенечной машины 2 (`sp_mlrs_mrv_tracked_1_equipment`)
- ТОС на базе гусенечной машины 2 (`sp_tos_mrv_tracked_1_equipment`)
### ES_mrv_chassis_tracked_2

[common/units/equipment/ES_mrv_chassis_tracked_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_tracked_2.txt)

- Гусеничная машина 3 (`mrv_tracked_2_equipment`)
- ЗРК на базе гусенечной машины 3 (`sp_aa_mrv_tracked_2_equipment`)
- Мобильная установка с ПТУР на базе гусенечной машины 3 (`sp_atgm_mrv_tracked_2_equipment`)
- САУ на базе гусенечной машины 3 (`sp_artillery_mrv_tracked_2_equipment`)
- Тяжелая САУ на базе гусенечной машины 3 (`sp_heavy_artillery_mrv_tracked_2_equipment`)
- РСЗО на базе гусенечной машины 3 (`sp_mlrs_mrv_tracked_2_equipment`)
- ТОС на базе гусенечной машины 3 (`sp_tos_mrv_tracked_2_equipment`)
### ES_mrv_chassis_tracked_3

[common/units/equipment/ES_mrv_chassis_tracked_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_tracked_3.txt)

- Гусеничная машина 4 (`mrv_tracked_3_equipment`)
- ЗРК на базе гусенечной машины 4 (`sp_aa_mrv_tracked_3_equipment`)
- Мобильная установка с ПТУР на базе гусенечной машины 4 (`sp_atgm_mrv_tracked_3_equipment`)
- САУ на базе гусенечной машины 4 (`sp_artillery_mrv_tracked_3_equipment`)
- Тяжелая САУ на базе гусенечной машины 4 (`sp_heavy_artillery_mrv_tracked_3_equipment`)
- РСЗО на базе гусенечной машины 4 (`sp_mlrs_mrv_tracked_3_equipment`)
- ТОС на базе гусенечной машины 4 (`sp_tos_mrv_tracked_3_equipment`)
### ES_mrv_chassis_tracked_4

[common/units/equipment/ES_mrv_chassis_tracked_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_tracked_4.txt)

- Гусеничная машина 5 (`mrv_tracked_4_equipment`)
- ЗРК на базе гусенечной машины 5 (`sp_aa_mrv_tracked_4_equipment`)
- Мобильная установка с ПТУР на базе гусенечной машины 5 (`sp_atgm_mrv_tracked_4_equipment`)
- САУ на базе гусенечной машины 5 (`sp_artillery_mrv_tracked_4_equipment`)
- Тяжелая САУ на базе гусенечной машины 5 (`sp_heavy_artillery_mrv_tracked_4_equipment`)
- РСЗО на базе гусенечной машины 5 (`sp_mlrs_mrv_tracked_4_equipment`)
- ТОС на базе гусенечной машины 5 (`sp_tos_mrv_tracked_4_equipment`)
### ES_mrv_chassis_wheeled_0

[common/units/equipment/ES_mrv_chassis_wheeled_0.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_wheeled_0.txt)

- Колёсный тягач 1 (`mrv_wheeled_0_equipment`)
- ЗРК на базе колесного тягача 1 (`sp_aa_mrv_wheeled_0_equipment`)
- Мобильная установка с ПТУР на базе колесного тягача 1 (`sp_atgm_mrv_wheeled_0_equipment`)
- САУ на базе колесного тягача 1 (`sp_artillery_mrv_wheeled_0_equipment`)
- РСЗО на базе тяжелой колесного тягача 1 (`sp_mlrs_mrv_wheeled_0_equipment`)
- ТОС на базе колесного тягача 1 (`sp_tos_mrv_wheeled_0_equipment`)
### ES_mrv_chassis_wheeled_1

[common/units/equipment/ES_mrv_chassis_wheeled_1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_wheeled_1.txt)

- Колёсный тягач 2 (`mrv_wheeled_1_equipment`)
- ЗРК на базе колесного тягача 2 (`sp_aa_mrv_wheeled_1_equipment`)
- Мобильная установка с ПТУР на базе колесного тягача 2 (`sp_atgm_mrv_wheeled_1_equipment`)
- САУ на базе колесного тягача 2 (`sp_artillery_mrv_wheeled_1_equipment`)
- РСЗО на базе тяжелой колесного тягача 2 (`sp_mlrs_mrv_wheeled_1_equipment`)
- ТОС на базе колесного тягача 2 (`sp_tos_mrv_wheeled_1_equipment`)
### ES_mrv_chassis_wheeled_2

[common/units/equipment/ES_mrv_chassis_wheeled_2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_wheeled_2.txt)

- Колёсный тягач 3 (`mrv_wheeled_2_equipment`)
- ЗРК на базе колесного тягача 3 (`sp_aa_mrv_wheeled_2_equipment`)
- Мобильная установка с ПТУР на базе колесного тягача 3 (`sp_atgm_mrv_wheeled_2_equipment`)
- САУ на базе колесного тягача 3 (`sp_artillery_mrv_wheeled_2_equipment`)
- РСЗО на базе тяжелой колесного тягача 3 (`sp_mlrs_mrv_wheeled_2_equipment`)
- ТОС на базе колесного тягача 3 (`sp_tos_mrv_wheeled_2_equipment`)
### ES_mrv_chassis_wheeled_3

[common/units/equipment/ES_mrv_chassis_wheeled_3.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_wheeled_3.txt)

- Колёсный тягач 4 (`mrv_wheeled_3_equipment`)
- ЗРК на базе колесного тягача 4 (`sp_aa_mrv_wheeled_3_equipment`)
- Мобильная установка с ПТУР на базе колесного тягача 4 (`sp_atgm_mrv_wheeled_3_equipment`)
- САУ на базе колесного тягача 4 (`sp_artillery_mrv_wheeled_3_equipment`)
- РСЗО на базе тяжелой колесного тягача 4 (`sp_mlrs_mrv_wheeled_3_equipment`)
- ТОС на базе колесного тягача 4 (`sp_tos_mrv_wheeled_3_equipment`)
### ES_mrv_chassis_wheeled_4

[common/units/equipment/ES_mrv_chassis_wheeled_4.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_mrv_chassis_wheeled_4.txt)

- Колёсный тягач 5 (`mrv_wheeled_4_equipment`)
- ЗРК на базе колесного тягача 5 (`sp_aa_mrv_wheeled_4_equipment`)
- Мобильная установка с ПТУР на базе колесного тягача 5 (`sp_atgm_mrv_wheeled_4_equipment`)
- САУ на базе колесного тягача 5 (`sp_artillery_mrv_wheeled_4_equipment`)
- РСЗО на базе тяжелой колесного тягача 5 (`sp_mlrs_mrv_wheeled_4_equipment`)
- ТОС на базе колесного тягача 5 (`sp_tos_mrv_wheeled_4_equipment`)
### ES_tank_chassis_embt

[common/units/equipment/ES_tank_chassis_embt.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_embt.txt)

- ifv_heavy_euro_EMBT_ADT140_equipment (`ifv_heavy_euro_EMBT_ADT140_equipment`)
- apc_tank_euro_EMBT_ADT140_equipment (`apc_tank_euro_EMBT_ADT140_equipment`)
- sp_aa_tank_euro_EMBT_ADT140_equipment (`sp_aa_tank_euro_EMBT_ADT140_equipment`)
- sp_atgm_tank_euro_EMBT_ADT140_equipment (`sp_atgm_tank_euro_EMBT_ADT140_equipment`)
- arv_tank_euro_EMBT_ADT140_equipment (`arv_tank_euro_EMBT_ADT140_equipment`)
- sp_artillery_tank_euro_EMBT_ADT140_equipment (`sp_artillery_tank_euro_EMBT_ADT140_equipment`)
- sp_heavy_artillery_tank_euro_EMBT_ADT140_equipment (`sp_heavy_artillery_tank_euro_EMBT_ADT140_equipment`)
- sp_mlrs_tank_euro_EMBT_ADT140_equipment (`sp_mlrs_tank_euro_EMBT_ADT140_equipment`)
### ES_tank_chassis_eng_centurion

[common/units/equipment/ES_tank_chassis_eng_centurion.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_eng_centurion.txt)

- Шасси Centurion (`tank_eng_centurion_equipment`)
- Тяжелая БМП на базе Centurion (`ifv_heavy_eng_centurion_equipment`)
- БТР на базе Centurion (`apc_tank_eng_centurion_equipment`)
- ЗРК на базе Centurion (`sp_aa_tank_eng_centurion_equipment`)
- Мобильный ПТРК на базе Centurion (`sp_atgm_tank_eng_centurion_equipment`)
- ИМР на базе Centurion (`arv_tank_eng_centurion_equipment`)
- САУ на базе Centurion (`sp_artillery_tank_eng_centurion_equipment`)
- Тяжелая САУ на базе Centurion (`sp_heavy_artillery_tank_eng_centurion_equipment`)
- РСЗО на базе Centurion (`sp_mlrs_tank_eng_centurion_equipment`)
### ES_tank_chassis_eng_challenger1

[common/units/equipment/ES_tank_chassis_eng_challenger1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_eng_challenger1.txt)

- Шасси Challenger 1 (`tank_eng_challenger1_equipment`)
- Тяжелая БМП на базе Challenger 1 (`ifv_heavy_eng_challenger1_equipment`)
- БТР на базе Challenger 1 (`apc_tank_eng_challenger1_equipment`)
- ЗРК на базе Challenger 1 (`sp_aa_tank_eng_challenger1_equipment`)
- Мобильный ПТРК на базе Challenger 1 (`sp_atgm_tank_eng_challenger1_equipment`)
- ИМР на базе Challenger 1 (`arv_tank_eng_challenger1_equipment`)
- САУ на базе Challenger 1 (`sp_artillery_tank_eng_challenger1_equipment`)
- Тяжелая САУ на базе Challenger 1 (`sp_heavy_artillery_tank_eng_challenger1_equipment`)
- РСЗО на базе Challenger 1 (`sp_mlrs_tank_eng_challenger1_equipment`)
### ES_tank_chassis_eng_challenger2

[common/units/equipment/ES_tank_chassis_eng_challenger2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_eng_challenger2.txt)

- Шасси Challenger 2 (`tank_eng_challenger2_equipment`)
- Тяжелая БМП на базе Challenger 2 (`ifv_heavy_eng_challenger2_equipment`)
- БТР на базе Challenger 2 (`apc_tank_eng_challenger2_equipment`)
- ЗРК на базе Challenger 2 (`sp_aa_tank_eng_challenger2_equipment`)
- Мобильный ПТРК на базе Challenger 2 (`sp_atgm_tank_eng_challenger2_equipment`)
- ИМР на базе Challenger 2 (`arv_tank_eng_challenger2_equipment`)
- САУ на базе Challenger 2 (`sp_artillery_tank_eng_challenger2_equipment`)
- Тяжелая САУ на базе Challenger 2 (`sp_heavy_artillery_tank_eng_challenger2_equipment`)
- РСЗО на базе Challenger 2 (`sp_mlrs_tank_eng_challenger2_equipment`)
### ES_tank_chassis_eng_chieftain

[common/units/equipment/ES_tank_chassis_eng_chieftain.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_eng_chieftain.txt)

- Шасси Chieftain (`tank_eng_chieftain_equipment`)
- Тяжелая БМП на базе Chieftain (`ifv_heavy_eng_chieftain_equipment`)
- БТР на базе Chieftain (`apc_tank_eng_chieftain_equipment`)
- ЗРК на базе Chieftain (`sp_aa_tank_eng_chieftain_equipment`)
- Мобильный ПТРК на базе Chieftain (`sp_atgm_tank_eng_chieftain_equipment`)
- ИМР на базе Chieftain (`arv_tank_eng_chieftain_equipment`)
- САУ на базе Chieftain (`sp_artillery_tank_eng_chieftain_equipment`)
- Тяжелая САУ на базе Chieftain (`sp_heavy_artillery_tank_eng_chieftain_equipment`)
- РСЗО на базе Chieftain (`sp_mlrs_tank_eng_chieftain_equipment`)
### ES_tank_chassis_fra_amx30

[common/units/equipment/ES_tank_chassis_fra_amx30.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_fra_amx30.txt)

- Шасси AMX-30 (`tank_fra_amx30_equipment`)
- Тяжелая БМП на базе AMX-30 (`ifv_heavy_fra_amx30_equipment`)
- БТР на базе AMX-30 (`apc_tank_fra_amx30_equipment`)
- ЗРК на базе AMX-30 (`sp_aa_tank_fra_amx30_equipment`)
- Мобильный ПТРК на базе AMX-30 (`sp_atgm_tank_fra_amx30_equipment`)
- ИМР на базе AMX-30 (`arv_tank_fra_amx30_equipment`)
- САУ на базе AMX-30 (`sp_artillery_tank_fra_amx30_equipment`)
- Тяжелая САУ на базе AMX-30 (`sp_heavy_artillery_tank_fra_amx30_equipment`)
- РСЗО на базе AMX-30 (`sp_mlrs_tank_fra_amx30_equipment`)
### ES_tank_chassis_fra_leclerc

[common/units/equipment/ES_tank_chassis_fra_leclerc.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_fra_leclerc.txt)

- Шасси Leclerc (`tank_fra_leclerc_equipment`)
- Тяжелая БМП на базе Leclerc (`ifv_heavy_fra_leclerc_equipment`)
- БТР на базе Leclerc (`apc_tank_fra_leclerc_equipment`)
- ЗРК на базе Leclerc (`sp_aa_tank_fra_leclerc_equipment`)
- Мобильный ПТРК на базе Leclerc (`sp_atgm_tank_fra_leclerc_equipment`)
- ИМР на базе Leclerc (`arv_tank_fra_leclerc_equipment`)
- САУ на базе Leclerc (`sp_artillery_tank_fra_leclerc_equipment`)
- Тяжелая САУ на базе Leclerc (`sp_heavy_artillery_tank_fra_leclerc_equipment`)
- РСЗО на базе Leclerc (`sp_mlrs_tank_fra_leclerc_equipment`)
### ES_tank_chassis_ger_leopard1

[common/units/equipment/ES_tank_chassis_ger_leopard1.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ger_leopard1.txt)

- Шасси Leopard 1 (`tank_ger_leopard1_equipment`)
- Тяжелая БМП на базе Leopard 1 (`ifv_heavy_ger_leopard1_equipment`)
- БТР на базе Leopard 1 (`apc_tank_ger_leopard1_equipment`)
- ЗРК на базе Leopard 1 (`sp_aa_tank_ger_leopard1_equipment`)
- Мобильный ПТРК на базе Leopard 1 (`sp_atgm_tank_ger_leopard1_equipment`)
- ИМР на базе Leopard 1 (`arv_tank_ger_leopard1_equipment`)
- САУ на базе Leopard 1 (`sp_artillery_tank_ger_leopard1_equipment`)
- Тяжелая САУ на базе Leopard 1 (`sp_heavy_artillery_tank_ger_leopard1_equipment`)
- РСЗО на базе Leopard 1 (`sp_mlrs_tank_ger_leopard1_equipment`)
### ES_tank_chassis_ger_leopard2

[common/units/equipment/ES_tank_chassis_ger_leopard2.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ger_leopard2.txt)

- Тяжелая БМП на базе Leopard 2 (`ifv_heavy_ger_leopard2_equipment`)
- БТР на базе Leopard 2 (`apc_tank_ger_leopard2_equipment`)
- ЗРК на базе Leopard 2 (`sp_aa_tank_ger_leopard2_equipment`)
- Мобильный ПТРК на базе Leopard 2 (`sp_atgm_tank_ger_leopard2_equipment`)
- ИМР на базе Leopard 2 (`arv_tank_ger_leopard2_equipment`)
- САУ на базе Leopard 2 (`sp_artillery_tank_ger_leopard2_equipment`)
- Тяжелая САУ на базе Leopard 2 (`sp_heavy_artillery_tank_ger_leopard2_equipment`)
- РСЗО на базе Leopard 2 (`sp_mlrs_tank_ger_leopard2_equipment`)
### ES_tank_chassis_ger_leopard2_kf51

[common/units/equipment/ES_tank_chassis_ger_leopard2_kf51.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ger_leopard2_kf51.txt)

- Тяжелая БМП на базе Panther KF51 (`ifv_heavy_ger_kf51_equipment`)
- БТР на базе Panther KF51 (`apc_tank_ger_kf51_equipment`)
- ЗРК на базе Panther KF51 (`sp_aa_tank_ger_kf51_equipment`)
- Мобильный ПТРК на базе Panther KF51 (`sp_atgm_tank_ger_kf51_equipment`)
- ИМР на базе Panther KF51 (`arv_tank_ger_kf51_equipment`)
- САУ на базе Panther KF51 (`sp_artillery_tank_ger_kf51_equipment`)
- Тяжелая САУ на базе Panther KF51 (`sp_heavy_artillery_tank_ger_kf51_equipment`)
- РСЗО на базе Panther KF51 (`sp_mlrs_tank_ger_kf51_equipment`)
### ES_tank_chassis_ita_ariete

[common/units/equipment/ES_tank_chassis_ita_ariete.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ita_ariete.txt)

- Шасси Ariete (`tank_ita_ariete_equipment`)
- Тяжелая БМП на базе Ariete (`ifv_heavy_ita_ariete_equipment`)
- БТР на базе Ariete (`apc_tank_ita_ariete_equipment`)
- ЗРК на базе Ariete (`sp_aa_tank_ita_ariete_equipment`)
- Мобильный ПТРК на базе Ariete (`sp_atgm_tank_ita_ariete_equipment`)
- ИМР на базе Ariete (`arv_tank_ita_ariete_equipment`)
- САУ на базе Ariete (`sp_artillery_tank_ita_ariete_equipment`)
- Тяжелая САУ на базе Ariete (`sp_heavy_artillery_tank_ita_ariete_equipment`)
- РСЗО на базе Ariete (`sp_mlrs_tank_ita_ariete_equipment`)
### ES_tank_chassis_sov_obj640

[common/units/equipment/ES_tank_chassis_sov_obj640.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_obj640.txt)

- БМПТ на базе Об.640 (`bmpt_tank_rus_obj640_equipment`)
- БТР на базе Об.640 (`apc_tank_rus_obj640_equipment`)
- ЗРК на базе Об.640 (`sp_aa_tank_rus_obj640_equipment`)
- Мобильная установка с ПТУР на базе Об.640 (`sp_atgm_tank_rus_obj640_equipment`)
- ИМР на базе Об.640 (`arv_tank_rus_obj640_equipment`)
- САУ на базе Об.640 (`sp_artillery_tank_rus_obj640_equipment`)
- Тяжелая САУ на базе Об.640 (`sp_heavy_artillery_tank_rus_obj640_equipment`)
- РСЗО на базе Об.640 (`sp_mlrs_tank_rus_obj640_equipment`)
- ТОС на базе Об.640 (`sp_tos_tank_rus_obj640_equipment`)
### ES_tank_chassis_sov_t14

[common/units/equipment/ES_tank_chassis_sov_t14.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t14.txt)

- БМПТ на базе Т-14 (`bmpt_tank_rus_t14_equipment`)
- БТР на базе Т-14 (`apc_tank_rus_t14_equipment`)
- ЗРК на базе Т-14 (`sp_aa_tank_rus_t14_equipment`)
- Мобильная установка с ПТУР на базе Т-14 (`sp_atgm_tank_rus_t14_equipment`)
- ИМР на базе Т-14 (`arv_tank_rus_t14_equipment`)
- САУ на базе Т-14 (`sp_artillery_tank_rus_t14_equipment`)
- Тяжелая САУ на базе Т-14 (`sp_heavy_artillery_tank_rus_t14_equipment`)
- РСЗО на базе Т-14 (`sp_mlrs_tank_rus_t14_equipment`)
- ТОС на базе Т-14 (`sp_tos_tank_rus_t14_equipment`)
### ES_tank_chassis_sov_t55

[common/units/equipment/ES_tank_chassis_sov_t55.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t55.txt)

- Шасси Т-54/55 (`tank_sov_t55_equipment`)
- БМПТ на базе Т-54/55 (`bmpt_tank_sov_t55_equipment`)
- БТР на базе Т-54/55 (`apc_tank_sov_t55_equipment`)
- ЗРК на базе Т-54/55 (`sp_aa_tank_sov_t55_equipment`)
- Мобильная установка с ПТУР на базе Т-54/55 (`sp_atgm_tank_sov_t55_equipment`)
- ИМР на базе Т-54/55 (`arv_tank_sov_t55_equipment`)
- САУ на базе Т-54/55 (`sp_artillery_tank_sov_t55_equipment`)
- Тяжелая САУ на базе Т-54/55 (`sp_heavy_artillery_tank_sov_t55_equipment`)
- РСЗО на базе Т-54/55 (`sp_mlrs_tank_sov_t55_equipment`)
- ТОС на базе Т-54/55 (`sp_tos_tank_sov_t55_equipment`)
### ES_tank_chassis_sov_t62

[common/units/equipment/ES_tank_chassis_sov_t62.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t62.txt)

- Шасси Т-62 (`tank_sov_t62_equipment`)
- БМПТ на базе Т-62 (`bmpt_tank_sov_t62_equipment`)
- БТР на базе Т-62 (`apc_tank_sov_t62_equipment`)
- ЗРК на базе Т-62 (`sp_aa_tank_sov_t62_equipment`)
- Мобильная установка с ПТУР на базе Т-62 (`sp_atgm_tank_sov_t62_equipment`)
- ИМР на базе Т-62 (`arv_tank_sov_t62_equipment`)
- САУ на базе Т-62 (`sp_artillery_tank_sov_t62_equipment`)
- Тяжелая САУ на базе Т-62 (`sp_heavy_artillery_tank_sov_t62_equipment`)
- РСЗО на базе Т-62 (`sp_mlrs_tank_sov_t62_equipment`)
- ТОС на базе Т-62 (`sp_tos_tank_sov_t62_equipment`)
### ES_tank_chassis_sov_t64

[common/units/equipment/ES_tank_chassis_sov_t64.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t64.txt)

- БМПТ на базе Т-64 (`bmpt_tank_sov_t64_equipment`)
- БТР на базе Т-64 (`apc_tank_sov_t64_equipment`)
- ЗРК на базе Т-64 (`sp_aa_tank_sov_t64_equipment`)
- Мобильная установка с ПТУР на базе Т-64 (`sp_atgm_tank_sov_t64_equipment`)
- ИМР на базе Т-64 (`arv_tank_sov_t64_equipment`)
- САУ на базе Т-64 (`sp_artillery_tank_sov_t64_equipment`)
- Тяжелая САУ на базе Т-64 (`sp_heavy_artillery_tank_sov_t64_equipment`)
- РСЗО на базе Т-64 (`sp_mlrs_tank_sov_t64_equipment`)
- ТОС на базе Т-64 (`sp_tos_tank_sov_t64_equipment`)
### ES_tank_chassis_sov_t72

[common/units/equipment/ES_tank_chassis_sov_t72.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t72.txt)

- БМПТ на базе Т-72 (`bmpt_tank_sov_t72_equipment`)
- БТР на базе Т-72 (`apc_tank_sov_t72_equipment`)
- ЗРК на базе Т-72 (`sp_aa_tank_sov_t72_equipment`)
- Мобильная установка с ПТУР на базе Т-72 (`sp_atgm_tank_sov_t72_equipment`)
- ИМР на базе Т-72 (`arv_tank_sov_t72_equipment`)
- САУ на базе Т-72 (`sp_artillery_tank_sov_t72_equipment`)
- Тяжелая САУ на базе Т-72 (`sp_heavy_artillery_tank_sov_t72_equipment`)
- РСЗО на базе Т-72 (`sp_mlrs_tank_sov_t72_equipment`)
- ТОС на базе Т-72 (`sp_tos_tank_sov_t72_equipment`)
### ES_tank_chassis_sov_t80

[common/units/equipment/ES_tank_chassis_sov_t80.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t80.txt)

- БМПТ на базе Т-80 (`bmpt_tank_sov_t80_equipment`)
- БТР на базе Т-80 (`apc_tank_sov_t80_equipment`)
- ЗРК на базе Т-80 (`sp_aa_tank_sov_t80_equipment`)
- Мобильная установка с ПТУР на базе Т-80 (`sp_atgm_tank_sov_t80_equipment`)
- ИМР на базе Т-80 (`arv_tank_sov_t80_equipment`)
- САУ на базе Т-80 (`sp_artillery_tank_sov_t80_equipment`)
- Тяжелая САУ на базе Т-80 (`sp_heavy_artillery_tank_sov_t80_equipment`)
- РСЗО на базе Т-80 (`sp_mlrs_tank_sov_t80_equipment`)
- ТОС на базе Т-80 (`sp_tos_tank_sov_t80_equipment`)
### ES_tank_chassis_sov_t84

[common/units/equipment/ES_tank_chassis_sov_t84.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t84.txt)

- БМПТ на базе Т-84 (`bmpt_tank_ukr_t84_equipment`)
- БТР на базе Т-84 (`apc_tank_ukr_t84_equipment`)
- ЗРК на базе Т-84 (`sp_aa_tank_ukr_t84_equipment`)
- Мобильная установка с ПТУР на базе Т-84 (`sp_atgm_tank_ukr_t84_equipment`)
- ИМР на базе Т-84 (`arv_tank_ukr_t84_equipment`)
- САУ на базе Т-84 (`sp_artillery_tank_ukr_t84_equipment`)
- Тяжелая САУ на базе Т-84 (`sp_heavy_artillery_tank_ukr_t84_equipment`)
- РСЗО на базе Т-84 (`sp_mlrs_tank_ukr_t84_equipment`)
- ТОС на базе Т-84 (`sp_tos_tank_ukr_t84_equipment`)
### ES_tank_chassis_sov_t90

[common/units/equipment/ES_tank_chassis_sov_t90.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_sov_t90.txt)

- БМПТ на базе Т-90 (`bmpt_tank_rus_t90_equipment`)
- БТР на базе Т-90 (`apc_tank_rus_t90_equipment`)
- ЗРК на базе Т-90 (`sp_aa_tank_rus_t90_equipment`)
- Мобильная установка с ПТУР на базе Т-90 (`sp_atgm_tank_rus_t90_equipment`)
- ИМР на базе Т-90 (`arv_tank_rus_t90_equipment`)
- САУ на базе Т-90 (`sp_artillery_tank_rus_t90_equipment`)
- Тяжелая САУ на базе Т-90 (`sp_heavy_artillery_tank_rus_t90_equipment`)
- РСЗО на базе Т-90 (`sp_mlrs_tank_rus_t90_equipment`)
- ТОС на базе Т-90 (`sp_tos_tank_rus_t90_equipment`)
### ES_tank_chassis_ukr_obj477

[common/units/equipment/ES_tank_chassis_ukr_obj477.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_ukr_obj477.txt)

- БМПТ на базе Объект 477 (`bmpt_tank_ukr_obj477_equipment`)
- БТР на базе Объект 477 (`apc_tank_ukr_obj477_equipment`)
- ЗРК на базе Объект 477 (`sp_aa_tank_ukr_obj477_equipment`)
- Мобильная установка с ПТУР на базе Объект 477 (`sp_atgm_tank_ukr_obj477_equipment`)
- ИМР на базе Объект 477 (`arv_tank_ukr_obj477_equipment`)
- САУ на базе Объект 477 (`sp_artillery_tank_ukr_obj477_equipment`)
- Тяжелая САУ на базе Объект 477 (`sp_heavy_artillery_tank_ukr_obj477_equipment`)
- РСЗО на базе Объект 477 (`sp_mlrs_tank_ukr_obj477_equipment`)
- ТОС на базе Объект 477 (`sp_tos_tank_ukr_obj477_equipment`)
### ES_tank_chassis_usa_m48patton

[common/units/equipment/ES_tank_chassis_usa_m48patton.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_usa_m48patton.txt)

- Шасси M48 Patton (`tank_usa_m48patton_equipment`)
- Тяжелая БМП на базе M48 Patton (`ifv_heavy_usa_m48patton_equipment`)
- БТР на базе M48 Patton (`apc_tank_usa_m48patton_equipment`)
- ЗРК на базе M48 Patton (`sp_aa_tank_usa_m48patton_equipment`)
- Мобильный ПТРК на базе M48 Patton (`sp_atgm_tank_usa_m48patton_equipment`)
- ИМР на базе M48 Patton (`arv_tank_usa_m48patton_equipment`)
- САУ на базе M48 Patton (`sp_artillery_tank_usa_m48patton_equipment`)
- Тяжелая САУ на базе M48 Patton (`sp_heavy_artillery_tank_usa_m48patton_equipment`)
- РСЗО на базе M48 Patton (`sp_mlrs_tank_usa_m48patton_equipment`)
### ES_tank_chassis_usa_m60patton

[common/units/equipment/ES_tank_chassis_usa_m60patton.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_usa_m60patton.txt)

- Шасси M60 Patton (`tank_usa_m60patton_equipment`)
- Тяжелая БМП на базе M60 Patton (`ifv_heavy_usa_m60patton_equipment`)
- БТР на базе M60 Patton (`apc_tank_usa_m60patton_equipment`)
- ЗРК на базе M60 Patton (`sp_aa_tank_usa_m60patton_equipment`)
- Мобильный ПТРК на базе M60 Patton (`sp_atgm_tank_usa_m60patton_equipment`)
- ИМР на базе M60 Patton (`arv_tank_usa_m60patton_equipment`)
- САУ на базе M60 Patton (`sp_artillery_tank_usa_m60patton_equipment`)
- Тяжелая САУ на базе M60 Patton (`sp_heavy_artillery_tank_usa_m60patton_equipment`)
- РСЗО на базе M60 Patton (`sp_mlrs_tank_usa_m60patton_equipment`)
### ES_tank_chassis_usa_m60patton_abrams

[common/units/equipment/ES_tank_chassis_usa_m60patton_abrams.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_tank_chassis_usa_m60patton_abrams.txt)

- Шасси M1 Abrams (`tank_usa_abrams_equipment`)
- БТР на базе M1 Abrams (`apc_tank_usa_abrams_equipment`)
- ЗРК на базе M1 Abrams (`sp_aa_tank_usa_abrams_equipment`)
- Мобильный ПТРК на базе M1 Abrams (`sp_atgm_tank_usa_abrams_equipment`)
- ИМР на базе M1 Abrams (`arv_tank_usa_abrams_equipment`)
- САУ на базе M1 Abrams (`sp_artillery_tank_usa_abrams_equipment`)
- Тяжелая САУ на базе M1 Abrams (`sp_heavy_artillery_tank_usa_abrams_equipment`)
- РСЗО на базе M1 Abrams (`sp_mlrs_tank_usa_abrams_equipment`)
### ES_uifv_chassis_nto_atlas

[common/units/equipment/ES_uifv_chassis_nto_atlas.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_uifv_chassis_nto_atlas.txt)

- Шасси Atlas (`uifv_atlas_equipment`)
- Шасси RCV (`uifv_RCV_equipment`)
### ES_uifv_chassis_rus_uran

[common/units/equipment/ES_uifv_chassis_rus_uran.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/equipment/ES_uifv_chassis_rus_uran.txt)

- Шасси Уран-9 (`uifv_uran9_equipment`)

## 5. Все 87 подразделений: общие и страновые кандидаты

Ниже перечислены кандидаты, а не имитация внутреннего порядка выбора движка. Разные определения одной entity и модели по ID подразделения могут менять результат.

### Рота на БТР (`apc`)

Sprite: `apc`. [common/units/apc.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/apc.txt)

- `UKR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/geo_btr4mv_UKR.mesh`
- `RUS_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `DPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `LPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `BLR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `WGN_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `PMR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
### Артиллерийский дивизион поддержки (`artillery`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### САУ Поддержки (`support_spa`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### РСЗО Поддержки (`support_mlrs`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### Тяжелая САУ Поддержки (`support_heavy_spa`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### ТОС Поддержки (`support_tos`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### Минометный расчет (`mortar`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### Самоходный ПТРК поддержки (`sp_support_atgm`)

Sprite: `2s7pion`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `2s7pion_entity`: Модель из мода; `gfx/models/units/tanks/2s7pion_n_n.mesh`
### Расчет ПТРК (`atgm`)

Sprite: `artillery`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `artillery_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `ROM_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `POL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LIT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `LAT_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `BEL_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `SLO_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `AST_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `CZE_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
- `HUN_artillery_entity`: Ванильная модель; `gfx/models/buildings/artillery_frame.mesh (identical to base game)`
### Рота поддержки на легких танках (`light_support_tank_sov`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота поддержки на легких танках (`light_support_tank_nto`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Средний ЗРК (`sp_aa`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Инженерный взвод (`engineer`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Тяжелый инженерный взвод (`engineer_heavy`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Полевой госпиталь (`field_hospital`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Взвод обеспечения (`logistics_company`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Ремонтный взвод (`maintenance_company`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Тяжелый ремонтный взвод (`heavy_maintenance_company`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Взвод связи (`signal_company`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Взвод снайперов (`sniper`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Отряд дроноводов (`fpv_team`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Взвод разведчиков на БРДМ (`recon`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на советских БМП (`recon_ifv_sov`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на американских БМП (`recon_ifv_usa`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на тяжелых БМП (`recon_ifv_heavy_sov`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на тяжелых БМП НАТО (`recon_ifv_heavy_nto`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на БТР (`armored_recon`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на БМД (`afv_recon`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на ББМ (`imv_recon`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведгруппа на машинах (`imv_light_recon`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Военная полиция (`military_police`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### command (`command`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Пехотная КШМ (`command_inf`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Артиллерийская КШМ (`command_spa`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Танковая КШМ (`command_tank`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### unnamed_vehicle_support (`unnamed_vehicle_support`)

Sprite: `apc`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `UKR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/geo_btr4mv_UKR.mesh`
- `RUS_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `DPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `LPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `BLR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `WGN_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `PMR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
### lancet (`lancet`)

Sprite: `infantry`. [common/units/companies.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/companies.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Персонал штаба (`hq_support`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Персонал инженеров (`hq_engineer`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Разведывательный персонал БПЛА (`hq_drone_recon`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Персонал планового обслуживания (`hq_maintenance`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Медицинский персонал (`hq_field_hospital`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Персонал логистики и обслуживания (`hq_logistics`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Персонал сигнальщиков и разведчиков (`hq_signal`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Передовой авиадиспетчер (`hq_air_liaison`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Координация специальных операций (`hq_sso`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Координация ударов артиллерии (`hq_arty`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Координация применения танков (`hq_tank`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Пехотная охрана штаба на ББM (`hq_imv`)

Sprite: `infantry`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Охрана штаба на БТР (`hq_apc`)

Sprite: `apc`. [common/units/hq.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/hq.txt)

- `UKR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/geo_btr4mv_UKR.mesh`
- `RUS_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `DPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `LPR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `BLR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `WGN_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
- `PMR_apc_entity`: Модель из мода; `gfx/models/units/vehicles/btr82.mesh`
### Рота советских БМП (`ifv_sov`)

Sprite: `ifv_sov`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `RUS_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `BLR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `DPR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `ROM_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `LIT_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CZE_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `SLO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `HUN_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CRO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `UKR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/geo_bmp2_UKR.mesh`
### unnamed_vehicle (`unnamed_vehicle`)

Sprite: `ifv_sov`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `RUS_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `BLR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `DPR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `ROM_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `LIT_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CZE_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `SLO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `HUN_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CRO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `UKR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/geo_bmp2_UKR.mesh`
### Рота советских БМД (`afv_sov`)

Sprite: `infantry`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_afv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/geo_bmp1_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота американских БМП (`ifv_usa`)

Sprite: `BMP_nato`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `BMP_nato_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
- `ifv_usa_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `POL_ifv_usa_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
- `LIT_ifv_usa_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
- `ROM_ifv_usa_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
- `UKR_ifv_usa_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
### Рота немецких БМП (`ifv_ger`)

Sprite: `ifv_ger`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `ifv_ger_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
### Рота британских БМП (`ifv_eng`)

Sprite: `ifv_eng`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `ifv_eng_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
### Рота французких БМП (`ifv_fra`)

Sprite: `ifv_fra`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `ifv_fra_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
### Рота итальянских БМП (`ifv_ita`)

Sprite: `ifv_ita`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

Кандидаты не найдены.
### Рота шведских БМП (`ifv_swe`)

Sprite: `ifv_swe`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `ifv_swe_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
### Рота БМПТ (`bmpt`)

Sprite: `infantry`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_bmpt_entity`: Модель из мода; `gfx/models/units/tanks/geo_t72amt_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `RUS_bmpt_entity`: Модель из мода; `gfx/models/units/tanks/t80.mesh`
### Рота советских тяжелых БМП (`ifv_heavy_sov`)

Sprite: `ifv_sov`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `RUS_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `BLR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `DPR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `ROM_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `LIT_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CZE_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `SLO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `HUN_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `CRO_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/bmp2.mesh`
- `UKR_ifv_sov_entity`: Модель из мода; `gfx/models/units/vehicles/geo_bmp2_UKR.mesh`
### Рота западных тяжелых БМП (`ifv_heavy_nto`)

Sprite: `BMP_nato`. [common/units/ifv.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/ifv.txt)

- `BMP_nato_entity`: Модель из мода; `gfx/models/units/vehicles/m2_bradley.mesh`
### Рота пехотинцев (`infantry`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота морских пехотинцев (`marine`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `BEL_marine_entity`: Ванильная модель; `gfx/models/units/special_forces/BEL_marine.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `NTO_marine_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_marine_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_SF.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `RUS_marine_entity`: Модель из мода; `gfx/models/units/RUS_marine.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота горнострелков (`mountaineers`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `BEL_mountaineers_entity`: Ванильная модель; `gfx/models/units/special_forces/BEL_mountaineers.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `NTO_mountaineers_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_mountaineers_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_SF.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота десантников (`paratrooper`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `BEL_paratrooper_entity`: Ванильная модель; `gfx/models/units/special_forces/BEL_paratrooper.mesh`
- `HUN_paratrooper_entity`: Ванильная модель; `gfx/models/units/special_forces/HUN_paratrooper.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_paratrooper_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_SF.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота ТРО (`opolchenie`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `POL_opolchenie_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `UKR_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCH_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `ISI_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_opolchenie_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SKL_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `AST_opolchenie_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_opolchenie_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота заключённых (`prisoners`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота ЧВК Вагнер (`PMC_wagner`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_PMC_wagner_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота штурмовой пехоты (`assault_infantry`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Рота спецназа (`spetsnaz`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCH_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `ISI_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_spetsnaz_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SKL_spetsnaz_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `AST_spetsnaz_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_spetsnaz_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_spetsnaz_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_spetsnaz_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_spetsnaz_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `RUS_spetsnaz_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `WGN_spetsnaz_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `LPR_spetsnaz_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_spetsnaz_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Пограничники (`border_guard`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `border_guard_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Северокорейская Штурмовая пехота (`dprk_assault_infantry`)

Sprite: `infantry`. [common/units/infantry.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/infantry.txt)

- `infantry_entity`: Ванильная модель; `gfx/models/units/western_european_infantry.mesh`
- `ROM_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `POL_infantry_entity`: Ссылка на отсутствующую entity; `entity Stryker_entity not found`
- `BUL_infantry_entity`: Ванильная модель; `gfx/models/units/bfb_BUL_infantry.mesh`
- `LIT_infantry_entity`: Модель из мода; `gfx/models/units/stryker/stryker.mesh`
- `LAT_infantry_entity`: Ванильная модель; `gfx/models/units/LAT_infantry.mesh`
- `BEL_infantry_entity`: Ванильная модель; `gfx/models/units/infantry/BEL_infantry.mesh`
- `SLO_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `AST_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CZE_infantry_entity`: Ванильная модель; `gfx/models/units/CZE_infantry.mesh`
- `HUN_infantry_entity`: Ванильная модель; `gfx/models/units/HUN_infantry.mesh`
- `NTO_infantry_entity`: Ванильная модель; `gfx/models/units/ROM_infantry.mesh`
- `UKR_infantry_entity`: Модель из мода; `gfx/models/units/vehicles/geo_m1151_UKR.mesh`
- `VCH_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VDG_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VNO_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `VCU_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/CHE_MDinfantry.mesh`
- `ISI_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `HAR_infantry_entity`: Модель из мода; `gfx/models/units/CAUCAS/ISI_MDinfantry_2.mesh`
- `SKL_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SDG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `ING_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `SCR_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `DRG_infantry_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`
- `RUS_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `WGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_wagner.mesh`
- `LPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DPR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHE_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `DGN_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KLM_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `STA_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `NOO_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CHR_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `CBL_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
- `KUB_infantry_entity`: Модель из мода; `gfx/models/units/RUS_infantry.mesh`
### Тяжелая артиллерия (`sp_heavy_art`)

Sprite: `2s7pion`. [common/units/sp_art.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/sp_art.txt)

- `2s7pion_entity`: Модель из мода; `gfx/models/units/tanks/2s7pion_n_n.mesh`
- `sp_heavy_art_entity`: Модель из мода; `gfx/models/units/tanks/2s7pion_n_n.mesh`
### Артиллерийский дивизион (`towed_art`)

Sprite: `2s7pion`. [common/units/sp_art.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/sp_art.txt)

- `2s7pion_entity`: Модель из мода; `gfx/models/units/tanks/2s7pion_n_n.mesh`
- `towed_art_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
### САУ (`sp_art`)

Sprite: ``. [common/units/sp_art.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/sp_art.txt)

- `sp_art_entity`: Модель из мода; `gfx/models/units/tanks/2s3.mesh`
### TOS (`TOS`)

Sprite: `TOS`. [common/units/sp_art.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/sp_art.txt)

- `TOS_entity`: Модель из мода; `gfx/models/units/tanks/2s3.mesh`
### РСЗО (`MRLS`)

Sprite: `MRLS`. [common/units/sp_art.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/sp_art.txt)

- `MRLS_entity`: Модель из мода; `gfx/models/units/tanks/2s3.mesh`
### Рота советских танков (`tank_sov`)

Sprite: `tank_sov`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `UKR_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/geo_t64bm_UKR.mesh`
- `WGN_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t80.mesh`
- `RUS_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
- `DPR_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
- `LPR_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
- `BLR_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
- `PMR_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
- `POL_tank_sov_entity`: Модель из мода; `gfx/models/units/tanks/t72b3.mesh`
### Рота американских танков (`tank_usa`)

Sprite: `tank_usa`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `tank_usa_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
- `POL_tank_usa_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
### Рота немецких танков (`tank_ger`)

Sprite: `tank_ger`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `tank_ger_entity`: Модель из мода; `gfx/models/units/tanks/leopard2a5.mesh`
- `POL_tank_ger_entity`: Модель из мода; `gfx/models/units/tanks/leopard2a5.mesh`
- `LIT_tank_ger_entity`: Модель из мода; `gfx/models/units/tanks/leopard2a5.mesh`
### Рота британских танков (`tank_eng`)

Sprite: `tank_eng`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `tank_eng_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
### Рота французких танков (`tank_fra`)

Sprite: `tank_fra`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `tank_fra_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
### Рота итальянских танков (`tank_ita`)

Sprite: `tank_ita`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `tank_ita_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
### Рота советских легких танков (`light_tank_sov`)

Sprite: `light_tank_sov`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

Кандидаты не найдены.
### Рота западных легких танков (`light_tank_nto`)

Sprite: `light_tank_nto`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `light_tank_nto_entity`: Модель из мода; `gfx/models/units/tanks/m1_abrams.mesh`
### Самоходный ПТРК (`sp_atgm`)

Sprite: `sp_atgm`. [common/units/tank.txt](C:/Users/ksyx7/OneDrive/Documents/GitHub/East-Showdown/common/units/tank.txt)

- `sp_atgm_entity`: Модель из мода; `gfx/models/units/tanks/2s1.mesh`
- `UKR_sp_atgm_entity`: Модель из мода; `gfx/models/units/geo_infantry_UKR_ttsko.mesh`

## 6. Общие модели мода, подставленные другой технике

Эти 30 записей не отнесены к отсутствующим или ванильным. Но наличие модели не означает соответствия внешнему виду конкретного образца. Например, БМД используют общую 2С1, а часть ПТРК — 2С7 или 2С3.

- Шасси БМД-1 (`afv_sov_bmd1_equipment`) → `gfx/models/units/tanks/2s1.mesh`
- Шасси БМД-2 (`afv_sov_bmd2_equipment`) → `gfx/models/units/tanks/2s1.mesh`
- Шасси БМД-3 (`afv_sov_bmd3_equipment`) → `gfx/models/units/tanks/2s1.mesh`
- Шасси БМД-4 (`afv_rus_bmd4_equipment`) → `gfx/models/units/tanks/2s1.mesh`
- M114 (`usa_artillery_m114_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- M102 (`usa_artillery_m102_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- M198 (`usa_artillery_m198_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- M119 (`usa_artillery_m119_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- M777 (`usa_artillery_m777_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- 2a88 (`rus_artillery_2a88_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- 2П22 «Богдана» (`ukr_artillery_2p22_bohdana_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- ПТРК \"Шершень\" (`atgm_shershen_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК Spike (`pol_atgm_spike_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- ПТРК Jack s (`pol_atgm_jacks_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- ПТРК \"Малютка\" (`atgm_9k11_malutka_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК \"Фагот\" (`atgm_9k111_fagot_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- 9К111-1\"Конкурс\" (`atgm_9k111_1_konkurs_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- 9К115 \"Метис\" (`atgm_9k115_metis_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- 9К135 \"Корнет\" (`atgm_9k135_kornet_equipment`) → `gfx/models/units/tanks/2s3.mesh`
- ПТРК «Скиф» (`infantry_atgm_skif_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК «Стугна» (`infantry_atgm_stugna_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК «Барьер» (`infantry_atgm_barier_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК «Альта» (`infantry_atgm_alta_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- ПТРК «Корсар» (`infantry_atgm_korsar_equipment`) → `gfx/models/units/tanks/2s7pion_n_n.mesh`
- Шасси Об.640 (`tank_rus_obj640_equipment`) → `gfx/models/units/tanks/t80.mesh`
- Шасси Т-14 (`tank_rus_t14_equipment`) → `gfx/models/units/tanks/t90m.mesh`
- Шасси Т-80 (`tank_sov_t80_equipment`) → `gfx/models/units/tanks/t80.mesh`
- Шасси Т-84 (`tank_ukr_t84_equipment`) → `gfx/models/units/tanks/t80.mesh`
- Шасси Т-90 (`tank_rus_t90_equipment`) → `gfx/models/units/tanks/t90m.mesh`
- Объект 477 (`tank_ukr_obj477_equipment`) → `gfx/models/units/tanks/t80.mesh`
