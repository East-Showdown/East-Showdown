package org.main;

import java.nio.file.Path;
import java.util.Objects;

public class FilePair {
    private Path rusFile;
    private Path engFile;

    public FilePair(Path rusFile, Path engFile) {
        this.rusFile = rusFile;
        this.engFile = engFile;
    }

    public Path getRusFile() {
        return rusFile;
    }

    public Path getEngFile() {
        return engFile;
    }

    @Override
    public String toString() {
        return rusFile.getFileName() + " ⇔ " + engFile.getFileName();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        FilePair filePair = (FilePair) o;
        return Objects.equals(rusFile, filePair.rusFile) && Objects.equals(engFile, filePair.engFile);
    }

    @Override
    public int hashCode() {
        return Objects.hash(rusFile, engFile);
    }
}
