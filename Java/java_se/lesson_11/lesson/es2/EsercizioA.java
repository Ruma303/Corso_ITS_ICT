package its.lesson.es2;

/*
 * ESERCIZIO A — Il report statistico
 * Un array di dieci numeri, già dato;
 * Calcola somma, media, massimo e minimo con un solo scorrimento.
 */
public class EsercizioA {
    public static void main(String[] args) {
        int[] dati = {15, 3, 42, 8, 12, 77, 6, 19, 6, 5};

        int somma = 0;
        double media = 0;
        int minimo = dati[0];
        int massimo = dati[0];

        int secondoMassimo = 0;

        if (dati.length != 0) {
            for (int i = 0; i < dati.length; i++) {
                somma += dati[i];

                if (dati[i] < minimo)
                    minimo = dati[i];
                if (dati[i] > massimo) {
                    // BONUS 2: Trovare il secondo massimo più grande senza ordinare l'array e senza che sia un doppione del primo
                    secondoMassimo = massimo;
                    massimo = dati[i];
                }
            }
        }

        media = (double) somma / dati.length;

        // BONUS 1: Calcolo numeri sopra la media
        int numeriSopraMedia = 0;
        for (int num : dati) {
            if (num > media) {
                numeriSopraMedia++;
                System.out.println("Numero sopra la media:  " + num);
            }
        }

        if (numeriSopraMedia > 0) {
            int[] arrayNumeriSopraMedia = new int[numeriSopraMedia];
            int count = 0;
            for (int i = 0; i < dati.length; i++) {
                if (dati[i] > media) {
                    arrayNumeriSopraMedia[count] = dati[i];
                    count++;
                    // System.out.println(arrayNumeriSopraMedia[count]);
                }
            }
            System.out.println("Ci sono " + arrayNumeriSopraMedia.length + " numeri sopra la media " + media);
        }

        System.out.println("Somma: " + somma);
        System.out.println("Minimo: " + minimo);
        System.out.println("Massimo: " + massimo);
        System.out.println("Secondo massimo trovato: " + secondoMassimo);
        System.out.println(
                dati.length != 0
                        ? "Media: " + media
                        : "Impossibile calcolare la media di 0 elementi"
        );
    }
}
