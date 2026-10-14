package it.lesson.classes.threed;

import it.lesson.classes.abstracts.Forma3D;
import it.lesson.classes.twod.TriangoloEquilatero;

public class Tetraedro extends Forma3D {
    private TriangoloEquilatero t;

    Tetraedro(String colore, TriangoloEquilatero t) {
        super(colore);
        this.t = t;
    }

    @Override
    public double volume() {
        return (Math.pow(t.getBase(), 3) * Math.sqrt(2)) / 12;
    }

    @Override
    public double area() {
        return t.area();
    }

    @Override
    public double perimetro() {
        return t.perimetro();
    }

    @Override
    public String descrizione() {
        return "Oggetto di tipo " + this.getClass().getSimpleName() + ": " + super.descrizione()
                + ", base: " + t.getBase()
                + ", altezza: " + t.getAltezza()
                + ", area: " + area()
                + ", perimetro: " + perimetro()
                + ", volume: " + volume();
    }
}

