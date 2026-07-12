package com.composition.es2.model;

public class Allenatore {
    private String nome;
    private int eta;

    @Override
    public String toString() {
        return "Allenatore{" +
                "nome='" + nome + '\'' +
                ", eta=" + eta +
                '}';
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getEta() {
        return eta;
    }

    public void setEta(int eta) {
        this.eta = eta;
    }

    public Allenatore(String nome, int eta) {
        this.nome = nome;
        this.eta = eta;
    }
}
