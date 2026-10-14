package it.lesson.classes.abstracts;

import it.lesson.classes.threed.*;

// Prima implementazione senza interfacce
public abstract class Forma3D extends Forma {
    public abstract double volume();

    protected Forma3D(String colore) {
        super(colore);
    }

//    static void main() {
//        Forma[]  forme = {
//                c1 = new
//        }
//
//        // Forme 3D
//        Sfera s1 = new Sfera("Amaranto", c1);
//        System.out.println(s1.descrizione());
//        System.out.println(s1.volume());
//
//        Tetraedro tr = new Tetraedro("Nero", t1);
//        System.out.println(tr.descrizione());
//        System.out.println(tr.volume());
//
//        Cubo cu = new Cubo("Bianco", q1);
//        System.out.println(cu.descrizione());
//        System.out.println(cu.volume());
//
//        Parallelepipedo p1 = new Parallelepipedo("Viola", r1, 3);
//        System.out.println(p1.descrizione());
//        System.out.println(p1.volume());
// }
}
