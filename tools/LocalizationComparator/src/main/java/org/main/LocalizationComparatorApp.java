package org.main;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

/*TODO
    Добавить поддержку языков: Украинксий , польский, испанский, немецкий , французкий , португальский
 */
public class LocalizationComparatorApp extends Application implements SettingsChangeListener {

    private Scene scene;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        EditorView mergeEditorView = new EditorView();
        scene = new Scene(mergeEditorView.getView(), 1000, 700);

        Settings settings = mergeEditorView.getSettings();
        applyTheme(settings.getTheme());

        SettingsChangeListener.addListener(this);

        primaryStage.setTitle("Localization Comparator | v1.0");
        primaryStage.getIcons().add(new Image("logo.ico"));
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void applyTheme(String theme) {
        scene.getStylesheets().clear();
        if (theme.equals("Тёмная")) {
            scene.getStylesheets().add(getClass().getResource("/dark-theme.css").toExternalForm());
        } else {
            scene.getStylesheets().add(getClass().getResource("/light-theme.css").toExternalForm());
        }
    }

    @Override
    public void onThemeChanged(String newTheme) {
        applyTheme(newTheme);
    }

}
