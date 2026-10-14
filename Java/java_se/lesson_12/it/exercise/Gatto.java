package it.exercise;

public class Gatto extends Animale {

  public Gatto(String nome) {
    super(nome);
  }

  @Override 
  public double costoCuraGiornaliero() {
    return 5.0;
  } 

  @Override
  public void verso() {
    System.out.println("Miao!");
  }

  public void faLeFusa() {
    System.out.println("Il gatto fa le fusa!");
  }

  @Override 
  public String toString() {
    return super.toString() + " [Nome]: " + this.getNome();
  }
}
