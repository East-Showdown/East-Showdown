package org.main;

import java.nio.file.Path;
import java.nio.file.Paths;

public class MissingKeyEntry {
    private String filePath;
    private String key;
    private String fileName;
    private boolean translated;
    private boolean autoTranslated;

    public MissingKeyEntry(String filePath, String key) {
        this.filePath = filePath;
        this.key = key;
        Path path = Paths.get(filePath);
        this.fileName = path.getFileName().toString();
        this.translated = false;
        this.autoTranslated = false;
    }

    public String getFilePath() {
        return filePath;
    }

    public String getKey() {
        return key;
    }

    public String getFileName() {
        return fileName;
    }

    public boolean isTranslated() {
        return translated;
    }

    public void setTranslated(boolean translated) {
        this.translated = translated;
    }

    public boolean isAutoTranslated() {
        return autoTranslated;
    }

    public void setAutoTranslated(boolean autoTranslated) {
        this.autoTranslated = autoTranslated;
    }

}
