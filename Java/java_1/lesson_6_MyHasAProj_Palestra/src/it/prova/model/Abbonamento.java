package it.prova.model;

enum TipoAbbonamento {
  MENSILE,
  TRIMESTRALE,
  ANNUALE
}

public class Abbonamento {

  private TipoAbbonamento tipoAbbonamento;
  private Integer numeroDiAccessi;
  private Integer prezzoMensile;
  private Integer minutiAllenamentoSettimanale;

  /*
   * private Abbonamento(TipoAbbonamento tipoAbbonamento, Integer numeroDiAccessi,
   * Integer prezzoMensile,
   * Integer minutiAllenamentoSettimanale) {
   * this.tipoAbbonamento = tipoAbbonamento;
   * this.numeroDiAccessi = numeroDiAccessi;
   * this.prezzoMensile = prezzoMensile;
   * this.minutiAllenamentoSettimanale = minutiAllenamentoSettimanale;
   * }
   */

  public Abbonamento(String tipoAbbonamento, Integer numeroDiAccessi, Integer prezzoMensile,
      Integer minutiAllenamentoSettimanale) {
    this.tipoAbbonamento = TipoAbbonamento.valueOf(tipoAbbonamento);
    this.numeroDiAccessi = numeroDiAccessi;
    this.prezzoMensile = prezzoMensile;
    this.minutiAllenamentoSettimanale = minutiAllenamentoSettimanale;
  }

  public TipoAbbonamento getTipoAbbonamento() {
    return tipoAbbonamento;
  }

  // Converte i valori di TipoAbbonamento in String
  public String getNomeTipo() {
    return this.tipoAbbonamento.name();
  }

  public void setTipoAbbonamento(TipoAbbonamento tipoAbbonamento) {
    this.tipoAbbonamento = tipoAbbonamento;
  }

  public void setTipoAbbonamento(String tipoAbbonamento) {
    this.tipoAbbonamento = TipoAbbonamento.valueOf(tipoAbbonamento);
  }

  public Integer getNumeroDiAccessi() {
    return numeroDiAccessi;
  }

  public void setNumeroDiAccessi(Integer numeroDiAccessi) {
    this.numeroDiAccessi = numeroDiAccessi;
  }

  public Integer getPrezzoMensile() {
    return prezzoMensile;
  }

  public void setPrezzoMensile(Integer prezzoMensile) {
    this.prezzoMensile = prezzoMensile;
  }

  public Integer getMinutiAllenamentoSettimanale() {
    return minutiAllenamentoSettimanale;
  }

  public void setMinutiAllenamentoSettimanale(Integer minutiAllenamentoSettimanale) {
    this.minutiAllenamentoSettimanale = minutiAllenamentoSettimanale;
  }

  @Override
  public String toString() {
    return "Abbonamento [tipoAbbonamento=" + tipoAbbonamento + ", numeroDiAccessi=" + numeroDiAccessi
        + ", prezzoMensile=" + prezzoMensile + ", minutiAllenamentoSettimanale=" + minutiAllenamentoSettimanale + "]";
  }

  // Esercizi
  /*
   * public static Abbonamento trovaPiuEconomico(Abbonamento[] elencoAbbonamenti)
   * Restituisce l'abbonamento con il prezzo mensile più basso. Se ce ne sono più
   * di uno con lo stesso prezzo minimo, restituisce il primo trovato. Restituisce
   * null se l'array è vuoto.
   *
   * public static double prezzoMedioPerTipo(Abbonamento[] elencoAbbonamenti,
   * String tipo)
   * Calcola la media del prezzo mensile solo per gli abbonamenti del tipo
   * indicato. Restituisce 0.0 se non ne esistono.
   *
   * public boolean isSottoUtilizzato(int sogliaMinima)
   * Restituisce true se il numeroDiAccessi dell'abbonamento su cui è chiamato è
   * inferiore a sogliaMinima. Utile per identificare iscritti che frequentano
   * poco.
   *
   * public static int contaSottoUtilizzati(Abbonamento[] elencoAbbonamenti, int
   * sogliaMinima)
   * Conta quanti abbonamenti nell'array risultano sotto-utilizzati rispetto alla
   * soglia. Internamente usa isSottoUtilizzato.
   *
   * public static Abbonamento[] filtraPerTipo(Abbonamento[] elencoAbbonamenti,
   * String tipo)
   * Restituisce un nuovo array contenente solo gli abbonamenti del tipo indicato.
   * Restituisce un array vuoto se non ce ne sono.
   *
   */

  public static Abbonamento trovaPiuEconomico(Abbonamento[] elencoAbbonamenti) {
    Abbonamento abbonamento = elencoAbbonamenti[0];
    for (Abbonamento ab : elencoAbbonamenti)
      if (ab.getPrezzoMensile() < abbonamento.getPrezzoMensile())
        abbonamento = ab;
    return abbonamento;
  }

  public static double prezzoMedioPerTipo(Abbonamento[] elencoAbbonamenti, String tipo) {
    if (elencoAbbonamenti == null || elencoAbbonamenti.length == 0)
      return 0.0;

    // Convertiamo la stringa nell'Enum usando la classe TipoAbbonamento
    TipoAbbonamento tipoCercato = TipoAbbonamento.valueOf(tipo.toUpperCase());

    double somma = 0;
    int contatore = 0;

    for (Abbonamento ab : elencoAbbonamenti) {
      if (ab != null && ab.getTipoAbbonamento() == tipoCercato) {
        somma += ab.getPrezzoMensile();
        contatore++;
      }
    }

    // Se non ci sono abbonamenti di quel tipo, evitiamo la divisione per zero
    if (contatore == 0)
      return 0.0;

    return somma / contatore;
  }

  public boolean isSottoUtilizzato(int sogliaMinima) {
    if (this.getNumeroDiAccessi() < sogliaMinima)
      return true;
    return false;
  }

  public static int contaSottoUtilizzati(Abbonamento[] elencoAbbonamenti, int sogliaMinima) {
    int result = 0;
    for (Abbonamento ab : elencoAbbonamenti) {
      if (ab.isSottoUtilizzato(sogliaMinima)) {
        result++;
      }
    }
    return result;
  }

  public static Abbonamento[] filtraPerTipo(Abbonamento[] elencoAbbonamenti, String tipo) {
    if (elencoAbbonamenti == null || elencoAbbonamenti.length == 0 || tipo == null) {
      return new Abbonamento[0];
    }

    int contatore = 0;
    for (Abbonamento ab : elencoAbbonamenti) {
      if (ab != null && ab.getNomeTipo().equalsIgnoreCase(tipo)) {
        contatore++;
      }
    }

    // Se non abbiamo trovato nulla, restituiamo subito un array vuoto
    if (contatore == 0) {
      return new Abbonamento[0];
    }

    // Altrimenti, creiamo l'array della dimensione esatta e lo popoliamo
    Abbonamento[] result = new Abbonamento[contatore];
    int indiceResult = 0;

    for (Abbonamento ab : elencoAbbonamenti) {
      if (ab != null && ab.getNomeTipo().equalsIgnoreCase(tipo)) {
        result[indiceResult] = ab;
        indiceResult++;
      }
    }
    return result;
  }

}
