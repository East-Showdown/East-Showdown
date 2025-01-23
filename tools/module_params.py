import re

file_path = r"C:\Users\ksyx7\Documents\GitHub\East-Showdown\common\units\equipment\modules\ES_tank_modules_all.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

def divide_soft_attack(match):
    value = float(match.group(1))
    new_value = value / 2
    return f"soft_attack = {new_value:.2f}"

updated_content = re.sub(r'soft_attack = (\d+(\.\d+)?)', divide_soft_attack, content)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Значения изменены и сохранены.")
