package it.prova.test;

import it.prova.model.Abitante;
import it.prova.model.Indirizzo;

public class TestAbitante {
  public static void main(String[] args) {

    Abitante a1 = new Abitante("Mario", "Rossi", 50);
    Indirizzo i1 = new Indirizzo("Roma", "Via col vento", "67");
    a1.setIndirizzo(i1);

    Abitante a2 = new Abitante("Piero", "Ughi", 67);
    a2.setNome("Piero");
    a2.setCognome("Ughi");
    a2.setEta(90);
    Indirizzo i2 = new Indirizzo("Milano", "viale via viola", "25");
    a2.setIndirizzo(i2);

    Abitante a3 = new Abitante("Simone", "Letsgosky", 18);
    Indirizzo i3 = new Indirizzo("Roma", "Via col vento", "67");
    a3.setIndirizzo(i3);

    Abitante[] tizi = new Abitante[] { a1, a3 };
    Abitante[] tizi2 = new Abitante[] { a1, a2, a3 };

    String citta = "Roma";
    System.out.println(
        a1.abitaA(citta)
            ? a1.toString() + " abita a Roma"
            : a1.toString() + " NON abita a Roma");

    System.out.println(
        a1.abitaA("Palermo")
            ? a1.toString() + " abita a Palermo"
            : a1.toString() + " NON abita a Palermo");

    System.out.println(
        a1.haAlmenoUnConcittadino(tizi)
            ? a1.toString() + " ha almeno un concittadino"
            : a1.toString() + " NON HA concittadini");

    System.out.println(
        a2.haAlmenoUnConcittadino(tizi)
            ? a2.toString() + " ha almeno un concittadino"
            : a2.toString() + " NON HA concittadini");

    System.out.println(
        a1.sonoTuttiPiuAnziani(tizi)
            ? "Sono tutti più anziani di " + a1.toNome()
            : "NON sono tutti più anziani di " + a1.toNome());

    System.out.println(
        a3.sonoTuttiPiuAnziani(tizi)
            ? "Sono tutti più anziani di " + a3.toNome()
            : "NON sono tutti più anziani di " + a3.toNome());

    System.out.println("Nel mio palazzo abitano " +
        a3.quantiCoabitanoNelMioStessoPalazzo(tizi) + " persone");

    System.out.println("Ci sono " +
        a3.quantiMieiOmonimiNellaMiaStessaCitta(tizi) + " omonimi di "
        + a3.toNome()
      );

      System.out.println(
        a3.almenoLaMetaAbitanoNellaMiaStessaVia(tizi2)
            ? "Almeno la metà abitano nella via: " + a3.getIndirizzo()
            : "NON almeno la metà abitano nella via: " + a3.getIndirizzo());


  }
}
