package it.example.utility;

/*
1. public static String buildStringUntil(int until) . Se prende 5 restituisce 12345
2. public static String inverti(String daInvertire)

*/

public class MyStringUtility {
  public static String[] getStringsArray;
  public static int[] getIntegerArray;

  static {
    getStringsArray = new String[] { "Ugo", "Ada", "Zoi" };
    getIntegerArray = new int[] { 1, 3, 2, 6, 6, 7, 9, 8, -7, 4, 12, -2 };
  }

  public static String buildStringUtil(int util) {
    String result = "";
    int count = 0;
    do {
      result += (count + 1);
      count++;
    } while (count <= util);
    return result;
  }

  public static String inverti(String daInvertire) {
    String result = "";
    char[] parolaDaInvertire = daInvertire.toCharArray();
    for (int i = parolaDaInvertire.length - 1; i >= 0; i--) {
      result += (char) parolaDaInvertire[i];
    }
    return result;
  }

  public static boolean sonoTuttiDiUgualeLunghezza(String[] elenco) {
    int prevLen = elenco[0].length();
    for (String word : elenco) {
      if (word.length() != prevLen)
        return false;
    }
    return true;
  }

  public static boolean terminanoTuttiConIlCarattere(String[] elenco, char finale) {
    char[] prevString = elenco[0].toCharArray();
    char prevLastChar = prevString[prevString.length - 1];

    for (int i = 0; i < elenco.length; i++) {
      char[] currentString = elenco[i].toCharArray();
      char currentLastChar = currentString[currentString.length - 1];
      if (prevLastChar != currentLastChar) {
        return false;
      }
    }
    return true;
  }

  /*
   * Dato un array di nomi voglio calcolare la somma delle lunghezze dei singoli
   * elementi
   */
  public static int sommaLunghezzeNomi(String[] nomi) {
    int result = 0;
    for (String n : nomi)
      result += n.length();
    return result;
  }

  /*
   * Dato un array di interi verificare che siano tutti numeri pari
   */

  public static boolean verificaTuttiNumeriPari(int[] numbers) {
    for (int num : numbers)
      if (num % 2 != 0)
        return false;
    return true;
  }

  /*
   * Dato un array in interi in input verificare se tra i negativi esista almeno
   * un numero pari
   */

  public static boolean verificaSeTraNegativiEsisteNumeroPari(int[] numbers) {
    for (int num : numbers)
      if (num < 0 && num % 2 == 0)
        return true;
    return false;
  }

  /*
   * Dato un array di interi sommare gli elementi in posizione dispari, scorrendo
   * al contrario
   */
  public static int sommaPariAlContrario(int[] numbers) {
    int result = 0;
    for (int i = numbers.length -1; i>= 0; i--) {
      if (i %2 != 0)
        result += numbers[i];
    }
    return result;
  }

}
