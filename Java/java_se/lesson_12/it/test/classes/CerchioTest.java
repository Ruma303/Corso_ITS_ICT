package it.test.classes;

import it.lesson.classes.twod.Cerchio;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

public class CerchioTest {

    // Istanza condivisa
    private Cerchio c1;
    private String colore = "Rosso";
    private double raggio = 29.30;

    @BeforeEach
    void setUp() {
        c1 = new Cerchio(colore, raggio);
    }

    @Test
    void testColore() {
        assertEquals(colore, c1.getColore());
    }

    @Test
    void testRaggio() {
        assertEquals(raggio, c1.getRaggio());
    }

    @Test
    void perimetro() {
        // Delta molto alto: il valore aspettato rientra nel margine di errore
        assertEquals(30, c1.getRaggio(), 1.0, "Il perimetro del cerchio non combacia");
    }

    @Test
    void testArea() {
        // Not equal: l'area aspettata non è quella reale
        assertNotEquals(2697, c1.area(), 0.01, "L'area del cerchio non combacia");
    }
}