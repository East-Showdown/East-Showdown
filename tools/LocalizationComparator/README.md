# Руководство по Началу Работы (Getting Started)

Localization Comparator – инструмент для автоматизации и упрощения процесса локализации файлов игры Hearts of Iron IV.

# 
## Требования к системе

Перед началом убедитесь, что ваш компьютер соответствует следующим требованиям: <br>
**Операционная система**: Windows 10 или выше <br>
**Java**: JDK 17 или выше <br>
**Docker**: Установлен Docker Desktop (Необязательно) <br>
**Интернет-соединение**: Для работы LibreTranslate (Необязательно) <br>

## Установка Docker

**Docker** необходим для локального развертывания **LibreTranslate**, используемого программой для автоматического перевода. 
> [!NOTE]
> **Однако для работы программы он необязателен.** 

### Шаг 1: Скачивание Docker Desktop

1. Перейдите на официальный сайт Docker: https://www.docker.com/products/docker-desktop <br>
2. Нажмите кнопку "**Download Docker Desktop for Windows**".

![image](https://github.com/user-attachments/assets/b5bd6d4c-6cf6-45ec-9be0-2603dcef89de)

### Шаг 2: Установка Docker Desktop

1. Запустите скачанный установочный файл ```Docker Desktop Installer.exe```.
2. Следуя инструкциям выполните установку файла.
3. После завершения установки перезагрузите компьютер, если это требуется.

## Запуск LibreTranslate через Docker

**LibreTranslate** – это бесплатный сервис перевода, который будет использоваться программой для автоматического перевода локализаций.

![image](https://github.com/user-attachments/assets/d2957a07-8abe-4bce-bc26-0046bef339e0)

### Шаг 1: Скачивание и запуск Docker образа LibreTranslate

1. Откройте командную строку (CMD).
2. Введите следующую команду для скачивания и запуска LibreTranslate:
```Ruby
docker run -d -p 5000:5000 libretranslate/libretranslate --languages ru,en
```
```-d``` запускает контейнер в фоновом режиме. <br>
```-p``` 5000:5000 пробрасывает порт 5000 из контейнера на ваш локальный компьютер. <br> 
```libretranslate/libretranslate``` – имя Docker образа. <br>

![image](https://github.com/user-attachments/assets/77ed794a-0854-43c9-ac5b-859f2df54a68)

### Шаг 2: Проверка работы LibreTranslate

1. Откройте веб-браузер и перейдите по адресу: ```http://localhost:5000```
2. Вы должны увидеть интерфейс LibreTranslate с возможностью ввода текста для перевода.

## Запуск программы Localization Comparator
Теперь, когда Docker и LibreTranslate настроены, можно запускать программу Localization Comparator.

### Запуск программы через командную строку
1. Откройте командную строку (CMD).
2. Введите следующую команду для запуска JAR-файла программы:
```Ruby
java --module-path C:\HOI4-AutoLoc\Loc-issues-resolver\out\artifacts\localization_comparator_jar\javafx-sdk-21.0.2\lib --add-modules ALL-MODULE-PATH -jar C:\HOI4-AutoLoc\Loc-issues-resolver\out\artifacts\localization_comparator_jar\localization-comparator.jar
```
**Пояснение**: <br> 
```--module-path``` указывает путь к JavaFX SDK библиотекам. <br> 
```--add-modules ALL-MODULE-PATH``` добавляет все модули из указанного пути. <br> 
```-jar``` запускает указанный JAR-файл. <br> 

> [!IMPORTANT]
> Убедитесь, что пути в команде соответствуют вашему расположению файлов. Если JavaFX SDK находится в другом месте, замените путь соответственно.

### Альтернативный способ запуска (скриптовый)
Вы можете создать скрипт для упрощения запуска:
1. Создайте файл ```run.bat``` в корневой директории проекта ```C:\HOI4-AutoLoc\Loc-issues-resolver```.
2. Вставьте в файл следующий код:
```Ruby
@echo off
java --module-path C:\HOI4-AutoLoc\Loc-issues-resolver\out\artifacts\localization_comparator_jar\javafx-sdk-21.0.2\lib --add-modules ALL-MODULE-PATH -jar C:\HOI4-AutoLoc\Loc-issues-resolver\out\artifacts\localization_comparator_jar\localization-comparator.jar
pause
```
3. Сохраните файл и откройте его.

![image](https://github.com/user-attachments/assets/70b47c15-947d-4f6b-b7bd-4fd1da6101b8)

## Решение распространённых проблем.
### Проблема: JavaFX runtime components are missing
**Сообщение об ошибке**:
```Ruby
JavaFX runtime components are missing, and are required to run this application
```
**Решение:**
Проверьте пути: <br> 

Убедитесь, что путь к JavaFX SDK указан правильно в команде запуска.<br> 
Убедитесь, что все необходимые библиотеки JavaFX (```javafx.controls```, ```javafx.fxml``` и т.д.) находятся в указанной директории.<br> 

### Проблема: LibreTranslate не запускается
Если LibreTranslate не доступен по адресу http://localhost:5000, убедитесь, что Docker контейнер запущен.<br> 
**Решение:**

1. Проверьте статус Docker контейнера:<br> 
```Ruby
docker ps
```
Вы должны увидеть запущенный контейнер LibreTranslate.<br> 

2. Если контейнер не запущен, перезапустите его:<br> 
```Ruby
docker run -d -p 5000:5000 libretranslate/libretranslate
```
3. Проверьте логи контейнера для выявления ошибок:
```Ruby
docker logs <container_id>
```
Замените ```<container_id>```  на ID вашего контейнера.















