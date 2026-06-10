package it.example.test;

import it.example.utility.MyStringUtility;

public class TestMyStringUtility {
  public static void main(String[] args) {
    String[] names = MyStringUtility.getStringsArray;

    int[] numbers = MyStringUtility.getIntegerArray;

    System.out.println("Build string util: " + MyStringUtility.buildStringUtil(4));

    System.out.println("Stringa \"Pizza\" invertita: " + MyStringUtility.inverti("Pizza"));

    if (MyStringUtility.sonoTuttiDiUgualeLunghezza(MyStringUtility.getStringsArray))
      System.out.println("Le stringhe sono tutte della stessa lunghezza");
    else
      System.out.println("Le stringhe hanno lunghezza differente");

    System.out.println("Somma lunghezza di tutti i nomi: " + MyStringUtility.sommaLunghezzeNomi(names));

    if (MyStringUtility.verificaTuttiNumeriPari(numbers))
      System.out.println("Tutti i numeri sono pari");
    else
      System.out.println("Non tutti i numeri sono pari");

    if (MyStringUtility.verificaSeTraNegativiEsisteNumeroPari(numbers))
      System.out.println("Esiste almeno un numero pari e negativo");
    else
      System.out.println("NON esiste un singolo numero pari e negativo");

    System.out.println("Stampa numeri in posizione dispari scorrendo al contrario: " + MyStringUtility.sommaPariAlContrario(numbers));
  }

}
