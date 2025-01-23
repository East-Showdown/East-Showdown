package org.main;

import java.io.*;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

public class Settings {

    private String vscodePath;
    private String notepadPlusPlusPath;
    private String notepadPath;
    private String preferredEditor;
    private String theme;
    private boolean rememberRusDir;
    private boolean rememberEngDir;
    private String rusDir;
    private String engDir;


    private Map<String, String> translationExceptions = new HashMap<>();

    private static final String SETTINGS_FILE = "settings.properties";

    public Settings() {
        loadSettings();
    }

    public void loadSettings() {
        Properties properties = new Properties();
        try (InputStream input = new FileInputStream(SETTINGS_FILE)) {
            properties.load(input);
            vscodePath = properties.getProperty("vscodePath", "");
            notepadPlusPlusPath = properties.getProperty("notepadPlusPlusPath", "");
            notepadPath = properties.getProperty("notepadPath", "notepad");
            preferredEditor = properties.getProperty("preferredEditor", "Notepad");
            theme = properties.getProperty("theme", "Светлая");
            rememberRusDir = Boolean.parseBoolean(properties.getProperty("rememberRusDir", "false"));
            rememberEngDir = Boolean.parseBoolean(properties.getProperty("rememberEngDir", "false"));
            rusDir = properties.getProperty("rusDir", "");
            engDir = properties.getProperty("engDir", "");


            for (String key : properties.stringPropertyNames()) {
                if (key.startsWith("exception.")) {
                    String exceptionKey = key.substring("exception.".length());
                    translationExceptions.put(exceptionKey, properties.getProperty(key));
                }
            }

        } catch (IOException ex) {
            vscodePath = "";
            notepadPlusPlusPath = "";
            notepadPath = "";
            preferredEditor = "Notepad";
            theme = "Светлая";
        }
    }

    public void saveSettings() {
        Properties properties = new Properties();
        properties.setProperty("vscodePath", vscodePath);
        properties.setProperty("notepadPlusPlusPath", notepadPlusPlusPath);
        properties.setProperty("notepadPath", notepadPath);
        properties.setProperty("preferredEditor", preferredEditor);
        properties.setProperty("theme", theme);
        properties.setProperty("rememberRusDir", String.valueOf(rememberRusDir));
        properties.setProperty("rememberEngDir", String.valueOf(rememberEngDir));
        properties.setProperty("rusDir", rusDir);
        properties.setProperty("engDir", engDir);


        for (Map.Entry<String, String> entry : translationExceptions.entrySet()) {
            properties.setProperty("exception." + entry.getKey(), entry.getValue());
        }

        try (OutputStream output = new FileOutputStream(SETTINGS_FILE)) {
            properties.store(output, null);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public String getVscodePath() {
        return vscodePath;
    }

    public void setVscodePath(String vscodePath) {
        this.vscodePath = vscodePath;
    }

    public String getNotepadPlusPlusPath() {
        return notepadPlusPlusPath;
    }

    public void setNotepadPlusPlusPath(String notepadPlusPlusPath) {
        this.notepadPlusPlusPath = notepadPlusPlusPath;
    }

    public String getNotepadPath() {
        return notepadPath;
    }

    public void setNotepadPath(String notepadPath) {
        this.notepadPath = notepadPath;
    }

    public String getPreferredEditor() {
        return preferredEditor;
    }

    public void setPreferredEditor(String preferredEditor) {
        this.preferredEditor = preferredEditor;
    }

    public String getTheme() {
        return theme;
    }

    public void setTheme(String theme) {
        this.theme = theme;
    }

    public Map<String, String> getTranslationExceptions() {
        return translationExceptions;
    }

    public boolean getRememberRusDir() {
        return rememberRusDir;
    }

    public void setRememberRusDir(boolean rememberRusDir) {
        this.rememberRusDir = rememberRusDir;
    }

    public boolean getRememberEngDir() {
        return rememberEngDir;
    }

    public void setRememberEngDir(boolean rememberEngDir) {
        this.rememberEngDir = rememberEngDir;
    }

    public String getRusDir() {
        return rusDir;
    }

    public void setRusDir(String rusDir) {
        this.rusDir = rusDir;
    }

    public String getEngDir() {
        return engDir;
    }

    public void setEngDir(String engDir) {
        this.engDir = engDir;
    }


    public String getTranslationExceptionsAsString() {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, String> entry : translationExceptions.entrySet()) {
            sb.append(entry.getKey()).append("=").append(entry.getValue()).append("\n");
        }
        return sb.toString();
    }

    public void setTranslationExceptionsFromString(String exceptionsString) {
        translationExceptions.clear();
        String[] lines = exceptionsString.split("\\n");
        for (String line : lines) {
            if (line.contains("=")) {
                String[] parts = line.split("=", 2);
                translationExceptions.put(parts[0].trim(), parts[1].trim());
            }
        }
    }

    public void loadTranslationExceptionsFromFile(String filePath) {
        Properties properties = new Properties();
        try (InputStream input = new FileInputStream(filePath)) {
            properties.load(input);
            translationExceptions.clear();
            for (String key : properties.stringPropertyNames()) {
                translationExceptions.put(key, properties.getProperty(key));
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}
