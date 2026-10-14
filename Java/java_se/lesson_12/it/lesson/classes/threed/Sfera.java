package it.lesson.classes.threed;

import it.lesson.classes.abstracts.Forma3D;
import it.lesson.classes.twod.Cerchio;

// Forme 3d
public class Sfera extends Forma3D {
    private Cerchio c;

    // Nel nostro esempio prendiamo un Cerchio e non un raggio
    Sfera(String colore, Cerchio c) {
        super(colore);
        this.c = c;
    }

    @Override
    public double volume() {
        return (double) 4 / 3 * (Math.PI * Math.pow(c.getRaggio(), 3));
    }

    @Override
    public double area() {
        return c.area();
    }

    @Override
    public double perimetro() {
        return c.perimetro();
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", raggio: " + c.getRaggio()
                + ", area: " + area()
                + ", perimetro: " + perimetro()
                + ", volume: " + volume();
    }
}
