package org.main;

import javafx.stage.DirectoryChooser;
import javafx.stage.Window;
import javafx.scene.control.TextField;

import java.io.File;

public class DirectoryChooserHelper {

    public static void chooseDirectory(TextField targetField) {
        DirectoryChooser directoryChooser = new DirectoryChooser();
        directoryChooser.setTitle("Select Directory");
        File selectedDirectory = directoryChooser.showDialog(null);
        if (selectedDirectory != null) {
            targetField.setText(selectedDirectory.getAbsolutePath());
        }
    }
}
