package org.main;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.layout.*;
import javafx.stage.Modality;
import javafx.stage.Stage;

public class EditExceptionsView {

    private Stage stage;
    private TextArea exceptionsTextArea;
    private Settings settings;

    public EditExceptionsView(Settings settings) {
        this.settings = settings;
        setupUI();
    }

    private void setupUI() {
        stage = new Stage();
        stage.setTitle("Редактирование Исключений");
        stage.getIcons().add(new Image("logo.ico"));
        stage.initModality(Modality.APPLICATION_MODAL);

        VBox root = new VBox(10);
        root.setPadding(new Insets(10));

        exceptionsTextArea = new TextArea();
        exceptionsTextArea.setText(settings.getTranslationExceptionsAsString());

        Button saveButton = new Button("Сохранить");
        saveButton.setOnAction(e -> {
            settings.setTranslationExceptionsFromString(exceptionsTextArea.getText());
            stage.close();
        });

        root.getChildren().addAll(new Label("Исключения (каждая пара с новой строки в формате ключ=значение):"), exceptionsTextArea, saveButton);
        Scene scene = new Scene(root, 600, 400);
        stage.setScene(scene);
    }

    public void showAndWait() {
        stage.showAndWait();
    }
}
