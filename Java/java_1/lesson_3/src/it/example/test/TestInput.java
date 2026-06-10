package it.example.test;

import java.util.Scanner;

public class TestInput {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    inserisciNumeriEdEsciQuandoTrovaUnNegativo(scanner);
    scanner.close();
  }

  public static boolean inserisciNumeriEdEsciQuandoTrovaUnNegativo(Scanner sc) {
    boolean result = false;
    System.out.println("Inserisci un numero intero:\n");
    do {
      int num = sc.nextInt();
      if (num < 0) {
        System.out.println("Il numero " + num + " è un numero intero negativo. Uscita dal programma.");
        return true;
      }
      System.out.println("Il numero " + num + " NON è negativo. Inserisci un numero intero negativo.");
    } while (sc.hasNextInt());
    return result;
  }
}
