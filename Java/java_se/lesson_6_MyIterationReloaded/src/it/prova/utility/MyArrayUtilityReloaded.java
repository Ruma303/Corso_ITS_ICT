package it.prova.utility;

public class MyArrayUtilityReloaded {

  public static int[] incrementaOgniElementoDiUnTot(int[] input, int incremento) {
    int[] result = new int[input.length];
    for (int a = 0; a < result.length; a++) {
      result[a] = input[a] + incremento;
    }
    return result;
  }

  public static String costruisciStringaDiCaratteriASecondaDi(String fraseInput, int discrimine) {
    String result = "";
    boolean pari = discrimine % 2 == 0;

    if (pari)
      for (int n = 0; n < fraseInput.length(); n += 2)
        result += fraseInput.charAt(n);
    else
      for (int n = 1; n < fraseInput.length(); n += 2)
        result += fraseInput.charAt(n);

    return result;
  }

  public static String costruisciStringaDiCaratteriASecondaDi2(String fraseInput, int discrimine) {
    String result = "";
    for (int n = 0; n < fraseInput.length(); n++) {
      // Verifico lunghezza stringa totale se pari o dispari

      // Costruisco la stringa se discrimine è pari
      if (discrimine % 2 == 0) {
        // Accedo al singolo carattere per vedere se la sua posizione è pari
        if (n % 2 == 0)
          result += fraseInput.charAt(n);
        else
          continue;
      }

      // Costruisco la stringa se discrimine è dispari
      else {
        // Accedo al singolo carattere per vedere se la sua posizione è dispari
        if (n % 2 != 0)
          result += fraseInput.charAt(n);
        else
          continue;
      }
    }
    return result;
  }

  public static int[] riempiArrayConMultipli(int quanti, int moltiplicando) {
    int[] result = new int[quanti];
    for (int n = 0; n <= result.length - 1; n++)
      result[n] = moltiplicando * (n + 1);
    return result;
  }

  public static int[] calcolaArrayModificato(int[] input, int daSottrarre) {
    int[] result = new int[input.length];
    for (int n = 0; n < result.length; n++) {
      int temp = input[n] - daSottrarre;
      if (temp < 0) {
        temp = 0;
        result[n] = temp;
      }
      result[n] = temp;
    }
    return result;
  }
}
