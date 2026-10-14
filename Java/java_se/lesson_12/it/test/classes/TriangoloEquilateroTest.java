package it.test.classes;

import it.lesson.classes.twod.TriangoloEquilatero;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TriangoloEquilateroTest {
    
    private TriangoloEquilatero t;
    private String colore = "Bianco";
    private double base = 5;

    @BeforeEach
    void setUp() {
        t = new TriangoloEquilatero(colore, base);
    }

    @Test
    void testBase() {
        assertEquals(base, t.getBase());
    }

    @Test
    void testPerimetro() {
        assertEquals(15, t.perimetro());
    }

    @Test
    void testArea() {
        assertEquals(10.9, t.area(), 0.2);
    }
}