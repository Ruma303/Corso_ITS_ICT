package exercise1;

public class Apprendista extends Dipendente {

  protected int mesiFormazione;
  
  public Apprendista(String nome, double stipendio, int mesiFormazione) {
    super(nome, stipendio);
    if (mesiFormazione < 0) {
      throw new IllegalArgumentException("Il numero di mesi di formazione non può essere negativo");
    }
    this.mesiFormazione = mesiFormazione;
  }

  public Apprendista(String nome, double stipendio) {
    this(nome, stipendio, 0);
  }

  public int getMesiFormazione() {
    return this.mesiFormazione;
  }

  @Override 
  public double calcolaBonus() {
    return ((this.getStipendio() * 5) / 100);
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