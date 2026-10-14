package itc.ebuy.models;

import itc.ebuy.datatypes.Durata;
import itc.ebuy.datatypes.FloatGZ;

import java.time.Instant;
import java.util.Objects;

public class Asta extends Post {

    private final Durata durata;    // <<imm>>
    private final FloatGZ rialzo;   // <<imm>>

    private Asta(Builder b) {
        super(b);                   // valida la parte comune
        this.durata = Objects.requireNonNull(b.durata, "durata obbligatoria");
        this.rialzo = Objects.requireNonNull(b.rialzo, "rialzo obbligatorio");
    }

    public Durata getDurata() { return durata; }
    public FloatGZ getRialzo() { return rialzo; }

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder extends Post.Builder<Builder> {
        private Durata durata;
        private FloatGZ rialzo;

        public Builder durata(Durata v) { this.durata = v; return this; }
        public Builder rialzo(FloatGZ v) { this.rialzo = v; return this; }

        @Override
        protected Builder self() {
            return this;
        }

        @Override
        public Asta build() {
            return new Asta(this);
        }
    }

    // Operazioni
    public Instant scadenza() {
        return getPubblicazione().plus(durata.valore());
    }

    // calcola_prezzo() e ottieni_vincitore() dipendono dalle offerte,
    // quindi le scriviamo quando arriviamo alle associazioni.

}