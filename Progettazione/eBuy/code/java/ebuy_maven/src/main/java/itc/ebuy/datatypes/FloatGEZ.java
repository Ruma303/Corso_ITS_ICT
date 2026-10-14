package itc.ebuy.datatypes;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Objects;

public record FloatGEZ(BigDecimal valore) {

    public static final int SCALA = 2;
    public static final RoundingMode ARROTONDAMENTO = RoundingMode.HALF_UP;
    public static final FloatGEZ ZERO = new FloatGEZ(BigDecimal.ZERO);

    public FloatGEZ {
        Objects.requireNonNull(valore, "valore non può essere nullo");
        if (valore.signum() < 0)
            throw new VincoloViolatoException("Il valore deve essere >= 0.00, ricevuto: " + valore);
        valore = valore.setScale(SCALA, ARROTONDAMENTO);
    }

    public static FloatGEZ of(String s) {
        return new FloatGEZ(new BigDecimal(s));
    }

    public FloatGEZ somma(FloatGEZ altro) {
        return new FloatGEZ(valore.add(altro.valore));
    }
}