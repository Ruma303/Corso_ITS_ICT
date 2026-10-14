package it.exercise;

public class Cane extends Animale {
  
    public Cane(String nome) {
        super(nome);
    }

    @Override 
    public double costoCuraGiornaliero() {
      return 8.0;
    } 

    @Override
    public void verso() {
      System.out.println("Bau!");
    }

    public void scodinzola() {
      System.out.println("Il cane scodinzola!");
    }

    @Override 
    public String toString() {
      return super.toString() + " [Nome]: " + this.getNome();
    }
}
