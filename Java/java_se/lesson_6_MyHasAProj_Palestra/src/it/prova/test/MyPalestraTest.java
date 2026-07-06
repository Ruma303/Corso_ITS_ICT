package it.prova.test;

import it.prova.model.Abbonamento;
import it.prova.model.Iscritto;

public class MyPalestraTest {
  public static void main(String[] args) {
    // Test abbonamenti

    Abbonamento ab1 = new Abbonamento("MENSILE", 20, 45, 300);
    Abbonamento ab2 = new Abbonamento("TRIMESTRALE", 50, 50, 300);
    Abbonamento ab3 = new Abbonamento("MENSILE", 25, 50, 650);
    Abbonamento ab4 = new Abbonamento("ANNUALE", 20, 60, 290);
    Abbonamento[] abbonamentiMensili = { ab1, ab2, ab3, ab4 };

    System.out.println("L'abbonamento più economico è: " +
        Abbonamento.trovaPiuEconomico(abbonamentiMensili));

    System.out.println(
        "Il prezzo medio tra gli abbonamenti di tipo " + ab3.getTipoAbbonamento() + " è: " +
            Abbonamento.prezzoMedioPerTipo(abbonamentiMensili, ab3.getNomeTipo()) + " euri");

    int sogliaMinima = 50;
    System.out.println(
        ab1.isSottoUtilizzato(sogliaMinima)
            ? ab1.toString() + " ha un numero di accessi sotto la soglia minima: " + sogliaMinima
            : ab1.toString() + " NON ha un numero di accessi sotto la soglia minima: " + sogliaMinima);

    System.out.println(
        "Ci sono " + Abbonamento.contaSottoUtilizzati(abbonamentiMensili, sogliaMinima)
            + " abbonamenti sotto-utilizzati rispetto alla soglia minima " + sogliaMinima);

    String tipoAbbonamento = "MENSILE";
    Abbonamento[] abbPerTipo = Abbonamento.filtraPerTipo(abbonamentiMensili, tipoAbbonamento);
    System.out.println(
        "Ci sono " + abbPerTipo.length + " abbonamenti dello stesso tipo '" + tipoAbbonamento + "'");
    for (Abbonamento ab : abbPerTipo)
      System.out.println(ab);

    // Test iscritti

    // Iscritti con abbonamento MENSILE
    Iscritto i1 = new Iscritto("Mario", "Rossi", "RSSMRA80A01F205X", ab1);
    Iscritto i2 = new Iscritto("Giulia", "Bianchi", "BNCGLI85B41F205W", ab3);
    Iscritto i3 = new Iscritto("Luca", "Verdi", "VRDLCU90C12F205Z", ab1);

    // Iscritti con abbonamento TRIMESTRALE
    Iscritto i4 = new Iscritto("Elena", "Gialli", "GLLFormat92D51F205K", ab2);
    Iscritto i5 = new Iscritto("Stefano", "Neri", "NRESFN78E15F205J", ab2);

    // Iscritti con abbonamento ANNUALE
    Iscritto i6 = new Iscritto("Francesca", "Viola", "VLAFNC95F55F205Y", ab4);
    Iscritto i7 = new Iscritto("Alessandro", "Bruni", "BRNLSN88G20F205U", ab4);

    // Iscritti con abbonamento NULL (3 iscritti)
    Iscritto i8 = new Iscritto("Roberto", "Arancini", "RBTRAN82H11F205O", null);
    Iscritto i9 = new Iscritto("Silvia", "Rosa", "RSOSLV87I42F205P", null);
    Iscritto i10 = new Iscritto("Matteo", "Verdi", "VRDMTT99J05F205Q", null);

    Iscritto[] tuttiIscritti = { i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 };

    System.out.println(
      i4.isAbbonamentiStessoTipo(i5)
      ? i4.toNome() + " ha lo stesso abbonamento di " + i5.toNome()
      : i4.toNome() + " NON ha lo stesso abbonamento di " + i5.toNome()
    );

    System.out.println(
      "Esistono " + i4.contaIscrittiStessoTipo(tuttiIscritti) + " che hanno lo stesso tipo di abbonamento"
    );

    String spesaTotale = String.valueOf(Iscritto.spesaTotaleStessoGruppo(tuttiIscritti));
    System.out.println(
      "Spesa totale gruppo dello stesso tipo di abbonamento: " + spesaTotale + "€"
    );

    int soglia = 2;
    System.out.println(
      i3.isIscrittoConPiuDiN(tuttiIscritti, soglia)
      ? "Numero di iscritti supera la soglia " + soglia
      : "Numero di iscritti NON supera la soglia " + soglia
    );

    System.out.println(
      "Il compagno di gruppo con più accessi è " + Iscritto.trovaCompagnoDiGruppoConPiuAccessi(tuttiIscritti).toNome()
    );

    double rounded = Math.round(Iscritto.mediaPrezzoDiversiTipi(tuttiIscritti) * 100.0) / 100.0;
    System.out.println(
      "La media del prezzo è " + rounded + "€"
    );

    System.out.println(
      i7.isIlPiuCostoso(tuttiIscritti)
      ? "L'abbonamento di " + i7.toNome() + " è il più costoso"
      : "L'abbonamento di " + i7.toNome() + " NON è il più costoso"
    );

  }
}
