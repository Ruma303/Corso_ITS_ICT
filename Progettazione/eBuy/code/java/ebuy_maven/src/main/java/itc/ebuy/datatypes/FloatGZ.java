package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Objects;

public record FloatGZ(BigDecimal valore) {

    public static final int SCALA = 2;
    public static final RoundingMode ARROTONDAMENTO = RoundingMode.HALF_UP;
    public static final FloatGEZ ZERO = new FloatGEZ(BigDecimal.ZERO);

    public FloatGZ {
        Objects.requireNonNull(valore, "valore non può essere nullo");
        if (valore.signum() <= 0)
            throw new VincoloViolatoException("Il valore deve essere > 0.00, ricevuto: " + valore);
        valore = valore.setScale(SCALA, ARROTONDAMENTO);
    }

    public static FloatGZ of(String s) {
        return new FloatGZ(new BigDecimal(s));
    }

    public FloatGZ somma(FloatGZ altro) {
        return new FloatGZ(valore.add(altro.valore));
    }
}