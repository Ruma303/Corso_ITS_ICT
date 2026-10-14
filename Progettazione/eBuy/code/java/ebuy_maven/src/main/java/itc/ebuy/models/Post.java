package itc.ebuy.models;

import itc.ebuy.datatypes.*;
import itc.ebuy.exceptions.VincoloViolatoException;

import java.time.Instant;
import java.util.Objects;
import java.util.Optional;

public abstract class Post {

    private String descrizione;                 // modificabile nell'UML (niente <<imm>>)
    private final FloatGEZ prezzo;              // <<imm>>
    private final StatoPost stato;              // <<imm>>
    private final Instant pubblicazione;        // <<imm>>
    private final Condizione condizione;        // [0..1], può essere null

    protected Post(Builder<?> b) {
        this.descrizione = requireDescrizione(b.descrizione);
        this.prezzo = Objects.requireNonNull(b.prezzo, "prezzo obbligatorio");
        this.stato = Objects.requireNonNull(b.stato, "stato obbligatorio");
        this.pubblicazione = Objects.requireNonNull(b.pubblicazione, "pubblicazione obbligatoria");
        this.condizione = b.condizione;
    }

    private static String requireDescrizione(String d) {
        Objects.requireNonNull(d, "descrizione obbligatoria");
        if (d.isBlank()) throw new VincoloViolatoException("descrizione vuota");
        return d.strip();
    }

    @Override
    public String toString() {
        return "[" + getClass().getSimpleName() + "]"
                + " desc.: " + descrizione
                + ", prezzo: " + prezzo.valore().toPlainString() + "€"
                + ", (" + stato + ")"
                + ", pubblicato: " + pubblicazione;
    }

    // GETTERS
    public String getDescrizione() { return descrizione; }
    public FloatGEZ getPrezzo() { return prezzo; }
    public StatoPost getStato() { return stato; }
    public Instant getPubblicazione() { return pubblicazione; }
    public Optional<Condizione> getCondizione() { return Optional.ofNullable(condizione); }

    // SETTERS
    public void setDescrizione(String descrizione) {
        this.descrizione = requireDescrizione(descrizione);
    }

    // BUILDER (self-type generico, per le sottoclassi)
    public abstract static class Builder<T extends Builder<T>> {
        private String descrizione;
        private FloatGEZ prezzo;
        private StatoPost stato;
        private Instant pubblicazione;
        private Condizione condizione;

        protected abstract T self();
        public abstract Post build();

        public T descrizione(String v)      { this.descrizione = v; return self(); }
        public T prezzo(FloatGEZ v)          { this.prezzo = v; return self(); }
        public T stato(StatoPost v)         { this.stato = v; return self(); }
        public T pubblicazione(Instant v)   { this.pubblicazione = v; return self(); }
        public T condizione(Condizione v)   { this.condizione = v; return self(); }
    }
}
