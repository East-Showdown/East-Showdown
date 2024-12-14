package org.main;

import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.layout.*;
import javafx.stage.Stage;

import java.util.List;

public class MappedFilesView {

    private Stage stage;
    private ListView<FilePair> filePairsListView;

    public MappedFilesView(List<FilePair> filePairs) {
        setupUI(filePairs);
    }

    private void setupUI(List<FilePair> filePairs) {
        stage = new Stage();
        stage.setTitle("Сопоставленные Файлы");
        stage.getIcons().add(new Image("logo.ico"));

        VBox root = new VBox(10);
        root.setPadding(new Insets(10));

        filePairsListView = new ListView<>();
        filePairsListView.getItems().addAll(filePairs);
        filePairsListView.setCellFactory(lv -> new ListCell<FilePair>() {
            @Override
            protected void updateItem(FilePair item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setText(null);
                } else {
                    setText(item.getRusFile().getFileName() + " ⇔ " + item.getEngFile().getFileName());
                }
            }
        });

        root.getChildren().addAll(new Label("Сопоставленные Пары Файлов:"), filePairsListView);

        Scene scene = new Scene(root, 600, 400);
        stage.setScene(scene);
    }

    public void showAndWait() {
        stage.showAndWait();
    }
}
