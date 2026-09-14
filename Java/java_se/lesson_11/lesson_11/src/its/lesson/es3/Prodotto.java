package its.lesson.es3;

/*
 * ESERCIZIO C — La classe Prodotto
 * Questo file contiene solo lo scheletro della classe.
 * Tre campi privati: codice, descrizione, prezzo.
 * Almeno due costruttori: uno vuoto e uno con argomenti
 * Getter e setter necessari
 */
public class Prodotto {

    public static int numElementi = 0;
  
    private String codice;
    private String descrizione;
    private double prezzo;
    private int quantita;

    Prodotto() {
      this.codice = "UNKNOWN";
      this.descrizione = "UNKNOWN";
      this.prezzo = 0.00d;
      this.quantita = 0;
    }

    Prodotto(
      String codice,
      String descrizione,
      double prezzo
    ) {
        this.codice = codice;
        this.descrizione = descrizione;
        this.prezzo = prezzo;
    }

    Prodotto(
      String codice,
      String descrizione,
      double prezzo,
      int quantita
    ) {
        this.codice = codice;
        this.descrizione = descrizione;
        this.prezzo = prezzo;
        this.quantita = quantita;
    }

    public String getCodice() {
        return codice;
    }

    public void setCodice(String codice) {
        this.codice = codice;
    }

    public String getDescrizione() {
        return descrizione;
    }

    public void setDescrizione(String descrizione) {
        this.descrizione = descrizione;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public int getQuantita() {
        return quantita;
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("Prodotto {");
        sb.append("codice='").append(codice).append('\'');
        sb.append(", descrizione='").append(descrizione).append('\'');
        sb.append(", prezzo=").append(prezzo);
        sb.append('}');
        return sb.toString();
    }

    public double getPrezzi() {
      return this.prezzo * this.quantita;
    }
}
