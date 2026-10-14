package it.lesson.classes.prodotto;

public class Prodotto {
    private static int counter = 0;

    private String codice;
    private double prezzo;
    private int quantita;

    Prodotto(String codice, double prezzo, int quantita) {
        setCodice(codice);
        setPrezzo(prezzo);
        setQuantita(quantita);
        counter++;
    }

    public static int getCounter() {
        return counter;
    }

    public String getCodice() {
        return codice;
    }

    public void setCodice(String codice) {
        if (codice.equals("") || codice.length() < 3) {
            throw new IllegalArgumentException("Codice non valido");
        }
        this.codice = codice;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        if (prezzo < 0) {
            System.err.println("Prezzo non valido. Inserire un prezzo maggiore o uguale a 0");
        }
        this.prezzo = prezzo;
    }

    public int getQuantita() {
        return quantita;
    }

    public void setQuantita(int quantita) {
        if (quantita < 0) {
            System.err.println("Quantità non valida. Inserire un numero maggiore o uguale a 0");
        }
        this.quantita = quantita;
    }
}
