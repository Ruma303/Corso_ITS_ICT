package it.lesson.classes.twod;

import it.lesson.classes.abstracts.Forma;

public class TriangoloEquilatero extends Forma {
    private double base, altezza;

    public TriangoloEquilatero(String colore,  double base) {
        super(colore);
        if (base <= 0) {
            throw new IllegalArgumentException("Il lato dev'essere positivo");
        }
        this.base = base;
        this.altezza = (base * Math.sqrt(3)) / 2; // Valore calcolato computazionalmente
    }

    public double getBase() {
        return base;
    }

    public double getAltezza() {
        return altezza;
    }

    @Override
    public double perimetro() {
        return base * 3;
    }

    @Override
    public double area() {
        return (base * altezza) / 2;
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", base: " + base
                + ", altezza: " + altezza
                + ", area: " + area()
                + ", perimetro: " + perimetro();
    }
}