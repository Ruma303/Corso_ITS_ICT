package it.lesson.classes.prodotto;

public class Contatore {
    public static int contatore  = 0;
    public int contatorePrivato = 0;

    Contatore() {
        this.contatore++;
        this.contatorePrivato++;
    }

    static void main() {
        new Contatore();
        new Contatore();
        Contatore c3 = new Contatore();
        System.out.println("Contatore delle classi: " + c3.contatore + ", contatore privato: " + c3.contatorePrivato);
    }
}

