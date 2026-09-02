package com.its.lesson;

public class ConsoleOutput implements Output {
    @Override
    public void scrivi(String messaggio) {
        System.out.println("\nConsole Output Logger: " + messaggio + "\n");
    }

    public ConsoleOutput() {
    }
}
