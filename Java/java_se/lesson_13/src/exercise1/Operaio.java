package exercise1;

import exercise1.Dipendente;

public class Operaio extends Dipendente {

  protected int oreStraordinario;

  public Operaio(String nome, double stipendio) {
    this(nome, stipendio, 0);
  }

  public Operaio(String nome, double stipendio, int oreStraordinario) {
    super(nome, stipendio);
    if (oreStraordinario < 0) {
      throw new IllegalArgumentException("Il numero di ore di straordinario non può essere negativo");
    }
    this.oreStraordinario = oreStraordinario;
  }

  @Override 
  public double calcolaBonus() {
    return ((this.getStipendio() * 10) / 100);
  }

  public int getOreStraordinario() {
    return this.oreStraordinario;
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