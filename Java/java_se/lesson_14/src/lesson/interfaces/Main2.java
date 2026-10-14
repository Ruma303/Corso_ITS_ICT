package lesson.interfaces;

import java.util.ArrayList;
import java.util.List;

interface Scontabile {
    double MAX = 100d;                                      // public static final

    double applicaSconto(double percentuale); // public abstract

    default String etichetta(String etichetta) {    // ha un corpo
        return etichetta;
    }

    static boolean scontoValido(double p) {
        return p >= 0 && p <= MAX;
    }
}

interface Spedibile {
    double costoSpedizione();
}

class Prodotto implements Scontabile, Spedibile {
    private String codice;
    private double prezzo;

    Prodotto(String codice, double prezzo) {
        this.codice = codice;
        this.prezzo = prezzo;
    }

    @Override
    public double applicaSconto(double percentuale) {
        prezzo =  prezzo * (1 - percentuale);
        return prezzo;
    }

    @Override
    public double costoSpedizione() {
        return prezzo > 100 ? 0 : 4.90;
    }

    public String getCodice() {
        return codice;
    }

    public double getPrezzo() {
        return prezzo ;
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("Prodotto {");
        sb.append("codice='").append(codice).append('\'');
        sb.append(", prezzo=").append(prezzo);
        sb.append(", scontabile = ").append(Scontabile.scontoValido(prezzo));
        sb.append('}');
        return sb.toString();
    }
}


public class Main2 {
    static void main(String[] args) {
        Prodotto p1 = new Prodotto("123", 89.0);
        Prodotto p2 = new Prodotto("456", 120.0);
        Prodotto p3 = new Prodotto("789", 100.0);

        // Programmazione a interfacce
        Scontabile p4 = new Prodotto("2958", 15.0);

        List<Prodotto> prodotti = new ArrayList<Prodotto>();
        prodotti.add(p1);
        prodotti.add(p2);
        p2.applicaSconto(0.3);
        prodotti.add(p3);
        prodotti.add( (Prodotto) p4);

        for (Prodotto p : prodotti) {
            System.out.println(p);
        }
    }
}