#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║  HOI4 Localization Tool - Russian/Ukrainian to English        ║
║                                                               ║
║  Created by: iAmScienceMan                                    ║
║  Originally made for: East-Showdown                           ║
║  License: EPL 2.0 (Eclipse Public License 2.0)                ║
║                                                               ║
║  Femboys rule the world                                       ║
╚═══════════════════════════════════════════════════════════════╝

Інструмент для локалізації модів HOI4.
Порівнює російську та англійську локалізацію, знаходить відсутні переклади
та генерує файли для перекладачів.

Tool for HOI4 mod localization.
Compares Russian and English localization, finds missing translations
and generates files for translators.
"""

__author__ = "iAmScienceMan"
__project__ = "East-Showdown"
__version__ = "1.1.0"
__license__ = "EPL-2.0"
__credits__ = "iAmScienceMan"
__motto__ = "Femboys rule the world"

import os
import sys
import re
import shutil
from pathlib import Path
from datetime import datetime

# Увімкнення ANSI кольорів на Windows 10+ / Enable ANSI colors on Windows 10+
if sys.platform == 'win32':
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

# Перехід до директорії скрипта (виправлення для Windows)
# Change to script directory (Windows fix)
script_dir = os.path.dirname(os.path.abspath(__file__))
try:
    os.chdir(script_dir)
except Exception as e:
    print(f"CRITICAL ERROR: Cannot change to script directory: {e}")
    print("Make sure to run this script from the localisation/ folder.")
    input("Press Enter to exit...")
    sys.exit(1)

# Константи директорій / Directory constants
RUSSIAN_DIR = "./russian"
ENGLISH_DIR = "./english"
TEMP_DIR = "./temp"
WIP_DIR = "./wip"
REPORT_FILE = "localization_report.txt"


# ANSI коди кольорів / ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'


# Російський інтерфейс / Russian UI
UI_RU = {
    'check_header': 'Проверка полноты локализации',
    'create_header': 'Создание файлов для перевода',
    'error_source_dir': 'Ошибка: исходная директория не найдена по пути',
    'error_target_dir': 'Ошибка: целевая директория не найдена по пути',
    'error_missing_keys': 'Ошибка: сначала запустите скрипт проверки локализации!',
    'error_no_temp_file': 'не найден',
    'step1_merge': '[1] Объединение всех ключей из каждой локали в отдельные файлы...',
    'processing_source': 'Обработка исходных файлов',
    'processing_target': 'Обработка целевых файлов',
    'processed_source': '✓ Обработано исходных файлов:',
    'processed_target': '✓ Обработано целевых файлов:',
    'step2_compare': '[2] Сравнение ключей между локалями...',
    'unique_source': 'Уникальных ключей в источнике:',
    'unique_target': 'Уникальных ключей в цели:',
    'all_keys_present': '✓ Все ключи источника присутствуют в целевой локализации!',
    'localization_complete': 'Локализация завершена на 100%!',
    'missing_keys_found': '✗ Найдены отсутствующие ключи в целевой локализации:',
    'completion': 'Завершенность целевой локализации:',
    'step3_search': '[3] Поиск отсутствующих ключей по файлам и создание отчета...',
    'summary': 'Итоги',
    'localization_completion': 'Завершенность локализации:',
    'missing_keys': 'Отсутствующих ключей:',
    'report_saved': 'Детальный отчет сохранен в:',
    'temp_saved': 'Временные файлы сохранены в:',
    'file': 'Файл:',
    'missing_in_file': 'Отсутствующих ключей:',
    'path_original': 'Путь к оригиналу:',
    'path_translation': 'Путь к переводу:',
    'creating_wip': 'Создание файлов с отсутствующими ключами...',
    'created': 'Создан:',
    'files_created': 'Создано файлов:',
    'total_keys': 'Всего ключей для перевода:',
    'files_location': 'Файлы находятся в директории:',
    'instructions': 'Инструкция:',
    'instruction1': f'1. Откройте файлы в {WIP_DIR}',
    'instruction2_rus_eng': '2. Переведите русские значения на английский',
    'instruction2_eng_rus': '2. Переведите английские значения на русский',
    'instruction3_rus_eng': '3. Скопируйте содержимое в соответствующие файлы в ./english/',
    'instruction3_eng_rus': '3. Скопируйте содержимое в соответствующие файлы в ./russian/',
    'cleaning_wip': f'Очистка существующей директории {WIP_DIR}...',
    'select_function': 'Выберите функцию:',
    'option_check': '1. Проверка (Check) - проверить полноту локализации',
    'option_create': '2. Создание (Create) - создать файлы для перевода',
    'option_both': '3. Оба (Both) - сначала проверка, затем создание',
    'select_direction': 'Выберите направление сравнения:',
    'direction_rus_eng': '1. RUS → ENG - найти ключи, отсутствующие в английском',
    'direction_eng_rus': '2. ENG → RUS - найти ключи, отсутствующие в русском',
}

# Український інтерфейс / Ukrainian UI
UI_UA = {
    'check_header': 'Перевірка повноти локалізації',
    'create_header': 'Створення файлів для перекладу',
    'error_source_dir': 'Помилка: вихідна директорія не знайдена за адресою',
    'error_target_dir': 'Помилка: цільова директорія не знайдена за адресою',
    'error_missing_keys': 'Помилка: спочатку запустіть скрипт перевірки локалізації!',
    'error_no_temp_file': 'не знайдено',
    'step1_merge': "[1] Об'єднання всіх ключів з кожної локалі в окремі файли...",
    'processing_source': 'Обробка вихідних файлів',
    'processing_target': 'Обробка цільових файлів',
    'processed_source': '✓ Оброблено вихідних файлів:',
    'processed_target': '✓ Оброблено цільових файлів:',
    'step2_compare': '[2] Порівняння ключів між локалями...',
    'unique_source': 'Унікальних ключів у джерелі:',
    'unique_target': 'Унікальних ключів у цілі:',
    'all_keys_present': '✓ Всі ключі джерела присутні в цільовій локалізації!',
    'localization_complete': 'Локалізація завершена на 100%!',
    'missing_keys_found': '✗ Знайдено відсутніх ключів у цільовій локалізації:',
    'completion': 'Завершеність цільової локалізації:',
    'step3_search': '[3] Пошук відсутніх ключів у файлах та створення звіту...',
    'summary': 'Підсумок',
    'localization_completion': 'Завершеність локалізації:',
    'missing_keys': 'Відсутніх ключів:',
    'report_saved': 'Детальний звіт збережено в:',
    'temp_saved': 'Тимчасові файли збережено в:',
    'file': 'Файл:',
    'missing_in_file': 'Відсутніх ключів:',
    'path_original': 'Шлях до оригіналу:',
    'path_translation': 'Шлях до перекладу:',
    'creating_wip': 'Створення файлів з відсутніми ключами...',
    'created': 'Створено:',
    'files_created': 'Створено файлів:',
    'total_keys': 'Всього ключів для перекладу:',
    'files_location': 'Файли знаходяться в директорії:',
    'instructions': 'Інструкція:',
    'instruction1': f'1. Відкрийте файли в {WIP_DIR}',
    'instruction2_rus_eng': '2. Перекладіть російські значення на англійську',
    'instruction2_eng_rus': '2. Перекладіть англійські значення на російську',
    'instruction3_rus_eng': '3. Скопіюйте вміст у відповідні файли в ./english/',
    'instruction3_eng_rus': '3. Скопіюйте вміст у відповідні файли в ./russian/',
    'cleaning_wip': f'Очищення існуючої директорії {WIP_DIR}...',
    'select_function': 'Оберіть функцію:',
    'option_check': '1. Перевірка (Check) - перевірити повноту локалізації',
    'option_create': '2. Створення (Create) - створити файли для перекладу',
    'option_both': '3. Обидва (Both) - спочатку перевірка, потім створення',
    'select_direction': 'Оберіть напрямок порівняння:',
    'direction_rus_eng': '1. RUS → ENG - знайти ключі, відсутні в англійській',
    'direction_eng_rus': '2. ENG → RUS - знайти ключі, відсутні в російській',
}

# Англійський інтерфейс / English UI
UI_EN = {
    'check_header': 'Localization Completeness Check',
    'create_header': 'Creating Translation Files',
    'error_source_dir': 'Error: source directory not found at',
    'error_target_dir': 'Error: target directory not found at',
    'error_missing_keys': 'Error: run the localization check script first!',
    'error_no_temp_file': 'not found',
    'step1_merge': '[1] Merging all keys from each locale into separate files...',
    'processing_source': 'Processing source files',
    'processing_target': 'Processing target files',
    'processed_source': '✓ Processed source files:',
    'processed_target': '✓ Processed target files:',
    'step2_compare': '[2] Comparing keys between locales...',
    'unique_source': 'Unique source keys:',
    'unique_target': 'Unique target keys:',
    'all_keys_present': '✓ All source keys are present in target localization!',
    'localization_complete': 'Localization is 100% complete!',
    'missing_keys_found': '✗ Missing keys found in target localization:',
    'completion': 'Target localization completion:',
    'step3_search': '[3] Searching for missing keys in files and creating report...',
    'summary': 'Summary',
    'localization_completion': 'Localization completion:',
    'missing_keys': 'Missing keys:',
    'report_saved': 'Detailed report saved to:',
    'temp_saved': 'Temporary files saved to:',
    'file': 'File:',
    'missing_in_file': 'Missing keys:',
    'path_original': 'Path to source:',
    'path_translation': 'Path to target:',
    'creating_wip': 'Creating files with missing keys...',
    'created': 'Created:',
    'files_created': 'Files created:',
    'total_keys': 'Total keys to translate:',
    'files_location': 'Files are located in:',
    'instructions': 'Instructions:',
    'instruction1': f'1. Open files in {WIP_DIR}',
    'instruction2_rus_eng': '2. Translate Russian values to English',
    'instruction2_eng_rus': '2. Translate English values to Russian',
    'instruction3_rus_eng': '3. Copy contents to corresponding files in ./english/',
    'instruction3_eng_rus': '3. Copy contents to corresponding files in ./russian/',
    'cleaning_wip': f'Cleaning existing {WIP_DIR} directory...',
    'select_function': 'Select function:',
    'option_check': '1. Check - verify localization completeness',
    'option_create': '2. Create - generate translation files',
    'option_both': '3. Both - check first, then create',
    'select_direction': 'Select comparison direction:',
    'direction_rus_eng': '1. RUS → ENG - find keys missing in English',
    'direction_eng_rus': '2. ENG → RUS - find keys missing in Russian',
}


def _get_credits_line():
    """Генерує рядок кредитів / Generates credits line"""
    return f"Generated by {__author__}'s tool | {__project__} | {__motto__}"


def _show_credits_banner():
    """Показує банер з кредитами / Shows credits banner"""
    print("=" * 65)
    print(f"  HOI4 Localization Tool v{__version__}")
    print(f"  Created by: {Colors.GREEN}{__author__}{Colors.NC}")
    print(f"  Originally made for: {Colors.BLUE}{__project__}{Colors.NC}")
    print(f"  License: {__license__}")
    print()
    print(f"  {Colors.YELLOW}{__motto__}{Colors.NC}")
    print("=" * 65)
    print()


def print_colored(text, color):
    """Друкує текст з ANSI кольором / Prints text with ANSI color"""
    print(f"{color}{text}{Colors.NC}")


def print_separator(char='=', length=42):
    """Друкує розділову лінію / Prints separator line"""
    print(char * length)


def extract_keys_from_file(filepath, language_tag):
    """
    Витягує ключі локалізації з .yml файлу
    Extracts localization keys from a .yml file
    """
    keys = []
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            for line in f:
                if line.strip().startswith('#') or language_tag in line:
                    continue
                if ':' in line:
                    stripped = line.lstrip()
                    key = stripped.split(':')[0]
                    if key and re.match(r'^[A-Za-z_]', key):
                        keys.append(key)
    except Exception as e:
        print_colored(f"Error reading file {filepath}: {e}", Colors.RED)
    return keys


def find_full_line(filepath, key):
    """
    Знаходить повний рядок для ключа у yml файлі
    Finds the complete line for a key in yml file
    """
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            for line in f:
                stripped = line.lstrip()
                if stripped.startswith(f"{key}:"):
                    return stripped.rstrip()
    except Exception as e:
        print_colored(f"Error reading file {filepath}: {e}", Colors.RED)
    return None


def check_localization(ui, direction):
    """
    Перевіряє повноту локалізації
    Checks localization completeness
    """
    if direction == 'rus_eng':
        source_dir = RUSSIAN_DIR
        target_dir = ENGLISH_DIR
        source_tag = 'l_russian:'
        target_tag = 'l_english:'
        source_suffix = '_l_russian.yml'
        target_suffix = '_l_english.yml'
    else:
        source_dir = ENGLISH_DIR
        target_dir = RUSSIAN_DIR
        source_tag = 'l_english:'
        target_tag = 'l_russian:'
        source_suffix = '_l_english.yml'
        target_suffix = '_l_russian.yml'

    print_separator()
    print(ui['check_header'])
    print_separator()
    print()

    if not os.path.isdir(source_dir):
        print_colored(f"{ui['error_source_dir']} {source_dir}", Colors.RED)
        return 1

    if not os.path.isdir(target_dir):
        print_colored(f"{ui['error_target_dir']} {target_dir}", Colors.RED)
        return 1

    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR)

    print_colored(ui['step1_merge'], Colors.BLUE)
    print()

    source_all_keys_file = os.path.join(TEMP_DIR, 'source_all_keys.txt')
    target_all_keys_file = os.path.join(TEMP_DIR, 'target_all_keys.txt')
    source_keys_with_files_file = os.path.join(TEMP_DIR, 'source_keys_with_files.txt')

    source_all_keys = []
    source_keys_with_files = []

    source_lang = "RUS" if direction == 'rus_eng' else "ENG"
    target_lang = "ENG" if direction == 'rus_eng' else "RUS"

    print(f"{ui['processing_source']} ({source_lang})...")
    source_files_count = 0
    for filename in sorted(os.listdir(source_dir)):
        if filename.endswith('.yml'):
            filepath = os.path.join(source_dir, filename)
            keys = extract_keys_from_file(filepath, source_tag)
            for key in keys:
                source_all_keys.append(key)
                source_keys_with_files.append(f"{key}|{filename}")
            source_files_count += 1

    print_colored(f"  {ui['processed_source']} {source_files_count}", Colors.GREEN)
    print()

    target_all_keys = []

    print(f"{ui['processing_target']} ({target_lang})...")
    target_files_count = 0
    for filename in sorted(os.listdir(target_dir)):
        if filename.endswith('.yml'):
            filepath = os.path.join(target_dir, filename)
            keys = extract_keys_from_file(filepath, target_tag)
            for key in keys:
                target_all_keys.append(key)
            target_files_count += 1

    print_colored(f"  {ui['processed_target']} {target_files_count}", Colors.GREEN)
    print()

    source_unique = sorted(set(source_all_keys))
    target_unique = sorted(set(target_all_keys))

    with open(source_all_keys_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(source_unique))

    with open(target_all_keys_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(target_unique))

    with open(source_keys_with_files_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(source_keys_with_files)))

    with open(os.path.join(TEMP_DIR, 'direction.txt'), 'w', encoding='utf-8') as f:
        f.write(direction)

    print_colored(ui['step2_compare'], Colors.BLUE)
    print()
    print_colored(f"  {ui['unique_source']} {len(source_unique)}", Colors.GREEN)
    print_colored(f"  {ui['unique_target']} {len(target_unique)}", Colors.GREEN)
    print()

    missing_keys = sorted(set(source_unique) - set(target_unique))
    missing_count = len(missing_keys)

    missing_keys_file = os.path.join(TEMP_DIR, 'missing_keys.txt')
    with open(missing_keys_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(missing_keys))

    if missing_count == 0:
        print_colored(f"  {ui['all_keys_present']}", Colors.GREEN)
        print()
        print_separator()
        print(ui['localization_complete'])
        print_separator()
        return 0

    print_colored(f"  {ui['missing_keys_found']} {missing_count}", Colors.RED)
    print()

    percentage = 0
    if len(source_unique) > 0:
        percentage = ((len(source_unique) - missing_count) * 100) // len(source_unique)
        print_colored(f"{ui['completion']} {percentage}%", Colors.YELLOW)
        print()

    print_colored(ui['step3_search'], Colors.BLUE)
    print()

    with open(REPORT_FILE, 'w', encoding='utf-8') as report:
        report.write(f"Missing Localization Keys Report ({source_lang} -> {target_lang})\n")
        report.write(f"Created: {datetime.now()}\n")
        report.write(f"{_get_credits_line()}\n")
        report.write("=" * 40 + "\n\n")
        report.write(f"STATISTICS:\n")
        report.write(f"  Total {source_lang} keys: {len(source_unique)}\n")
        report.write(f"  Total {target_lang} keys: {len(target_unique)}\n")
        report.write(f"  Missing keys: {missing_count}\n")
        report.write(f"  Completion: {percentage}%\n\n")

        key_to_file = {}
        with open(source_keys_with_files_file, 'r', encoding='utf-8') as f:
            for line in f:
                if '|' in line:
                    key, filename = line.strip().split('|', 1)
                    key_to_file[key] = filename

        grouped_lines = []
        for key in missing_keys:
            if key in key_to_file:
                source_file = key_to_file[key]
                target_file = source_file.replace(source_suffix, target_suffix)
                grouped_lines.append(f"{target_file}|{key}")

        grouped_lines.sort()

        current_file = ""
        keys_in_file = []
        keys_count = 0

        for line in grouped_lines:
            if '|' not in line:
                continue
            file, key = line.split('|', 1)

            if file != current_file:
                if current_file:
                    source_file = current_file.replace(target_suffix, source_suffix)
                    print_colored(f"{ui['file']} {current_file}", Colors.YELLOW)
                    print_colored(f"  {ui['missing_in_file']} {keys_count}", Colors.RED)
                    print_colored(f"  {ui['path_original']} {source_dir}/{source_file}", Colors.BLUE)
                    print_colored(f"  {ui['path_translation']} {target_dir}/{current_file}", Colors.BLUE)
                    print()

                    report.write(f"\nFILE: {current_file} ({keys_count} keys)\n")
                    for k in keys_in_file:
                        report.write(f"  - {k}\n")

                current_file = file
                keys_in_file = [key]
                keys_count = 1
            else:
                keys_in_file.append(key)
                keys_count += 1

        if current_file:
            source_file = current_file.replace(target_suffix, source_suffix)
            print_colored(f"{ui['file']} {current_file}", Colors.YELLOW)
            print_colored(f"  {ui['missing_in_file']} {keys_count}", Colors.RED)
            print_colored(f"  {ui['path_original']} {source_dir}/{source_file}", Colors.BLUE)
            print_colored(f"  {ui['path_translation']} {target_dir}/{current_file}", Colors.BLUE)
            print()

            report.write(f"\nFILE: {current_file} ({keys_count} keys)\n")
            for k in keys_in_file:
                report.write(f"  - {k}\n")

    print_separator()
    print(ui['summary'])
    print_separator()
    print(f"{ui['localization_completion']} {Colors.YELLOW}{percentage}%{Colors.NC}")
    print(f"{ui['missing_keys']} {Colors.RED}{missing_count}{Colors.NC}")
    print()
    print_colored(f"{ui['report_saved']} {REPORT_FILE}", Colors.GREEN)
    print_colored(f"{ui['temp_saved']} {TEMP_DIR}/", Colors.GREEN)
    print()

    return 1


def create_wip_files(ui, direction):
    """
    Створює WIP файли для перекладу
    Creates WIP files for translation
    """
    if direction == 'rus_eng':
        source_dir = RUSSIAN_DIR
        source_suffix = '_l_russian.yml'
        target_suffix = '_l_english.yml'
        target_tag = 'l_english:'
        instruction2 = ui['instruction2_rus_eng']
        instruction3 = ui['instruction3_rus_eng']
    else:
        source_dir = ENGLISH_DIR
        source_suffix = '_l_english.yml'
        target_suffix = '_l_russian.yml'
        target_tag = 'l_russian:'
        instruction2 = ui['instruction2_eng_rus']
        instruction3 = ui['instruction3_eng_rus']

    print_separator()
    print(ui['create_header'])
    print_separator()
    print()

    missing_keys_file = os.path.join(TEMP_DIR, 'missing_keys.txt')
    source_keys_with_files_file = os.path.join(TEMP_DIR, 'source_keys_with_files.txt')

    if not os.path.exists(missing_keys_file):
        print_colored(ui['error_missing_keys'], Colors.RED)
        return 1

    if not os.path.exists(source_keys_with_files_file):
        print_colored(f"Error: {source_keys_with_files_file} {ui['error_no_temp_file']}", Colors.RED)
        return 1

    if os.path.exists(WIP_DIR):
        print(ui['cleaning_wip'])
        shutil.rmtree(WIP_DIR)
    os.makedirs(WIP_DIR)

    print_colored(ui['creating_wip'], Colors.BLUE)
    print()

    key_to_file = {}
    with open(source_keys_with_files_file, 'r', encoding='utf-8') as f:
        for line in f:
            if '|' in line:
                key, filename = line.strip().split('|', 1)
                key_to_file[key] = filename

    total_keys = 0
    files_created = set()

    with open(missing_keys_file, 'r', encoding='utf-8') as f:
        missing_keys = [line.strip() for line in f if line.strip()]

    for missing_key in missing_keys:
        if missing_key not in key_to_file:
            continue

        source_file = key_to_file[missing_key]
        source_path = os.path.join(source_dir, source_file)

        target_file = source_file.replace(source_suffix, target_suffix)
        wip_file = os.path.join(WIP_DIR, target_file)

        if wip_file not in files_created:
            with open(wip_file, 'w', encoding='utf-8') as f:
                f.write(f"# {_get_credits_line()}\n")
                f.write(f"{target_tag}\n")
            files_created.add(wip_file)
            print_colored(f"{ui['created']} {target_file}", Colors.GREEN)

        full_line = find_full_line(source_path, missing_key)

        with open(wip_file, 'a', encoding='utf-8') as f:
            if full_line:
                f.write(f" {full_line}\n")
            else:
                f.write(f' {missing_key}: "[TRANSLATION NEEDED]"\n')

        total_keys += 1

    print()
    print_separator()
    print(ui['summary'])
    print_separator()
    print_colored(f"{ui['files_created']} {len(files_created)}", Colors.GREEN)
    print_colored(f"{ui['total_keys']} {total_keys}", Colors.GREEN)
    print()
    print_colored(f"{ui['files_location']} {WIP_DIR}", Colors.YELLOW)
    print()
    print_colored(ui['instructions'], Colors.BLUE)
    print(ui['instruction1'])
    print(instruction2)
    print(instruction3)
    print()

    return 0


def main():
    """
    Головна функція CLI інтерфейсу
    Main CLI interface function
    """
    _show_credits_banner()

    print("Choose language / Виберіть мову / Оберіть мову:")
    print("  1. English")
    print("  2. Русский (Russian)")
    print("  3. Українська (Ukrainian)")
    print()

    while True:
        lang_input = input("Enter choice (1/2/3 or en/ru/ua): ").strip().lower()
        if lang_input in ['1', 'en', 'eng', 'english']:
            ui = UI_EN
            break
        elif lang_input in ['2', 'ru', 'rus', 'russian']:
            ui = UI_RU
            break
        elif lang_input in ['3', 'ua', 'ukr', 'ukrainian']:
            ui = UI_UA
            break
        else:
            print_colored("Invalid choice. Please enter 1, 2, 3, en, ru, or ua", Colors.RED)

    print()

    print(ui['select_direction'])
    print(f"  {ui['direction_rus_eng']}")
    print(f"  {ui['direction_eng_rus']}")
    print()

    while True:
        dir_input = input("Enter choice (1/2): ").strip().lower()
        if dir_input in ['1', 'rus', 'r']:
            direction = 'rus_eng'
            break
        elif dir_input in ['2', 'eng', 'e']:
            direction = 'eng_rus'
            break
        else:
            print_colored("Invalid choice. Please enter 1 or 2", Colors.RED)

    print()

    print(ui['select_function'])
    print(f"  {ui['option_check']}")
    print(f"  {ui['option_create']}")
    print(f"  {ui['option_both']}")
    print()

    while True:
        func_input = input("Enter choice (1/2/3 or check/create/both): ").strip().lower()
        if func_input in ['1', 'check']:
            print()
            result = check_localization(ui, direction)
            print()
            try:
                input("Press Enter to exit...")
            except EOFError:
                pass
            sys.exit(result)
        elif func_input in ['2', 'create']:
            print()
            result = create_wip_files(ui, direction)
            print()
            try:
                input("Press Enter to exit...")
            except EOFError:
                pass
            sys.exit(result)
        elif func_input in ['3', 'both']:
            print()
            result = check_localization(ui, direction)
            print()
            result2 = create_wip_files(ui, direction)
            print()
            try:
                input("Press Enter to exit...")
            except EOFError:
                pass
            sys.exit(result or result2)
        else:
            print_colored("Invalid choice. Please enter 1, 2, 3, check, create, or both", Colors.RED)


if __name__ == '__main__':
    main()
