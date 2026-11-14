# Калибр 3М14
Внешняя игровая модель по предоставленным референсам. 4026 треугольников.
Экспорт и материалы основаны на генераторе Х-55; геометрия создана отдельно.
Готовые mesh, DDS с mipmaps и idle.anim находятся в gfx/models/units/missiles/kalibr.
Привязка: rus_medium_guided_missile_kalibr → rus_kalibr → rus_kalibr_entity.
Масштаб entity 0.60, как у Х-55. Нос -Z, вертикаль Y.
Исходник: kalibr.obj + kalibr.mtl + kalibr_diffuse.png.
Пересборка: python tools/kalibr/build_kalibr.py
Рендер: python tools/kalibr/render_kalibr.py
Проверены геометрия, нормали, UV, DDS, анимация и связь с оборудованием.
Проверка полёта непосредственно в HOI4 не проводилась.
