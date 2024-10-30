package org.main;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.layout.*;
import javafx.stage.*;

import java.io.File;

public class SettingsView implements SettingsChangeListener{

    private Stage stage;
    private TextField vscodePathField;
    private TextField notepadPlusPlusPathField;
    private TextField notepadPathField;
    private ChoiceBox<String> preferredEditorChoiceBox;
    private ChoiceBox<String> themeChoiceBox;

    private Settings settings;

    public SettingsView(Settings settings) {
        this.settings = settings;
        this.settings = settings;
        setupUI();
        applyTheme(settings.getTheme());
        SettingsChangeListener.addListener(this);
    }

    private void setupUI() {
        stage = new Stage();
        stage.setTitle("Настройки");
        stage.getIcons().add(new Image("logo.ico"));
        stage.initModality(Modality.APPLICATION_MODAL);
        VBox root = new VBox(10);
        root.setPadding(new Insets(10));
        vscodePathField = new TextField();
        vscodePathField.setText(settings.getVscodePath());
        Button browseVsCodeButton = new Button("Обзор");
        notepadPlusPlusPathField = new TextField();
        notepadPlusPlusPathField.setText(settings.getNotepadPlusPlusPath());
        Button browseNotepadPlusPlusButton = new Button("Обзор");
        notepadPathField = new TextField();
        notepadPathField.setText(settings.getNotepadPath());
        Button browseNotepadButton = new Button("Обзор");
        preferredEditorChoiceBox = new ChoiceBox<>();
        preferredEditorChoiceBox.getItems().addAll("Visual Studio Code", "Notepad++", "Notepad");
        preferredEditorChoiceBox.setValue(settings.getPreferredEditor());
        themeChoiceBox = new ChoiceBox<>();
        themeChoiceBox.getItems().addAll("Светлая", "Тёмная");
        themeChoiceBox.setValue(settings.getTheme());
        Button editExceptionsButton = new Button("Редактировать Исключения");
        Button loadConfigButton = new Button("Загрузить Конфиг");

        Button saveButton = new Button("Сохранить");
        saveButton.setOnAction(e -> {
            settings.setVscodePath(vscodePathField.getText());
            settings.setNotepadPlusPlusPath(notepadPlusPlusPathField.getText());
            settings.setNotepadPath(notepadPathField.getText());
            settings.setPreferredEditor(preferredEditorChoiceBox.getValue());
            String oldTheme = settings.getTheme();
            String newTheme = themeChoiceBox.getValue();
            settings.setTheme(newTheme);
            settings.saveSettings();

            if (!oldTheme.equals(newTheme)) {
                SettingsChangeListener.notifyThemeChanged(newTheme);
                applyTheme(newTheme);
            }
        });



        browseVsCodeButton.setOnAction(e -> {
            String path = chooseExecutableFile();
            if (path != null) {
                vscodePathField.setText(path);
            }
        });

        browseNotepadPlusPlusButton.setOnAction(e -> {
            String path = chooseExecutableFile();
            if (path != null) {
                notepadPlusPlusPathField.setText(path);
            }
        });

        browseNotepadButton.setOnAction(e -> {
            String path = chooseExecutableFile();
            if (path != null) {
                notepadPathField.setText(path);
            }
        });

        editExceptionsButton.setOnAction(e -> {
            EditExceptionsView editExceptionsView = new EditExceptionsView(settings);
            editExceptionsView.showAndWait();
        });

        loadConfigButton.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Выберите файл конфига");
            File file = fileChooser.showOpenDialog(stage);
            if (file != null) {
                settings.loadTranslationExceptionsFromFile(file.getAbsolutePath());
            }
        });

        GridPane grid = new GridPane();
        grid.setVgap(10);
        grid.setHgap(10);
        grid.add(new Label("Путь к Visual Studio Code:"), 0, 0);
        grid.add(vscodePathField, 1, 0);
        grid.add(browseVsCodeButton, 2, 0);
        grid.add(new Label("Путь к Notepad++:"), 0, 1);
        grid.add(notepadPlusPlusPathField, 1, 1);
        grid.add(browseNotepadPlusPlusButton, 2, 1);
        grid.add(new Label("Путь к Notepad:"), 0, 2);
        grid.add(notepadPathField, 1, 2);
        grid.add(browseNotepadButton, 2, 2);
        grid.add(new Label("Предпочтительный редактор:"), 0, 3);
        grid.add(preferredEditorChoiceBox, 1, 3);
        grid.add(new Label("Тема приложения:"), 0, 4);
        grid.add(themeChoiceBox, 1, 4);
        root.getChildren().addAll(grid, editExceptionsButton, loadConfigButton, saveButton);
        Scene scene = new Scene(root, 600, 300);
        stage.setScene(scene);
    }

    public void showAndWait() {
        stage.showAndWait();
    }

    private String chooseExecutableFile() {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Выберите исполняемый файл редактора");
        File file = fileChooser.showOpenDialog(stage);
        if (file != null) {
            return file.getAbsolutePath();
        }
        return null;
    }

    @Override
    public void onThemeChanged(String newTheme) {
        applyTheme(newTheme);
    }

    private void applyTheme(String theme) {
        Scene scene = stage.getScene();
        scene.getStylesheets().clear();
        if (theme.equals("Тёмная")) {
            scene.getStylesheets().add(getClass().getResource("/dark-theme.css").toExternalForm());
        } else {
            scene.getStylesheets().add(getClass().getResource("/light-theme.css").toExternalForm());
        }
    }

}
