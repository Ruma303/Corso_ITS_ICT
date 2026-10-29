package its.example.enums;

import java.util.*;
import java.util.function.Predicate;
import java.util.function.Supplier;
import java.util.stream.Collectors;

enum Giorno {LUNEDI, MARTEDI, MERCOLEDI, GIOVEDI, VENERDI, SABATO, DOMENICA};

enum StatoOrdine {
    NUOVO("In attesa di conferma", 0),
    CONFERMATO("Ordine confermato", 1),
    SPEDITO("Ordine spedito", 2),
    CONSEGNATO("Ordine consegnato", 3),
    ANNULLATO("Ordine annullato", 4);

    private final String descrizione;
    private final int ordine;

    StatoOrdine(String descrizione, int ordine) {
        this.descrizione = descrizione;
        this.ordine = ordine;
    }

    public String getDescrizione() {
        return descrizione;
    }

    public int getOrdine() {
        return ordine;
    }

    private static final Predicate<StatoOrdine> isFinale = o -> o == CONSEGNATO
            || o == ANNULLATO;

    public boolean isFinale() {
        return isFinale.test(this);
    }

    public boolean checkFinale() {
        return this.isFinale();
    }

    public String descrizione() {
        return "ordinal = " + this.ordinal() + " valore = " + this.name() + " stato finale: " + this.checkFinale();
    }

    @Override
    public String toString() {
        return "[" + this.getClass().getSimpleName() + "] ordinal = " + this.ordinal() + " valore = " + this.name();
    }
}

class Ordine implements Comparable<Ordine>, Iterable<StatoOrdine> {
    private final Giorno giorno;
    private final StatoOrdine statoOrdine;

    Ordine(Giorno giorno, StatoOrdine statoOrdine) {
        this.giorno = giorno;
        this.statoOrdine = statoOrdine;
    }

    @Override
    public Iterator<StatoOrdine> iterator() {
        List<StatoOrdine> statiOrdine = Arrays.asList(StatoOrdine.values());
        return statiOrdine.iterator();
    }

    @Override
    public int compareTo(Ordine o) {
        return Integer.compare(this.statoOrdine.getOrdine(), o.statoOrdine.getOrdine());
    }

    public Giorno getGiorno() {
        return giorno;
    }


    public StatoOrdine getStatoOrdine() {
        return statoOrdine;
    }

    public String toString() {
        return "[" + this.getClass().getSimpleName()
                + "] giorno = " + this.giorno.name()
                + ", descrizione = " + statoOrdine.descrizione();
    }
}

public class Main {
    static void main(String[] args) {
        // Debug singolo valore Enum
        Giorno g1 = Giorno.valueOf("MERCOLEDI");
        System.out.println("[" + g1 + "] ordinal = " + g1.ordinal() + " valore = " + g1.name());

        // Test di funzioni enum
        StatoOrdine stato = StatoOrdine.CONSEGNATO;
        stato.checkFinale();

        // Debug intero set di valori enum
        System.out.println("\nTutti i valori disponibili di StatoOrdine:");
        for (StatoOrdine o : StatoOrdine.values()) {
            System.out.println("\t" + o.ordinal() + " -> " + o.name());
        }

        // Gestione eccezioni
        System.out.println("Gestione eccezioni");
        try {
            Giorno.valueOf("LUNEDì"); // Accento -> valore errato
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
        System.out.println();


        // equals e ==, preferire ==

        // Switch expression con enum

        // Iterazione
        Ordine mioOrdine = new Ordine(Giorno.LUNEDI, StatoOrdine.NUOVO);
        for (StatoOrdine s : mioOrdine) {
            System.out.println(s);
        }


        // Generazione della lista di StatoOrdine
        StatoOrdine[] statoOrdini = generateStatiOrdiniSupplier().get();

        // Generazione lista di Ordine
        Ordine[] ordini = generateOrdini();
        // Converte da Array in List, apre uno stream e ordina
        List<Ordine> sortedOrdini = Arrays.stream(ordini).sorted().toList();
        sortedOrdini.forEach(System.out::println);


        // Altri use-case

        // Controllare e contare gli ordini annullati
        System.out.println("\nNumero ordini annullati : " +
                Arrays.stream(ordini)
                        .peek(o -> System.out.println(o))
                        .filter(o -> o.getStatoOrdine() == StatoOrdine.ANNULLATO)
                        .count()
        );

        // Rimuovere gli ordini annullati
        System.out.println("\nRimozione ordini annullati : " +
                Arrays.stream(statoOrdini)
                        .filter(o -> o != StatoOrdine.ANNULLATO)
                        .toList()
        );

        // Creare una mappa di Giorno : StatoOrdine (solo per gli ordini finali)
        Map<Giorno, StatoOrdine> ordiniFiniti = sortedOrdini.stream()
                .filter(o -> o.getStatoOrdine().isFinale())
                .collect(Collectors.toMap(
                        Ordine::getGiorno,                      // Chiave: il Giorno
                        Ordine::getStatoOrdine,             // Valore: lo StatoOrdine
                        (esistente, nuovo) -> nuovo         // Merge function: se c'è un duplicato nello stesso giorno, prende il nuovo
                ));

        // 1. Iterazione classica tramite entrySet()
        System.out.println("\nOrdini finiti disponibili di StatoOrdine:");
        for (Map.Entry<Giorno, StatoOrdine> entry : ordiniFiniti.entrySet()) {
            System.out.println("\tGiorno: " + entry.getKey() + " -> Stato Ordine: " + entry.getValue());
        }

        // 2. Iterazione moderna con forEach (Java 8+)
        System.out.println();
        ordiniFiniti.forEach((giorno, statoOrdine) -> {
            System.out.println("\t" + giorno + " : " + statoOrdine);
        });
    }

    static Supplier<StatoOrdine[]> generateStatiOrdiniSupplier() {
        return () -> new StatoOrdine[]{
                StatoOrdine.NUOVO,
                StatoOrdine.CONFERMATO,
                StatoOrdine.SPEDITO,
                StatoOrdine.CONSEGNATO,
                StatoOrdine.ANNULLATO,
                StatoOrdine.ANNULLATO,
                StatoOrdine.ANNULLATO,
                StatoOrdine.ANNULLATO,
                StatoOrdine.NUOVO
        };
    }

    static Ordine[] generateOrdini() {
        return new Ordine[]{
                new Ordine(Giorno.LUNEDI, StatoOrdine.NUOVO),
                new Ordine(Giorno.MARTEDI, StatoOrdine.CONFERMATO),
                new Ordine(Giorno.MERCOLEDI, StatoOrdine.CONSEGNATO),
                new Ordine(Giorno.SABATO, StatoOrdine.ANNULLATO),
                new Ordine(Giorno.DOMENICA, StatoOrdine.NUOVO)
        };
    }
}