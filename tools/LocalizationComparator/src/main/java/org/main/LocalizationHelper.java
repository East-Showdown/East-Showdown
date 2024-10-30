package org.main;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class LocalizationHelper {

    private static final Pattern keyValuePattern = Pattern.compile("^([A-Za-z0-9_.-]+):(?:([0-9]+)\\s*)?\\s*\"(.*)\"$");

    public static Map<String, String> extractLocalization(Path filePath) throws IOException {
        Map<String, String> localizationMap = new HashMap<>();
        List<String> lines = Files.readAllLines(filePath, StandardCharsets.UTF_8);
        String currentLanguage = null;

        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i);

            if (i == 0) {
                line = removeBOM(line);
            }

            System.out.println("Обработка строки: " + line);

            line = line.trim();

            if (line.isEmpty() || line.startsWith("#")) {
                System.out.println("Пропуск пустой или комментария.");
                continue;
            }

            if (line.endsWith(":") && line.startsWith("l_")) {
                currentLanguage = line.substring(0, line.length() - 1);
                System.out.println("Установлен текущий язык: " + currentLanguage);
                continue;
            }

            Matcher matcher = keyValuePattern.matcher(line);
            if (matcher.matches()) {
                String key = matcher.group(1);
                String version = matcher.group(2);
                String value = matcher.group(3);
                String fullKey = currentLanguage + "." + key;
                localizationMap.put(fullKey, value);
                System.out.println("Добавлен ключ: " + fullKey + " со значением: " + value);
            } else {
                System.out.println("Строка не соответствует формату: " + line);
            }
        }

        System.out.println("Все ключи в карте локализаций:");
        for (String key : localizationMap.keySet()) {
            System.out.println(key);
        }

        return localizationMap;
    }

    public static String fetchRussianValue(String filePath, String key) throws IOException {
        Path path = Paths.get(filePath);
        Map<String, String> localization = extractLocalization(path);
        System.out.println("Поиск значения для ключа: " + key);

        if (localization.containsKey(key)) {
            System.out.println("Значение найдено: " + localization.get(key));
        } else {
            System.out.println("Значение для ключа не найдено.");
        }

        return localization.getOrDefault(key, null);
    }

    public static String fetchEnglishValue(String filePath, String key) throws IOException {
        Path path = Paths.get(filePath);
        if (!Files.exists(path)) {
            return null;
        }
        Map<String, String> localization = extractLocalization(path);
        return localization.getOrDefault(key, null);
    }

    public static void saveEnglishTranslation(Path engFilePath, String key, String translation, boolean includeVersion) throws IOException {
        List<String> lines = new ArrayList<>();
        String languagePrefix = "l_english:";

        if (Files.exists(engFilePath)) {
            lines = Files.readAllLines(engFilePath, StandardCharsets.UTF_8);
        } else {
            lines.add(languagePrefix);
        }

        boolean keyFound = false;
        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i).trim();
            if (line.startsWith(languagePrefix)) {
                continue;
            }
            String existingKey = null;
            if (line.contains(":")) {
                existingKey = line.substring(0, line.indexOf(":")).trim();
            }
            if (key.equals(existingKey)) {
                String versionPart = includeVersion ? ":0" : ":";
                lines.set(i, key + versionPart + " \"" + translation + "\"");
                keyFound = true;
                break;
            }
        }

        if (!keyFound) {
            String versionPart = includeVersion ? ":0" : ":";
            lines.add(key + versionPart + " \"" + translation + "\"");
        }

        Files.write(engFilePath, lines, StandardCharsets.UTF_8, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
    }

    private static String removeBOM(String line) {
        final String UTF8_BOM = "\uFEFF";
        if (line.startsWith(UTF8_BOM)) {
            return line.substring(1);
        }
        return line;
    }

}
