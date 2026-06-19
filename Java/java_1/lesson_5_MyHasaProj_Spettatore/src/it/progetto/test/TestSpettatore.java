package it.progetto.test;

import it.progetto.model.*;

public class TestSpettatore {

  public static void main(String[] args) {


    Biglietto b1 = new Biglietto("Il Re Leone",    'A', 1,  45.0f);
    Biglietto b2 = new Biglietto("Il Re Leone",    'A', 2,  45.0f);
    Biglietto b3 = new Biglietto("Cats",           'B', 5,  30.0f);
    Biglietto b4 = new Biglietto("Notre Dame",     'C', 12, 55.0f);
    Biglietto b5 = new Biglietto("Notre Dame",     'A', 3,  55.0f);

    Biglietto[] tuttiBiglietti = {b1, b2, b3, b4, b5};
    Biglietto[] invenduti = { b3, b4 };



    Spettatore s1 = new Spettatore("Mario",  "Rossi",   1111, b1);
    Spettatore s2 = new Spettatore("Giulia", "Bianchi", 2222, b2);
    Spettatore s3 = new Spettatore("Luca",   "Verdi",   3333, b5);

    Spettatore[] spettatori = { s1, s2, s3 };


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

    

  }

}
