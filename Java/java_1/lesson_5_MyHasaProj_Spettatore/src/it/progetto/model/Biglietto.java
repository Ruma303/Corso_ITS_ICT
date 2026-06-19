package it.progetto.model;

public class Biglietto {

  private String nomeSpettacolo;
  private char letteraFila;
  private int numeroPosto;
  private float prezzo;

  public Biglietto(
      String nomeSpettacolo,
      char letteraFila,
      int numeroPosto,
      float prezzo) {
    this.nomeSpettacolo = nomeSpettacolo;
    this.letteraFila = letteraFila;
    this.numeroPosto = numeroPosto;
    this.prezzo = prezzo;
  }

  public String getNomeSpettacolo() {
    return nomeSpettacolo;
  }

  public char getLetteraFila() {
    return letteraFila;
  }

  public int getNumeroPosto() {
    return numeroPosto;
  }

  public float getPrezzo() {
    return prezzo;
  }

  @Override
  public String toString() {
    return "Biglietto [nomeSpettacolo=" + nomeSpettacolo + ", letteraFila=" + letteraFila + ", numeroPosto="
        + numeroPosto + ", prezzo=" + prezzo + "]";
  }

  // Esercizi
  public static Biglietto trovaIlPiuEconomico(Biglietto[] elencoBiglietti) {
    Biglietto biglietto = elencoBiglietti[0];
    for (Biglietto b : elencoBiglietti)
      if (b.getPrezzo() < biglietto.getPrezzo())
        biglietto = b;
    return biglietto;
  }

  public boolean bigliettoAncoraInvenduto(Biglietto[] elencoBigliettiInvenduti) {
    for (Biglietto b : elencoBigliettiInvenduti)
      if (b == this) // oppure confronto per valore, dipende dal contesto
        return true;
    return false;
  }
}
