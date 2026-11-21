package its.exercise;

/*  LABORATORIO — l'eccezione personalizzata
 *
 *  TODO 5 — falla estendere RuntimeException (unchecked: e' un errore di
 *           programmazione, non una condizione esterna).
 *           Il costruttore riceve i due stati e compone il messaggio
 *           chiamando super(...).
 */
public class TransizioneNonValidaException extends RuntimeException {

    public TransizioneNonValidaException(StatoOrdine da, StatoOrdine a) {
        super("Transazione da " + da.name() + " a " + a.name() + " non valida");
    }
}
