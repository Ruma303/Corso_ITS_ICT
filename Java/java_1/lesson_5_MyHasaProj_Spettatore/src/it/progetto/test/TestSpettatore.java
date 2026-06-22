package it.progetto.test;

import it.progetto.model.*;

public class TestSpettatore {

  public static void main(String[] args) {


    Biglietto b1 = new Biglietto("Il Re Leone",    'A', 1,  45.0f);
    Biglietto b2 = new Biglietto("Il Re Leone",    'A', 2,  45.0f);
    Biglietto b3 = new Biglietto("Cats",           'B', 5,  30.0f);
    Biglietto b4 = new Biglietto("Notre Dame",     'C', 12, 65.0f);
    Biglietto b5 = new Biglietto("Notre Dame",     'A', 3,  55.0f);
    Biglietto b6 = new Biglietto("Notre Dame",     'B', 3,  55.0f);
    Biglietto b7 = new Biglietto("Notre Dame",     'F', 3,  55.0f);

    Biglietto[] tuttiBiglietti = {b1, b2, b3, b4, b5, b6};
    Biglietto[] invenduti = { b3, b7 };
    Biglietto[] bigliettiIlReLeone = { b1, b2 };

    Spettatore s1 = new Spettatore("Mario",  "Rossi",   1111, b1);
    Spettatore s2 = new Spettatore("Giulia", "Bianchi", 2222, b2);
    Spettatore s3 = new Spettatore("Luca",   "Verdi",   3333, b4);
    Spettatore s4 = new Spettatore("Giuseppe",   "Neri",   4444, b5);
    Spettatore s5 = new Spettatore("Giacomo",   "Gialli",   5555, b6);
    Spettatore s6 = new Spettatore("Viola",   "Rosa",   6666, null);
    Spettatore s7 = new Spettatore("Rosa",   "Viola",   7777, null);

    Spettatore[] spettatori = { s1, s2, s3, s4, s5, s6, s7 };


    // Test Biglietti

    System.out.println("Il biglietto più economico è " + Biglietto.trovaIlPiuEconomico(tuttiBiglietti));

    System.out.println(
      b2.bigliettoAncoraInvenduto(invenduti)
      ? " Il " + b2 + " è invenduto"
      : " Il " + b2 + " è stato venduto"
    );

    System.out.println(
      b3.bigliettoAncoraInvenduto(invenduti)
      ? " Il " + b3 + " è invenduto"
      : " Il " + b3 + " è stato venduto"
    );

    // Test Spettatori
    char filaA = 'A';

    System.out.println(
      "Incasso dei paganti nella fila '" + filaA + "' : " + s1.incassoDeiPagantiNellaMiaFila(spettatori) + "€"
    );

    System.out.println(
      "Allo spettacolo di " + s1.toNome() + " partecipano " + s1.numeroSpettatoriDelMioStessoSpettacolo(spettatori) + " spettatori"
    );

    int aspettativa = 2;

    System.out.println(
      s4.numeroSpettatoriMioSpettacoloSuperaAspettativa(spettatori, aspettativa)
      ? "Lo spettacolo '" + s4.getBiglietto().getNomeSpettacolo() + "' supera le aspettative di " + aspettativa + " spettatori"
      : "Lo spettacolo '" + s4.getBiglietto().getNomeSpettacolo() + "' NON supera le aspettative di " + aspettativa + " spettatori"
    );

    System.out.println(
      "Ci sono " + Spettatore.contaQuantiSenzaBiglietto(spettatori) + " senza biglietto"
    );

    System.out.println(
      "Ci sono " + s1.contaQuantiNellaMiaStessaFila(spettatori) + " spettatori nella fila di " + s1.toNome()
    );

    System.out.println(
      b4.eIlPiuCaroTraIBigliettiDeiPaganti(spettatori)
      ? "Il biglietto '" + b4.getNomeSpettacolo() + "' è il più caro tra i biglietti dei paganti"
      : "Il biglietto '" + b4.getNomeSpettacolo() + "' NON è il più caro tra i biglietti dei paganti"
    );

    String spettacoloDaRicercare = "Il re leone";
    boolean spettacoloIdentico = Biglietto.sonoTuttiBigliettiPerLoSpettacoloIntitolato(bigliettiIlReLeone, spettacoloDaRicercare);
    System.out.println(
        spettacoloIdentico
      ? "Sono tutti biglietti per lo spettacolo '" + spettacoloDaRicercare + "'"
      : "NON sono tutti biglietti per lo spettacolo '" + spettacoloDaRicercare + "'"
    );
  }
}
