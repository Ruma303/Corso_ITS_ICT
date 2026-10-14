package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

class FloatGEZTest {

    @ParameterizedTest
    @ValueSource(strings = {"0", "0.00", "1", "19.99", "1000000"})
    void valoriValidi(String s) {
        assertDoesNotThrow(() -> FloatGEZ.of(s));
    }

    @ParameterizedTest
    @ValueSource(strings = {"-0.01", "-1", "-1000"})
    void valoriNegativiRifiutati(String s) {
        assertThrows(VincoloViolatoException.class, () -> FloatGEZ.of(s));
    }

    @Test
    void nullLanciaNullPointer() {
        assertThrows(NullPointerException.class, () -> new FloatGEZ(null));
    }

    @Test
    @DisplayName("Verifica che la scala decimale di precisione è 2")
    void scalaPrecisioneEDue() {
        assertEquals(2, FloatGZ.SCALA);
    }

    @Test
    void scalaNormalizzataADue() {
        assertEquals(2, FloatGEZ.of("5").valore().scale());
    }

    @Test
    void valoriNumericamenteUgualiSonoEqual() {
        assertEquals(FloatGEZ.of("2.0"), FloatGEZ.of("2.00"));
        assertEquals(FloatGEZ.of("2.0").hashCode(), FloatGEZ.of("2.00").hashCode());
    }

    @Test
    void sommaRestituisceNuovaIstanza() {
        assertEquals(FloatGEZ.of("3.50"), FloatGEZ.of("1.25").somma(FloatGEZ.of("2.25")));
    }
}