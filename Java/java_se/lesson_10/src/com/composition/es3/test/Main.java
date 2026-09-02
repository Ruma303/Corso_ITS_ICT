package com.composition.es3.test;

/*
* Logger componibile: interfaccia Output(scrivi(String))
* Implementa ConsoleOutput e FileOutput
* Classe Logger HAS-A Output
* Cambia destinazione senza toccare Logger
* Aggiungi prefisso timestamp
* */

import com.composition.es3.business.ConsoleOutput;
import com.composition.es3.business.FileOutput;
import com.composition.es3.business.Logger;

public class Main {
    static void main() {
        Logger l1 = new Logger(new ConsoleOutput());
        Logger l2 = new Logger(new FileOutput("./test.log"));

        l1.getOutput().scrivi("Sto scrivendo dal main");
        l2.getOutput().scrivi("Sto scrivendo dal main");
    }
}
