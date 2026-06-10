package it.example.test;
/* Creare un nuovo progetto Java che chiameremo EserciziJava_day3.

All'interno del progetto avremo il solito package it.example.test
All'interno del package suddetto avremo la classe TestIteration.java con al suo interno un main e gli n metodi che realizzano le tracce in basso. Insomma riprendiamo il modus operandi degli esercizi per casa. I nomi dei metodi devono essere autoesplicativi.

1. dati una parola in input e un char restituire quante volte il char è contenuto nella parola
2. dato un array in input trovare il minore e restituirlo in output
3. dato un array di interi in input verificare se al suo interno esista almeno un negativo */

public class TestIteration {

  public static void main(String[] args) {
    String word = "Hello, Java";
    int[] numbers = { 1, 3, 2, 6, 6, 7, 9, 8, -7, 4, 12, -2 };;

    System.out.println(calcolaQuanteVolteCharPresenteInUnaStringa(word, 'a')); // 2
    System.out.println(trovaNumeroMinoreInArray(numbers)); // -7
    System.out.println(verificaSeEsisteUnNegativo(numbers)); // true
  }

  public static int calcolaQuanteVolteCharPresenteInUnaStringa(String str, char c) {
    int result = 0;
    char[] word = str.toCharArray();
    for (int j = 0; j < word.length; j++) {
      if (word[j] == c)
        result++;
    }
    return result;
  }

  public static int trovaNumeroMinoreInArray(int[] numbers) {
    int result = numbers[0]; // Prendo il primo numero come confronto
    for (int n = 0; n < numbers.length; n++) {
      if (numbers[n] < result) {
        result = numbers[n];
      }
    }
    return result;
  }

  public static boolean verificaSeEsisteUnNegativo(int[] numbers) {
    boolean result = false;
    int numbersOfNegatives = 0;
    for (int n : numbers) {
      if (n < 0) {
        numbersOfNegatives++;
        if (numbersOfNegatives == 2) {
          return true;
        }
      }
    }
    return result;
  }
}