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

    Televisore tv2 = new Televisore("Panasonic", "UltraWide", 49, 1200);
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
      : "tv2 NON costa meno di " + budget
    );



  }
}
