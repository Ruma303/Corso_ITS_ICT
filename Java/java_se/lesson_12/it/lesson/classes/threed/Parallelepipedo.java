package it.lesson.classes.threed;

import it.lesson.classes.abstracts.Forma3D;
import it.lesson.classes.twod.Rettangolo;

public class Parallelepipedo extends Forma3D {
    private Rettangolo r;
    private double lunghezza;

    Parallelepipedo(String colore, Rettangolo r, double lunghezza) {
        super(colore);
        this.r = r;
        if (lunghezza <= 0) {
            throw new IllegalArgumentException("La lunghezza dev'essere positiva");
        }
        this.lunghezza = lunghezza;
    }

    public double getLunghezza() {
        return lunghezza;
    }

    @Override
    public double volume() {
        return r.getBase() * r.getAltezza() * this.lunghezza;
    }

    @Override
    public double area() {
        return r.area();
    }

    @Override
    public double perimetro() {
        return r.perimetro();
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", base: " + r.getBase()
                + ", altezza: " + r.getAltezza()
                + ", lunghezza: " + getLunghezza()
                + ", area: " + area()
                + ", perimetro: " + perimetro()
                + ", volume: " + volume();
    }
}
