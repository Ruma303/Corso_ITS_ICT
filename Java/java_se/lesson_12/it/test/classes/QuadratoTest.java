package it.test.classes;

import it.lesson.classes.twod.Quadrato;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class QuadratoTest {

    private Quadrato q1;
    private String colore = "Verde";
    private double lato = 5;


    @BeforeEach
    void setUp() {
            q1 = new Quadrato(colore, lato);
    }

    @Test
    void getColore() {
        assertNotEquals("Rosa", q1.getColore(), "Il colore reale è Verde" );
    }

    @Test
    void getLato() {
        assertEquals(lato, q1.getLato(), "Non è il lato atteso");
    }

    @Test
    void area() {
        assertEquals(25.0, q1.area(), 0.01, "L'area del quadrato non corrisponde");
    }

    @Test
    void perimetro() {
            assertEquals(20.0, q1.perimetro(), 0.01, "Il perimetro del quadrato non corrisponde");
    }
}