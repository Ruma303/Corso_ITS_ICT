package com.its.lesson;

// INFO: Creare una classe Prodotto con nome, prezzo e categoria che contiene 3 costruttori
// Utilizzare this().

public class Prodotto {
    public String nome;
    public Double prezzo;
    public String categoria;

    public Prodotto() {
        this("Senza nome", 0.0, "Generico");
    }

    public Prodotto(String nome, Double prezzo) {
        this.nome = nome;
        this.prezzo = prezzo;
    }

    public Prodotto(String nome, Double prezzo, String categoria) {
        this(nome, prezzo);
        this.categoria = categoria;
    }

    @Override
    public String toString() {
        return "Prodotto {" +
                "nome='" + nome + '\'' +
                ", prezzo=" + prezzo +
                ", categoria='" + categoria + '\'' +
                '}';
    }
}
