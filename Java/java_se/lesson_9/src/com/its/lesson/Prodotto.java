package com.its.lesson;

public class Prodotto {
    private String nome;
    private double prezzo;
    private String descrizione;

    public Prodotto(String nome, double prezzo, String descrizione) {
        this.nome = nome;
        this.prezzo = prezzo;
        this.descrizione = descrizione;
    }

    public Prodotto() {
        this.nome = "Unknown";
        this.prezzo = 0.0D;
        this.descrizione = "Unknown";
    }

    public Prodotto(String nome, double prezzo) {
        this.nome = nome;
        this.prezzo = prezzo;
        this.descrizione = "Unknown";
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("Prodotto {");
        sb.append("nome='").append(nome).append('\'');
        sb.append(", prezzo=").append(prezzo);
        sb.append(", descrizione='").append(descrizione).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
