package its.example.ex1;

import java.util.*;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {

        List<Articolo> articoli = new ArrayList<>(
                List.of(
                        new Libro("ABC123", 20.20, "Il Signore degli Anelli"),
                        new Libro("DEF456", 16.90, "1984"),

                        // Articoli con lo stesso codice
                        new Libro("GHI678", 13.20, "Dune"),
                        new Libro("GHI678", 13.20, "Dune"),
                        new Libro("GHI678", 13.20, "Dune"),

                        // Corsi con durata espressa in ore
                        new Corso("123ABC", 49.99, 20),
                        new Corso("456DEF", 69.99, 40),
                        new Corso("678GHI", 45.20, 100)
                )
        );

        for (Articolo a : articoli) {
            // Downcasting
            if (a instanceof Libro l) {
                System.out.println(l.getTitolo());
            }
            if (a instanceof Corso c) {
                System.out.println(c.getOre());
            }
        }

        //* Confronto Articoli usando Comparable
        if (articoli.get(2).equals(articoli.get(3)) && articoli.get(3).equals(articoli.get(4))) {
            System.out.println("Gli articoli in posizione 3, 4 e 5 SONO UGUALI");
        } else {
            System.out.println("Gli articoli in posizione 3, 4 e 5 NON SONO UGUALI");
        }


        //* Uso di stream e lambda

        // Comparazione (sorting) tramite Comparable
        // Usando Collections
        Collections.sort(articoli);

        // Usando gli stream - creazione di una lista mutabile per riordinarla in seguito
        List<Articolo> articoliSorted = new ArrayList<>(
                articoli.stream()
                        .sorted()
                        .toList()
        );

        // Formattazione per singolo elemento
        List<String> printFormattedArticoli = articoliSorted.stream()
                .sorted()
                .map(articolo -> articolo.toString() + "\n")
                .toList();
        System.out.println("\nLista ordinata per codice:\n" + printFormattedArticoli);

        // Somma di tutti i prezzi non ivati
        Double somma = articoli.stream().mapToDouble(Articolo::getPrezzo).sum();
        System.out.println("\nSomma articoli non ivati: " + somma + "€");


        // Comparazione (sorting) tramite Comparator
        // Ordinare per prezzo decrescendente
        articoliSorted.sort(Comparator.comparingDouble(Articolo::getPrezzo).reversed());
        System.out.println("\nLista ordinata per prezzo decrescente:");
        articoliSorted.forEach(System.out::println);


        //* ESERCIZI:  use-case

        // Solo corsi con almeno 40 ore
        List<Corso> corsiDaAlmeno40Ore = articoliSorted.stream()
                .filter(a -> a instanceof Corso)
                .map(a -> (Corso) a)
                .filter(c -> c.getOre() >= 40)
                .toList();

        // Stampa ogni corso, uno per riga
        System.out.println("\nTutti i corsi da almeno 40 ore: ");

        // Mostriamo anche un numero. Gli stream da soli non li espongono
        IntStream.range(1, corsiDaAlmeno40Ore.size())
                .forEach(i -> System.out.println(
                        "\t" + i + ". " + corsiDaAlmeno40Ore.get(i).descrizione()
                ));

        // Per ogni codice indicare la sua iva
        Map<String, Double> mappaCodiceIva = new HashMap<>();
        for (Articolo a : articoli) {
            if (a instanceof Corso c) {
                mappaCodiceIva.put(c.getCodice(), c.getIva());
            }
            if (a instanceof Libro l) {
                mappaCodiceIva.put(l.getCodice(), l.getIva());
            }
        }
        System.out.println("\nMappa articoli: Codice - Iva:\n" + mappaCodiceIva);

        // Per ogni Articolo (codice) salvare il suo prezzo
        Map<String, Double> articoliCodicePrezzo = new HashMap<>();
        for (Articolo a : articoli) {
            if (a instanceof Vendibile v) {
                // getCodice deriva da Articolo, prezzoFinale deriva dall'interfaccia Vendibile
                articoliCodicePrezzo.put(a.getCodice(), v.prezzoFinale());
            }
        }
        System.out.println("\nMappa articoli: Codice - Prezzo:\n" + articoliCodicePrezzo);


        // Indicare quante volte compare l'iva
        Map<Double, Integer> mappaQuanteVolteIva = new HashMap<>();
        for (Double iva : mappaCodiceIva.values()) {
            // Creare chiave (Iva) : valore (somma di quante volte compare)
            mappaQuanteVolteIva.put(
                    iva,
                    mappaQuanteVolteIva.getOrDefault(iva, 0) + 1
            );
        }
        System.out.println("\nNumero di occorrenze per IVA:" + mappaQuanteVolteIva);

        // Trovare il corso con il prezzo finale più basso


        // Somma di tutti i prezzi con iva più alta
        // Individuare l'aliquota IVA più alta
        Double ivaPiuAlta = mappaQuanteVolteIva.keySet().stream()
                .max(Double::compareTo)
                .orElseThrow(() -> new IllegalStateException("Nessuna IVA presente"));

        // Sommare i prezzi finali degli articoli con l'IVA più alta
        double sommaPrezziConIvaPiuAlta = articoli.stream()
                .filter(a -> a instanceof Vendibile)
                .filter(a -> {
                    if (a instanceof Libro l) {
                        return Double.compare(l.getIva(), ivaPiuAlta) == 0;
                    }
                    if (a instanceof Corso c) {
                        return Double.compare(c.getIva(), ivaPiuAlta) == 0;
                    }
                    return false;
                })
                .mapToDouble(a -> ((Vendibile) a).prezzoFinale())
                .sum();

        System.out.printf(
                "%nSomma dei prezzi con IVA %.0f%%: %.2f€%n",
                ivaPiuAlta,
                sommaPrezziConIvaPiuAlta
        );

        // Trovare il prezzo finale medio dei libri
        double sommaPrezziFinali = articoliSorted.stream()
                .filter(a -> a instanceof Vendibile)
                .map(a -> (Vendibile) a)
                .mapToDouble(Vendibile::prezzoFinale)
                .sum();

        System.out.printf("Somma di tutti i prezzi finali: %.2f€%n", sommaPrezziFinali);

        // Creare lista di articoli duplicati (usa Comparable)


    }
}
