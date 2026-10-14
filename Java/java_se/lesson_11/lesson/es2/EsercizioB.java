package its.lesson.es2;

import java.util.Scanner;

/*
 * Date due stringhe harcodate e una presa dall'utente, stampare questi tre confronti:
 * s1 == s2
 * s1 == s3
 * s1.equals(s3)
 */

public class EsercizioB {
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = "Java";

        Scanner sc = new Scanner(System.in);
        System.out.print("Digita esattamente la parola Java: ");
        String s3 = sc.nextLine();

        String s4 = new String("Java");

        System.out.println(s1 == s2 ? "true: s1 è uguale a s2" : "false: s1 è diverso da s3");

        System.out.println(s1 == s3 ? "true: s1 è uguale a s3" : "false: s1 è diverso da s3");

        System.out.println(s1.equals(s3) ? "true: s3 è proprio Java" : "false: s3 non è la parola Java");

        System.out.println(s1 == s4.intern() ? "true: s4 è lo stesso riferimento di s1" : "false: s4 è un altro riferimento rispetto a s1");

        // BONUS 1: prendere altre due parole in input, controllare se le parole sono uguali, stampare il confronto sia di == che contenuto
        System.out.println("\n-------\n");

        System.out.println("Inserisci una parola: ");
        String s5 = sc.nextLine();

        System.out.println("Inserisci una seconda parola: ");
        String s6 = sc.nextLine();

        System.out.println(s5 == s6 ? "I riferimenti tra s5 e s6 sono uguali" : "I riferimenti tra s5 e s6 sono diversi");
        System.out.println(s5.equals(s6) ? "I contenuti di s5 e s6 sono uguali: '" + s5.toString() + "'": "I contenuti di s5 '" + s5 + "' e s6 '" + s6 + "' sono diversi");

        sc.close();

        // BONUS 2: della prima stringa del bonus 1, ignorare le maiuscole e confrontare con la prima hardcodata s1
        System.out.println("\n-------\n");

        System.out.println(
          s5.equalsIgnoreCase(s1) 
          ? "I contenuti di s1 e s5 sono gli stessi: " + s1
          : "Il contenuto di s1 '" + s1 + "' è diverso da s5 '" + s5.toLowerCase() +"'"
        );
    }
}
