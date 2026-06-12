package it.example.test;

import it.example.utility.*;

public class TestMyArrayUtility2 {
  public static void main(String[] args) {

    int[] numbers = MyArrayUtility2.numbers;
    int[] primo = MyArrayUtility2.primo;
    int[] secondo = MyArrayUtility2.secondo;
    // int[] terzo = MyArrayUtility2.terzo;
    String[] nomi = MyArrayUtility2.nomi;

    System.out.println("Il numero più piccolo è: " + MyArrayUtility2.trovaMinoreIterandoAlContrario(numbers));

    System.out.println("Sono stati trovati " + MyArrayUtility2.trovaQuantiZeriIterandoAlContrario(numbers) + " zeri");

    System.out.println(
      MyArrayUtility2.verificaSeSommaDispariEDispari(numbers)
      ? "La somma dei dispari è un dispari, no way"
      : "La somma dei dispari NON è un dispari"
    );

    System.out.println(
      MyArrayUtility2.verificaSeSecondoArrayContieneMultiploDiPrimo(primo, secondo)
      ? "Tutti i valori del primo array sono multipli del primo"
      : "Alcuni valori del secondo array non sono multipli del primo"
    );

    char carattereFinaleDiControllo = 'o';
    System.out.println(
      MyArrayUtility2.terminanoTuttiConIlCarattere(nomi, carattereFinaleDiControllo)
      ? "Tutti i nomi terminano con '" + carattereFinaleDiControllo + "'"
      : "NON tutti i nomi terminano con '" + carattereFinaleDiControllo + "'"
    );

    int nuovoElemento = 10;
    int[] nuovoArray =  MyArrayUtility2.aggiungiInCoda(secondo, nuovoElemento);

    System.out.println("");
    for (int n : nuovoArray)
      System.out.println(n);

    int posizioneDaRimuovere = 2;
    int[] terzo = { 1, 4, 27, 3, 6, 7, 1 };
    int[] nuovoArray2 = MyArrayUtility2.rimuoviDaPosizioneX(terzo, posizioneDaRimuovere);
    /*
    int[] nuovoArray3 = MyArrayUtility2.rimuoviDaPosizioneX2(terzo, posizioneDaRimuovere);

    System.out.println("");
    for (int u : nuovoArray2)
      System.out.println(u); */

    System.out.println(
      MyArrayUtility2.valutaSeTantiDispariQuantiPari(terzo)
      ? "C'è la stessa quantità di numeri pari e dispari "
      : "Non c'è la stessa quantità di numeri pari e dispari "
    );

    int divisore = 3;
    System.out.println(
      "Ci sono " +
      MyArrayUtility2.quantiSonoDivisibiliPer(terzo, divisore) +
      " numeri divisibili per " + divisore
    );
  }
}