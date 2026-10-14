package exercise1;

public class Manager extends Dipendente {

  protected int numPersone;

  public Manager(String nome, double stipendio) {
    this(nome, stipendio, 0);
  }

  public Manager(String nome, double stipendio, int numPersone) {
    super(nome, stipendio);
    if (numPersone < 0) {
      throw new IllegalArgumentException("Il numero di persone coordinate non può essere negativo");
    }
    this.numPersone = numPersone;
  }

  @Override 
  public double calcolaBonus() {
    return ((this.getStipendio() * 30) / 100);
  }

  public int getNumPersone() {
    return this.numPersone;
  }

  @Override
  public String toString() {
    String formattedStipendio = String.format("%.2f", stipendio);
    String formattedBonus = String.format("%.2f", this.calcolaBonus());
    return nome 
    + "\t" + this.getClass().getSimpleName() 
    + "\tbase\t" + formattedStipendio
    + "\tbonus\t" + formattedBonus;
  }
}