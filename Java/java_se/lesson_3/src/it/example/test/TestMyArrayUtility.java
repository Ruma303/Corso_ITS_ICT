package it.example.test;

import it.example.utility.MyArrayUtility;

public class TestMyArrayUtility {

  public static void main(String[] args) {
    int[] numbers = MyArrayUtility.getIntegerArray;
    System.out.println("Prodotto di tutti i numeri: " + MyArrayUtility.ottieneProdottoDaArrayDiInteri(numbers));

    String[] names = MyArrayUtility.getNamesArray;
    System.out.println(MyArrayUtility.ottieniParolaPiuLunga(names) + " è la parola più lunga");

    System.out.println("Luca è presente " + MyArrayUtility.quanteVolteEPresente(names, "Luca") + " volte");

    if (MyArrayUtility.verificaSeSommaEZero(numbers))
      System.out.println("La somma finale è zero");
    else
      System.out.println("La somma finale NON è zero");

    System.out.println("Ci sono " + MyArrayUtility.quanteParoleHannoLunghezzaDispari(names) + " parole di lunghezza dispari");
  }

}
