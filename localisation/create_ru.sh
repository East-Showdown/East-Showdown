#!/bin/bash

# Скрипт для создания файлов с отсутствующими ключами для перевода
# Создает файлы в ./wip/ с русскими значениями для последующего перевода

RUSSIAN_DIR="./russian"
TEMP_DIR="./temp"
WIP_DIR="./wip"

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "=========================================="
echo "Создание файлов для перевода"
echo "=========================================="
echo ""

# Проверка наличия результатов предыдущего скрипта
if [ ! -f "$TEMP_DIR/missing_keys.txt" ]; then
    echo -e "${RED}Ошибка: сначала запустите скрипт проверки локализации!${NC}"
    echo "Файл $TEMP_DIR/missing_keys.txt не найден"
    exit 1
fi

if [ ! -f "$TEMP_DIR/russian_keys_with_files.txt" ]; then
    echo -e "${RED}Ошибка: файл $TEMP_DIR/russian_keys_with_files.txt не найден${NC}"
    exit 1
fi

# Создание директории WIP
if [ -d "$WIP_DIR" ]; then
    echo "Очистка существующей директории $WIP_DIR..."
    rm -rf "$WIP_DIR"
fi
mkdir -p "$WIP_DIR"

echo -e "${BLUE}Создание файлов с отсутствующими ключами...${NC}"
echo ""

# Читаем все отсутствующие ключи
total_keys=0
files_created=0

# Создаем ассоциации ключ->файл
declare -a file_keys

while IFS= read -r missing_key; do
    # Найти, в каком русском файле находится этот ключ
    source_line=$(grep "^${missing_key}|" "$TEMP_DIR/russian_keys_with_files.txt" | head -n1)
    
    if [ -n "$source_line" ]; then
        russian_file=$(echo "$source_line" | cut -d'|' -f2)
        russian_path="$RUSSIAN_DIR/$russian_file"
        
        # Преобразовать в английское имя
        english_file=$(echo "$russian_file" | sed 's/_l_russian\.yml/_l_english.yml/')
        wip_file="$WIP_DIR/$english_file"
        
        # Если это первый ключ для этого файла, создать заголовок
        if [ ! -f "$wip_file" ]; then
            echo "l_english:" > "$wip_file"
            files_created=$((files_created + 1))
            echo -e "${GREEN}Создан: $english_file${NC}"
        fi
        
        # Найти полную строку с ключом в русском файле
        full_line=$(grep "^[[:space:]]*${missing_key}:" "$russian_path" | head -n1)
        
        if [ -n "$full_line" ]; then
            # Удалить начальные пробелы и добавить один пробел
            cleaned_line=$(echo "$full_line" | sed 's/^[[:space:]]*//')
            echo " $cleaned_line" >> "$wip_file"
            total_keys=$((total_keys + 1))
        else
            # Если не нашли полную строку, добавить только ключ
            echo " $missing_key: \"[TRANSLATION NEEDED]\"" >> "$wip_file"
            total_keys=$((total_keys + 1))
        fi
    fi
done < "$TEMP_DIR/missing_keys.txt"

echo ""
echo "=========================================="
echo "Итоги"
echo "=========================================="
echo -e "${GREEN}Создано файлов: $files_created${NC}"
echo -e "${GREEN}Всего ключей для перевода: $total_keys${NC}"
echo ""
echo -e "${YELLOW}Файлы находятся в директории: $WIP_DIR${NC}"
echo ""
echo -e "${BLUE}Инструкция:${NC}"
echo "1. Откройте файлы в $WIP_DIR"
echo "2. Переведите русские значения на английский"
echo "3. Скопируйте содержимое в соответствующие файлы в ./english/"
echo ""
