package com.orchestra.test;

/*
 1. creare la classe astratta Strumento con atributi anno, marca e metodo astratto suona()
 2. Creare classe concreta Flauto che estende Strumento con atributo materiale
 3. Creare classe concreta Chitarra che estende Strumento con atributo numCorde
 4. Creare classe concreta Pianoforte che estende Strumento con atributo numTasti
 4. Creare classe Orchestra con metodo main che crea una serie di strumenti e fà suonare tutti in fila.
 */

// Rifare con pattern builder

public class Main {
    static void main(String[] args) {
        Chitarra c1 = new Chitarra(2026, "Solar", 6);
        c1.suona();

        Flauto f1 = new Flauto.Builder()
                .setAnno(2026)
                .setMarca("Gibson")
                .setMateriale("Acero")
                .build();
        f1.suona();
    }
}