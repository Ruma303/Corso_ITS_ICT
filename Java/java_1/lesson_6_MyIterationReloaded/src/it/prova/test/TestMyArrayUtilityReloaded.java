package it.prova.test;

import it.prova.utility.MyArrayUtilityReloaded;

public class TestMyArrayUtilityReloaded {
  public static void main(String[] args) {

    int[] numbers1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    int incremento = 5;
    System.out.println(
        "Il nuovo array di interi dove ogni valore viene incrementato di '" + incremento + "' è: ");
    for (int n : MyArrayUtilityReloaded.incrementaOgniElementoDiUnTot(numbers1, incremento))
      System.out.print(n + ", ");

    String prova1 = "Hello";
    System.out.println(
        "Versione 1 = Nuova stringa di lunghezza dispari: "
            + MyArrayUtilityReloaded.costruisciStringaDiCaratteriASecondaDi(prova1, 2));

    System.out.println(
        "Versione 1 = Nuova stringa di lunghezza dispari: "
            + MyArrayUtilityReloaded.costruisciStringaDiCaratteriASecondaDi(prova1, 3));

    System.out.println(
        "Versione 2 = Nuova stringa di lunghezza dispari: "
            + MyArrayUtilityReloaded.costruisciStringaDiCaratteriASecondaDi2(prova1, 2));
    System.out.println(
        "Versione 2 = Nuova stringa di lunghezza dispari: "
            + MyArrayUtilityReloaded.costruisciStringaDiCaratteriASecondaDi2(prova1, 3));

    int quanti = 4;
    int moltiplicando = 3;
    System.out.println(
        "Il nuovo array di numeri contiene '" + quanti + "' elementi, e ogni elemento è moltiplicato per '"
            + moltiplicando + "':");
    for (int n : MyArrayUtilityReloaded.riempiArrayConMultipli(quanti, moltiplicando))
      System.out.print(n + " ");

    int[] arrayDaSottrarre = { 5, 7, 4, 63, 52, 1, 21, 32, 6, 91 };
    int daSottrarre = 6;
    System.out.println(
        "Il nuovo array di numeri ha ogni valore sottratto per '" + daSottrarre + "'':");
    for (int n : MyArrayUtilityReloaded.calcolaArrayModificato(arrayDaSottrarre, daSottrarre))
      System.out.print(n + " ");
  }
}
