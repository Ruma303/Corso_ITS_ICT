package it.prova.model;

public class Televisore {
  private String marca;
  private String modello;
  private int pollici;
  private int prezzo;

  public Televisore() {
    this("_", "_", 0, 0);
  }

  public Televisore(
      String marca,
      String modello,
      int prezzo,
      int pollici
    ) {
    this.marca = marca;
    this.modello = modello;
    this.prezzo = prezzo;
    this.pollici = pollici;
  }

  public String getMarca() {
    return this.marca;
  }

  public void setMarca(String marca) {
    this.marca = marca;
  }

  public String getModello() {
    return this.modello;
  }

  public void setModello(String modello) {
    this.modello = modello;
  }

  public int getPollici() {
    return this.pollici;
  }

  public void setPollici(int pollici) {
    this.pollici = pollici;
  }

  public int getPrezzo() {
    return this.prezzo;
  }

  public void setPrezzo(int prezzo) {
    this.prezzo = prezzo;
  }

  public boolean costaMenoDelBudgetDisponibile(int budgetDisponibile) {
    if (this.getPrezzo() < budgetDisponibile)
      return true;
    return false;
  }

  public boolean stessaMarcaDi(Televisore input) {
    return this.getMarca().equalsIgnoreCase(input.getMarca()) ? true : false;
  }

  public boolean piuGrandeDi(Televisore altroTelevisore) {
    return this.getPollici() == altroTelevisore.getPollici() ? true : false;
  }

  /*
   * si deve fare il rapporto tra prezzo e pollici per avere il costo per pollice
   * inferiore
   */
  public boolean miglioreQualitaPrezzoDi(Televisore altroTelevisore) {
    double rapportoThisTv = this.getPrezzo() / this.getPollici();
    double rapportoAltraTv = altroTelevisore.getPrezzo() / altroTelevisore.getPollici();
    System.out.println("Rapporto prima tv: " + rapportoThisTv);
    System.out.println("Rapporto tv di confronto: " + rapportoAltraTv);
    return (rapportoAltraTv < rapportoThisTv) ? true : false;
  }

  public boolean esisteAlmenoUnoPiuEconomico(Televisore[] catalogo) {
    for (Televisore tv : catalogo) {
      if (tv.getPrezzo() < this.getPrezzo())
        return true;
    }
    return false;
  }

  public int quantiSonoPiuGrandi(Televisore[] catalogo) {
    int listaPiuGrandi = 0;
    for (Televisore tv : catalogo) {
      if (tv.getPollici() > this.getPollici())
        listaPiuGrandi++;
    }
    return listaPiuGrandi;
  }

  public int quantiSonoPiuCariAvendoStessaMarca(Televisore[] catalogo) {
    int listPiuCari = 0;
    for (Televisore tv : catalogo) {
      if (this.getMarca().equalsIgnoreCase(tv.getMarca()) && tv.getPrezzo() > this.getPrezzo())
        listPiuCari++;
    }
    return listPiuCari;
  }

  public boolean ePiuCaroDellaMedia(Televisore[] input) {
    int sommaPrezzi = 0;
    for (Televisore tv : input) {
      sommaPrezzi += tv.getPrezzo();
    }
    double mediaPrezzi = sommaPrezzi / input.length;
    System.out.println("La media è: " + mediaPrezzi);
    return (this.getPrezzo() > mediaPrezzi) ? true : false;
  }

  public static Televisore getPiuCostoso(Televisore[] catalogo) {
    Televisore tvPiuCostosa = catalogo[0];
    for (Televisore tv : catalogo) {
      if (tv.getPrezzo() > tvPiuCostosa.getPrezzo()) {
        tvPiuCostosa = tv;
      }
    }
    return tvPiuCostosa;
  }

  @Override
  public String toString() {
    return this.getMarca()
        + " " + this.getModello()
        + " " + this.getPollici()
        + " " + this.getPrezzo();
  }

  public String getNome() {
    return this.getMarca() + " " + this.getModello();
  }
}
