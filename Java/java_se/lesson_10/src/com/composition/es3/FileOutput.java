package com.composition.es3;

public class FileOutput implements Output {
    private String fileName;

    @Override
    public void scrivi(String messaggio) {
        // Al momento non implementiamo PrintWriter
        System.err.println("\nFile Output Logger: " + messaggio + " sul file " + this.fileName + "\n");

    }

    public FileOutput(String fileName) {
        this.fileName = fileName;
    }
}
