package itc.ebuy.exceptions;

import itc.ebuy.datatypes.FloatGEZ;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class VincoloViolatoExceptionTest {

    @Test
    void conservaIlMessaggio() {
        var e = new VincoloViolatoException("errore");
        assertEquals("errore", e.getMessage());
    }

    @Test
    void eccezioneEUnRuntimeException() {
        var e = new VincoloViolatoException("errore");
        assertInstanceOf(RuntimeException.class, e);
    }

    // Per un test che verifica anche
    // il messaggio lanciato da un datatype:
    @Test
    void verificaMessaggioLanciato() {
        var e = assertThrows(VincoloViolatoException.class, () -> FloatGEZ.of("-1"));
        assertTrue(e.getMessage().contains("-1"));
    }
}