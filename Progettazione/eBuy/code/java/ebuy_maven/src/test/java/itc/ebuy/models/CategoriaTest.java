package itc.ebuy.models;

import itc.ebuy.exceptions.VincoloViolatoException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;
class CategoriaTest {

    @Test
    @DisplayName("null lancia VincoloViolatoException")
    void nullLanciaEccezione() {
        assertThrows(VincoloViolatoException.class, () -> new Categoria(null));
    }

    @ParameterizedTest
    @ValueSource(strings = {"", " ", "   ", "\t", "\n", "\r"})
    @DisplayName("Stringhe vuote o di soli spazi lanciano VincoloViolatoException")
    void nomiVuotiORifiutati(String nome) {
        assertThrows(VincoloViolatoException.class, () -> new Categoria(nome));
    }

    @ParameterizedTest
    @ValueSource(strings = {"Sport", "IT", "1 2 3"})
    void nomiValidiAccettati(String nome) {
        assertEquals(nome, new Categoria(nome).getNome());
    }

    @Test
    void ilNomeVieneRipulitoDagliSpazi() {
        assertEquals("Sport", new Categoria("  Sport  ").getNome());
    }

    @Test
    void categorieConLoStessoNomeSonoUguali() {
        Categoria a = new Categoria("Sport");
        Categoria b = new Categoria(" Sport ");
        assertEquals(a, b);
        assertEquals(a.hashCode(), b.hashCode());
    }

    @Test
    void categorieDiverseNonSonoUguali() {
        assertNotEquals(new Categoria("Sport"), new Categoria("IT"));
    }

    @Test
    void nonEUgualeANullNeADUnAltroTipo() {
        Categoria c = new Categoria("Sport");
        assertNotEquals(null, c);
        assertNotEquals("Sport", c);
    }

    @Test
    void toStringContieneIlNome() {
        assertTrue(new Categoria("Sport").toString().contains("Sport"));
    }
}