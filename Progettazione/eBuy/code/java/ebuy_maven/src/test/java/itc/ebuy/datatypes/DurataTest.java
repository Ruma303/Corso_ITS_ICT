package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

class DurataTest {

    @Test
    @DisplayName("Una durata positiva è accettata")
    void durataPositivaValida() {
        Durata d = new Durata(Duration.ofHours(3));
        assertEquals(Duration.ofHours(3), d.valore());
    }

    @Test
    @DisplayName("Durata >= 0 è ammessa")
    void durataZeroValida() {
        assertDoesNotThrow(() -> new Durata(Duration.ZERO));
    }

    @Test
    @DisplayName("Una durata negativa viola il vincolo e lancia eccezione")
    void durataNegativaLanciaEccezione() {
        assertThrows(VincoloViolatoException.class,
                () -> new Durata(Duration.ofSeconds(-1)));
    }

    @Test
    @DisplayName("Durata null lancia errore NullPointerException")
    void durataNullLanciaNullPointer() {
        assertThrows(NullPointerException.class, () -> new Durata(null));
    }

    @Test
    @DisplayName("Creazione durata usando la factory giorni(int numGiorni)")
    void factoryGiorni() {
        assertEquals(new Durata(Duration.ofDays(5)), Durata.giorni(5));
    }
}