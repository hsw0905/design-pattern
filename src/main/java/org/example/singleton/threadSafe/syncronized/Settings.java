package org.example.singleton.threadSafe.syncronized;

public class Settings {
    private static Settings instance;
    private Settings() {
    }

//    단점 : synchronized 메커니즘(락/해제)에 따른 성능 부하
    public static synchronized Settings getInstance() {
        if (instance == null) {
            instance = new Settings();
        }
        return instance;
    }
}
