package it.lesson.classes.twod;

import it.lesson.classes.abstracts.Forma;

public class Cerchio extends Forma {
    private double raggio;

    public Cerchio(String colore, double raggio) {
        super(colore);
        if (raggio <= 0) {
            throw new IllegalArgumentException("Il raggio non può essere nullo");
        }
        this.raggio = raggio;
    }

    public double getRaggio() {
        return raggio;
    }

    @Override
    public double perimetro() {
        return 2 * Math.PI * raggio;
    }

    @Override
    public double area() {
        return Math.PI * Math.pow(raggio, 2);
    }

    public String getColore() {
        return super.getColore();
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", raggio: " + raggio
                + ", area: " + area()
                + ", perimetro: " + perimetro();
    }
}