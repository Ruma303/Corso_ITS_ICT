package it.test.classes;

import it.lesson.classes.twod.Rettangolo;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class RettangoloTest {

    private Rettangolo r;
    private String colore = "Blu";
    private double base = 5;
    private double altezza = 3;

    @BeforeEach
    void setUp() {
        r = new Rettangolo(colore, base, altezza);
    }

    @Test
    void getBase() {
        assertEquals(base, r.getBase());
    }

    @Test
    void getAltezza() {
        assertEquals(altezza, r.getAltezza());
    }

    @Test
    void area() {
        assertEquals(15, r.area(), 0.02);
    }

    @Test
    void perimetro() {
        assertEquals(16, r.perimetro());
    }
}