package org.example.singleton.threadSafe.eagerInitialization;

public class Settings {
    private static final Settings INSTANCE = new Settings();
    private Settings() {
    }

    // 단점: 미리 만든다는 점(이 인스턴스가 리소스가 많이 소모된다면?)
    public static Settings getInstance() {
        return INSTANCE;
    }
}
