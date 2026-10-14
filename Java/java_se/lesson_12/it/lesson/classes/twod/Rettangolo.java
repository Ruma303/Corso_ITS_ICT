package it.lesson.classes.twod;

import it.lesson.classes.abstracts.Forma;

public class Rettangolo extends Forma {
    private double base, altezza;

    public Rettangolo(String colore, double base, double altezza) {
        super(colore);
        if (base <= 0 || altezza <= 0) {
            throw new IllegalArgumentException("Base e altezza devono essere positivi");
        }
        this.base = base;
        this.altezza = altezza;
    }

    public double getBase() {
        return base;
    }

    public double getAltezza() {
        return altezza;
    }

    @Override
    public double area() {
        return base * altezza;
    }

    @Override
    public double perimetro() {
        return base * 2 + altezza * 2;
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
