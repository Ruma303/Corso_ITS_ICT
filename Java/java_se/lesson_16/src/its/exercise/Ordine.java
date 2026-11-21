package its.exercise;

/*  LABORATORIO — l'ordine  */
public class Ordine {

    private final String codice;
    private final double importo;
    private StatoOrdine stato;

    public Ordine(String codice, double importo) {
        if (importo < 0) throw new IllegalArgumentException("Importo negativo: " + importo);
        this.codice = codice;
        this.importo = importo;
        this.stato = StatoOrdine.NUOVO;
    }

    public String getCodice() {
        return codice;
    }

    public double getImporto() {
        return importo;
    }

    public StatoOrdine getStato() {
        return stato;
    }

    // TODO 6 — cambiaStato(StatoOrdine nuovo):
    //          se la transizione non e' ammessa, lancia TransizioneNonValidaException.
    //          Altrimenti aggiorna lo stato.
    public void cambiaStato(StatoOrdine nuovo) {
        if (nuovo == null) throw new IllegalArgumentException("Stato null non valida");
        if (!stato.puoDiventare(nuovo)) {
            throw new TransizioneNonValidaException(this.stato, nuovo);
        }
        this.stato = nuovo;
    }

    @Override
    public String toString() {
        return String.format("%-6s %8.2f  %-11s", codice, importo, stato);
    }
}
