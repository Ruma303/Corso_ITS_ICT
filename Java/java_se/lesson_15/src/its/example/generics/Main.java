package its.example.generics;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.function.Supplier;

@FunctionalInterface
interface MySupplier<T> extends Supplier<T> {

    T get();

    default Long conta() {
        return get() instanceof List<?> lista
                ? lista.stream().count()
                : 0L;
    }
}

public class Main {
    static void main(String[] args) {
        Box<String> stringhe = new Box<>();
        stringhe.metti("Ciao");
        System.out.println(stringhe.prendi("Ciao"));

        Coppia<String, Integer> coppia = new Coppia<>("Ada", 18);
        System.out.println(coppia.debug());

        MySupplier<List<String>> nomi = new MySupplier<>() {
            List<String> list = new ArrayList<>(
                    List.of("Piero", "Ada", "Ada", "Sandro")
            );

            @Override
            public List<String> get() {
                return list.stream().distinct().toList();
            }
        };
        System.out.println(nomi.conta() + " elementi: " + nomi.get());
    }
}

class Coppia<K, V> {
    K k;
    V v;

    Coppia(K k, V v) {
        this.k = k;
        this.v = v;
    }

    String debug() {
        return "K: " + getK() + ", V: " + getV();
    }

    K getK() {
        return k;
    }

    V getV() {
        return v;
    }
}

class Box<T> {
    private T contenuto;

    public Box() {
        contenuto = null;
    }

    public void metti(T contenuto) {
        this.contenuto = contenuto;
    }

    public T prendi(T contenuto) {
        return contenuto;
    }
}

class G {
    static <T> void stampaTutti(List<T> lista) {
        for (T item : lista) {
            System.out.println(item + "\n");
        }
    }

    static <T extends Comparable<T>> T massimo(List<T> lista) {
        Collections.sort(lista);
        T max = lista.get(0);
        for (T item : lista) {
            if (item.compareTo(max) > 0) {
                max = item;
            }
        }
        return max;
    }

    // Wildcard lettura
    static double somma(List<? extends Number> numeri) {
        double somma = 0;
        for (Number item : numeri) {
            somma = somma + item.doubleValue();
        }
        return somma;
    }
}