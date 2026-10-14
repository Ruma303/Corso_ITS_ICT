package its.lesson.es3;

import java.util.Scanner;

/*
 * ESERCIZIO C — Il programma che usa la classe Prodotto
 * Creare un array di 3 prodotti con relativi attributi e stamparli
 */
public class GestioneProdotti {
    public static void main(String[] args) {

        Prodotto[] prodotti = new Prodotto[4];

        Prodotto p1 = new Prodotto("P01", "Laptop 14 pollici", 749.99);
        Prodotto p2 = new Prodotto("P02", "Mouse wireless", 29.50);
        Prodotto p3 = new Prodotto("P03", "Tastiera meccanica", 89.90);
        Prodotto p4 = new Prodotto();

        prodotti[0] = p1;
        prodotti[1] = p2;
        prodotti[2] = p3;
        prodotti[3] = p4;

        for (int i = 0; i < prodotti.length; i++) {
            System.out.println("Prodotto " + (i + 1) + ". Codice: " + prodotti[i].getCodice() + ", Descrizione: " + prodotti[i].getDescrizione() +
                    ", Prezzo: " + prodotti[i].getPrezzo()
            );
        }

        /*
         * BONUS:
         * 1. Totale catalogo in euro
         * 2. Prodotto più caro
         * 3. Hardcodando una stringa, cercare il prodotto tramite il codice
         * 4. Creare un prodotto chiedendolo tramite Scanner
         * 5. Aggiungere la prop quantità,
         * fare un metodo che ritorna prezzo x quantità
         * utilizzare il metodo per ogni riga e poi per il totale
         * */

        // Bonus 1
        double somma = 0;
        for (Prodotto p : prodotti) {
            somma += p.getPrezzo();
        }
        System.out.println("La somma di tutti i prodotti è: " + somma + "€");

        // Bonus 2
        double prezzoPiuAlto = 0;
        int indiceProdottoPiuAlto = 0;
        for (int i = 0; i < prodotti.length; i++) {
            if (prodotti[i].getPrezzo() > prezzoPiuAlto) {
                prezzoPiuAlto = prodotti[i].getPrezzo();
                indiceProdottoPiuAlto = i;
            }
        }
        System.out.println("Il prodotto con il prezzo più alto è : " + prodotti[indiceProdottoPiuAlto].toString());

        // Bonus 3
        String codice = "P06";
        boolean trovato = false;
        for (Prodotto p : prodotti) {
            if (codice.equals(p.getCodice())) {
                System.out.println("Prodotto trovato! " + p.toString());
                trovato = true;
                break;
            }
        }

        if (!trovato) {
            System.out.println("Nessun prodotto trovato con il codice " + codice);
        }

        // Bonus 4
        // Scanner sc = new Scanner(System.in);

        // System.out.print("Inserisci il codice del prodotto: ");
        // String c1Codice = sc.nextLine();
        // System.out.print("\nInserisci la descrizione del prodotto: ");
        // String c1Descrizione = sc.nextLine();
        // System.out.print("\nInserisci il prezzo del prodotto: ");
        // String prezzoInput = sc.nextLine();
        // double c1Prezzo = Double.parseDouble(prezzoInput);

        // Prodotto p5 = new Prodotto(c1Codice, c1Descrizione, c1Prezzo);
        Prodotto p5 = new Prodotto("P05", "Strisce led", 21.48, 4);
        System.out.println(p5.toString());

        // Bonus 5
        Prodotto p6 = new Prodotto("P06", "Monitor 4k", 2999.98, 1);
        Prodotto p7 = new Prodotto("P07", "Cuffie wireless", 59.99, 1);
        Prodotto p8 = new Prodotto("P08", "Kecaps personalizzati", 2.30, 64);

        System.out.printf("Tutti i keycaps insieme sono costati %.2f € %n", p8.getPrezzi());

        prodotti = new Prodotto[8];
        prodotti[0] = p1;
        prodotti[1] = p2;
        prodotti[2] = p3;
        prodotti[3] = p4;
        prodotti[4] = p5;
        prodotti[5] = p6;
        prodotti[6] = p7;
        prodotti[7] = p8;

        for (Prodotto prodotto : prodotti) {
          somma += prodotto.getPrezzi();
        }

        System.out.printf("Il costo complessivo di tutti i prodotti è %.2f €", somma);
        
        //sc.close();
    }
}
