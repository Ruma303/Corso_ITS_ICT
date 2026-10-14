package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.util.Objects;

public record IntGEZ(Integer valore) {
    public IntGEZ {
        Objects.requireNonNull(valore, "Il valore non può essere nullo");
        if (valore < 0) {
            throw new VincoloViolatoException("Il valore deve essere >= 0, ricevuto: " + valore);
        }
    }
}
