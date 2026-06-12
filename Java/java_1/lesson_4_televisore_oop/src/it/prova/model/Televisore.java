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
      int pollici,
      int prezzo) {
    this.marca = marca;
    this.modello = modello;
    this.prezzo = prezzo;
    this.prezzo = prezzo;
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
    return true;
  }

  public boolean piuGrandeDi(Televisore altroTelevisore) {
return true;
  }

  /*
   * si deve fare il rapporto tra prezzo e pollici per avere il costo per pollice
   * inferiore
   */
  public boolean miglioreQualitaPrezzoDi(Televisore altroTelevisore) {
return true;
  }

  @Override
  public String toString() {
    return this.getMarca()
        + " " + this.getModello()
        + " " + this.getPollici()
        + " " + this.getPrezzo();
  }

}
