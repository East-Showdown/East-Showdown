package org.main;

import java.util.ArrayList;
import java.util.List;

public interface SettingsChangeListener {
    void onThemeChanged(String newTheme);

    List<SettingsChangeListener> listeners = new ArrayList<>();

    static void addListener(SettingsChangeListener listener) {
        listeners.add(listener);
    }

    static void notifyThemeChanged(String newTheme) {
        for (SettingsChangeListener listener : listeners) {
            listener.onThemeChanged(newTheme);
        }
    }
}
