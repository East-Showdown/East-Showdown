package org.main;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.transformation.FilteredList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.ArrayList;
import java.util.Optional;

public class FileMappingView {

    private Stage stage;
    private ListView<Path> rusFilesListView;
    private ListView<Path> engFilesListView;
    private ListView<FilePair> filePairsListView;

    private ObservableList<Path> rusFiles;
    private ObservableList<Path> engFiles;
    private ObservableList<FilePair> filePairs;

    public FileMappingView(List<Path> rusFiles, List<Path> engFiles, List<FilePair> initialPairs) {
        this.rusFiles = FXCollections.observableArrayList(rusFiles);
        this.engFiles = FXCollections.observableArrayList(engFiles);
        this.filePairs = FXCollections.observableArrayList(initialPairs);

        for (FilePair pair : initialPairs) {
            this.rusFiles.remove(pair.getRusFile());
            this.engFiles.remove(pair.getEngFile());
        }

        setupUI();
    }

    private void setupUI() {
        stage = new Stage();
        stage.setTitle("Сопоставление Файлов Локализации");
        stage.getIcons().add(new Image("logo.ico"));

        BorderPane root = new BorderPane();
        root.setPadding(new Insets(10));

        TextField rusSearchField = new TextField();
        rusSearchField.setPromptText("Поиск...");
        TextField engSearchField = new TextField();
        engSearchField.setPromptText("Поиск...");

        FilteredList<Path> filteredRusFiles = new FilteredList<>(rusFiles, p -> true);
        FilteredList<Path> filteredEngFiles = new FilteredList<>(engFiles, p -> true);

        rusSearchField.textProperty().addListener((observable, oldValue, newValue) -> {
            filteredRusFiles.setPredicate(path -> {
                if (newValue == null || newValue.isEmpty()) {
                    return true;
                }
                String lowerCaseFilter = newValue.toLowerCase();
                return path.getFileName().toString().toLowerCase().contains(lowerCaseFilter);
            });
        });

        engSearchField.textProperty().addListener((observable, oldValue, newValue) -> {
            filteredEngFiles.setPredicate(path -> {
                if (newValue == null || newValue.isEmpty()) {
                    return true;
                }
                String lowerCaseFilter = newValue.toLowerCase();
                return path.getFileName().toString().toLowerCase().contains(lowerCaseFilter);
            });
        });

        rusFilesListView = new ListView<>(filteredRusFiles);
        rusFilesListView.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
        rusFilesListView.setPrefWidth(300);
        rusFilesListView.setPrefHeight(400);
        rusFilesListView.setPlaceholder(new Label("Нет русских файлов"));

        rusFilesListView.setCellFactory(lv -> {
            ListCell<Path> cell = new ListCell<>() {
                @Override
                protected void updateItem(Path item, boolean empty) {
                    super.updateItem(item, empty);
                    if (empty || item == null) {
                        setText(null);
                        setTooltip(null);
                    } else {
                        setText(item.getFileName().toString());
                        setTooltip(new Tooltip(item.toString()));
                    }
                }
            };

            cell.setOnContextMenuRequested(event -> {
                if (!cell.isEmpty()) {
                    ContextMenu contextMenu = new ContextMenu();
                    MenuItem renameItem = new MenuItem("Переименовать");
                    renameItem.setOnAction(e -> {
                        try {
                            renameFile(cell.getItem(), true);
                        } catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }
                    });
                    MenuItem addPrefixItem = new MenuItem("Добавить префикс");
                    addPrefixItem.setOnAction(e -> {
                        try {
                            addPrefixToFiles(rusFilesListView.getSelectionModel().getSelectedItems(), true);
                        } catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }
                    });
                    contextMenu.getItems().addAll(renameItem, addPrefixItem);
                    contextMenu.show(cell, event.getScreenX(), event.getScreenY());
                }
            });

            return cell;
        });

        engFilesListView = new ListView<>(filteredEngFiles);
        engFilesListView.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
        engFilesListView.setPrefWidth(300);
        engFilesListView.setPrefHeight(400);
        engFilesListView.setPlaceholder(new Label("Нет английских файлов"));

        engFilesListView.setCellFactory(lv -> {
            ListCell<Path> cell = new ListCell<>() {
                @Override
                protected void updateItem(Path item, boolean empty) {
                    super.updateItem(item, empty);
                    if (empty || item == null) {
                        setText(null);
                        setTooltip(null);
                    } else {
                        String fileName = item.getFileName().toString();
                        setText(fileName);
                        setTooltip(new Tooltip(item.toString()));
                    }
                }
            };

            cell.setOnContextMenuRequested(event -> {
                if (!cell.isEmpty()) {
                    ContextMenu contextMenu = new ContextMenu();
                    MenuItem renameItem = new MenuItem("Переименовать");
                    renameItem.setOnAction(e -> {
                        try {
                            renameFile(cell.getItem(), false);
                        } catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }
                    });
                    MenuItem addPrefixItem = new MenuItem("Добавить префикс");
                    addPrefixItem.setOnAction(e -> {
                        try {
                            addPrefixToFiles(engFilesListView.getSelectionModel().getSelectedItems(), false);
                        } catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }
                    });
                    contextMenu.getItems().addAll(renameItem, addPrefixItem);
                    contextMenu.show(cell, event.getScreenX(), event.getScreenY());
                }
            });

            return cell;
        });

        filePairsListView = new ListView<>(filePairs);
        filePairsListView.setPrefWidth(600);
        filePairsListView.setPrefHeight(200);
        filePairsListView.setPlaceholder(new Label("Нет сопоставленных пар"));

        filePairsListView.setCellFactory(lv -> new ListCell<FilePair>() {
            @Override
            protected void updateItem(FilePair item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setText(null);
                    setTooltip(null);
                    setGraphic(null);
                } else {
                    String rusFileName = item.getRusFile().getFileName().toString();
                    String engFileName = item.getEngFile().getFileName().toString();
                    setText(null);

                    Label textLabel = new Label(rusFileName + " ⇔ " + engFileName);
                    HBox hbox = new HBox(5, textLabel);
                    if (areFileNamesVeryDifferent(rusFileName, engFileName)) {
                        Label warningLabel = new Label("⚠");
                        warningLabel.setTextFill(Color.RED);
                        Tooltip.install(warningLabel, new Tooltip("Названия файлов сильно различаются."));
                        hbox.getChildren().add(warningLabel);
                    }
                    setGraphic(hbox);

                    String tooltipText = "Русский файл: " + item.getRusFile().toString() +
                            "\nАнглийский файл: " + item.getEngFile().toString();
                    setTooltip(new Tooltip(tooltipText));
                }
            }
        });

        Button addPairButton = new Button("Добавить Пару");
        Button removePairButton = new Button("Удалить Пару");

        addPairButton.setOnAction(e -> addPair());
        removePairButton.setOnAction(e -> removePair());

        HBox buttonsBox = new HBox(10, addPairButton, removePairButton);
        buttonsBox.setAlignment(Pos.CENTER);

        Button saveButton = new Button("Сохранить Сопоставления");
        saveButton.setOnAction(e -> {
            stage.close();
        });

        VBox leftBox = new VBox(10, new Label("Русские Файлы"), rusSearchField, rusFilesListView);
        VBox rightBox = new VBox(10, new Label("Английские Файлы"), engSearchField, engFilesListView);
        HBox listsBox = new HBox(10, leftBox, rightBox);
        listsBox.setAlignment(Pos.CENTER);

        VBox centerBox = new VBox(10, listsBox, buttonsBox, new Label("Сопоставленные Пары"), filePairsListView);
        centerBox.setAlignment(Pos.CENTER);

        root.setCenter(centerBox);
        root.setBottom(saveButton);
        BorderPane.setAlignment(saveButton, Pos.CENTER);
        BorderPane.setMargin(saveButton, new Insets(10));

        Scene scene = new Scene(root, 700, 700);
        stage.setScene(scene);

        scene.addEventFilter(KeyEvent.KEY_PRESSED, event -> {
            if (event.isControlDown() && event.getCode() == KeyCode.F) {
                rusSearchField.requestFocus();
                event.consume();
            }
        });
    }

    private void addPair() {
        Path selectedRusFile = rusFilesListView.getSelectionModel().getSelectedItem();
        Path selectedEngFile = engFilesListView.getSelectionModel().getSelectedItem();

        if (selectedRusFile != null && selectedEngFile != null) {
            FilePair newPair = new FilePair(selectedRusFile, selectedEngFile);
            if (!filePairs.contains(newPair)) {
                filePairs.add(newPair);

                rusFiles.remove(selectedRusFile);
                engFiles.remove(selectedEngFile);

                rusFilesListView.getSelectionModel().clearSelection();
                engFilesListView.getSelectionModel().clearSelection();
            } else {
                showAlert(Alert.AlertType.WARNING, "Предупреждение", "Эта пара уже существует.");
            }
        } else {
            showAlert(Alert.AlertType.WARNING, "Предупреждение", "Пожалуйста, выберите оба файла для создания пары.");
        }
    }

    private void removePair() {
        FilePair selectedPair = filePairsListView.getSelectionModel().getSelectedItem();
        if (selectedPair != null) {
            filePairs.remove(selectedPair);

            rusFiles.add(selectedPair.getRusFile());
            engFiles.add(selectedPair.getEngFile());

            FXCollections.sort(rusFiles);
            FXCollections.sort(engFiles);
        } else {
            showAlert(Alert.AlertType.WARNING, "Предупреждение", "Пожалуйста, выберите пару для удаления.");
        }
    }

    public void showAndWait() {
        stage.showAndWait();
    }

    public List<FilePair> getFilePairs() {
        return new ArrayList<>(filePairs);
    }

    private void showAlert(Alert.AlertType type, String title, String message) {
        Alert alert = new Alert(type);
        alert.initOwner(stage);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void renameFile(Path file, boolean isRussianFile) throws IOException {
        TextInputDialog dialog = new TextInputDialog(file.getFileName().toString());
        dialog.initOwner(stage);
        dialog.setTitle("Переименовать файл");
        dialog.setHeaderText(null);
        dialog.setContentText("Введите новое имя файла:");

        Optional<String> result = dialog.showAndWait();
        result.ifPresent(newFileName -> {
            try {
                Path parentDir = file.getParent();
                Path newFilePath = parentDir.resolve(newFileName);
                Files.move(file, newFilePath);
                if (isRussianFile) {
                    rusFiles.set(rusFiles.indexOf(file), newFilePath);
                } else {
                    engFiles.set(engFiles.indexOf(file), newFilePath);
                }
            } catch (IOException e) {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось переименовать файл.");
            }
        });
    }

    private boolean areFileNamesVeryDifferent(String name1, String name2) {
        String baseName1 = name1.contains(".") ? name1.substring(0, name1.lastIndexOf('.')) : name1;
        String baseName2 = name2.contains(".") ? name2.substring(0, name2.lastIndexOf('.')) : name2;

        int maxLength = Math.max(baseName1.length(), baseName2.length());
        int commonLength = longestCommonSubstring(baseName1, baseName2).length();

        double similarity = (double) commonLength / maxLength;
        return similarity < 0.5;
    }

    private String longestCommonSubstring(String s1, String s2) {
        int[][] num = new int[s1.length()][s2.length()];
        int maxlen = 0;
        int lastSubsBegin = 0;
        StringBuilder sequence = new StringBuilder();

        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    if (i == 0 || j == 0) {
                        num[i][j] = 1;
                    } else {
                        num[i][j] = 1 + num[i - 1][j - 1];
                    }
                    if (num[i][j] > maxlen) {
                        maxlen = num[i][j];
                        int thisSubsBegin = i - num[i][j] + 1;
                        if (lastSubsBegin == thisSubsBegin) {
                            sequence.append(s1.charAt(i));
                        } else {
                            lastSubsBegin = thisSubsBegin;
                            sequence = new StringBuilder();
                            sequence.append(s1.substring(lastSubsBegin, i + 1));
                        }
                    }
                }
            }
        }
        return sequence.toString();
    }

    private void addPrefixToFiles(List<Path> selectedFiles, boolean isRussianFile) throws IOException {
        if (selectedFiles == null || selectedFiles.isEmpty()) {
            showAlert(Alert.AlertType.WARNING, "Предупреждение", "Пожалуйста, выберите файлы для добавления префикса.");
            return;
        }

        TextInputDialog dialog = new TextInputDialog();
        dialog.initOwner(stage);
        dialog.setTitle("Добавить префикс");
        dialog.setHeaderText(null);
        dialog.setContentText("Введите префикс:");

        Optional<String> result = dialog.showAndWait();
        if (result.isPresent()) {
            String prefix = result.get();
            for (Path file : selectedFiles) {
                Path parentDir = file.getParent();
                String newFileName = prefix + file.getFileName().toString();
                Path newFilePath = parentDir.resolve(newFileName);
                Files.move(file, newFilePath);

                if (isRussianFile) {
                    rusFiles.set(rusFiles.indexOf(file), newFilePath);
                } else {
                    engFiles.set(engFiles.indexOf(file), newFilePath);
                }
            }
        }
    }


}
