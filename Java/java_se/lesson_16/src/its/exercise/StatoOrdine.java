package its.exercise;

/*  LABORATORIO — l'enum degli stati
 *  Questa e' quasi completa: leggi i TODO.
 */
public enum StatoOrdine {

    // TODO 1 — aggiungi a ciascuna costante la sua descrizione, fra parentesi.
    //          Esempio: NUOVO("In attesa di conferma")
    NUOVO("In attesa di conferma"),
    CONFERMATO("Ordine confermato"),
    SPEDITO("Ordine spedito"),
    CONSEGNATO("Ordine consegnato"),
    ANNULLATO("Ordine annullato");

    // TODO 2 — un campo final String descrizione, e un costruttore che lo riceve.
    //          Il costruttore di un enum e' sempre privato: non serve scriverlo.
    final String descrizione;

    StatoOrdine(String descrizione) {
        this.descrizione = descrizione;
    }

    // TODO 3 — getDescrizione()
    public String getDescrizione() {
        return descrizione;
    }

    public boolean isFinale() {
        return this == CONSEGNATO || this == ANNULLATO;
    }

    // TODO 4 — puoDiventare(StatoOrdine nuovo): quali passaggi sono ammessi?
    //          NUOVO      -> CONFERMATO o ANNULLATO
    //          CONFERMATO -> SPEDITO o ANNULLATO
    //          SPEDITO    -> CONSEGNATO
    //          CONSEGNATO e ANNULLATO -> nessuno
    //          Suggerimento: uno switch su this, con la freccia.

    public boolean puoDiventare(StatoOrdine nuovo) {
        return switch (this) {
            case NUOVO              -> nuovo == CONFERMATO || nuovo == ANNULLATO;
            case CONFERMATO  -> nuovo == SPEDITO || nuovo == ANNULLATO;
            case SPEDITO            -> nuovo == CONSEGNATO;
            case CONSEGNATO, ANNULLATO -> false;
            default -> false;
        };
    }
}
