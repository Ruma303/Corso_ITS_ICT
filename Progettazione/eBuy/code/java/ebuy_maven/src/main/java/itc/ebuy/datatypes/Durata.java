package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.time.Duration;
import java.util.Objects;

public record Durata(Duration valore) {

    public Durata {
        Objects.requireNonNull(valore, "Il valore non può essere nullo");
        if (valore.isNegative())
            throw new VincoloViolatoException("Durata deve essere >= 0, ricevuto: " + valore);
    }

    public static Durata giorni(long giorni) {
        return new Durata(Duration.ofDays(giorni));
    }
}