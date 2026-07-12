package com.composition.es1.test;

/*
* Computer HAS-A CPU(marca, GHz), RAM(GB), Disco(tipo,GB).
* Il costruttore riceve tutti i componenti.
* Metodo descriviConfig() stampa la configurazione completa.
* Crea tre computer diversi.
*/

import com.composition.es1.model.CPU;
import com.composition.es1.model.Computer;
import com.composition.es1.model.RAM;
import com.composition.es1.model.Storage;

public class Main {
    static void main(String[] args) {

        CPU c1Cpu = new CPU("Intel", 4);
        RAM c1Ram = new RAM(32);
        Storage c1Storage = new Storage("SSD", 4000);

        // Aggregazione - I componenti vivono separatamente e non dipendono dalla loro implementazione in Computer
        Computer c1 = new Computer(c1Cpu, c1Ram, c1Storage);

        System.out.println("\n");
        System.out.println(c1.descriviConfig());

        c1.getCpu().verificaPerformace();
        c1.getRam().verificaPerformace();

        // Composizione tramite le interfacce
        c1.getStorage().verificaPerformace();

        Computer c2 = new Computer(
                new CPU("Apple Silicon M5", 4),
                new RAM(24),
                new Storage("SSD", 1000)
        );

        System.out.println("\n");
        System.out.println(c2.descriviConfig());
        c2.testPerformace();

        // Composizione tramite classi
        // VERA COMPOSIZIONE: Il Main passa solo i dati, non gli oggetti.
        Computer c3 = new Computer("AMD", 3,24,"SSD", 2000);
        System.out.println("\n");
        System.out.println(c3.descriviConfig());
        c3.testPerformace();

    }
}
