package exercise1;

public abstract class Dipendente {
  protected String nome;
  protected double stipendio;

  Dipendente() {};
  
  Dipendente(String nome, double stipendio) {
    if (nome.isBlank() || nome.equals("") || nome.length() == 0) {
      throw new IllegalArgumentException("Il nome non può essere vuoto");
    }
    this.nome = nome;

    if (stipendio <= 0) {
      throw new IllegalArgumentException("Lo stipendio non può essere negativo o vuoto");
    }
    this.stipendio = stipendio;
  };
 
  public abstract double calcolaBonus();

  public double getStipendio() {
    return this.stipendio;
  }
}