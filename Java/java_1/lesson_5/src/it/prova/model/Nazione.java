package it.prova.model;

public class Nazione {
  private String denominazione;
  private double superficie;
  public int abitanti;

  public Nazione(String denominazione, double superficie, int abitanti) {
    this.denominazione = denominazione;
    this.superficie = superficie;
    this.abitanti = abitanti;
  }

  public String getDenominazione() {
    return denominazione;
  }

  public void setDenominazione(String denominazione) {
    this.denominazione = denominazione;
  }

  public double getSuperficie() {
    return superficie;
  }

  public void setSuperficie(double superficie) {
    this.superficie = superficie;
  }

  public int getAbitanti() {
    return abitanti;
  }

  public void setAbitanti(int abitanti) {
    this.abitanti = abitanti;
  }

  @Override
  public String toString() {
    return "Nazione: - denominazione: " + this.getDenominazione();
  }

  public String getName() {
    return this.getDenominazione();
  }

  public boolean piuEstesaDi(Nazione input) {
    return (this.getSuperficie() > input.getSuperficie()) ? true : false;
  }

  public boolean piuPopolosaDi(Nazione input) {
    return (this.getAbitanti() > input.getAbitanti()) ? true : false;
  }

  public boolean esisteAlmenoUnaPiuEstesa(Nazione[] nazioni) {
    for (Nazione n : nazioni)
      if (n.getSuperficie()>this.getSuperficie() ) {
        System.out.println(n.getSuperficie());
        return true;
      }
    return false;
  }
}
