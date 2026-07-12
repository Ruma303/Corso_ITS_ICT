package com.composition.es3;

/*
* Logger componibile: interfaccia Output(scrivi(String))
* Implementa ConsoleOutput e FileOutput
* Classe Logger HAS-A Output
* Cambia destinazione senza toccare Logger
* Aggiungi prefisso timestamp
* */

public class Main {
    static void main() {
        Logger l1 = new Logger(new ConsoleOutput());
        Logger l2 = new Logger(new FileOutput("./test.log"));

        l1.getOutput().scrivi("Sto scrivendo dal main");
        l2.getOutput().scrivi("Sto scrivendo dal main");
    }
}
