package its.example.interfaces;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class Main {

    public static void main(String[] args) {

        // Interfacce di default
        Predicate<String> lunga = s -> s.length() > 5;
        Function<String, Integer> lunghezza = s -> s.length();
        Consumer<String> stampa = System.out::println;

        // Il Supplier fornisce il generatore della lista
        Supplier<List<String>> listaSupplier = ArrayList::new;

        // Implementazioni
        String stringa = "Hello World";
        System.out.println("Stringa lunga? " + lunga.test(stringa));
        System.out.println("Stringa lunghezza? " + lunghezza.apply(stringa));
        stampa.accept(stringa);

        // 1. Otteniamo l'istanza della lista dal Supplier
        List<String> miaLista = listaSupplier.get();
        // System.out.println("Lista vuota: " +  listaSupplier.orElseGet(ArrayList::new));

        // 2. Ora possiamo aggiungere gli elementi normalmente
        miaLista.add("Hello");
        miaLista.add("World from Supplier");

        // 3. Stampiamo gli elementi della lista
        miaLista.forEach(System.out::println);

        Function<String, String> uppercase = s -> s.toUpperCase();
    }
}