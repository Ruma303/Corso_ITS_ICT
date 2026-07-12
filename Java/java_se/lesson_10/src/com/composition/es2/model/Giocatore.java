package com.composition.es2.model;

public class Giocatore {
    private String nome;
    private int eta;
    private String ruolo;
    private int goal;

    public Giocatore(String nome, int eta, String ruolo, int goal) {
        this.nome = nome;
        this.eta = eta;
        this.ruolo = ruolo;
        this.goal = goal;
    }

    @Override
    public String toString() {
        return "Giocatore{" +
                "nome='" + nome + '\'' +
                ", eta=" + eta +
                ", ruolo='" + ruolo + '\'' +
                ", goal=" + goal +
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

    public String getRuolo() {
        return ruolo;
    }

    public void setRuolo(String ruolo) {
        this.ruolo = ruolo;
    }

    public int getGoal() {
        return goal;
    }

    public void setGoal(int goal) {
        this.goal = goal;
    }
}
