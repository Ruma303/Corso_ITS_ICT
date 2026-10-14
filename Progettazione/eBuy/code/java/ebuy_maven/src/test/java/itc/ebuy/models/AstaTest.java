package itc.ebuy.models;

import itc.ebuy.datatypes.Durata;
import itc.ebuy.datatypes.FloatGEZ;
import itc.ebuy.datatypes.FloatGZ;
import itc.ebuy.datatypes.StatoPost;
import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class AstaTest {

    private Asta.Builder builderValido() {
        return Asta.builder()
                .descrizione("Chitarra")
                .prezzo(FloatGEZ.of("100"))
                .stato(StatoPost.BUONO)
                .pubblicazione(Instant.parse("2026-10-01T10:00:00Z"))
                .durata(Durata.giorni(5))
                .rialzo(FloatGZ.of("5"));
    }

    @Test
    void scadenzaEPubblicazionePiuDurata() {
        assertEquals(Instant.parse("2026-10-06T10:00:00Z"),
                builderValido().build().scadenza());
    }

    @Test
    void durataMancanteLanciaNullPointer() {
        var b = builderValido().durata(null);
        assertThrows(NullPointerException.class, b::build);
    }

    @Test
    void descrizioneVuotaViolaVincolo() {
        var b = builderValido().descrizione("   ");
        assertThrows(VincoloViolatoException.class, b::build);
    }
}