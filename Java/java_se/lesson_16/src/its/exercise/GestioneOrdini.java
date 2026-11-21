package its.exercise;

import java.util.Iterator;

/*  LABORATORIO — il programma
 *  Eseguilo cosi' com'e' PRIMA di modificare qualcosa: funziona, ma male.
 */
public class GestioneOrdini {
    public static void main(String[] args) {

        CodaLavorazione<Ordine> coda = new CodaLavorazione();
        coda.accoda(new Ordine("ORD01", 120.00));
        coda.accoda(new Ordine("ORD02", 45.50));
        coda.accoda(new Ordine("ORD03", 890.00));
        coda.anticipa(new Ordine("URG99", 15.00));

        System.out.println("=== CODA (" + coda.quanti() + " ordini) ===");
        System.out.println("Che inizia con: " + coda.sbircia() + "\n");

        // TODO 9 — scorri la coda con un for-each e stampa ogni ordine.
        //          Prima del TODO 8 non si puo' fare: serve Iterable.
        Iterator it1 = coda.iterator();

        while (it1.hasNext() && !coda.vuota()) {
            Ordine o = (Ordine) it1.next();
            System.out.println(o);
        }

        System.out.println("\n=== LAVORAZIONE ===");
        // TODO 10 — finche' la coda non e' vuota: prendi il prossimo ordine,
        //           portalo a CONFERMATO, poi SPEDITO, poi CONSEGNATO,
        //           stampalo e somma l'importo al fatturato.
        //           Senza il TODO 7 serve un cast: (Ordine) coda.prossimo()

        double fatturato = 0.0;
        while (!coda.vuota()) {
            Ordine o = coda.prossimo();
            o.cambiaStato(StatoOrdine.CONFERMATO);
            o.cambiaStato(StatoOrdine.SPEDITO);
            o.cambiaStato(StatoOrdine.CONSEGNATO);
            fatturato += o.getImporto();
            System.out.println(o);
        }
        System.out.println("Somma fatturato di tutti gli importi: " + fatturato);

        System.out.println("\n=== TRANSIZIONI NON AMMESSE ===");
        // TODO 11 — crea un ordine e prova a portarlo direttamente a CONSEGNATO.
        //            Cattura l'eccezione e stampa il messaggio.
        Ordine o5 = new Ordine("ORD05", 150.00);
        try {
            o5.cambiaStato(StatoOrdine.CONSEGNATO);
        } catch (TransizioneNonValidaException e) {
            System.err.println("[" + e.getClass().getSimpleName() + "] " + e.getMessage());
        }
        System.out.println("Stato attuale ordine 5: " + o5.getStato());

        System.out.println("Coda vuota? " + coda.vuota());
        if (coda.vuota()) {
            System.out.println("Coda vuota non esplode: " + coda.prossimo());
        }
    }
}
