package it.prova.test;

public class TryMethodsCall {

  public static void main(String[] args) {
    stampaNumeri(10);

    System.out.println(stampaMaggiore(10, 20));
    System.out.println(stampaMaggiore(20, 20));
    System.out.println(stampaMaggiore(20, 10));

    int[] valori = { 1, 3, 2, 6, 6, 7, 9, 8, 4, 12 };
    System.out.println(esisteElemento(valori, 04));

    System.out.println(sommaElementi(valori));
    System.out.println(trovaIlMaggiore(valori));

    // Usiamo anche args
    if (args.length > 0) {
      System.out.println("Numero totale di argomenti: " + args.length);
      for (String arg: args) System.out.println("\t- " + arg + " ");
    }
  }

  public static void stampaNumeri(int input) {
    for (int i = 0; i <= input; i++) {
      System.out.println(i);
    }
  }

  public static String stampaMaggiore(int val1, int val2) {
    String messaggio = "";

    if (val1 > val2) {
      messaggio = "val1 (" + val1 + ") > val2 (" + val2 + ")";
    } else if (val1 == val2) {
      messaggio = "val1 (" + val1 + ") == val2 (" + val2 + ")";
    } else {
      messaggio = "val1 (" + val1 + ") < val2 (" + val2 + ")";
    }
    return messaggio;

    /*
     * Oppure
     * if (val1 > val2) {
     * return "val1 (" + val1 + ") > val2 (" + val2 + ")";
     * } else if (val1 == val2) {
     * return "val1 (" + val1 + ") == val2 (" + val2 + ")";
     * } else {
     * return "val1 (" + val1 + ") < val2 (" + val2 + ")";
     * }
     */
  }

  public static boolean esisteElemento(int[] valori, int numeroDaRicercare) {
    for (int element : valori) {
      if (element == numeroDaRicercare)
        return true;
    }
    return false;
  }

  public static int sommaElementi(int[] valori) {
    int somma = 0;
    for (int i = 0; i < valori.length; i++)
      somma += i;
    return somma;
  }

  public static int trovaIlMaggiore(int[] valori) {
    int maggiore = 0;
    for (int i = 0; i < valori.length; i++) {
      if (valori[i] > maggiore) {
        maggiore = valori[i];
      }
    }
    return maggiore;
  }
}
