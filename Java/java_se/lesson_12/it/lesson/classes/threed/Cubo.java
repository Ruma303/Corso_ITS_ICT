package it.lesson.classes.threed;

import it.lesson.classes.abstracts.Forma3D;
import it.lesson.classes.twod.Quadrato;

public class Cubo extends Forma3D {
    private Quadrato q;

    Cubo(String colore, Quadrato q) {
        super(colore);
        this.q = q;
    }

    @Override
    public double volume() {
        return Math.pow(q.getLato(), 3);
    }

    @Override
    public double area() {
        return q.area();
    }

    @Override
    public double perimetro() {
        return q.perimetro();
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", lato: " + q.getLato()
                + ", area: " + area()
                + ", perimetro: " + perimetro()
                + ", volume: " + volume();
    }
}
