#!/bin/bash

# Минулий скрипт переклали російською мовою
# Зрада

# Скрипт порівняння локалізації
# Об'єднує всі ключі з кожної локалі та порівнює їх

RUSSIAN_DIR="./russian"
ENGLISH_DIR="./english"
TEMP_DIR="./temp"
REPORT_FILE="localization_report.txt"

# Кольори для виводу в терміналі
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # Без кольору

echo "=========================================="
echo "Перевірка повноти локалізації"
echo "=========================================="
echo ""

# Перевірка наявності директорій
if [ ! -d "$RUSSIAN_DIR" ]; then
    echo -e "${RED}Помилка: Російська директорія не знайдена за адресою $RUSSIAN_DIR${NC}"
    exit 1
fi

if [ ! -d "$ENGLISH_DIR" ]; then
    echo -e "${RED}Помилка: Англійська директорія не знайдена за адресою $ENGLISH_DIR${NC}"
    exit 1
fi

# Створення/очищення тимчасової директорії
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi
mkdir -p "$TEMP_DIR"

echo -e "${BLUE}[1] Об'єднання всіх ключів з кожної локалі в окремі файли...${NC}"
echo ""

RUSSIAN_ALL_KEYS="$TEMP_DIR/russian_all_keys.txt"
ENGLISH_ALL_KEYS="$TEMP_DIR/english_all_keys.txt"
RUSSIAN_KEYS_WITH_FILES="$TEMP_DIR/russian_keys_with_files.txt"
ENGLISH_KEYS_WITH_FILES="$TEMP_DIR/english_keys_with_files.txt"

# Очищення файлів
> "$RUSSIAN_ALL_KEYS"
> "$ENGLISH_ALL_KEYS"
> "$RUSSIAN_KEYS_WITH_FILES"
> "$ENGLISH_KEYS_WITH_FILES"

russian_files_count=0
russian_keys_count=0

# Обробка російських файлів
echo "Обробка російських файлів..."
for russian_file in "$RUSSIAN_DIR"/*.yml; do
    [ -e "$russian_file" ] || continue
    
    filename=$(basename "$russian_file")
    russian_files_count=$((russian_files_count + 1))
    
    # Витяг ключів: всі рядки з двокрапкою, крім коментарів і оголошення мови
    grep ':' "$russian_file" | grep -v '^#' | grep -v 'l_russian:' | sed 's/^[[:space:]]*//' | sed 's/:.*//' | grep -E '^[A-Za-z_]' | while IFS= read -r key; do
        if [ -n "$key" ]; then
            echo "$key" >> "$RUSSIAN_ALL_KEYS"
            echo "$key|$filename" >> "$RUSSIAN_KEYS_WITH_FILES"
            russian_keys_count=$((russian_keys_count + 1))
        fi
    done
done

echo -e "${GREEN}  ✓ Оброблено російських файлів: $russian_files_count${NC}"
echo ""

english_files_count=0
english_keys_count=0

# Обробка англійських файлів
echo "Обробка англійських файлів..."
for english_file in "$ENGLISH_DIR"/*.yml; do
    [ -e "$english_file" ] || continue
    
    filename=$(basename "$english_file")
    english_files_count=$((english_files_count + 1))
    
    # Витяг ключів: всі рядки з двокрапкою, крім коментарів і оголошення мови
    grep ':' "$english_file" | grep -v '^#' | grep -v 'l_english:' | sed 's/^[[:space:]]*//' | sed 's/:.*//' | grep -E '^[A-Za-z_]' | while IFS= read -r key; do
        if [ -n "$key" ]; then
            echo "$key" >> "$ENGLISH_ALL_KEYS"
            echo "$key|$filename" >> "$ENGLISH_KEYS_WITH_FILES"
            english_keys_count=$((english_keys_count + 1))
        fi
    done
done

echo -e "${GREEN}  ✓ Оброблено англійських файлів: $english_files_count${NC}"
echo ""

# Сортування ключів
sort -u "$RUSSIAN_ALL_KEYS" -o "$RUSSIAN_ALL_KEYS"
sort -u "$ENGLISH_ALL_KEYS" -o "$ENGLISH_ALL_KEYS"

russian_unique=$(wc -l < "$RUSSIAN_ALL_KEYS" | tr -d ' ')
english_unique=$(wc -l < "$ENGLISH_ALL_KEYS" | tr -d ' ')

echo -e "${BLUE}[2] Порівняння ключів між локалями...${NC}"
echo ""
echo -e "${GREEN}  Унікальних російських ключів: $russian_unique${NC}"
echo -e "${GREEN}  Унікальних англійських ключів: $english_unique${NC}"
echo ""

# Знаходження відсутніх ключів
MISSING_KEYS_FILE="$TEMP_DIR/missing_keys.txt"
comm -23 "$RUSSIAN_ALL_KEYS" "$ENGLISH_ALL_KEYS" > "$MISSING_KEYS_FILE"

missing_count=$(wc -l < "$MISSING_KEYS_FILE" | tr -d ' ')

if [ $missing_count -eq 0 ]; then
    echo -e "${GREEN}  ✓ Всі російські ключі присутні в англійській локалізації!${NC}"
    echo ""
    echo "=========================================="
    echo "Локалізація завершена на 100%!"
    echo "=========================================="
    exit 0
fi

echo -e "${RED}  ✗ Знайдено відсутніх ключів в англійській локалізації: $missing_count${NC}"
echo ""

# Розрахунок відсотка завершеності
if [ $russian_unique -gt 0 ]; then
    percentage=$(( (russian_unique - missing_count) * 100 / russian_unique ))
    echo -e "${YELLOW}Завершеність англійської локалізації: ${percentage}%${NC}"
    echo ""
fi

echo -e "${BLUE}[3] Пошук відсутніх ключів у файлах та створення звіту...${NC}"
echo ""

# Створення звіту
echo "Звіт про відсутні ключі локалізації" > "$REPORT_FILE"
echo "Створено: $(date)" >> "$REPORT_FILE"
echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "СТАТИСТИКА:" >> "$REPORT_FILE"
echo "  Всього російських ключів: $russian_unique" >> "$REPORT_FILE"
echo "  Всього англійських ключів: $english_unique" >> "$REPORT_FILE"
echo "  Відсутніх ключів: $missing_count" >> "$REPORT_FILE"
echo "  Завершеність: ${percentage}%" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# Створення тимчасового файлу для групування за файлами
GROUPED_FILE="$TEMP_DIR/grouped_by_files.txt"
> "$GROUPED_FILE"

# Для кожного відсутнього ключа знайти його файл
while IFS= read -r missing_key; do
    # Знайти, в якому російському файлі знаходиться цей ключ
    source_file=$(grep "^${missing_key}|" "$RUSSIAN_KEYS_WITH_FILES" | cut -d'|' -f2 | head -n1)
    
    if [ -n "$source_file" ]; then
        # Конвертувати ім'я файлу в англійський варіант
        english_file=$(echo "$source_file" | sed 's/_l_russian\.yml/_l_english.yml/')
        
        # Додати до файлу у форматі: english_file|missing_key
        echo "${english_file}|${missing_key}" >> "$GROUPED_FILE"
    fi
done < "$MISSING_KEYS_FILE"

# Сортування за файлами
sort "$GROUPED_FILE" -o "$GROUPED_FILE"

# Виведення результатів
echo "ВІДСУТНІ КЛЮЧІ ЗА ФАЙЛАМИ:" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

current_file=""
keys_in_file=""
keys_count=0

# Обробка згрупованих ключів
while IFS='|' read -r file key; do
    if [ "$file" != "$current_file" ]; then
        # Якщо це не перший файл, виведемо попередній
        if [ -n "$current_file" ]; then
            russian_file=$(echo "$current_file" | sed 's/_l_english\.yml/_l_russian.yml/')
            
            echo -e "${YELLOW}Файл: $current_file${NC}"
            echo -e "${RED}  Відсутніх ключів: $keys_count${NC}"
            echo -e "${BLUE}  Шлях до оригіналу: $RUSSIAN_DIR/$russian_file${NC}"
            echo -e "${BLUE}  Шлях до перекладу: $ENGLISH_DIR/$current_file${NC}"
            echo ""
            
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> "$REPORT_FILE"
            echo "ФАЙЛ: $current_file" >> "$REPORT_FILE"
            echo "Відсутніх ключів: $keys_count" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Шлях до російського оригіналу:" >> "$REPORT_FILE"
            echo "  $RUSSIAN_DIR/$russian_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Шлях до англійського файлу (додайте ключі сюди):" >> "$REPORT_FILE"
            echo "  $ENGLISH_DIR/$current_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
            echo "Відсутні ключі:" >> "$REPORT_FILE"
            echo "$keys_in_file" >> "$REPORT_FILE"
            echo "" >> "$REPORT_FILE"
        fi
        
        # Початок нового файлу
        current_file="$file"
        keys_in_file="  - $key"
        keys_count=1
    else
        # Додати ключ до поточного файлу
        keys_in_file="${keys_in_file}
  - $key"
        keys_count=$((keys_count + 1))
    fi
done < "$GROUPED_FILE"

# Вивести останній файл
if [ -n "$current_file" ]; then
    russian_file=$(echo "$current_file" | sed 's/_l_english\.yml/_l_russian.yml/')
    
    echo -e "${YELLOW}Файл: $current_file${NC}"
    echo -e "${RED}  Відсутніх ключів: $keys_count${NC}"
    echo -e "${BLUE}  Шлях до оригіналу: $RUSSIAN_DIR/$russian_file${NC}"
    echo -e "${BLUE}  Шлях до перекладу: $ENGLISH_DIR/$current_file${NC}"
    echo ""
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> "$REPORT_FILE"
    echo "ФАЙЛ: $current_file" >> "$REPORT_FILE"
    echo "Відсутніх ключів: $keys_count" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Шлях до російського оригіналу:" >> "$REPORT_FILE"
    echo "  $RUSSIAN_DIR/$russian_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Шлях до англійського файлу (додайте ключі сюди):" >> "$REPORT_FILE"
    echo "  $ENGLISH_DIR/$current_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "Відсутні ключі:" >> "$REPORT_FILE"
    echo "$keys_in_file" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
fi

echo "========================================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
echo "ПОВНИЙ СПИСОК ВІДСУТНІХ КЛЮЧІВ:" >> "$REPORT_FILE"
cat "$MISSING_KEYS_FILE" | while IFS= read -r key; do
    echo "  - $key" >> "$REPORT_FILE"
done

echo "=========================================="
echo "Підсумок"
echo "=========================================="
echo -e "Завершеність локалізації: ${YELLOW}${percentage}%${NC}"
echo -e "Відсутніх ключів: ${RED}$missing_count${NC}"
echo ""
echo -e "${GREEN}Детальний звіт збережено в: $REPORT_FILE${NC}"
echo -e "${GREEN}Тимчасові файли збережено в: $TEMP_DIR/${NC}"
echo ""

exit 1
