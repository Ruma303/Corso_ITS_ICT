package it.example.utility;

public class MyArrayUtility2 {

  public final static int[] numbers = { 1, 2, 0, 3, -1, 7, 12, 0, 2, 5, 0, 3, 1 };
  public final static int[] primo = { 1, 2, 3 };
  public final static int[] secondo = { 1, 4, 27 };
  public final static String[] nomi = { "Piero", "Ugo", "Andreo" };

  public final static int[] terzo = { 1, 4, 27, 3, 6, 7, 1 };

  /*
   * Dato un array di interi in input trovare il valore minore iterando al
   * contrario e restituirlo in output.
   */

  public static int trovaMinoreIterandoAlContrario(int[] numbers) {
    int result = numbers[0];
    for (int n = numbers.length - 1; n > 0; n--) {
      if (numbers[n] < result) {
        result = numbers[n];
      }
    }
    return result;
  }

  /*
   * Dato un array in input contare quanti zeri, sempre iterando al contrario.
   */

  public static int trovaQuantiZeriIterandoAlContrario(int[] numbers) {
    int result = 0;
    for (int n = numbers.length - 1; n > 0; n--)
      if (numbers[n] == 0)
        result++;
    return result;
  }

  /*
   * Dato un array di interi in input verificare se la somma dei valori in
   * posizioni dispari risulta un numero dispari.
   */
  public static boolean verificaSeSommaDispariEDispari(int[] numbers) {
    int sum = 0;
    for (int k = 0; k < numbers.length; k += 2)
      sum += numbers[k];
    System.out.println("Somma dei dispari: " + sum);
    if (sum % 2 != 0)
      return true;
    else
      return false;
  }

  /*
   * VerificaSeMultipli (public boolean verificaSeMultipliTraLoro(int[] primo,
   * int[] secondo): controlla se dato l’array primo e l’array secondo, secondo[i]
   * contiene un multiplo di primo[i]; NELLA STESSA POSIZIONE
   */
  public static boolean verificaSeSecondoArrayContieneMultiploDiPrimo(int[] primo, int[] secondo) {
    for (int p = 0; p < primo.length; p++) {
      if ((secondo[p] % primo[p]) != 0)
        return false;
    }
    return true;
  }

  /*
   * TermineCarattere: public static boolean terminanoTuttiConIlCarattere(String
   * [] elencoNomi, char carattereFinaleDiControllo)
   */
  public static boolean terminanoTuttiConIlCarattere(String[] elencoNomi, char carattereFinaleDiControllo) {
    char ultimoCarattere = elencoNomi[0].charAt(elencoNomi[0].length() - 1);
    for (int h = 0; h < elencoNomi.length; h++) {
      if (ultimoCarattere != carattereFinaleDiControllo)
        return false;
    }
    return true;
  }

  /*
   * public static int[] aggiungiInCoda(int[] input, int newElement) che
   * restituisci in uscita un nuovo array costituito dai valori di input con
   * l’aggiunta di una ulteriore casella che conterrà newElement
   */

  public static int[] aggiungiInCoda(int[] input, int newElement) {
    int[] result = new int[input.length + 1];
    for (int k = 0; k < input.length; k++) {
      result[k] = input[k];
    }
    result[result.length - 1] = newElement;
    return result;
  }

  /*
   * public static int[] rimuoviDaPosizioneX(int[] input, int indexToRemove) che
   * restituisce un nuovo array in uscita, costiuito dall’array input privato
   * della casella all’indice indexToRemove.
   */

  public static int[] rimuoviDaPosizioneX(int[] input, int indexToRemove) {
    int[] result = new int[input.length - 1];
    int indiceDiNuovoArray = 0;
    for (int i = 0; i < input.length; i++) {
      if (i != indexToRemove) {
        result[indiceDiNuovoArray] = input[i];
        indiceDiNuovoArray++;
      }
    }
    return result;
  }

  public static int[] rimuoviDaPosizioneX2(int[] input, int indexToRemove) {
    int[] result = new int[input.length - 1];
    int offset = 0;
    for (int i = 0; i < result.length; i++) {
      if (i == indexToRemove) {
        offset++;
        System.out.println("i = " + i + ", input[i] = " + input[i] + " offset = " + offset);
      }
      result[i] = input[i + offset];
    }
    return result;
  }

  /*
   * public static boolean valutaSeTantiDispariQuantiPari(int[] input) che valuta
   * se vi è la stessa quantità di numeri dispari e pari nell'array in input,
   * ignorando lo zero.
   */
  public static boolean valutaSeTantiDispariQuantiPari(int[] input) {
    int pari = 0;
    int dispari = 0;
    for (int n : input) {
      if (n != 0 && n % 2 == 0)
        pari++;
      if (n != 0 && n % 2 != 0)
        dispari++;
    }
    if (pari == dispari)
      return true;
    else
      return false;
  }

  /*
   * public static int quantiSonoDivisibiliPer(int[] valoriInInput, int divisore)
   * che calcola quanti dei numeri contenuti nell’array in input, sono divisibili
   * per il divisore dato in input.
   */

  public static int quantiSonoDivisibiliPer(int[] valoriInInput, int divisore) {
    int result = 0;
    for (int n: valoriInInput)
      if (divisore != 0 && n % divisore == 0)
        result++;
    return result;
  }

}
