package itc.ebuy.models;

import itc.ebuy.datatypes.Condizione;
import itc.ebuy.datatypes.FloatGEZ;
import itc.ebuy.datatypes.StatoPost;
import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Instant;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

class CompraloSubitoTest {

    private static final Instant PUBBLICAZIONE = Instant.parse("2026-10-01T10:00:00Z");
    private CompraloSubito c;

    private CompraloSubito.Builder builderValido() {
        return CompraloSubito.builder()
                .descrizione("Borsa")
                .prezzo(FloatGEZ.of("450.999"))
                .stato(StatoPost.DISCRETO)
                .pubblicazione(PUBBLICAZIONE)
                .condizione(Condizione.USATO);
    }

    @BeforeEach
    void setUp() {
        c = builderValido().build();
    }

    // --- costruzione valida ---

    @Test
    void buildValidaRestituisceCompraloSubitoConICampiImpostati() {

        assertEquals("Borsa", c.getDescrizione());
        assertEquals(StatoPost.DISCRETO, c.getStato());
        assertEquals(PUBBLICAZIONE, c.getPubblicazione());
        assertEquals(Optional.of(Condizione.USATO), c.getCondizione());
    }

    @Test
    @DisplayName("Il prezzo viene arrotondato alla scala del datatype")
    void prezzoArrotondato() {
        assertEquals(FloatGEZ.of("451.00"), c.getPrezzo());
    }

    // --- condizione opzionale [0..1] ---

    @Test
    void condizioneAssenteDaOptionalVuoto() {
        CompraloSubito c = builderValido().condizione(null).build();
        assertTrue(c.getCondizione().isEmpty());
    }

    // --- campi obbligatori ---

    @Test
    void descrizioneNullLanciaNullPointer() {
        var b = builderValido().descrizione(null);
        assertThrows(NullPointerException.class, b::build);
    }

    @Test
    void prezzoNullLanciaNullPointer() {
        var b = builderValido().prezzo(null);
        assertThrows(NullPointerException.class, b::build);
    }

    @Test
    void statoNullLanciaNullPointer() {
        var b = builderValido().stato(null);
        assertThrows(NullPointerException.class, b::build);
    }

    @Test
    void pubblicazioneNullLanciaNullPointer() {
        var b = builderValido().pubblicazione(null);
        assertThrows(NullPointerException.class, b::build);
    }

    // --- descrizione ---

    @Test
    void descrizioneBlankViolaVincolo() {
        var b = builderValido().descrizione("   ");
        assertThrows(VincoloViolatoException.class, b::build);
    }

    @Test
    void descrizioneViene_ripulitaDagliSpazi() {
        assertEquals("Borsa", builderValido().descrizione("  Borsa  ").build().getDescrizione());
    }

    // --- setter ---

    @Test
    void setDescrizioneAggiornaIlValore() {
        c.setDescrizione("Borsa in pelle");
        assertEquals("Borsa in pelle", c.getDescrizione());
    }

    @Test
    void setDescrizioneInvalidaLanciaEMantieneIlValoreVecchio() {
        assertThrows(VincoloViolatoException.class, () -> c.setDescrizione(" "));
        assertEquals("Borsa", c.getDescrizione());
    }

    // --- toString ---

    @Test
    void toStringContieneNomeClassePrezzoEDescrizione() {
        String s = builderValido().build().toString();
        assertAll(
                () -> assertTrue(s.contains("[CompraloSubito]")),
                () -> assertTrue(s.contains("Borsa")),
                () -> assertTrue(s.contains("451.00"))
        );
    }
}