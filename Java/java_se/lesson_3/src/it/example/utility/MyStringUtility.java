package it.example.utility;

public class MyStringUtility {
  public static String[] getStringsArray;
  public static int[] getIntegerArray;

  static {
    getStringsArray = new String[] { "Ugo", "Ada", "Zoi"};
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

  public static int sommaLunghezzeNomi(String[] nomi) {
    int result = 0;
    for (String n : nomi)
      result += n.length();
    return result;
  }

  public static boolean verificaTuttiNumeriPari(int[] numbers) {
    for (int num : numbers)
      if (num % 2 != 0)
        return false;
    return true;
  }

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

  public static int dimmiQuantiElementiStrettamenteMinoriDi(int[] elementi, int soglia) {
    int result = 0;
    for (int num: elementi) {
      if (num < soglia) {
        result++;
      }
    }
    return result;
  }

  public static boolean sonoTuttiDentroUnIntervallo(int[]valori, int sogliaMin, int sogliaMax) {
    for (int num: valori)
      if (num < sogliaMin || num > sogliaMax)
        return false;
    return true;
  }

  public static boolean nomiUgualiNellePrimeNPosizioni(String[]elenco, int nPosizioni) {
    String prev = elenco[0];
    for (int i = 0; i < nPosizioni; i++) {
      if (!elenco[i].equals(prev)) {
        return false;
      }
      prev = elenco[i];
    }
    return true;
  }

  public static boolean ePresenteSoloUnaVolta(String[] elenco, String nome) {
    int presence_counter = 0;
    for (String value : elenco) {
      if (value == nome) {
        if (presence_counter < 2)
          return false;
        presence_counter++;
      }
    }
    return true;
  }
}
