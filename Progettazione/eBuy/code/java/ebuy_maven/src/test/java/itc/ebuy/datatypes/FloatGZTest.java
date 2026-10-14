package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import java.math.BigDecimal;

import static org.junit.jupiter.api.Assertions.*;

class FloatGZTest {

    @ParameterizedTest
    @ValueSource(strings = {"1", "19.99", "100000", "15.55555"})
    void valoriValidi(String s) { assertDoesNotThrow(() -> FloatGZ.of(s));}

    @Test
    void zeroRifiutato() {
        assertThrows(VincoloViolatoException.class, () -> new FloatGZ(BigDecimal.ZERO));
    }

    @ParameterizedTest
    @ValueSource(strings = {"0", "0.00", "0000.000000"})
    void altriZeriRifiutati(String s) {
        assertThrows(VincoloViolatoException.class, () -> FloatGZ.of(s));
    }

    @ParameterizedTest
    @ValueSource(strings = {"-1", "-15.99", "-10000"})
    void valoriNegativiRifutati(String s) {
        assertThrows(VincoloViolatoException.class, () -> FloatGZ.of(s));
    }

    @Test
    void nullThrowsNullPointerException() {
        assertThrows(NullPointerException.class, () -> FloatGZ.of(null));
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
        assertEquals(FloatGZ.of("5.0"), FloatGZ.of("5.0"));
        assertEquals(FloatGZ.of("5.0").hashCode(), FloatGZ.of("5.0").hashCode());
    }

    @Test
    void sommaRestituisceNuovaIstanza(){
        assertEquals(FloatGZ.of("5.0"), FloatGZ.of("1.2").somma(FloatGZ.of("3.8")));
    }

}