# HOI4 Localization Tool (Go Edition)

быстрая версия `localisation_tool.py` на go. работает в 7x быстрее питона.

## производительность

| версия | время на 30k ключей |
|--------|---------------------|
| Python | ~130ms |
| Go | ~18ms |

## установка go

### macOS

```bash
# homebrew (рекомендуется)
brew install go

# или скачать с https://go.dev/dl/
```

### linux (arch)

```bash
# pacman
sudo pacman -S go

# или yay если используешь AUR
yay -S go
```

### linux (ubuntu/debian)

```bash
# apt (может быть старая версия)
sudo apt install golang-go

# или snap для свежей версии
sudo snap install go --classic

# или скачать с https://go.dev/dl/
wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.0.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

### windows

1. скачай инсталлятор с https://go.dev/dl/ (файл `.msi`)
2. запусти, жми next до конца
3. перезапусти терминал

или через winget:
```powershell
winget install GoLang.Go
```

или через scoop:
```powershell
scoop install go
```

## сборка

```bash
cd localisation/loc_tool
go build -ldflags="-s -w" -o ../loc_tool_go
```

на windows выходной файл будет `loc_tool_go.exe`:
```powershell
cd localisation\loc_tool
go build -ldflags="-s -w" -o ..\loc_tool_go.exe
```

флаги `-ldflags="-s -w"` убирают debug символы для меньшего размера бинарника.

## использование

запускай из директории `localisation/`:

```bash
# обычный режим (интерактивный)
./loc_tool_go

# с бенчмарком времени выполнения
./loc_tool_go -bench

# с записью отчёта в файл
./loc_tool_go -report

# всё вместе
./loc_tool_go -bench -report
```

на windows:
```powershell
.\loc_tool_go.exe
.\loc_tool_go.exe -bench
```

## что делает

1. **check** - сравнивает ключи между локализациями (rus/eng), показывает что не переведено
2. **create** - создаёт файлы в `wip/` с ключами для перевода
3. **both** - check + create за один запуск

## структура проекта

```
loc_tool/
├── go.mod        # go module definition
├── main.go       # cli интерфейс
├── checker.go    # логика проверки локализации
├── creator.go    # создание wip файлов
├── parser.go     # парсинг yml файлов
├── shardmap.go   # concurrent data structures
├── colors.go     # ansi цвета для терминала
└── README.md     # этот файл
```

## troubleshooting

### "go: command not found"
go не в PATH. перезапусти терминал или добавь вручную:
```bash
# linux/mac
export PATH=$PATH:/usr/local/go/bin

# windows - перезапусти powershell
```

### "cannot find package"
запусти из директории `loc_tool/`:
```bash
cd localisation/loc_tool
go build ...
```

### цвета не работают (windows)
используй windows terminal или powershell 7+. старый cmd.exe не поддерживает ansi цвета нормально.

### permission denied (linux/mac)
```bash
chmod +x loc_tool_go
```

## кросс-компиляция

можно собрать бинарник для другой платформы:

```bash
# собрать для windows на mac/linux
GOOS=windows GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go.exe

# собрать для linux на mac/windows
GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_linux

# собрать для mac на linux/windows
GOOS=darwin GOARCH=amd64 go build -ldflags="-s -w" -o loc_tool_go_mac
```

## разработка

если хочешь поменять код:

```bash
cd localisation/loc_tool

# запустить без сборки
go run .

# запустить тесты (если добавишь)
go test ./...

# проверить код
go vet ./...
```
