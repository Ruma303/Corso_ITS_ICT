package it.prova.model;

public class Iscritto {

  private String nome;
  private String cognome;
  private String codiceFiscale;
  private Abbonamento abbonamento;

  public Iscritto(String nome, String cognome, String codiceFiscale, Abbonamento abbonamento) {
    this.nome = nome;
    this.cognome = cognome;
    this.codiceFiscale = codiceFiscale;
    this.abbonamento = abbonamento;
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

  public String getCodiceFiscale() {
    return codiceFiscale;
  }

  public void setCodiceFiscale(String codiceFiscale) {
    this.codiceFiscale = codiceFiscale;
  }

  public Abbonamento getAbbonamento() {
    return abbonamento;
  }

  public void setAbbonamento(Abbonamento abbonamento) {
    this.abbonamento = abbonamento;
  }

  public String toNome() {
    return this.getCognome() + ", " + this.getNome();
  }

  // Esercizi

  /*
   * public boolean isAbbonamentiStessoTipo(Iscritto altro)
   * Restituisce true se questo iscritto e altro hanno lo stesso tipo di
   * abbonamento.
   *
   * public int contaIscrittiStessoTipo(Iscritto[] elencoIscritti)
   * Conta quanti iscritti nell'array (sé stesso incluso) hanno lo stesso tipo di
   * abbonamento.
   *
   * public static double spesaTotaleStessoGruppo(Iscritto[] elencoIscritti)
   * Calcola la somma dei prezzi mensili di tutti gli iscritti con lo stesso tipo
   * di abbonamento (sé stesso incluso).
   *
   * public boolean isIscrittoConPiuDiN(Iscritto[] elencoIscritti, int n)
   * Restituisce true se il numero di iscritti con lo stesso tipo di abbonamento
   * dell’iscritto su cui è chiamato, supera n.
   *
   * public static Iscritto trovaCompagnoDiGruppoConPiuAccessi(Iscritto[]
   * elencoIscritti)
   * Tra gli iscritti con lo stesso tipo di abbonamento restituisce quello con il
   * maggior numero di accessi. Restituisce null se non ne esistono.
   *
   * public static double mediaPrezzoDiversiTipi(Iscritto[] elencoIscritti)
   * Calcola la media dei prezzi mensili tra tutti gli iscritti dell'array,
   * indipendentemente dal tipo. Restituisce 0.0 se l'array è vuoto.
   *
   * public boolean isIlPiuCostoso(Iscritto[] elencoIscritti)
   * Restituisce true se l'abbonamento di questo iscritto ha il prezzo mensile più
   * alto tra tutti quelli presenti nell'array (sé stesso incluso).
   */

  public boolean isAbbonamentiStessoTipo(Iscritto altro) {
    if (this.getAbbonamento() == null || altro == null || altro.getAbbonamento() == null) {
      return false;
    }
    return altro.getAbbonamento().getTipoAbbonamento() == this.getAbbonamento().getTipoAbbonamento();
  }

  public int contaIscrittiStessoTipo(Iscritto[] elencoIscritti) {
    if (elencoIscritti == null || this.getAbbonamento() == null)
      return 0;

    int result = 0;
    String mioTipo = this.getAbbonamento().getNomeTipo();

    for (Iscritto is : elencoIscritti) {
      if (is == null || is.getAbbonamento() == null)
        continue;
      if (is.getAbbonamento().getNomeTipo().equalsIgnoreCase(mioTipo)) {
        result++;
      }
    }
    return result;
  }

  public static double spesaTotaleStessoGruppo(Iscritto[] elencoIscritti) {
    double somma = 0.0d;
    String tipoAbbonamento = elencoIscritti[0].getAbbonamento().getNomeTipo();

    for (Iscritto is : elencoIscritti) {
      if (is.getAbbonamento() == null)
        continue;
      if (tipoAbbonamento.equalsIgnoreCase(is.getAbbonamento().getNomeTipo()))
        somma += is.getAbbonamento().getPrezzoMensile();
    }

    return somma;
  }

  public boolean isIscrittoConPiuDiN(Iscritto[] elencoIscritti, int n) {
    int quanti = this.contaIscrittiStessoTipo(elencoIscritti);
    return quanti > n;
  }

  public static Iscritto trovaCompagnoDiGruppoConPiuAccessi(Iscritto[] elencoIscritti) {
    if (elencoIscritti == null)
      return null;
    Iscritto result = null;
    int numeroAccessi = 0;
    String tipoAbbonamento = elencoIscritti[0].getAbbonamento().getNomeTipo();

    for (Iscritto is : elencoIscritti) {
      if (is.getAbbonamento() == null) continue;
      int numAccessiCompagno = is.getAbbonamento().getNumeroDiAccessi();
      if (tipoAbbonamento.equalsIgnoreCase(is.getAbbonamento().getNomeTipo()) && numAccessiCompagno > numeroAccessi) {
        numeroAccessi = numAccessiCompagno;
        result = is;
      }
    }
    return result;
  }

  public static double mediaPrezzoDiversiTipi(Iscritto[] elencoIscritti) {
    double somma = 0.0d;
    int numeroIscrittiValidi = elencoIscritti.length;
    if (elencoIscritti == null || numeroIscrittiValidi == 0)
      return 0.0d;
    for (Iscritto is : elencoIscritti)
      if (is != null && is.getAbbonamento() != null) {
        somma += is.getAbbonamento().getPrezzoMensile();
        numeroIscrittiValidi++;
      }
    if (numeroIscrittiValidi <= 0)
      return 0.0d;
    return somma / numeroIscrittiValidi;
  }

  public boolean isIlPiuCostoso(Iscritto[] elencoIscritti) {
    if (elencoIscritti == null || this.getAbbonamento() == null)
      return false;
    double mioPrezzo = this.getAbbonamento().getPrezzoMensile();
    for (Iscritto is : elencoIscritti) {
      if (is == null || is.getAbbonamento() == null)
        continue;
      if (is.getAbbonamento().getPrezzoMensile() > mioPrezzo)
        return false;
    }
    return true;
  }
}
