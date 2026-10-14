package it.exercise;

public class Uccello extends Animale {

  public Uccello(String nome) {
    super(nome);
  }

  @Override 
  public double costoCuraGiornaliero() {
    return 3.0;
  } 

  @Override
  public void verso() {
    System.out.println("Cip cip!");
  }

  public void vola() {
    System.out.println("L'uccello vola!");
  }

  @Override 
  public String toString() {
    return super.toString() + " [Nome]: " + this.getNome();
  }
}
