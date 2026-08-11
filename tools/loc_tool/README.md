# HOI4 Localization Tool (Go Edition)

Быстрая версия `localisation_tool.py` на Go. Работает в **7x быстрее** Python.

---

## 🇷🇺 Русский

### Производительность

| Версия | Время на 30k ключей |
|--------|---------------------|
| Python | ~130ms              |
| Go     | ~18ms               |

### Что делает

Инструмент для проверки полноты локализации модов Hearts of Iron IV:

1. **Check** — сравнивает ключи между локализациями (rus/eng), показывает что не переведено
2. **Create** — создаёт файлы в `wip/` с ключами для перевода
3. **Both** — выполняет Check + Create за один запуск

### Скачать готовую версию

**Не хочешь собирать?** Скачай готовый бинарник для своей платформы:

👉 [Скачать релиз](https://github.com/iAmScienceMan/localisation-tool/releases/latest)

Доступны версии для Windows, Linux и macOS (Intel/Apple Silicon).

### Установка Go

#### macOS
```bash
# Homebrew (рекомендуется)
brew install go
```

#### Linux (Arch)
```bash
sudo pacman -S go
```

#### Linux (Ubuntu/Debian)
```bash
# Snap для свежей версии
sudo snap install go --classic

# Или вручную
wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.0.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

#### Windows
```powershell
# WinGet
winget install GoLang.Go

# Или Scoop
scoop install go
```

Или скачай инсталлятор `.msi` с https://go.dev/dl/

### Сборка

```bash
go build -ldflags="-s -w" -o loc_tool_go
```

На Windows:
```powershell
go build -ldflags="-s -w" -o loc_tool_go.exe
```

Флаги `-ldflags="-s -w"` убирают debug-символы для меньшего размера.

### Использование

Запускай из директории с папками `russian/` и `english/`:

```bash
# Обычный режим (интерактивный)
./loc_tool_go

# С бенчмарком времени выполнения
./loc_tool_go -bench

# С записью отчёта в файл
./loc_tool_go -report

# Всё вместе
./loc_tool_go -bench -report
```

### Структура проекта

```
loc_tool/
├── main.go       # CLI интерфейс
├── checker.go    # Логика проверки локализации
├── creator.go    # Создание WIP файлов
├── parser.go     # Парсинг YML файлов
├── shardmap.go   # Concurrent data structures
└── colors.go     # ANSI цвета для терминала
```

### Разработка

```bash
# Запустить без сборки
go run .

# Запустить тесты
go test ./...

# Проверить код
go vet ./...
```

### Кросс-компиляция

```bash
# Собрать для Windows на Mac/Linux
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go.exe

# Собрать для Linux на Mac/Windows
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_linux

# Собрать для Mac на Linux/Windows
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_mac
```

### Troubleshooting

**"go: command not found"**
Go не в PATH. Перезапусти терминал или добавь вручную:
```bash
export PATH=$PATH:/usr/local/go/bin
```

**"cannot find package"**
Убедись, что запускаешь из директории с `go.mod`:
```bash
cd localisation-tool
go build ...
```

**Цвета не работают (Windows)**
Используй Windows Terminal или PowerShell 7+. Старый cmd.exe плохо поддерживает ANSI.

**Permission denied (Linux/Mac)**
```bash
chmod +x loc_tool_go
```

---

## 🇬🇧 English

### Performance

| Version | Time for 30k keys |
|---------|-------------------|
| Python  | ~130ms            |
| Go      | ~18ms             |

### What it does

Tool for checking Hearts of Iron IV mod localization completeness:

1. **Check** — compares keys between localizations (rus/eng), shows untranslated keys
2. **Create** — generates files in `wip/` with keys needing translation
3. **Both** — runs Check + Create in one pass

### Download Pre-built Binary

**Don't want to build?** Download a ready-to-use binary for your platform:

👉 [Download Latest Release](https://github.com/iAmScienceMan/localisation-tool/releases/latest)

Available for Windows, Linux, and macOS (Intel/Apple Silicon).

### Installing Go

#### macOS
```bash
# Homebrew (recommended)
brew install go
```

#### Linux (Arch)
```bash
sudo pacman -S go
```

#### Linux (Ubuntu/Debian)
```bash
# Snap for latest version
sudo snap install go --classic

# Or manually
wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.0.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

#### Windows
```powershell
# WinGet
winget install GoLang.Go

# Or Scoop
scoop install go
```

Or download the `.msi` installer from https://go.dev/dl/

### Building

```bash
go build -ldflags="-s -w" -o loc_tool_go
```

On Windows:
```powershell
go build -ldflags="-s -w" -o loc_tool_go.exe
```

The `-ldflags="-s -w"` flags strip debug symbols for smaller binary size.

### Usage

Run from a directory containing `russian/` and `english/` folders:

```bash
# Interactive mode
./loc_tool_go

# With execution time benchmark
./loc_tool_go -bench

# With detailed report file
./loc_tool_go -report

# Both options
./loc_tool_go -bench -report
```

### Project structure

```
loc_tool/
├── main.go       # CLI interface
├── checker.go    # Localization checking logic
├── creator.go    # WIP file creation
├── parser.go     # YML file parsing
├── shardmap.go   # Concurrent data structures
└── colors.go     # ANSI terminal colors
```

### Development

```bash
# Run without building
go run .

# Run tests
go test ./...

# Check code
go vet ./...
```

### Cross-compilation

```bash
# Build for Windows on Mac/Linux
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go.exe

# Build for Linux on Mac/Windows
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_linux

# Build for Mac on Linux/Windows
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_mac
```

### Troubleshooting

**"go: command not found"**
Go is not in PATH. Restart terminal or add manually:
```bash
export PATH=$PATH:/usr/local/go/bin
```

**"cannot find package"**
Make sure you're running from the directory with `go.mod`:
```bash
cd localisation-tool
go build ...
```

**Colors not working (Windows)**
Use Windows Terminal or PowerShell 7+. Old cmd.exe has poor ANSI support.

**Permission denied (Linux/Mac)**
```bash
chmod +x loc_tool_go
```

---

## 📝 License

MIT

## 👤 Author

**iAmScienceMan**
Originally created for: **East-Showdown**

*Femboys rule the world*
