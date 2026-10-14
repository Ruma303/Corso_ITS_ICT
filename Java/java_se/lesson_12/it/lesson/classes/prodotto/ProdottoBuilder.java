package it.lesson.classes.prodotto;

public class ProdottoBuilder {
    private static int counter = 0;

    private String codice;
    private double prezzo;
    private int quantita;

    ProdottoBuilder(String codice, double prezzo, int quantita) {
        this.codice = codice;
        this.prezzo = prezzo;
        this.quantita = quantita;
        counter++;
    }

    public static int getCounter() {
        return counter;
    }

    public String getCodice() {
        return codice;
    }

    public static class builder {
        private String codice;
        private double prezzo;
        private int quantita;

        // Metodo di costruzione
        public ProdottoBuilder build() {
            return new ProdottoBuilder(codice, prezzo, quantita);
        }

        // Setters con parametri opzionali
        public builder codice(String codice) {
            if (codice.equals("") || codice.length() < 3) {
                throw new IllegalArgumentException("Codice non valido");
            }
            this.codice = codice;
            return this;
        }

        public builder quantita(int quantita) {
            if (quantita < 0) {
                System.err.println("Quantità non valida. Inserire un numero maggiore o uguale a 0");
            }
            this.quantita = quantita;
            return this;
        }

        public builder prezzo(double prezzo) {
            if (prezzo < 0) {
                System.err.println("Prezzo non valido. Inserire un prezzo maggiore o uguale a 0");
            }
            this.prezzo = prezzo;
            return this;
        }
    }

    public double getPrezzo() {
        return prezzo;
    }

    public int getQuantita() {
        return quantita;
    }

    @Override
    public String toString() {
        return "Prodotto: [ codice: " + codice + ", prezzo: " + prezzo + "€, quantità: " + quantita + " ]";
    }
}

class Test {
    static void main(String[] args) {
        // Uso del builder pattern
        ProdottoBuilder p1 = new ProdottoBuilder.builder()
                .codice("P02")
                .prezzo(29.30)
                .quantita(2)
                .build();

        System.out.println(p1.toString());
    }
}
