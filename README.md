# East-Showdown

## READ THIS

Dear friends and mod subscribers! We ask for a moment of your attention.
Today a rather unusual incident happened involving us, namely: Polish television featured our mod. Unfortunately, not in the way we would have liked to see it.

When we were working on Poland, we never had any intention of offending anyone. The non-historical focus branches and the possibility of bringing radicals to power are a fictional concept, created solely for gameplay purposes as an alternative reality. We would like to offer our sincere apologies to the entire Polish nation!

The created focus branches were developed exclusively by the Ukrainian part of the team, which conducted clarifying discussions and consultations with enthusiasts from Poland itself. We all love Poland, and once again we emphasize: we did not want to offend anyone.

The mod was, is, and will remain neutral. We strongly condemn the events / certain individuals represented in the game, and their mentions are used solely for informational purposes.

---

[![HOI4 Version](https://img.shields.io/badge/HOI4-1.17.*-blue.svg)](https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/)
[![Steam Workshop](https://img.shields.io/badge/Steam-Workshop-green.svg)](https://steamcommunity.com/sharedfiles/filedetails/?id=2948642461)
[![License](https://img.shields.io/badge/license-EPL--2.0-orange.svg)](LICENSE)

Комплексная модификация-конверсия для Hearts of Iron IV. Мод разрабатывается на русском языке с переводом на английский и украинский.

---

## 🇷🇺 Русский

### Установка

1. Скопируйте папку `East-Showdown` в:
   ```
   Документы\Paradox Interactive\Hearts of Iron IV\mod
   ```

2. Скопируйте файл `descriptor.mod` из папки мода в папку `mod` (на уровень выше) и переименуйте его в `East-Showdown.mod`

3. Откройте `East-Showdown.mod` и добавьте в конец строку:
   ```
   path="C:/Users/ВашеИмя/Documents/Paradox Interactive/Hearts of Iron IV/mod/East-Showdown"
   ```
   **Важно:** Используйте `/` вместо `\` и убедитесь что в пути **нет кириллицы**

4. Запустите игру и активируйте мод в лаунчере

### Устранение проблем

**Проблема:** При запуске мода загружается обычная игра

**Причины:**
- В пути есть **кириллица** (русские/украинские буквы)
- Используются `\` вместо `/` в пути
- Неправильный путь к папке мода

**Решение:**
1. Откройте файл `East-Showdown.mod` в текстовом редакторе
2. Проверьте строку `path=`:
   ```
   path="C:/Users/Username/Documents/Paradox Interactive/Hearts of Iron IV/mod/East-Showdown"
   ```
3. Убедитесь что:
   - В пути **нет кириллицы** (переместите мод если нужно, например в `D:/East-Showdown`)
   - Все слэши `/`, а не `\`
   - Путь указывает на папку с модом

Если проблема не решилась, обратитесь к сообществу в Discord.

### Для разработчиков

#### Клонирование репозитория

```bash
git clone https://github.com/East-Showdown/East-Showdown.git
```

#### Git Workflow

Рекомендуется использовать **GitHub Desktop** для управления версиями. Если вам не страшна консоль — используйте **Git CLI** :D

Убедитесь, что коммиты содержат осмысленные описания изменений и комментируйте код для других разработчиков.

#### Инструмент локализации

Мод включает ~30,688 ключей локализации на трёх языках. Исходный код инструмента находится в `tools/loc_tool/`.

Подробнее: [`tools/loc_tool/README.md`](tools/loc_tool/README.md)

#### Структура проекта

```
common/           Основные данные игры (фокусы, решения, идеи, ИИ)
events/           События (33 файла)
interface/        UI/GUI
localisation/     Локализация (russian/, english/, ukrainian/)
gfx/              Графические ресурсы (1.4GB)
map/              Данные карты
history/          Стартовые конфигурации стран
tools/            Инструменты разработки
```

---

## 🇬🇧 English

### Installation

1. Copy the `East-Showdown` folder to:
   ```
   Documents\Paradox Interactive\Hearts of Iron IV\mod
   ```

2. Copy `descriptor.mod` from the mod folder to the `mod` folder (one level up) and rename it to `East-Showdown.mod`

3. Open `East-Showdown.mod` and add this line at the end:
   ```
   path="C:/Users/YourName/Documents/Paradox Interactive/Hearts of Iron IV/mod/East-Showdown"
   ```
   **Important:** Use `/` instead of `\` and ensure the path contains **no Cyrillic characters**

4. Launch the game and activate the mod in the launcher

### Troubleshooting

**Issue:** The mod launches vanilla game instead

**Causes:**
- Path contains **Cyrillic characters** (Russian/Ukrainian letters)
- Using `\` instead of `/` in path
- Incorrect path to mod folder

**Solution:**
1. Open `East-Showdown.mod` in a text editor
2. Check the `path=` line:
   ```
   path="C:/Users/Username/Documents/Paradox Interactive/Hearts of Iron IV/mod/East-Showdown"
   ```
3. Ensure:
   - Path has **no Cyrillic characters** (move mod if needed, e.g., to `D:/East-Showdown`)
   - All slashes are `/`, not `\`
   - Path points to the mod folder

If the issue persists, contact the Discord community.

### For Developers

#### Cloning the repository

```bash
git clone https://github.com/East-Showdown/East-Showdown.git
```

#### Git Workflow

We recommend using **GitHub Desktop** for version control. If you're not afraid of the console — use **Git CLI** :D

Ensure commits have meaningful descriptions and comment your code for other developers.

#### Localization tool

The mod includes ~30,688 localization keys across three languages. Source code for the tool is located in `tools/loc_tool/`.

Details: [`tools/loc_tool/README.md`](tools/loc_tool/README.md)

#### Project structure

```
common/           Core game data (focuses, decisions, ideas, AI)
events/           Events (33 files)
interface/        UI/GUI definitions
localisation/     Multi-language text (russian/, english/, ukrainian/)
gfx/              Graphics assets (1.4GB)
map/              Map data
history/          Starting country configurations
tools/            Development tools
```

---

## 📋 Specifications

- **Supported HOI4 version:** 1.17.*
- **Steam Workshop ID:** 2948642461
- **Languages:** Russian (primary), English, Ukrainian
- **Replace paths:** 66 directives replacing base game content

## 🛠️ Development Tools

Located in `tools/`:
- `module_params.py` - Bulk edit tank module parameters
- `bridge_hp_calculator.py` - Calculate bridge/dam HP
- `AudioConverter/` - Audio re-encoding to OGG (ffmpeg)
- `LocalizationComparator/` - Visual localization comparison (Java/JavaFX)

## 📚 Documentation

- [HOI4 Modding Wiki](https://hoi4.paradoxwikis.com/)
- [National Focus Modding](https://hoi4.paradoxwikis.com/National_focus_modding)
- [Event Modding](https://hoi4.paradoxwikis.com/Event_modding)
- [Decision Modding](https://hoi4.paradoxwikis.com/Decision_modding)

## 📝 License

MOD CONTENT LICENSE AND CONTRIBUTOR AGREEMENT

---
