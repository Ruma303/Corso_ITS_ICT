package it.lesson.classes.twod;

import it.lesson.classes.abstracts.Forma;

public class Quadrato extends Forma {
    private double lato;

    public double getLato() {
        return lato;
    }

    public Quadrato(String colore, double lato) {
        super(colore);
        if (lato <= 0) {
            throw new IllegalArgumentException("Il lato dev'essere positivo");
        }
        this.lato = lato;
    }

    @Override
    public double area() {
        return lato * lato;
    }

    @Override
    public double perimetro() {
        return lato * 4;
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", lato: " + lato
                + ", area: " + area()
                + ", perimetro: " + perimetro();
    }
}