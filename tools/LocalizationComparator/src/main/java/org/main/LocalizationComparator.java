package org.main;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class LocalizationComparator {

    private final LocalizationParser parser = new LocalizationParser();
    private List<FilePair> filePairs = new ArrayList<>();
    private List<Path> unmatchedRusFiles = new ArrayList<>();

    public void setFilePairs(List<FilePair> filePairs) {
        this.filePairs = filePairs;
    }

    public List<FilePair> getFilePairs() {
        return filePairs;
    }

    public boolean hasUnmatchedRusFiles() {
        return !unmatchedRusFiles.isEmpty();
    }

    public List<Path> getMissingEnglishFiles(String engDir) {
        List<Path> missingEngFiles = new ArrayList<>();
        for (Path rusFile : unmatchedRusFiles) {
            String engFileName = rusFile.getFileName().toString().replace("_l_russian.yml", "_l_english.yml");
            Path engFilePath = Paths.get(engDir, engFileName);
            if (!Files.exists(engFilePath)) {
                missingEngFiles.add(engFilePath);
            }
        }
        return missingEngFiles;
    }

    public Map<Path, Set<String>> findMissingKeys(List<Path> russianFiles, List<Path> englishFiles) throws IOException {
        Map<Path, Set<String>> missingKeysMap = new HashMap<>();
        unmatchedRusFiles.clear();

        if (!filePairs.isEmpty()) {
            for (FilePair pair : filePairs) {
                Path rusFile = pair.getRusFile();
                Path engFile = pair.getEngFile();

                Set<String> rusKeys = parser.parseKeys(rusFile);
                Set<String> engKeys = parser.parseKeys(engFile);

                Set<String> normalizedRusKeys = removeLanguagePrefix(rusKeys, "l_russian.");
                Set<String> normalizedEngKeys = removeLanguagePrefix(engKeys, "l_english.");

                Set<String> missingKeys = new HashSet<>(normalizedRusKeys);
                missingKeys.removeAll(normalizedEngKeys);

                if (!missingKeys.isEmpty()) {
                    missingKeysMap.put(rusFile, missingKeys);
                }
            }
        } else {
            Map<String, Set<String>> englishKeyMap = new HashMap<>();
            for (Path engFile : englishFiles) {
                String fileName = engFile.getFileName().toString();
                Set<String> keys = parser.parseKeys(engFile);

                Set<String> normalizedEngKeys = removeLanguagePrefix(keys, "l_english.");
                englishKeyMap.put(fileName, normalizedEngKeys);
            }

            for (Path rusFile : russianFiles) {
                String rusFileName = rusFile.getFileName().toString();
                Set<String> rusKeys = parser.parseKeys(rusFile);

                Set<String> normalizedRusKeys = removeLanguagePrefix(rusKeys, "l_russian.");

                String engFileName = matchEnglishFile(rusFileName, englishFiles);
                if (engFileName != null && englishKeyMap.containsKey(engFileName)) {
                    Set<String> engKeys = englishKeyMap.get(engFileName);
                    Set<String> missing = new HashSet<>(normalizedRusKeys);
                    missing.removeAll(engKeys);
                    if (!missing.isEmpty()) {
                        missingKeysMap.put(rusFile, missing);
                    }
                } else {
                    missingKeysMap.put(rusFile, normalizedRusKeys);
                    unmatchedRusFiles.add(rusFile);
                }
            }
        }

        return missingKeysMap;
    }

    private Set<String> removeLanguagePrefix(Set<String> keys, String prefix) {
        Set<String> normalizedKeys = new HashSet<>();
        for (String key : keys) {
            normalizedKeys.add(key.replace(prefix, ""));
        }
        return normalizedKeys;
    }

    public String matchEnglishFile(String rusFileName, List<Path> englishFiles) {
        String rusBaseName = rusFileName.replace("_l_russian.yml", "").replace("_l_russian.yml", "");

        for (Path engFile : englishFiles) {
            String engFileName = engFile.getFileName().toString();
            String engBaseName = engFileName.replace("_l_english.yml", "").replace("_l_english.yml", "");

            if (engBaseName.equals(rusBaseName)) {
                return engFileName;
            }
        }
        return null;
    }
}
