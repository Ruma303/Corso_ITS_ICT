package com.composition.es2.model;

import java.util.ArrayList;
import java.util.List;

public class Squadra {

    private String nome;
    private Allenatore allenatore;
    private List<Giocatore> giocatori;

    public Squadra(String nome, Allenatore allenatore) {
        this.nome = nome;

        // Aggiunto per aggregazione
        this.allenatore = allenatore;

        // Aggiunti per composizione
        this.giocatori = creaGiocatori();
    }

    public void aggiungiGiocatore(String nome, int eta, String ruolo, int goal) {
        Giocatore g = new Giocatore(nome, eta, ruolo, goal);
        giocatori.add(g);
    }

    public List<Giocatore> creaGiocatori() {

        List<Giocatore> giocatori = new ArrayList<>();

        Giocatore g1 = new Giocatore("Cannavaro", 30, "capocannoniere", 4000);
        Giocatore g2 = new Giocatore("Minuzzo", 300000, "Centro destra", 0);

        giocatori.add(g1);
        giocatori.add(g2);

        return giocatori;
    }

    public boolean rimuoviGiocatore(String nome) {
        for (Giocatore g : giocatori) {
            if (g.getNome().equalsIgnoreCase(nome)) {
                giocatori.remove(g);
                return true;
            }
        }
        return false;
    }

    public void descriviSquara() {
        System.out.println("\n" + this.toString());
    }

    public float etaMedia() {
        int result = 0;
        if (giocatori.isEmpty()) {
            return 0.0f;
        }
        for (Giocatore g : giocatori) {
            result += g.getEta();
        }

        return result /  giocatori.size();
    }

    public Giocatore capocannoniere() {
        for  (Giocatore g : giocatori) {
            if (g.getRuolo().equalsIgnoreCase("capocannoniere")) {
                return g;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "{" +
                "nome='" + nome + '\'' +
                ", allenatore=" + allenatore +
                ", giocatori=" + giocatori +
                '}';
    }
}
