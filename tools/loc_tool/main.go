package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strings"
)

const (
	version = "3.0.0"
	author  = "iAmScienceMan"
	project = "East-Showdown"
	license = "MIT"
	motto   = "Femboys rule the world"
)

// UI translations
var (
	uiEN = map[string]string{
		"check_header":          "Localization Completeness Check",
		"create_header":         "Creating Translation Files",
		"error_source_dir":      "Error: source directory not found at",
		"error_target_dir":      "Error: target directory not found at",
		"error_missing_keys":    "Error: run the localization check script first!",
		"error_no_temp_file":    "not found",
		"step1_merge":           "[1] Merging all keys from each locale into separate files...",
		"processing_source":     "Processing source files",
		"processing_target":     "Processing target files",
		"processed_source":      "✓ Processed source files:",
		"processed_target":      "✓ Processed target files:",
		"step2_compare":         "[2] Comparing keys between locales...",
		"unique_source":         "Unique source keys:",
		"unique_target":         "Unique target keys:",
		"all_keys_present":      "✓ All source keys are present in target localization!",
		"localization_complete": "Localization is 100% complete!",
		"missing_keys_found":    "✗ Missing keys found in target localization:",
		"completion":            "Target localization completion:",
		"step3_search":          "[3] Searching for missing keys in files and creating report...",
		"summary":               "Summary",
		"localization_completion": "Localization completion:",
		"missing_keys":          "Missing keys:",
		"report_saved":          "Detailed report saved to:",
		"temp_saved":            "Temporary files saved to:",
		"file":                  "File:",
		"missing_in_file":       "Missing keys:",
		"path_original":         "Path to source:",
		"path_translation":      "Path to target:",
		"creating_wip":          "Creating files with missing keys...",
		"created":               "Created:",
		"files_created":         "Files created:",
		"total_keys":            "Total keys to translate:",
		"files_location":        "Files are located in:",
		"instructions":          "Instructions:",
		"instruction1":          "1. Open files in ./wip",
		"instruction2_rus_eng":  "2. Translate Russian values to English",
		"instruction2_eng_rus":  "2. Translate English values to Russian",
		"instruction3_rus_eng":  "3. Copy contents to corresponding files in ./english/",
		"instruction3_eng_rus":  "3. Copy contents to corresponding files in ./russian/",
		"cleaning_wip":          "Cleaning existing ./wip directory...",
		"select_function":       "Select function:",
		"option_check":          "1. Check - verify localization completeness",
		"option_create":         "2. Create - generate translation files",
		"option_both":           "3. Both - check first, then create",
		"select_direction":      "Select comparison direction:",
		"direction_rus_eng":     "1. RUS → ENG - find keys missing in English",
		"direction_eng_rus":     "2. ENG → RUS - find keys missing in Russian",
	}

	uiRU = map[string]string{
		"check_header":          "Проверка полноты локализации",
		"create_header":         "Создание файлов для перевода",
		"error_source_dir":      "Ошибка: исходная директория не найдена по пути",
		"error_target_dir":      "Ошибка: целевая директория не найдена по пути",
		"error_missing_keys":    "Ошибка: сначала запустите скрипт проверки локализации!",
		"error_no_temp_file":    "не найден",
		"step1_merge":           "[1] Объединение всех ключей из каждой локали в отдельные файлы...",
		"processing_source":     "Обработка исходных файлов",
		"processing_target":     "Обработка целевых файлов",
		"processed_source":      "✓ Обработано исходных файлов:",
		"processed_target":      "✓ Обработано целевых файлов:",
		"step2_compare":         "[2] Сравнение ключей между локалями...",
		"unique_source":         "Уникальных ключей в источнике:",
		"unique_target":         "Уникальных ключей в цели:",
		"all_keys_present":      "✓ Все ключи источника присутствуют в целевой локализации!",
		"localization_complete": "Локализация завершена на 100%!",
		"missing_keys_found":    "✗ Найдены отсутствующие ключи в целевой локализации:",
		"completion":            "Завершенность целевой локализации:",
		"step3_search":          "[3] Поиск отсутствующих ключей по файлам и создание отчета...",
		"summary":               "Итоги",
		"localization_completion": "Завершенность локализации:",
		"missing_keys":          "Отсутствующих ключей:",
		"report_saved":          "Детальный отчет сохранен в:",
		"temp_saved":            "Временные файлы сохранены в:",
		"file":                  "Файл:",
		"missing_in_file":       "Отсутствующих ключей:",
		"path_original":         "Путь к оригиналу:",
		"path_translation":      "Путь к переводу:",
		"creating_wip":          "Создание файлов с отсутствующими ключами...",
		"created":               "Создан:",
		"files_created":         "Создано файлов:",
		"total_keys":            "Всего ключей для перевода:",
		"files_location":        "Файлы находятся в директории:",
		"instructions":          "Инструкция:",
		"instruction1":          "1. Откройте файлы в ./wip",
		"instruction2_rus_eng":  "2. Переведите русские значения на английский",
		"instruction2_eng_rus":  "2. Переведите английские значения на русский",
		"instruction3_rus_eng":  "3. Скопируйте содержимое в соответствующие файлы в ./english/",
		"instruction3_eng_rus":  "3. Скопіюйте вміст у відповідні файли в ./russian/",
		"cleaning_wip":          "Очистка существующей директории ./wip...",
		"select_function":       "Выберите функцию:",
		"option_check":          "1. Проверка (Check) - проверить полноту локализации",
		"option_create":         "2. Создание (Create) - создать файлы для перевода",
		"option_both":           "3. Оба (Both) - сначала проверка, затем создание",
		"select_direction":      "Выберите направление сравнения:",
		"direction_rus_eng":     "1. RUS → ENG - найти ключи, отсутствующие в английском",
		"direction_eng_rus":     "2. ENG → RUS - найти ключи, отсутствующие в русском",
	}

	uiUA = map[string]string{
		"check_header":          "Перевірка повноти локалізації",
		"create_header":         "Створення файлів для перекладу",
		"error_source_dir":      "Помилка: вихідна директорія не знайдена за адресою",
		"error_target_dir":      "Помилка: цільова директорія не знайдена за адресою",
		"error_missing_keys":    "Помилка: спочатку запустіть скрипт перевірки локалізації!",
		"error_no_temp_file":    "не знайдено",
		"step1_merge":           "[1] Об'єднання всіх ключів з кожної локалі в окремі файли...",
		"processing_source":     "Обробка вихідних файлів",
		"processing_target":     "Обробка цільових файлів",
		"processed_source":      "✓ Оброблено вихідних файлів:",
		"processed_target":      "✓ Оброблено цільових файлів:",
		"step2_compare":         "[2] Порівняння ключів між локалями...",
		"unique_source":         "Унікальних ключів у джерелі:",
		"unique_target":         "Унікальних ключів у цілі:",
		"all_keys_present":      "✓ Всі ключі джерела присутні в цільовій локалізації!",
		"localization_complete": "Локалізація завершена на 100%!",
		"missing_keys_found":    "✗ Знайдено відсутніх ключів у цільовій локалізації:",
		"completion":            "Завершеність цільової локалізації:",
		"step3_search":          "[3] Пошук відсутніх ключів у файлах та створення звіту...",
		"summary":               "Підсумок",
		"localization_completion": "Завершеність локалізації:",
		"missing_keys":          "Відсутніх ключів:",
		"report_saved":          "Детальний звіт збережено в:",
		"temp_saved":            "Тимчасові файли збережено в:",
		"file":                  "Файл:",
		"missing_in_file":       "Відсутніх ключів:",
		"path_original":         "Шлях до оригіналу:",
		"path_translation":      "Шлях до перекладу:",
		"creating_wip":          "Створення файлів з відсутніми ключами...",
		"created":               "Створено:",
		"files_created":         "Створено файлів:",
		"total_keys":            "Всього ключів для перекладу:",
		"files_location":        "Файли знаходяться в директорії:",
		"instructions":          "Інструкція:",
		"instruction1":          "1. Відкрийте файли в ./wip",
		"instruction2_rus_eng":  "2. Перекладіть російські значення на англійську",
		"instruction2_eng_rus":  "2. Перекладіть англійські значення на російську",
		"instruction3_rus_eng":  "3. Скопіюйте вміст у відповідні файли в ./english/",
		"instruction3_eng_rus":  "3. Скопіюйте вміст у відповідні файли в ./russian/",
		"cleaning_wip":          "Очищення існуючої директорії ./wip...",
		"select_function":       "Оберіть функцію:",
		"option_check":          "1. Перевірка (Check) - перевірити повноту локалізації",
		"option_create":         "2. Створення (Create) - створити файли для перекладу",
		"option_both":           "3. Обидва (Both) - спочатку перевірка, потім створення",
		"select_direction":      "Оберіть напрямок порівняння:",
		"direction_rus_eng":     "1. RUS → ENG - знайти ключі, відсутні в англійській",
		"direction_eng_rus":     "2. ENG → RUS - знайти ключі, відсутні в російській",
	}
)

func showBanner() {
	fmt.Println(strings.Repeat("=", 65))
	fmt.Printf("  HOI4 Localization Tool v%s\n", version)
	fmt.Printf("  Created by: %s%s%s\n", Green, author, Reset)
	fmt.Printf("  Originally made for: %s%s%s\n", Blue, project, Reset)
	fmt.Printf("  License: %s\n", license)
	fmt.Println()
	fmt.Printf("  %s%s%s\n", Yellow, motto, Reset)
	fmt.Println(strings.Repeat("=", 65))
	fmt.Println()
}

func readInput(reader *bufio.Reader) string {
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(strings.ToLower(input))
}

func main() {
	benchFlag := flag.Bool("bench", false, "Show benchmark timing")
	reportFlag := flag.Bool("report", false, "Write detailed report to file")
	flag.Parse()

	showBanner()

	reader := bufio.NewReader(os.Stdin)

	// Language selection
	fmt.Println("Choose language / Выберите язык / Оберіть мову:")
	fmt.Println("  1. English")
	fmt.Println("  2. Русский (Russian)")
	fmt.Println("  3. Українська (Ukrainian)")
	fmt.Println()

	var ui map[string]string
	for {
		fmt.Print("Enter choice (1/2/3 or en/ru/ua): ")
		input := readInput(reader)
		switch input {
		case "1", "en", "eng", "english":
			ui = uiEN
		case "2", "ru", "rus", "russian":
			ui = uiRU
		case "3", "ua", "ukr", "ukrainian":
			ui = uiUA
		default:
			fmt.Printf("%sInvalid choice. Please enter 1, 2, 3, en, ru, or ua%s\n", Red, Reset)
			continue
		}
		break
	}
	fmt.Println()

	// Direction selection
	fmt.Println(ui["select_direction"])
	fmt.Printf("  %s\n", ui["direction_rus_eng"])
	fmt.Printf("  %s\n", ui["direction_eng_rus"])
	fmt.Println()

	var direction Direction
	for {
		fmt.Print("Enter choice (1/2): ")
		input := readInput(reader)
		switch input {
		case "1", "rus", "r":
			direction = RusToEng
		case "2", "eng", "e":
			direction = EngToRus
		default:
			fmt.Printf("%sInvalid choice. Please enter 1 or 2%s\n", Red, Reset)
			continue
		}
		break
	}
	fmt.Println()

	// Function selection
	fmt.Println(ui["select_function"])
	fmt.Printf("  %s\n", ui["option_check"])
	fmt.Printf("  %s\n", ui["option_create"])
	fmt.Printf("  %s\n", ui["option_both"])
	fmt.Println()

	for {
		fmt.Print("Enter choice (1/2/3 or check/create/both): ")
		input := readInput(reader)

		var exitCode int
		switch input {
		case "1", "check":
			fmt.Println()
			_, err := CheckLocalization(ui, direction, *reportFlag, *benchFlag)
			if err != nil {
				fmt.Printf("%s%v%s\n", Red, err, Reset)
				exitCode = 1
			}
		case "2", "create":
			// For create mode, we need to run check first (silently or not)
			fmt.Println()
			fmt.Printf("%sRunning check first to gather missing keys...%s\n\n", Blue, Reset)
			result, err := CheckLocalization(ui, direction, false, false)
			if err != nil {
				fmt.Printf("%s%v%s\n", Red, err, Reset)
				exitCode = 1
			} else if len(result.MissingKeys) == 0 {
				fmt.Printf("%sNo missing keys to create WIP files for!%s\n", Green, Reset)
			} else {
				fmt.Println()
				err = CreateWIPFiles(ui, result, *benchFlag)
				if err != nil {
					fmt.Printf("%s%v%s\n", Red, err, Reset)
					exitCode = 1
				}
			}
		case "3", "both":
			fmt.Println()
			result, err := CheckLocalization(ui, direction, *reportFlag, *benchFlag)
			if err != nil {
				fmt.Printf("%s%v%s\n", Red, err, Reset)
				exitCode = 1
			} else if len(result.MissingKeys) > 0 {
				fmt.Println()
				err = CreateWIPFiles(ui, result, *benchFlag)
				if err != nil {
					fmt.Printf("%s%v%s\n", Red, err, Reset)
					exitCode = 1
				}
			}
		default:
			fmt.Printf("%sInvalid choice. Please enter 1, 2, 3, check, create, or both%s\n", Red, Reset)
			continue
		}

		fmt.Println()
		fmt.Print("Press Enter to exit...")
		reader.ReadString('\n')
		os.Exit(exitCode)
	}
}
