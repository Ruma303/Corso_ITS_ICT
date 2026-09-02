package com.composition.es3.business;

public class ConsoleOutput implements Output {
    private String fileName;

    @Override
    public void scrivi(String messaggio) {
        System.err.println("\nFile Output Logger: " + messaggio + " sul file " + this.fileName + "\n");
    }
}
