package com.orchestra.test;

/*
 1. Creare la classe astratta Strumento con attributi anno, marca e metodo astratto suona()
 2. Creare classe concreta Flauto che estende Strumento con attributo materiale
 3. Creare classe concreta Chitarra che estende Strumento con attributo numCorde
 4. Creare classe concreta Pianoforte che estende Strumento con attributo numTasti
 4. Creare classe Orchestra con metodo main che crea una serie di strumenti e fa suonare tutti in fila.
 */

import com.orchestra.model.*;

import java.util.ArrayList;
import java.util.List;

public class Orchestra {
    public static void main(String[] args) {

        // 1. Creazione classica (Costruttore)
        Chitarra c1 = new Chitarra(2026, "Solar", 6);

        // 2. Creazione Builder Classico (new NomeClasse.Builder())
        Flauto f1 = new Flauto.Builder()
                .setAnno(2026)
                .setMarca("Yamaha")
                .setMateriale("Argento")
                .build();

        // 3. Creazione Builder Moderno (NomeClasse.builder())
        // Non serve scrivere "new Pianoforte.Builder()", l'esperienza d'uso è pulitissima.
        Pianoforte p1 = Pianoforte.builder()
                .anno(1980)
                .marca("Steinway & Sons")
                .numeroTasti(88)
                .build();

        // Mettiamo tutti gli strumenti in fila (Polimorfismo)
        List<Strumento> orchestra = new ArrayList<>();
        orchestra.add(c1);
        orchestra.add(f1);
        orchestra.add(p1);

        System.out.println("--- INIZIO CONCERTO ---");
        for (Strumento strumento : orchestra) {
            strumento.suona(); // Esegue l'override corretto per ogni sottoclasse
        }
    }
}