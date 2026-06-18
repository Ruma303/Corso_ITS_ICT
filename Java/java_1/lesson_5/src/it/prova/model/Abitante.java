package it.prova.model;

import it.prova.model.Indirizzo;

public class Abitante {
  private String nome;
  private String cognome;
  private Integer eta;
  private Indirizzo indirizzo;

  public Abitante() {
  }

  public Abitante(String nome, String cognome, Integer eta) {
    this.nome = nome;
    this.cognome = cognome;
    this.eta = eta;
  }

  public Abitante(String nome, String cognome, Integer eta, Indirizzo indirizzo) {
    this(nome, cognome, eta);
    this.indirizzo = indirizzo;
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public String getCognome() {
    return cognome;
  }

  public void setCognome(String cognome) {
    this.cognome = cognome;
  }

  public Integer getEta() {
    return eta;
  }

  public void setEta(Integer eta) {
    this.eta = eta;
  }

  public Indirizzo getIndirizzo() {
    return this.indirizzo;
  }

  public void setIndirizzo(Indirizzo indirizzo) {
    this.indirizzo = indirizzo;
  }

  @Override
  public String toString() {
    return "Abitante [nome=" + nome + ", cognome=" + cognome + ", eta=" + eta + "]";
  }

  public String toNome() {
    return this.getCognome() + ", " + this.getNome();
  }

  // Esercizi

  public boolean abitaA(String cittaInput) {
    return this.getIndirizzo().getCitta().equalsIgnoreCase(cittaInput);
  }

  public boolean haAlmenoUnConcittadino(Abitante[] elenco) {
    for (Abitante tizio : elenco)
      if (this.getIndirizzo().getCitta().equalsIgnoreCase(tizio.getIndirizzo().getCitta()))
        return true;
    return false;
  }

  public boolean sonoTuttiPiuAnziani(Abitante[] elenco) {
    for (Abitante tizio : elenco)
      if (this.getEta() > tizio.getEta())
        return false;
    return true;
  }

  public int quantiCoabitanoNelMioStessoPalazzo(Abitante[] elencoInput) {
    int coabitano = 0;
    for (Abitante tizio : elencoInput) {

      boolean stessaCitta = this.getIndirizzo().getCitta().equalsIgnoreCase(tizio.getIndirizzo().getCitta());
      boolean stessaVia = this.getIndirizzo().getVia().equalsIgnoreCase(tizio.getIndirizzo().getVia());
      boolean stessoCivico = this.getIndirizzo().getCivico().equalsIgnoreCase(tizio.getIndirizzo().getCivico());

      if (stessaCitta && stessaVia && stessoCivico)
        coabitano++;
    }
    return coabitano;
  }

  public int quantiMieiOmonimiNellaMiaStessaCitta(Abitante[] elencoInput) {
    int omonimi = 0;
    for (Abitante tizio : elencoInput) {
      if (this.getNome().equalsIgnoreCase(tizio.getNome()) &&
          this.getCognome().equalsIgnoreCase(tizio.getCognome())) {
        omonimi++;
      }
    }
    return omonimi;
  }

  public boolean almenoLaMetaAbitanoNellaMiaStessaVia(Abitante[] elencoInput) {
    int meta =  elencoInput.length / 2;
    int tizi = 0;
    for (Abitante tizio : elencoInput) {
      if (this.getIndirizzo().getCitta().equalsIgnoreCase(tizio.getIndirizzo().getCitta()) &&
          this.getIndirizzo().getVia().equalsIgnoreCase(tizio.getIndirizzo().getVia())) {
            tizi++;
            if (tizi > meta)
              return true;
      }
    }
    return false;
  }
}
