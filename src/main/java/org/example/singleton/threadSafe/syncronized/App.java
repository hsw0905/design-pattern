package org.example.singleton.threadSafe.syncronized;

public class App {
    public static void main(String[] args) {
        Settings settings = Settings.getInstance();
        System.out.println(settings == Settings.getInstance());
    }
}
