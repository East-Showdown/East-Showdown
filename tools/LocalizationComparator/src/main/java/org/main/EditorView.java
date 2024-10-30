package org.main;

import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.transformation.FilteredList;
import javafx.concurrent.Task;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.stage.DirectoryChooser;
import javafx.stage.Window;
import javafx.scene.input.MouseEvent;
import org.json.JSONObject;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;
import java.util.List;

public class EditorView {

    private BorderPane root;
    private TableView<MissingKeyEntry> tableView;
    private ObservableList<MissingKeyEntry> data;
    private TextArea russianTextArea;
    private TextArea englishTextArea;
    private Button saveButton;
    private Button translateButton;
    private TextField rusDirField;
    private TextField engDirField;
    private CheckBox rememberRusDirCheckBox;
    private CheckBox rememberEngDirCheckBox;
    private LocalizationFileScanner scanner;
    private LocalizationComparator comparator;
    private Map<Path, Set<String>> missingKeysMap;
    private Map<String, String> translationExceptions = new HashMap<>();
    private Map<String, String> specialSymbolsMap = new HashMap<>();
    private Map<String, String> translationExceptionsPlaceholders = new HashMap<>();
    private Set<String> autoTranslatedKeys = new HashSet<>();
    private Map<String, String> temporaryTranslations = new HashMap<>();
    private boolean isProgrammaticChange = false;
    private List<Path> englishFilesList;
    private CheckBox includeVersionCheckBox;
    private Settings settings;

    public EditorView() {
        settings = new Settings();
        root = new BorderPane();
        data = FXCollections.observableArrayList();
        scanner = new LocalizationFileScanner();
        comparator = new LocalizationComparator();
        setupUI();
    }

    private void setupUI() {
        VBox topBox = new VBox();
        topBox.setPadding(new Insets(10));
        topBox.setSpacing(10);

        Label rusDirLabel = new Label("Директория Русской Локализации:");
        rusDirField = new TextField();
        rusDirField.setPromptText("Выберите директорию русской локализации");
        Button browseRusButton = new Button("Обзор");
        rememberRusDirCheckBox = new CheckBox("Запомнить выбор");
        HBox rusBox = new HBox(10, rusDirField, browseRusButton, rememberRusDirCheckBox);
        HBox.setHgrow(rusDirField, Priority.ALWAYS);

        Label engDirLabel = new Label("Директория Английской Локализации:");
        engDirField = new TextField();
        engDirField.setPromptText("Выберите директорию английской локализации");
        Button browseEngButton = new Button("Обзор");
        rememberEngDirCheckBox = new CheckBox("Запомнить выбор");
        HBox engBox = new HBox(10, engDirField, browseEngButton, rememberEngDirCheckBox);
        HBox.setHgrow(engDirField, Priority.ALWAYS);

        if (settings.getRememberRusDir()) {
            rusDirField.setText(settings.getRusDir());
            rememberRusDirCheckBox.setSelected(true);
        }

        if (settings.getRememberEngDir()) {
            engDirField.setText(settings.getEngDir());
            rememberEngDirCheckBox.setSelected(true);
        }

        Button compareButton = new Button("Сравнить");
        compareButton.setMaxWidth(Double.MAX_VALUE);
        Button mapFilesButton = new Button("Сопоставить Файлы");
        mapFilesButton.setMaxWidth(Double.MAX_VALUE);
        Button settingsButton = new Button("Настройки");
        settingsButton.setMaxWidth(Double.MAX_VALUE);

        topBox.getChildren().addAll(
                rusDirLabel, rusBox,
                engDirLabel, engBox,
                compareButton,
                mapFilesButton,
                settingsButton
        );

        SplitPane splitPane = new SplitPane();
        splitPane.setDividerPositions(0.5);

        TextField searchField = new TextField();
        searchField.setPromptText("Поиск...");

        tableView = new TableView<>();
        TableColumn<MissingKeyEntry, String> fileColumn = new TableColumn<>("Файл");
        fileColumn.setCellValueFactory(new PropertyValueFactory<>("fileName"));
        fileColumn.setPrefWidth(200);

        fileColumn.setCellFactory(column -> new TableCell<MissingKeyEntry, String>() {
            @Override
            protected void updateItem(String item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setText(null);
                    setTooltip(null);
                } else {
                    setText(item);
                    MissingKeyEntry entry = getTableView().getItems().get(getIndex());
                    Tooltip tooltip = new Tooltip(entry.getFilePath());
                    setTooltip(tooltip);
                }
            }
        });

        TableColumn<MissingKeyEntry, String> keyColumn = new TableColumn<>("Отсутствующий Ключ");
        keyColumn.setCellValueFactory(new PropertyValueFactory<>("key"));
        keyColumn.setPrefWidth(400);

        keyColumn.setCellFactory(column -> new TableCell<MissingKeyEntry, String>() {
            @Override
            protected void updateItem(String item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setText(null);
                    setContextMenu(null);
                } else {
                    setText(item);
                    MissingKeyEntry entry = getTableView().getItems().get(getIndex());
                    ContextMenu contextMenu = new ContextMenu();
                    MenuItem openEngFileItem = new MenuItem("Открыть английский файл");
                    openEngFileItem.setOnAction(e -> openEnglishFileInEditor(entry));
                    contextMenu.getItems().add(openEngFileItem);
                    setContextMenu(contextMenu);
                }
            }
        });

        tableView.getColumns().addAll(fileColumn, keyColumn);
        tableView.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);

        FilteredList<MissingKeyEntry> filteredData = new FilteredList<>(data, p -> true);
        tableView.setItems(filteredData);

        searchField.textProperty().addListener((observable, oldValue, newValue) -> {
            filteredData.setPredicate(entry -> {
                if (newValue == null || newValue.isEmpty()) {
                    return true;
                }
                String lowerCaseFilter = newValue.toLowerCase();
                return entry.getFileName().toLowerCase().contains(lowerCaseFilter)
                        || entry.getKey().toLowerCase().contains(lowerCaseFilter);
            });
        });

        root.addEventFilter(KeyEvent.KEY_PRESSED, event -> {
            if (event.isControlDown() && event.getCode() == KeyCode.F) {
                searchField.requestFocus();
                event.consume();
            }
        });

        VBox tableContainer = new VBox();
        tableContainer.getChildren().addAll(searchField, tableView);

        VBox detailPane = new VBox();
        detailPane.setPadding(new Insets(10));
        detailPane.setSpacing(10);

        Label rusValueLabel = new Label("Значение на Русском:");
        russianTextArea = new TextArea();
        russianTextArea.setEditable(false);
        russianTextArea.setWrapText(true);
        russianTextArea.setPrefHeight(100);

        Label engValueLabel = new Label("Перевод на Английский:");
        englishTextArea = new TextArea();
        englishTextArea.setWrapText(true);
        englishTextArea.setPrefHeight(100);

        englishTextArea.textProperty().addListener((observable, oldValue, newValue) -> {
            if (isProgrammaticChange) {
                return;
            }
            ObservableList<MissingKeyEntry> selectedEntries = tableView.getSelectionModel().getSelectedItems();
            if (selectedEntries != null && selectedEntries.size() == 1) {
                MissingKeyEntry selectedEntry = selectedEntries.get(0);
                temporaryTranslations.put(selectedEntry.getKey(), newValue);
                selectedEntry.setTranslated(true);
                selectedEntry.setAutoTranslated(false);
            }
        });



        saveButton = new Button("Сохранить Перевод");
        saveButton.setDisable(true);

        includeVersionCheckBox = new CheckBox("Сохранять с версией (:0)");
        includeVersionCheckBox.setSelected(false);

        translateButton = new Button("Перевести");

        VBox saveBox = new VBox(10, saveButton, includeVersionCheckBox, translateButton);
        saveBox.setAlignment(Pos.CENTER_LEFT);

        Label warningLabel = new Label("❗");
        warningLabel.setStyle("-fx-font-size: 24px; -fx-text-fill: red;");
        warningLabel.setVisible(false);
        Tooltip.install(warningLabel, new Tooltip("Есть русские файлы без соответствующих английских файлов. Нажмите, чтобы сгенерировать."));

        warningLabel.setOnMouseClicked(e -> {
            generateMissingEnglishFiles();
        });

        warningLabel.setAlignment(Pos.CENTER_LEFT);
        VBox.setMargin(warningLabel, new Insets(0, 0, 0, 0));

        ProgressBar progressBar = new ProgressBar();
        progressBar.setPrefWidth(300);
        progressBar.setVisible(false);

        Label progressLabel = new Label();
        progressLabel.setVisible(false);

        detailPane.getChildren().addAll(
                rusValueLabel, russianTextArea,
                engValueLabel, englishTextArea,
                saveBox,
                warningLabel,
                progressBar,
                progressLabel
        );

        splitPane.getItems().addAll(tableContainer, detailPane);

        Label statusLabel = new Label("Статус: Готово");
        BorderPane.setMargin(statusLabel, new Insets(5));
        root.setBottom(statusLabel);

        root.setTop(topBox);
        root.setCenter(splitPane);

        browseRusButton.setOnAction(e -> {
            String selectedDir = chooseDirectory();
            if (selectedDir != null) {
                rusDirField.setText(selectedDir);
            }
        });

        browseEngButton.setOnAction(e -> {
            String selectedDir = chooseDirectory();
            if (selectedDir != null) {
                engDirField.setText(selectedDir);
            }
        });

        rememberRusDirCheckBox.selectedProperty().addListener((obs, oldVal, newVal) -> {
            settings.setRememberRusDir(newVal);
            if (newVal) {
                settings.setRusDir(rusDirField.getText());
            } else {
                settings.setRusDir("");
            }
            settings.saveSettings();
        });

        rememberEngDirCheckBox.selectedProperty().addListener((obs, oldVal, newVal) -> {
            settings.setRememberEngDir(newVal);
            if (newVal) {
                settings.setEngDir(engDirField.getText());
            } else {
                settings.setEngDir("");
            }
            settings.saveSettings();
        });

        rusDirField.textProperty().addListener((obs, oldVal, newVal) -> {
            if (rememberRusDirCheckBox.isSelected()) {
                settings.setRusDir(newVal);
                settings.saveSettings();
            }
        });

        engDirField.textProperty().addListener((obs, oldVal, newVal) -> {
            if (rememberEngDirCheckBox.isSelected()) {
                settings.setEngDir(newVal);
                settings.saveSettings();
            }
        });

        mapFilesButton.setOnAction(e -> {
            String rusDir = rusDirField.getText();
            String engDir = engDirField.getText();

            if (rusDir.isEmpty() || engDir.isEmpty()) {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Пожалуйста, выберите обе директории локализации.");
                return;
            }

            try {
                List<Path> russianFiles = scanner.scanLocalizationFiles(rusDir);
                List<Path> englishFiles = scanner.scanLocalizationFiles(engDir);

                FileMappingView fileMappingView = new FileMappingView(russianFiles, englishFiles, comparator.getFilePairs());
                fileMappingView.showAndWait();

                List<FilePair> filePairs = fileMappingView.getFilePairs();
                comparator.setFilePairs(filePairs);

            } catch (IOException ex) {
                ex.printStackTrace();
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Произошла ошибка при сканировании файлов локализации.");
            }
        });

        compareButton.setOnAction(e -> {
            String rusDir = rusDirField.getText();
            String engDir = engDirField.getText();

            if (rusDir.isEmpty() || engDir.isEmpty()) {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Пожалуйста, выберите обе директории локализации.");
                return;
            }

            try {
                List<Path> russianFiles = scanner.scanLocalizationFiles(rusDir);
                List<Path> englishFiles = scanner.scanLocalizationFiles(engDir);
                this.englishFilesList = englishFiles;

                if (comparator.getFilePairs().isEmpty()) {
                    missingKeysMap = comparator.findMissingKeys(russianFiles, englishFiles);
                } else {
                    missingKeysMap = comparator.findMissingKeys(russianFiles, englishFiles);
                }

                data.clear();
                for (Map.Entry<Path, Set<String>> entry : missingKeysMap.entrySet()) {
                    Path file = entry.getKey();
                    for (String key : entry.getValue()) {
                        data.add(new MissingKeyEntry(file.toString(), key));
                    }
                }

                statusLabel.setText("Статус: Сравнение завершено. Найдено отсутствующих ключей: " + data.size());

                if (comparator.hasUnmatchedRusFiles()) {
                    warningLabel.setVisible(true);
                } else {
                    warningLabel.setVisible(false);
                }

            } catch (IOException ex) {
                ex.printStackTrace();
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Произошла ошибка при сравнении файлов локализации.");
            }
        });

        settingsButton.setOnAction(e -> {
            SettingsView settingsView = new SettingsView(settings);
            settingsView.showAndWait();
        });

        tableView.setOnMouseClicked((MouseEvent event) -> {
            if (event.getClickCount() == 2) {
                MissingKeyEntry selectedEntry = tableView.getSelectionModel().getSelectedItem();
                if (selectedEntry != null) {
                    openFileInEditor(selectedEntry.getFilePath(), selectedEntry.getKey());
                }
            }
        });

        tableView.setRowFactory(tv -> {
            TableRow<MissingKeyEntry> row = new TableRow<>();
            row.setOnContextMenuRequested(event -> {
                if (!row.isEmpty()) {
                    MissingKeyEntry entry = row.getItem();
                    ContextMenu contextMenu = new ContextMenu();
                    MenuItem openEngFileItem = new MenuItem("Открыть английский файл");
                    openEngFileItem.setOnAction(e -> openEnglishFileInEditor(entry));
                    contextMenu.getItems().add(openEngFileItem);
                    contextMenu.show(row, event.getScreenX(), event.getScreenY());
                }
            });
            return row;
        });

        saveButton.setOnAction(e -> {
            ObservableList<MissingKeyEntry> selectedEntries = tableView.getSelectionModel().getSelectedItems();
            if (selectedEntries != null && !selectedEntries.isEmpty()) {
                try {
                    boolean allTranslated = true;
                    for (MissingKeyEntry entry : selectedEntries) {
                        String translation = temporaryTranslations.get(entry.getKey());
                        if (translation == null || translation.trim().isEmpty()) {
                            allTranslated = false;
                            showAlert(Alert.AlertType.WARNING, "Предупреждение", "Перевод для ключа " + entry.getKey() + " не может быть пустым.");
                            continue;
                        }
                        saveTranslation(entry, translation);
                        temporaryTranslations.remove(entry.getKey());
                        entry.setTranslated(true);
                        entry.setAutoTranslated(false);
                    }
                    if (allTranslated) {
                        showAlert(Alert.AlertType.INFORMATION, "Успех", "Переводы успешно сохранены.");
                    } else {
                        showAlert(Alert.AlertType.WARNING, "Предупреждение", "Некоторые переводы не были сохранены из-за отсутствия текста.");
                    }

                    russianTextArea.clear();
                    englishTextArea.clear();
                    saveButton.setDisable(true);

                } catch (IOException ex) {
                    ex.printStackTrace();
                    showAlert(Alert.AlertType.ERROR, "Ошибка", "Произошла ошибка при сохранении переводов.");
                }
            }
        });

        translateButton.setOnAction(e -> {
            ObservableList<MissingKeyEntry> selectedEntries = tableView.getSelectionModel().getSelectedItems();
            if (selectedEntries != null && !selectedEntries.isEmpty()) {
                Task<Void> translationTask = new Task<>() {
                    @Override
                    protected Void call() throws Exception {
                        int total = selectedEntries.size();
                        int count = 0;
                        for (MissingKeyEntry entry : selectedEntries) {
                            String russianValue = getRussianValue(entry);
                            if (russianValue != null) {
                                String translatedText = translateText(russianValue, "ru", "en");
                                if (translatedText != null) {
                                    temporaryTranslations.put(entry.getKey(), translatedText);

                                    entry.setTranslated(true);
                                    entry.setAutoTranslated(true);

                                    if (total == 1) {
                                        Platform.runLater(() -> {
                                            isProgrammaticChange = true;
                                            englishTextArea.setText(translatedText);
                                            isProgrammaticChange = false;
                                        });
                                    }
                                } else {
                                    String errorMessage = "Не удалось перевести ключ: " + entry.getKey();
                                    Platform.runLater(() -> {
                                        showAlert(Alert.AlertType.ERROR, "Ошибка", errorMessage);
                                    });
                                }
                            }
                            count++;
                            updateProgress(count, total);
                            int progressCount = count;
                            Platform.runLater(() -> {
                                String progressText = String.format("Перевод ключей: %d/%d (%.0f%%)", progressCount, total, (double) progressCount / total * 100);
                                progressLabel.setText(progressText);
                            });
                        }
                        return null;
                    }
                };

                progressBar.setVisible(true);
                progressLabel.setVisible(true);
                progressBar.progressProperty().bind(translationTask.progressProperty());

                translationTask.setOnSucceeded(event -> {
                    progressBar.setVisible(false);
                    progressLabel.setVisible(false);
                    translateButton.setDisable(false);
                    saveButton.setDisable(false);
                    tableView.setDisable(false);

                    MissingKeyEntry selectedEntry = tableView.getSelectionModel().getSelectedItem();
                    if (selectedEntry != null && temporaryTranslations.containsKey(selectedEntry.getKey())) {
                        englishTextArea.setText(temporaryTranslations.get(selectedEntry.getKey()));
                    }
                });

                translationTask.setOnFailed(event -> {
                    progressBar.setVisible(false);
                    progressLabel.setVisible(false);
                    translateButton.setDisable(false);
                    saveButton.setDisable(false);
                    tableView.setDisable(false);
                    Throwable exception = translationTask.getException();
                    exception.printStackTrace();
                    showAlert(Alert.AlertType.ERROR, "Ошибка", "Произошла ошибка при переводе.");
                });

                translateButton.setDisable(true);
                saveButton.setDisable(true);
                tableView.setDisable(true);

                Thread thread = new Thread(translationTask);
                thread.setDaemon(true);
                thread.start();

            } else {
                showAlert(Alert.AlertType.WARNING, "Предупреждение", "Пожалуйста, выберите ключ(и) для перевода.");
            }
        });

        tableView.getSelectionModel().selectedItemProperty().addListener((obs, oldSelection, newSelection) -> {
            ObservableList<MissingKeyEntry> selectedEntries = tableView.getSelectionModel().getSelectedItems();
            if (selectedEntries.size() == 1) {
                displayDetail(selectedEntries.get(0));
                englishTextArea.setEditable(true);
                saveButton.setDisable(false);
            } else if (selectedEntries.size() > 1) {
                russianTextArea.clear();
                russianTextArea.setEditable(false);
                englishTextArea.clear();
                englishTextArea.setEditable(false);
                englishTextArea.setPromptText("Введите перевод");
                saveButton.setDisable(false);
            }
        });


        tableView.setRowFactory(tv -> new TableRow<MissingKeyEntry>() {
            @Override
            protected void updateItem(MissingKeyEntry item, boolean empty) {
                super.updateItem(item, empty);
                if (item == null || empty) {
                    setStyle("");
                } else {
                    if (item.isTranslated()) {
                        if (item.isAutoTranslated()) {
                            setStyle("-fx-background-color: lightblue;");
                        } else {
                            setStyle("-fx-background-color: lightgreen;");
                        }
                    } else {
                        setStyle("");
                    }
                }
            }
        });
    }

    private void displayDetail(MissingKeyEntry entry) {
        try {
            String russianValue = getRussianValue(entry);
            russianTextArea.setText(russianValue != null ? russianValue : "Не найдено");
            if (temporaryTranslations.containsKey(entry.getKey())) {
                isProgrammaticChange = true;
                englishTextArea.setText(temporaryTranslations.get(entry.getKey()));
                isProgrammaticChange = false;
            } else {
                String engFilePath = findEnglishFileForEntry(entry);
                if (engFilePath != null) {
                    String fullEngKey = "l_english." + entry.getKey();
                    String englishValue = LocalizationHelper.fetchEnglishValue(engFilePath, fullEngKey);
                    if (englishValue != null && !englishValue.trim().isEmpty()) {
                        isProgrammaticChange = true;
                        englishTextArea.setText(englishValue);
                        isProgrammaticChange = false;
                    } else {
                        isProgrammaticChange = true;
                        englishTextArea.setText("");
                        isProgrammaticChange = false;
                    }
                } else {
                    isProgrammaticChange = true;
                    englishTextArea.setText("");
                    isProgrammaticChange = false;
                }
            }

            englishTextArea.setEditable(true);
            saveButton.setDisable(false);

        } catch (IOException ex) {
            ex.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось загрузить значения для выбранного ключа.");
        }
    }

    private String getRussianValue(MissingKeyEntry entry) throws IOException {
        String fullRusKey = "l_russian." + entry.getKey();
        return LocalizationHelper.fetchRussianValue(entry.getFilePath(), fullRusKey);
    }

    private void saveTranslation(MissingKeyEntry entry, String translation) throws IOException {
        String engFilePathStr = findEnglishFileForEntry(entry);
        if (engFilePathStr == null) {
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось определить файл для сохранения перевода.");
            return;
        }

        Path engFilePath = Paths.get(engFilePathStr);

        String key = entry.getKey();

        boolean includeVersion = includeVersionCheckBox.isSelected();

        LocalizationHelper.saveEnglishTranslation(engFilePath, key, translation, includeVersion);
    }

    private String chooseDirectory() {
        DirectoryChooser directoryChooser = new DirectoryChooser();
        directoryChooser.setTitle("Выберите Директорию");
        Window window = root.getScene().getWindow();
        File selectedDirectory = directoryChooser.showDialog(window);
        if (selectedDirectory != null) {
            return selectedDirectory.getAbsolutePath();
        }
        return null;
    }

    private void showAlert(Alert.AlertType type, String title, String message) {
        Platform.runLater(() -> {
            Alert alert = new Alert(type);
            alert.setTitle(title);
            alert.setHeaderText(null);
            alert.setContentText(message);
            alert.showAndWait();
        });
    }

    public BorderPane getView() {
        return root;
    }

    public Settings getSettings() {
        return settings;
    }

    private String findEnglishFileForEntry(MissingKeyEntry entry) {
        String engDir = engDirField.getText();
        Path rusPath = Paths.get(entry.getFilePath());
        String rusFileName = rusPath.getFileName().toString();

        Path engFilePath = null;

        if (!comparator.getFilePairs().isEmpty()) {
            for (FilePair pair : comparator.getFilePairs()) {
                if (pair.getRusFile().getFileName().toString().equals(rusFileName)) {
                    engFilePath = pair.getEngFile();
                    break;
                }
            }
        } else {
            String engFileName = comparator.matchEnglishFile(rusFileName, englishFilesList);
            if (engFileName != null) {
                engFilePath = Paths.get(engDir, engFileName);
            } else {
                engFilePath = Paths.get(engDir, rusFileName);
            }
        }

        if (engFilePath != null && Files.exists(engFilePath)) {
            return engFilePath.toString();
        } else {
            return null;
        }
    }

    private void openEnglishFileInEditor(MissingKeyEntry entry) {
        try {
            String engFilePath = findEnglishFileForEntry(entry);
            if (engFilePath != null) {
                openFileInEditor(engFilePath, entry.getKey());
            } else {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось найти соответствующий английский файл.");
            }
        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось открыть английский файл.");
        }
    }

    public void initializeTranslationExceptions() {
        translationExceptions = settings.getTranslationExceptions();
    }

    private String preprocessText(String text) {
        if (translationExceptions.isEmpty()) {
            initializeTranslationExceptions();
        }

        specialSymbolsMap = new HashMap<>();
        translationExceptionsPlaceholders = new HashMap<>();
        int placeholderCounter = 1;

        List<String> specialSymbols = Arrays.asList("§R", "§!", "§g", "\n");

        for (String symbol : specialSymbols) {
            String placeholder = "SYM" + placeholderCounter++;
            specialSymbolsMap.put(placeholder, symbol);
            text = text.replace(symbol, placeholder);
        }

        for (Map.Entry<String, String> entry : translationExceptions.entrySet()) {
            String word = entry.getKey();
            String placeholder = "WORD" + placeholderCounter++;
            translationExceptionsPlaceholders.put(placeholder, entry.getValue());
            text = text.replace(word, placeholder);
        }

        return text;
    }

    private String postprocessText(String translatedText) {
        for (Map.Entry<String, String> entry : translationExceptionsPlaceholders.entrySet()) {
            String placeholder = entry.getKey();
            String correctTranslation = entry.getValue();
            translatedText = translatedText.replace(placeholder, correctTranslation);
        }

        for (Map.Entry<String, String> entry : specialSymbolsMap.entrySet()) {
            String placeholder = entry.getKey();
            String symbol = entry.getValue();
            translatedText = translatedText.replace(placeholder, symbol);
        }

        return translatedText;
    }

    private String translateText(String text, String sourceLang, String targetLang) {
        try {
            String preprocessedText = preprocessText(text);

            String url = "http://localhost:5000/translate";

            JSONObject requestBody = new JSONObject();
            requestBody.put("q", preprocessedText);
            requestBody.put("source", sourceLang);
            requestBody.put("target", targetLang);
            requestBody.put("format", "text");

            String requestBodyString = requestBody.toString();

            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .header("Accept", "application/json")
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(requestBodyString))
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() != 200) {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Ошибка при выполнении запроса к API перевода.");
                System.out.println("Ошибка API: " + response.body());
                return null;
            }

            JSONObject jsonResponse = new JSONObject(response.body());

            if (jsonResponse.has("translatedText")) {
                String translatedText = jsonResponse.getString("translatedText");

                translatedText = postprocessText(translatedText);

                return translatedText;
            } else if (jsonResponse.has("error")) {
                String errorMessage = jsonResponse.getString("error");
                showAlert(Alert.AlertType.ERROR, "Ошибка API перевода", errorMessage);
                System.out.println("Ошибка API: " + errorMessage);
                return null;
            } else {
                showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось выполнить автоматический перевод.");
                System.out.println("Неизвестный ответ API: " + response.body());
                return null;
            }

        } catch (Exception e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось выполнить автоматический перевод.");
            return null;
        }
    }

    private void openFileInEditor(String filePath, String key) {
        try {
            File file = new File(filePath);

            String preferredEditor = settings.getPreferredEditor();
            preferredEditor = preferredEditor.trim();
            System.out.println("Preferred editor: " + preferredEditor);

            String editorPath = null;
            List<String> command = new ArrayList<>();

            if (preferredEditor.equalsIgnoreCase("Visual Studio Code")) {
                editorPath = settings.getVscodePath();
                if (editorPath == null || editorPath.isEmpty()) {
                    editorPath = "code";
                }
                int lineNumber = findLineNumberForKey(filePath, key);
                if (lineNumber != -1) {
                    command.add(editorPath);
                    command.add("-g");
                    command.add(filePath + ":" + lineNumber);
                } else {
                    command.add(editorPath);
                    command.add(filePath);
                }
            } else if (preferredEditor.equalsIgnoreCase("Notepad++")) {
                editorPath = settings.getNotepadPlusPlusPath();
                if (editorPath == null || editorPath.isEmpty()) {
                    editorPath = "notepad++";
                }
                command.add(editorPath);
                command.add(filePath);
            } else if (preferredEditor.equalsIgnoreCase("Notepad")) {
                editorPath = settings.getNotepadPath();
                if (editorPath == null || editorPath.isEmpty()) {
                    Desktop.getDesktop().open(file);
                    return;
                }
                command.add(editorPath);
                command.add(filePath);
            } else {
                Desktop.getDesktop().open(file);
                return;
            }

            ProcessBuilder pb = new ProcessBuilder(command);
            pb.start();

        } catch (IOException e) {
            e.printStackTrace();
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось открыть файл в редакторе.");
        }
    }

    private int findLineNumberForKey(String filePath, String key) {
        try {
            List<String> lines = Files.readAllLines(Paths.get(filePath), StandardCharsets.UTF_8);
            for (int i = 0; i < lines.size(); i++) {
                if (lines.get(i).contains(key)) {
                    return i + 1;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return -1;
    }

    private void generateMissingEnglishFiles() {
        String engDir = engDirField.getText();
        if (engDir.isEmpty()) {
            showAlert(Alert.AlertType.ERROR, "Ошибка", "Пожалуйста, выберите директорию английской локализации.");
            return;
        }

        List<Path> missingEngFiles = comparator.getMissingEnglishFiles(engDir);
        if (missingEngFiles.isEmpty()) {
            showAlert(Alert.AlertType.INFORMATION, "Информация", "Все соответствующие английские файлы присутствуют.");
            return;
        }

        for (Path engFilePath : missingEngFiles) {
            Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
            alert.setTitle("Создание файла");
            alert.setHeaderText(null);
            alert.setContentText("Создать файл " + engFilePath.getFileName() + "?");
            Optional<ButtonType> result = alert.showAndWait();
            if (result.isPresent() && result.get() == ButtonType.OK) {
                try {
                    Files.createDirectories(engFilePath.getParent());
                    Files.createFile(engFilePath);
                    Files.writeString(engFilePath, "l_english:\n", StandardCharsets.UTF_8);
                } catch (IOException ex) {
                    ex.printStackTrace();
                    showAlert(Alert.AlertType.ERROR, "Ошибка", "Не удалось создать файл: " + engFilePath.getFileName());
                }
            }
        }
    }
}
