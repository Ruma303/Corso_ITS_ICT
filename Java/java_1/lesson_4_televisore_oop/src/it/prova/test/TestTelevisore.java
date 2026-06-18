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
    tv1.setMarca("Marca sconosciuta");
    tv1.setModello("Modello sconosciuto");
    tv1.setPollici(100);
    tv1.setPrezzo(3000);

    Televisore tv2 = new Televisore("Panasonic", "UltraWide", 1200, 80);
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
            ? "La prima tv " + tv4.getNome() + " è più grande di quella confrontata "
                + tv2.getNome()
            : "La prima tv " + tv4.getNome() + " è più piccola di quella confrontata "
                + tv2.getNome());

    System.out.println(
        tv4.miglioreQualitaPrezzoDi(tv2)
            ? "Questa tv " + tv4 + " ha un rapporto prezzo / pollici più conveniente di " + tv2.getNome()
            : "La tv " + tv2 + " ha un rapporto prezzo / pollici più conveniente di " + tv4.getNome());

    Televisore[] televisori = new Televisore[] { tv1, tv2, tv3, tv4 };

    System.out.println(
        tv2.esisteAlmenoUnoPiuEconomico(televisori)
            ? "Esiste un televisore più economico di " + tv2.getNome()
            : "NON esiste un televisore più economico di " + tv2.getNome());

    System.out
        .println("Esistono " + tv2.quantiSonoPiuGrandi(televisori) + " televisori più grandi di " + tv2.getNome());

    System.out
        .println("Esistono " + tv3.quantiSonoPiuCariAvendoStessaMarca(televisori)
            + " televisori più cari avendo la stessa marca " + tv3.getMarca());

    System.out.println(
        tv1.ePiuCaroDellaMedia(televisori)
            ? "Il televisore " + tv1.getNome() + " è più caro della media"
            : "Il televisore " + tv1.getNome() + " NON è più caro della media");

    Televisore tvPiuCostosa = Televisore.getPiuCostoso(televisori);
    System.out
        .println("La tv più costosa è " + tvPiuCostosa.getNome() + " e costa " + tvPiuCostosa.getPrezzo());
    }
}
