package it.example.utility;

/*
Dentro la classe it.prova.utility.MyArrayUtility andare a definire i seguenti metodi e poi testarli da un'altra classe in cui sarà presente il main (una classe diversa da quella di prima così non creiamo confusione):

- Dato un array di interi in input calcola il prodotto di quelli in posizione dispari
- Dato un array di parole in input, voglio in output la parola più lunga
- Public static int quanteVolteEPresente(String[] elenco, String nome)
- Dato in input un array di interi (sia positivi che negativi) voglio sapere se la somma finale degli elementi è zero
- Dato un array di parole voglio contare quante di esse hanno lunghezza dispari
*/

public class MyArrayUtility {

  public static int[] getIntegerArray;
  public static String[] getNamesArray;

  static {
    getIntegerArray = new int[] { 1, 3, 2, 6, 6, 7, 9, 8, -7, 4, 12, -2 };
    getNamesArray = new String[] { "Alessandro", "Giovanni", "Francesco", "Luca", "Matteo", "Andrea", "Gabriele", "Luca", "Simone", "Federico",
     "Luca", "Davide", "Gianfrancandreantonio", "Ada" };
  }

  public static double ottieneProdottoDaArrayDiInteri(int[] numbers) {
    double result = 1;
    for (int k : numbers) {
      result *= k;
    }
    return result;
  }

  public static String ottieniParolaPiuLunga(String[] words) {
    String result = words[0];
    int maxWordLength = words[0].length();
    for (String word : words) {
      if (word.length() > maxWordLength) {
        result = word;
      }
    }
    return result;
  }

  public static int quanteVolteEPresente(String[] elenco, String nome) {
    int result = 0;
    for (String n : elenco) {
      if (n == nome) {
        result++;
      }
    }
    return result;
  }

  public static boolean verificaSeSommaEZero(int[] numbers) {
    int sum = 0;
    for (int d : numbers)
      sum += d;
    if (sum == 0)
        return true;
    return false;
  }

  public static int quanteParoleHannoLunghezzaDispari(String[] words) {
    int numParoleLunDispari = 0;
    for (String word : words) {
      if (word.length() % 2 != 0) {
        numParoleLunDispari++;
      }
    }
    return numParoleLunDispari;
  }
}
