package com.composition.es2.test;

/*
* Creare una Squadra che prenda un Allenatore e dei Giocatori.
* Come esercizio, l'Allenatore verrà inserito per aggregazione,
* mentre i giocatori verranno inseriti per composizione.
* */

import com.composition.es2.model.Allenatore;
import com.composition.es2.model.Squadra;

public class Main {
    static void main(String[] args) {

        Allenatore allenatore1 = new Allenatore("Alessio", 01);
        Squadra italia = new Squadra("Italia", allenatore1);

        italia.creaGiocatori();
        italia.descriviSquara();

        italia.aggiungiGiocatore("Michela", 15, "Ala", 592346582);
        System.out.println("\nAggiunto giocatore: " + italia);

        italia.rimuoviGiocatore("Minuzzo");
        System.out.println("\nSquadra dopo aver rimosso giocatore: " + italia);

        System.out.println("\nEtà media squadra: " + (int)italia.etaMedia() + " anni");
        System.out.println("\nCapocannoniere: " + italia.capocannoniere());

    }
}
