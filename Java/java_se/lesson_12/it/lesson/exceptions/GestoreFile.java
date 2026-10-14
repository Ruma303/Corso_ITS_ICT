package it.lesson.exceptions;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class GestoreFile {
    public String leggiPrimaLinea(String percorsoFile) throws IOException {
        File file = new File(percorsoFile);
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            return reader.readLine();
        }
    }
}