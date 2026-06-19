package it.progetto.model;

public class Spettatore {

  private String nome;
  private String cognome;
  private Integer numeroCartaDiCredito;
  private Biglietto biglietto;

  public Spettatore() {
  }

  public Spettatore(
      String nome,
      String cognome,
      Integer numeroCartaDiCredito,
      Biglietto biglietto) {
    this.nome = nome;
    this.cognome = cognome;
    this.numeroCartaDiCredito = numeroCartaDiCredito;
    this.biglietto = biglietto;
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

  public Integer getNumeroCartaDiCredito() {
    return numeroCartaDiCredito;
  }

  public void setNumeroCartaDiCredito(Integer numeroCartaDiCredito) {
    this.numeroCartaDiCredito = numeroCartaDiCredito;
  }

  public Biglietto getBiglietto() {
    return biglietto;
  }

  public void setBiglietto(Biglietto biglietto) {
    this.biglietto = biglietto;
  }

  public String toNome() {
    return this.getCognome() + ", " + this.getNome();
  }

  @Override
  public String toString() {
    return "Spettatore [nome=" + nome + ", cognome=" + cognome + ", numeroCartaDiCredito=" + numeroCartaDiCredito
        + ", biglietto=" + biglietto + "]";
  }

  // Esercizi

  public int incassoDeiPagantiNellaMiaFila(Spettatore[] elencoPagantiTotali) {
    char fila = this.getBiglietto().getLetteraFila();
    int incasso = 1; // Compreso io
    for (Spettatore pagante : elencoPagantiTotali) {
      if (pagante.getBiglietto().getLetteraFila() == fila)
        incasso += pagante.getBiglietto().getPrezzo();
    }
    return incasso;
  }

  public int numeroSpettatoriDelMioStessoSpettacolo(Spettatore[] elencoPagantiTotali) {
    String spettacolo = this.getBiglietto().getNomeSpettacolo();
    int numeroSpettatori = 1; // Compreso io
    for (Spettatore spettatore : elencoPagantiTotali)
      if (spettatore.getBiglietto().getNomeSpettacolo().equalsIgnoreCase(spettacolo))
        numeroSpettatori++;
    return numeroSpettatori;
  }

  public boolean numeroSpettatoriMioSpettacoloSuperaAspettativa(Spettatore[] paganti, int aspettativa) {
    int numeroSpettatori = paganti.length;
    if (aspettativa > numeroSpettatori)
      return true;
    return false;
  }
}
