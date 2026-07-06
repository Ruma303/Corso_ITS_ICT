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
    // Null Guard
    if (this.getBiglietto() == null)
      return 0;

    char fila = this.getBiglietto().getLetteraFila();
    float incasso = 0.0f;

    for (Spettatore pagante : elencoPagantiTotali) {
      // Se non ha un biglietto (Evita il NullPointerException)
      if (pagante.getBiglietto() == null)
        continue;

      if (pagante.getBiglietto().getLetteraFila() == fila) {
        incasso += pagante.getBiglietto().getPrezzo();
      }
    }
    return (int) incasso;
  }

  public int numeroSpettatoriDelMioStessoSpettacolo(Spettatore[] elencoPagantiTotali) {
    // Null Guard
    if (this.getBiglietto() == null)
      return 0;

    String spettacolo = this.getBiglietto().getNomeSpettacolo();
    int numeroSpettatori = 0;

    for (Spettatore spettatore : elencoPagantiTotali) {
      // SALTA lo spettatore se non ha un biglietto
      if (spettatore.getBiglietto() == null)
        continue;

      if (spettatore.getBiglietto().getNomeSpettacolo().equalsIgnoreCase(spettacolo)) {
        numeroSpettatori++;
      }
    }
    return numeroSpettatori;
  }

  public boolean numeroSpettatoriMioSpettacoloSuperaAspettativa(Spettatore[] paganti, int aspettativa) {
    // Prima dobbiamo calcolare quanti partecipano al MIO spettacolo
    int spettatoriMioSpettacolo = numeroSpettatoriDelMioStessoSpettacolo(paganti);
    return spettatoriMioSpettacolo > aspettativa;
  }

  public static int contaQuantiSenzaBiglietto(Spettatore[] elencoSpettatori) {
    int spettatoriSenzaBiglietto = 0;
    for (Spettatore sp : elencoSpettatori)
      if (sp.getBiglietto() == null)
        spettatoriSenzaBiglietto++;
    return spettatoriSenzaBiglietto;
  }

  public int contaQuantiNellaMiaStessaFila(Spettatore[] elencoSpettatori) {
    // Null Guard
    if (this.getBiglietto() == null)
      return 0;

    int tizi = 0;
    char miaFila = this.getBiglietto().getLetteraFila();

    for (Spettatore sp : elencoSpettatori)
      if (sp.getBiglietto() == null)
        continue;
      else if (sp.getBiglietto().getLetteraFila() == miaFila)
        tizi++;
    return tizi;
  }
}
