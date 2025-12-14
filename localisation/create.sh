#!/bin/bash

# Скрипт для створення файлів з відсутніми ключами для перекладу
# Створює файли в ./wip/ з російськими значеннями для подальшого перекладу

RUSSIAN_DIR="./russian"
TEMP_DIR="./temp"
WIP_DIR="./wip"

# Кольори
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "=========================================="
echo "Створення файлів для перекладу"
echo "=========================================="
echo ""

# Перевірка наявності результатів попереднього скрипту
if [ ! -f "$TEMP_DIR/missing_keys.txt" ]; then
    echo -e "${RED}Помилка: Спочатку запустіть скрипт перевірки локалізації!${NC}"
    echo "Файл $TEMP_DIR/missing_keys.txt не знайдено"
    exit 1
fi

if [ ! -f "$TEMP_DIR/russian_keys_with_files.txt" ]; then
    echo -e "${RED}Помилка: Файл $TEMP_DIR/russian_keys_with_files.txt не знайдено${NC}"
    exit 1
fi

# Створення директорії WIP
if [ -d "$WIP_DIR" ]; then
    echo "Очищення існуючої директорії $WIP_DIR..."
    rm -rf "$WIP_DIR"
fi
mkdir -p "$WIP_DIR"

echo -e "${BLUE}Створення файлів з відсутніми ключами...${NC}"
echo ""

# Читаємо всі відсутні ключі
total_keys=0
files_created=0

# Створюємо асоціації ключ->файл
declare -a file_keys

while IFS= read -r missing_key; do
    # Знайти, в якому російському файлі знаходиться цей ключ
    source_line=$(grep "^${missing_key}|" "$TEMP_DIR/russian_keys_with_files.txt" | head -n1)
    
    if [ -n "$source_line" ]; then
        russian_file=$(echo "$source_line" | cut -d'|' -f2)
        russian_path="$RUSSIAN_DIR/$russian_file"
        
        # Конвертувати в англійське ім'я
        english_file=$(echo "$russian_file" | sed 's/_l_russian\.yml/_l_english.yml/')
        wip_file="$WIP_DIR/$english_file"
        
        # Якщо це перший ключ для цього файлу, створити заголовок
        if [ ! -f "$wip_file" ]; then
            echo "l_english:" > "$wip_file"
            files_created=$((files_created + 1))
            echo -e "${GREEN}Створено: $english_file${NC}"
        fi
        
        # Знайти повний рядок з ключем у російському файлі
        full_line=$(grep "^[[:space:]]*${missing_key}:" "$russian_path" | head -n1)
        
        if [ -n "$full_line" ]; then
            # Видалити початкові пробіли і додати один пробіл
            cleaned_line=$(echo "$full_line" | sed 's/^[[:space:]]*//')
            echo " $cleaned_line" >> "$wip_file"
            total_keys=$((total_keys + 1))
        else
            # Якщо не знайшли повний рядок, додати тільки ключ
            echo " $missing_key: \"[TRANSLATION NEEDED]\"" >> "$wip_file"
            total_keys=$((total_keys + 1))
        fi
    fi
done < "$TEMP_DIR/missing_keys.txt"

echo ""
echo "=========================================="
echo "Підсумок"
echo "=========================================="
echo -e "${GREEN}Створено файлів: $files_created${NC}"
echo -e "${GREEN}Всього ключів для перекладу: $total_keys${NC}"
echo ""
echo -e "${YELLOW}Файли знаходяться в директорії: $WIP_DIR${NC}"
echo ""
echo -e "${BLUE}Інструкція:${NC}"
echo "1. Відкрийте файли в $WIP_DIR"
echo "2. Перекладіть російські значення на англійську"
echo "3. Скопіюйте вміст у відповідні файли в ./english/"
echo ""