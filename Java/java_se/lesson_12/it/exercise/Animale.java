package it.exercise;

abstract class Animale {
  
   protected String nome;
   
   public Animale(String nome) {
       this.nome = nome;
   }

   public String getNome() {
     return this.nome;
   }
   
   public abstract void verso();
   public abstract double costoCuraGiornaliero(); 
   
   public String descrizione() {
       return "Animale di nome: " + nome;
   }

   @Override 
   public String toString() {
     return "[Specie]: " + this.getClass().getSimpleName();
   }
}