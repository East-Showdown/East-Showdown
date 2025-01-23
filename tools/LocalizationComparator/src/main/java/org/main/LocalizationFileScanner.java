package org.main;

import java.io.IOException;
import java.nio.file.*;
import java.util.ArrayList;
import java.util.List;

public class LocalizationFileScanner {

    public List<Path> scanLocalizationFiles(String directory) throws IOException {
        List<Path> yamlFiles = new ArrayList<>();
        Files.walk(Paths.get(directory))
                .filter(path -> Files.isRegularFile(path) && path.toString().endsWith(".yml"))
                .forEach(yamlFiles::add);
        return yamlFiles;
    }
}
