def calculate_hp(base_hp, material_coef, construction_coef, state_coef):
    return base_hp * material_coef * construction_coef * state_coef

base_hp_map = {
    "малый мост": 100.0,
    "средний мост": 300.0,
    "большой мост": 400.0,
    "очень большой мост": 500.0,
    "дамба малая": 600.0,
    "дамба средняя": 800.0,
    "дамба крупная": 1200.0
}

material_coef_map = {
    "железобетон/сталь": 1.2,
    "бетон средний возраст": 1.0,
    "камень старый": 0.8,
    "смешанный": 0.9
}

construction_coef_map = {
    "арочный мост": 1.3,
    "балочный мост": 1.0,
    "вантовый мост": 0.8,
    "дамба гравитационная": 1.2,
    "дамба арочно-гравитационная": 1.3,
    "дамба насыпная": 0.7
}

state_coef_map = {
    "новый или реконструирован": 1.0,
    "средний возраст": 0.95,
    "старый": 0.9,
    "очень старый": 0.8,
    "аварийное": 0.4
}

base_hp = base_hp_map["средний мост"]
material_coef = material_coef_map["железобетон/сталь"]
construction_coef = construction_coef_map["балочный мост"]
state_coef = state_coef_map["очень старый"]

total_hp = calculate_hp(base_hp, material_coef, construction_coef, state_coef)

print(f"Общая прочность (HP) объекта: {total_hp}")