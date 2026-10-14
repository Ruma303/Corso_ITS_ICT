package it.lesson.classes.abstracts;


import it.lesson.classes.twod.Cerchio;
import it.lesson.classes.twod.Quadrato;
import it.lesson.classes.twod.Rettangolo;
import it.lesson.classes.twod.TriangoloEquilatero;

public abstract class Forma {
    private String colore;

    protected Forma(String colore) {
        this.colore = colore;
    }

    public String getColore() {
        return colore;
    }

    public abstract double area();

    public abstract double perimetro();

    public String descrizione() {
        return "colore: " + colore;
    }

     public static void main(String[] args) {
        Cerchio c1 = new Cerchio("Rosso", 29.30);
        System.out.println(c1.descrizione());
        System.out.println(c1.perimetro());
        System.out.println(c1.area());

        TriangoloEquilatero t1 = new TriangoloEquilatero("Giallo", 5);
        System.out.println(t1.descrizione());
        System.out.println(t1.perimetro());
        System.out.println(t1.area());

        Quadrato q1 = new Quadrato("Rosa", 10);
        System.out.println(q1.descrizione());
        System.out.println(q1.perimetro());
        System.out.println(q1.area());

        Rettangolo r1 = new Rettangolo("Blu", 5, 4);
        System.out.println(r1.descrizione());
        System.out.println(r1.perimetro());
        System.out.println(r1.area());

        Forma f1 = new Cerchio("Verde", 20);
        // Richiama area() di Cerchio, non Forma, in quanto non ha implementazione
        System.out.println(f1.area());
        // Come richiamo descrizione() di Forma, in quanto ha una sua implementazione?
        System.out.println(f1.descrizione());


        // * Esempio NON FUNZIONANTE di trasformazioni ripetute sulla singola istanza
        // Sfruttiamo costantemente upcasting e downcasting per
        // invocare lo stesso metodo ma da diversi tipi reali a runtime
        Forma f = new Rettangolo("Verde", 5, 4);

        if (f instanceof Rettangolo) {
            // Chiamaiamo descrizione di Rettangolo
            System.out.println(f.descrizione());

            // ? UPCASTING di nuovo verso Forma
            f = (Forma) f;
            // Chiamiamo descrizione di Forma
            System.out.println(f.descrizione());

            f = (Cerchio) f; // ! Errore: f è a runtime un Rettangolo
            if (f instanceof Cerchio) {
                // Chiamiamo descrizione di Forma
                System.out.println(f.descrizione());
            }
        }
        // * Esempio funzionante
        
        // La variabile f mantiene il tipo dichiarato Forma
//        Forma f = new Rettangolo("Verde", 5.0, 4.0);
//        if (f instanceof Rettangolo) {
//            System.out.println(f.descrizione());
//        }
//
//        // Riassegnazione lecita: sfruttiamo l'upcasting automatico
//        f = new Cerchio("Rosso", 3.0);
//        if (f instanceof Cerchio) {
//            System.out.println(f.descrizione());
//        }


    }
}