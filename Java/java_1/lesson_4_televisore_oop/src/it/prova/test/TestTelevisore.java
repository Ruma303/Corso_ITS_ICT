package it.prova.test;

import it.prova.model.*;

public class TestTelevisore {
  public static void main(String[] args) {

    Televisore tv1 = new Televisore();
    System.out.println("Televisore con valori di default: "
        + " " + tv1.getMarca()
        + " " + tv1.getModello()
        + " " + tv1.getPollici()
        + " " + tv1.getPrezzo());

    Televisore tv2 = new Televisore("Panasonic", "UltraWide", 1200, 89);
    System.out.println(tv2);

    Televisore tv3 = new Televisore();
    tv3.setMarca("Samsung");
    tv3.setModello("OLED");
    tv3.setPollici(89);
    tv3.setPrezzo(1_300);
    System.out.println(tv3);

    int budget = 2000;
    System.out.println(
        tv2.costaMenoDelBudgetDisponibile(budget)
            ? "tv2 costa meno di " + budget
            : "tv2 NON costa meno di " + budget);

    Televisore tv4 = new Televisore();
    tv4.setMarca("Samsung");
    tv4.setModello("Infinity Wrapper");
    tv4.setPollici(50);
    tv4.setPrezzo(1_800);
    System.out.println(tv4);

    System.out.println(
        tv4.stessaMarcaDi(tv3)
            ? "Le due tv sono della stessa marca"
            : "Le due tv NON sono della stessa marca");

    System.out.println(
        tv4.stessaMarcaDi(tv2)
            ? "Le due tv sono della stessa marca"
            : "Le due tv NON sono della stessa marca");

    System.out.println(
        tv4.piuGrandeDi(tv2)
            ? "La prima tv " + tv4.getMarca() + " " + tv4.getModello() + " è più grande di quella confrontata "
                + tv2.getMarca() + " " + tv2.getModello()
            : "La prima tv " + tv4.getMarca() + " " + tv4.getModello() + " è più piccola di quella confrontata "
                + tv2.getMarca() + " " + tv2.getModello());

    System.out.println(
        tv4.miglioreQualitaPrezzoDi(tv2)
            ? "Questa tv " + tv4 + " ha un rapporto prezzo / pollici più conveniente di " + tv2.getMarca() + " "
                + tv2.getModello()
            : "La tv " + tv2 + " ha un rapporto prezzo / pollici più conveniente di " + tv4.getMarca() + " "
                + tv4.getModello());
  }
}
