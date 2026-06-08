package it.prova.test;

public class TryNumbers {

  public static void main(String[] args) {

    int val1 = 7;
    int val2 = 9;

    System.out.println("Esercitazioni sui costrutti condizionali");

    if (val1 > val2) {
      System.out.println("val1 > val2");
    } else if (val1 == val2) {
      System.out.println("val1 == val2");
    } else {
      System.out.println("val1 < val2");
    }

    if (val1 != 7) {
      System.out.println("val1 non è uguale a 7");
    } else if (val1 == 7 | val1 > 0) {
      System.out.println("val1 è 7 ed è maggiore di 0");
    }

    System.out.println("\nStampare i numeri da 20 a 1 al contrario");

    for (int i = 20; i >= 0; i--) {
      if (i == 10)
        continue;
      if (i < 3)
        break;
      System.out.println(i);
    }

    System.out.println("\nStampare i numeri dispari da 1 a 100");
    for (int i = 1; i <= 100; i++) {
      if (i % 2 != 0) {
        System.out.println(i);
        continue;
      }
    }

    System.out.println("\nStampare i valori dell'array");

    int[] valoriDaEsplorare = { 5, 8, 12, 55, 9 };
    System.out.println("\nStampare lineare");
    for (int j = 0; j < valoriDaEsplorare.length; j++)
      System.out.println("Posizione: " + (j + 1) + ". " + valoriDaEsplorare[j]);

    System.out.println("\nStampare lineare al contrario");
    for (int j = valoriDaEsplorare.length - 1; j >= 0 ; j--)
      System.out.println("Indice: " + j + ". " + valoriDaEsplorare[j]);

  }
}
