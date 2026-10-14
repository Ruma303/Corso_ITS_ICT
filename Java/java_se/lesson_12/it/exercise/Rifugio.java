package it.exercise;

public class Rifugio {
  private double budget;

  public Rifugio(double budget) {
    this.budget = budget;
  }

  public double getBudget() {
    return this.budget;
  }

  public void aggiungiFondi(double importo) {
    if (importo <= 0) {
      throw new IllegalArgumentException("Inserire un importo positivo e non nullo");
    }
    this.budget += importo;
  }

  public void cura(Animale animale, int giorni) {
    if (animale == null)
      throw new NullPointerException("L'istanza di animale è nulla");
    if (giorni <= 0)
      throw new IllegalArgumentException("Inserire un numero di giorni positivo e non nullo");

      double costoComplessivo = animale.costoCuraGiornaliero() * giorni;
      if (this.budget < costoComplessivo) {
        throw new IllegalStateException("Il costo di cure supera il budget disponibile del rifugio");
      }
      this.budget -= costoComplessivo;
      System.out.println("Pagamento cure in corso: -" + costoComplessivo);
      System.out.println("[Budget Rifugio] = " + this.budget);
  }
}
