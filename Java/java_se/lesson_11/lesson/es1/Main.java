package its.lesson.es1;

import java.util.Arrays;

public class Main {
    static void main() {
        String nome = new String("Mario");
        String nomeAtteso = "Mario";

        int[] voti = {12, 23, 30};

        int somma = 0;
        // Qui non va il <=
        for (int i = 0; i < voti.length; i++) {
            somma = somma + voti[i];
        }

        // Preferire un casting
        double media = (double) somma / voti.length;

        System.out.println(somma);
        System.out.println(media);

        if (nome.equals(nomeAtteso)) {
            System.out.println("Studente: " + nome);
        }
        if (media >= 18 && media <= 30)
            System.out.println("Promosso: " + media);

        System.out.println(
                contiene(voti, 18)
                        ? "Nei voti compare 18"
                        : "Nei voti non compare 18"
        );
    }

    public static boolean contiene(int[] voti, int voto) {
        for (int i = 0; i < voti.length; i++) {
            if (voti[i] == voto)
                return true;
        }
        return false;
    }

    // Utilizzo di stream
    public static boolean contieneStream(int[] voti, int voto) {
        return Arrays.stream(voti).anyMatch(i -> i == voto);
    }
}