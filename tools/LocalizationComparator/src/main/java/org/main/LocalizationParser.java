package org.main;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LocalizationParser {

    private static final Logger logger = LoggerFactory.getLogger(LocalizationParser.class);

    public Set<String> parseKeys(Path filePath) throws IOException {
        Set<String> keys = new HashSet<>();
        logger.debug("Начало парсинга файла: {}", filePath.toString());

        List<String> lines = Files.readAllLines(filePath, StandardCharsets.UTF_8);
        String currentLanguage = null;

        Pattern pattern = Pattern.compile("^([A-Za-z0-9_.-]+):([0-9]+)?\\s*\"(.*)\"$");

        for (int i = 0; i < lines.size(); i++) {
            String line = lines.get(i).trim();

            if (i == 0) {
                line = removeBOM(line);
            }

            if (line.isEmpty() || line.startsWith("#")) {
                continue;
            }

            if (line.endsWith(":") && line.startsWith("l_")) {
                currentLanguage = line.substring(0, line.length() - 1);
                logger.debug("Установлен текущий язык: {}", currentLanguage);
                continue;
            }

            Matcher matcher = pattern.matcher(line);
            if (matcher.matches()) {
                String key = matcher.group(1);
                String version = matcher.group(2);
                String value = matcher.group(3);

                if (isValidKey(key)) {
                    String fullKey = currentLanguage + "." + key;
                    keys.add(fullKey);
                    logger.debug("Найден ключ: {}", fullKey);
                } else {
                    logger.warn("Некорректный ключ: {} в файле {}", key, filePath.toString());
                }

                if (!isValidValue(value)) {
                    logger.warn("Некорректное значение для ключа {}: {}", key, value);
                }

                if (!validateColoring(value)) {
                    logger.warn("Некорректное форматирование цвета в ключе {}: {}", key, value);
                }

                if (!validateVariables(value)) {
                    logger.warn("Некорректное форматирование переменных в ключе {}: {}", key, value);
                }

                handleNestedKeys(value);
            } else {
                logger.warn("Строка не соответствует ожидаемому формату: {} (файл: {}, строка: {})",
                        line, filePath.toString(), i + 1);
            }
        }

        logger.debug("Завершение парсинга файла: {}", filePath.toString());
        return keys;
    }

    private String removeBOM(String line) {
        final String UTF8_BOM = "\uFEFF";
        if (line.startsWith(UTF8_BOM)) {
            logger.debug("BOM обнаружен и удалён из строки.");
            return line.substring(1);
        }
        return line;
    }

    private boolean isValidKey(String key) {
        return key.matches("^[A-Za-z0-9_.-]+$");
    }

    private boolean isValidValue(String value) {
        return !value.contains("\n");
    }

    private boolean validateColoring(String value) {
        Pattern pattern = Pattern.compile("§[A-Za-z0-9]!");
        Matcher matcher = pattern.matcher(value);
        int lastMatchEnd = 0;
        while (matcher.find()) {
            lastMatchEnd = matcher.end();
        }
        if (lastMatchEnd < value.length()) {
            return false;
        }
        return true;
    }

    private boolean validateVariables(String value) {
        Pattern pattern = Pattern.compile("\\[\\?\\w+\\|[\\w\\.]+\\]");
        Matcher matcher = pattern.matcher(value);
        while (matcher.find()) {
            String var = matcher.group();
        }
        return true;
    }

    private void handleNestedKeys(String value) {
        Pattern pattern = Pattern.compile("\\$(\\w+)\\$");
        Matcher matcher = pattern.matcher(value);
        while (matcher.find()) {
            String nestedKey = matcher.group(1);
            logger.debug("Обнаружен вложенный ключ: {}", nestedKey);
        }
    }
}
