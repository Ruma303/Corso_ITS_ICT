package com.its.lesson;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.List;

public class Main {
    static void main() {
        int somma1 = Matematica.somma(1, 2);
        double somma2 = Matematica.somma(30, -20D);
        long somma3 = Matematica.somma(10, 10L);
        double somma4 = Matematica.somma(5000000000D, -30);

        List<Number> listaNumero = Arrays.asList(somma1, somma2, somma3, somma4);

        for (Number numero : listaNumero) {
            String methodName = Thread.currentThread().getStackTrace()[1].getMethodName();
            System.out.println(numero.getClass().getSimpleName() + " from " + methodName + ": " + numero);
        }

        Prodotto vuoto = new Prodotto();
        Prodotto borsa = new Prodotto("Borsa", 1000000D);
        Prodotto collana = new Prodotto("Collana", 200000D, "Gioielleria");

        List<Prodotto> listaProdotto = Arrays.asList(vuoto, borsa, collana);
        for (Prodotto prodotto : listaProdotto)
            System.out.println(prodotto);

        // --- Istanziazione della superclasse ---
        ContoBancario c1 = new ContoBancario(
                1000.0, "Pierino",
                BigInteger.valueOf(4780352734956423L), "Banca"
        );
        System.out.println("\n" + c1);
        c1.deposita(20);
        // c1.deposita(-3); // ! Genererebbe un errore !
        System.out.println(c1.informazioniBanca());
        System.out.println("Nuovo saldo: " + c1.getSaldo());

        // --- Istanziazione della sottoclasse con setter esterni ---
        ContoRisparmio c2 = new ContoRisparmio("Luigi", "Banca2");
        c2.setSaldo(1500.0);
        c2.setNumOp(BigInteger.valueOf(20000));
        System.out.println("\n" + c2);
        System.out.println("Tasso d'interesse: " + c2.getTassoInteresse() + "%");
        c2.applicaInteressi();
        System.out.println("Nuovo saldo: " + c2.getSaldo());

        // --- Costruttore di conversione: ContoRisparmio a partire da c1 ---
        ContoRisparmio c3 = new ContoRisparmio(c1);
        System.out.println("\n" + c3);
        c3.applicaInteressi();
        System.out.println("Nuovo saldo dopo interessi: " + c3.getSaldo());

        // ============================================================
        // 1. UPCASTING
        // L'oggetto è un ContoRisparmio, ma il riferimento è di tipo ContoBancario.
        // Il compilatore vede solo l'interfaccia di ContoBancario.
        // ============================================================
        ContoBancario contoGenerico = new ContoRisparmio("Anna", "Banca3");
        contoGenerico.setSaldo(2500.0);
        contoGenerico.setNumOp(BigInteger.valueOf(20000));

        // contoGenerico.applicaInteressi(); // ERRORE DI COMPILAZIONE

        // ============================================================
        // 2. DOWNCASTING SICURO con instanceof (stile classico, Java 8+)
        // ============================================================
        if (contoGenerico instanceof ContoRisparmio) {
            ContoRisparmio sicuro = (ContoRisparmio) contoGenerico;
            sicuro.applicaInteressi();
            System.out.println("\nInteressi applicati. Saldo: " + sicuro.getSaldo());
        } else {
            System.out.println("Non è un ContoRisparmio.");
        }

        // ============================================================
        // 3. DOWNCASTING con Pattern Matching (Java 16+)
        // Controllo e cast in un'unica espressione.
        // ============================================================
        if (contoGenerico instanceof ContoRisparmio contoRisparmio) {
            contoRisparmio.applicaInteressi();
            System.out.println("Interessi riapplicati. Saldo: " + contoRisparmio.getSaldo());
        }

        // ============================================================
        // 4. ClassCastException: esempio di downcasting ERRATO
        // ============================================================
        ContoBancario contoBase = new ContoBancario(500.0, "Marco", BigInteger.ZERO, "BancaX");
        try {
            // contoBase è un ContoBancario puro, NON un ContoRisparmio
            ContoRisparmio errore = (ContoRisparmio) contoBase; // ClassCastException!
        } catch (ClassCastException e) {
            System.out.println("\nClassCastException catturata: " + e.getMessage());
        }
    }
}
