#!/bin/bash

# Скрипт сравнения локализации
# Объединяет все ключи из каждой локали и сравнивает их

RUSSIAN_DIR="./russian"
ENGLISH_DIR="./english"
TEMP_DIR="./temp"
REPORT_FILE="localization_report.txt"

# Цвета для вывода в терминале
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # Без цвета

echo "=========================================="
echo "Проверка полноты локализации"
echo "=========================================="
echo ""

# Проверка наличия директорий
if [ ! -d "$RUSSIAN_DIR" ]; then
    echo -e "${RED}Ошибка: русская директория не найдена по пути $RUSSIAN_DIR${NC}"
    exit 1
fi

if [ ! -d "$ENGLISH_DIR" ]; then
    echo -e "${RED}Ошибка: английская директория не найдена по пути $ENGLISH_DIR${NC}"
    exit 1
fi

# Создание/очистка временной директории
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi
mkdir -p "$TEMP_DIR"

echo -e "${BLUE}[1] Объединение всех ключей из каждой локали в отдельные файлы...${NC}"
echo ""

RUSSIAN_ALL_KEYS="$TEMP_DIR/russian_all_keys.txt"
ENGLISH_ALL_KEYS="$TEMP_DIR/english_all_keys.txt"
RUSSIAN_KEYS_WITH_FILES="$TEMP_DIR/russian_keys_with_files.txt"
ENGLISH_KEYS_WITH_FILES="$TEMP_DIR/english_keys_with_files.txt"

# Очистка файлов
> "$RUSSIAN_ALL_KEYS"
> "$ENGLISH_ALL_KEYS"
> "$RUSSIAN_KEYS_WITH_FILES"
> "$ENGLISH_KEYS_WITH_FILES"

russian_files_count=0
russian_keys_count=0

# Обработка русских файлов
echo "Обработка русских файлов..."
for russian_file in "$RUSSIAN_DIR"/*.yml; do
    [ -e "$russian_file" ] || continue
    
    filename=$(basename "$russian_file")
    russian_files_count=$((russian_files_count + 1))
    
    # Извлечение ключей: все строки с двоеточием, кроме комментариев и объявления языка
    grep ':' "$russian_file" | grep -v '^#' | grep -v 'l_russian:' | sed 's/^[[:space:]]*//' | sed 's/:.*//' | grep -E '^[A-Za-z_]' | while IFS= read -r key; do
        if [ -n "$key" ]; then
            echo "$key" >> "$RUSSIAN_ALL_KEYS"
            echo "$key|$filename" >> "$RUSSIAN_KEYS_WITH_FILES"
            russian_keys_count=$((russian_keys_count + 1))
        fi
    done
done

echo -e "${GREEN}  ✓ Обработано русских файлов: $russian_files_count${NC}"
echo ""

english_files_count=0
english_keys_count=0

# Обработка английских файлов
echo "Обработка английских файлов..."
for english_file in "$ENGLISH_DIR"/*.yml; do
    [ -e "$english_file" ] || continue
    
    filename=$(basename "$english_file")
    english_files_count=$((english_files_count + 1))
    
    # Извлечение ключей: все строки с двоеточием, кроме комментариев и объявления языка
    grep ':' "$english_file" | grep -v '^#' | grep -v 'l_english:' | sed 's/^[[:space:]]*//' | sed 's/:.*//' | grep -E '^[A-Za-z_]' | while IFS= read -r key; do
        if [ -n "$key" ]; then
            echo "$key" >> "$ENGLISH_ALL_KEYS"
            echo "$key|$filename" >> "$ENGLISH_KEYS_WITH_FILES"
            english_keys_count=$((english_keys_count + 1))
        fi
    done
done

echo -e "${GREEN}  ✓ Обработано английских файлов: $english_files_count${NC}"
echo ""

# Сортировка ключей
sort -u "$RUSSIAN_ALL_KEYS" -o "$RUSSIAN_ALL_KEYS"
sort -u "$ENGLISH_ALL_KEYS" -o "$ENGLISH_ALL_KEYS"

russian_unique=$(wc -l < "$RUSSIAN_ALL_KEYS" | tr -d ' ')
english_unique=$(wc -l < "$ENGLISH_ALL_KEYS" | tr -d ' ')

echo -e "${BLUE}[2] Сравнение ключей между локалями...${NC}"
echo ""
echo -e "${GREEN}  Уникальных русских ключей: $russian_unique${NC}"
echo -e "${GREEN}  Уникальных английских ключей: $english_unique${NC}"
echo ""

# Поиск отсутствующих ключей
MISSING_KEYS_FILE="$TEMP_DIR/missing_keys.txt"
comm -23 "$RUSSIAN_ALL_KEYS" "$ENGLISH_ALL_KEYS" > "$MISSING_KEYS_FILE"

missing_count=$(wc -l < "$MISSING_KEYS_FILE" | tr -d ' ')

if [ $missing_count -eq 0 ]; then
    echo -e "${GREEN}  ✓ Все русские ключи присутствуют в английской локализации!${NC}"
    echo ""
    echo "=========================================="
    echo "Локализация завершена на 100%!"
    echo "=========================================="
    exit 0
fi

echo -e "${RED}  ✗ Найдены отсутствующие ключи в английской локализации: $missing_count${NC}"
echo ""

# Расчет процента завершенности
if [ $russian_unique -gt 0 ]; then
    percentage=$(( (russian_unique - missing_count) * 100 / russian_unique ))
    echo -e "${YELLOW}Завершенность английской локализации: ${percentage}%${NC}"
    echo ""
fi

echo -e "${BLUE}[3] Поиск отсутствующих ключей по файлам и создание отчета...${NC}"
echo ""

# Создание отчета
echo "Отчет об отсутствующих ключах локализации" > "$REPORT_FILE"
echo "Создан: $(date)" >> "$REPORT_FILE"
echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "СТАТИСТИКА:" >> "$REPORT_FILE"
echo "  Всего русских ключей: $russian_unique" >> "$REPORT_FILE"
echo "  Всего английских ключей: $english_unique" >> "$REPORT_FILE"
echo "  Отсутствующих ключей: $missing_count" >> "$REPORT_FILE"
echo "  Завершенность: ${percentage}%" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Создание временного файла для группировки по файлам
GROUPED_FILE="$TEMP_DIR/grouped_by_files.txt"
> "$GROUPED_FILE"

# Для каждого отсутствующего ключа найти его файл
while IFS= read -r missing_key; do
    # Найти, в каком русском файле находится этот ключ
    source_file=$(grep "^${missing_key}|" "$RUSSIAN_KEYS_WITH_FILES" | cut -d'|' -f2 | head -n1)
    
    if [ -n "$source_file" ]; then
        # Преобразовать имя файла в английский вариант
        english_file=$(echo "$source_file" | sed 's/_l_russian\.yml/_l_english.yml/')
        
        # Добавить в файл в формате: english_file|missing_key
        echo "${english_file}|${missing_key}" >> "$GROUPED_FILE"
    fi
done < "$MISSING_KEYS_FILE"

# Сортировка по файлам
sort "$GROUPED_FILE" -o "$GROUPED_FILE"

# Вывод результатов
echo "ОТСУТСТВУЮЩИЕ КЛЮЧИ ПО ФАЙЛАМ:" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

current_file=""
keys_in_file=""
keys_count=0

# Обработка сгруппированных ключей
while IFS='|' read -r file key; do
    if [ "$file" != "$current_file" ]; then
        # Если это не первый файл, выводим предыдущий
        if [ -n "$current_file" ]; then
            russian_file=$(echo "$current_file" | sed 's/_l_english\.yml/_l_russian.yml/')
            
            echo -e "${YELLOW}Файл: $current_file${NC}"
            echo -e "${RED}  Отсутствующих ключей: $keys_count${NC}"
            echo -e "${BLUE}  Путь к оригиналу: $RUSSIAN_DIR/$russian_file${NC}"
            echo -e "${BLUE}  Путь к переводу: $ENGLISH_DIR/$current_file${NC}"
            echo ""
            
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> "$REPORT_FILE"
            echo "ФАЙЛ: $current_file" >> "$REPORT_FILE"
            echo "Отсутствующих ключей: $keys_count" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Путь к русскому оригиналу:" >> "$REPORT_FILE"
            echo "  $RUSSIAN_DIR/$russian_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Путь к английскому файлу (добавьте ключи сюда):" >> "$REPORT_FILE"
            echo "  $ENGLISH_DIR/$current_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Отсутствующие ключи:" >> "$REPORT_FILE"
            echo "$keys_in_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
        fi
        
        # Начало нового файла
        current_file="$file"
        keys_in_file="  - $key"
        keys_count=1
    else
        # Добавить ключ к текущему файлу
        keys_in_file="${keys_in_file}
  - $key"
        keys_count=$((keys_count + 1))
    fi
done < "$GROUPED_FILE"

# Вывод последнего файла
if [ -n "$current_file" ]; then
    russian_file=$(echo "$current_file" | sed 's/_l_english\.yml/_l_russian.yml/')
    
    echo -e "${YELLOW}Файл: $current_file${NC}"
    echo -e "${RED}  Отсутствующих ключей: $keys_count${NC}"
    echo -e "${BLUE}  Путь к оригиналу: $RUSSIAN_DIR/$russian_file${NC}"
    echo -e "${BLUE}  Путь к переводу: $ENGLISH_DIR/$current_file${NC}"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> "$REPORT_FILE"
    echo "ФАЙЛ: $current_file" >> "$REPORT_FILE"
    echo "Отсутствующих ключей: $keys_count" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Путь к русскому оригиналу:" >> "$REPORT_FILE"
    echo "  $RUSSIAN_DIR/$russian_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Путь к английскому файлу (добавьте ключи сюда):" >> "$REPORT_FILE"
    echo "  $ENGLISH_DIR/$current_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Отсутствующие ключи:" >> "$REPORT_FILE"
    echo "$keys_in_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
fi

echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "ПОЛНЫЙ СПИСОК ОТСУТСТВУЮЩИХ КЛЮЧЕЙ:" >> "$REPORT_FILE"
cat "$MISSING_KEYS_FILE" | while IFS= read -r key; do
    echo "  - $key" >> "$REPORT_FILE"
done

echo "=========================================="
echo "Итоги"
echo "=========================================="
echo -e "Завершенность локализации: ${YELLOW}${percentage}%${NC}"
echo -e "Отсутствующих ключей: ${RED}$missing_count${NC}"
echo ""
echo -e "${GREEN}Детальный отчет сохранен в: $REPORT_FILE${NC}"
echo -e "${GREEN}Временные файлы сохранены в: $TEMP_DIR/${NC}"
echo ""

exit 1
