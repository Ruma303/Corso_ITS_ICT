package its.example.ex1;

import java.util.Objects;

// Diciamo che un Articolo è confrontabile con un altro Articolo
public abstract class Articolo implements Comparable<Articolo> {

    private String codice;
    private double prezzo;

    public Articolo(String codice, double prezzo) {
        this.setCodice(codice);
        this.setPrezzo(prezzo);
    }

    public String getCodice() {
        return codice;
    }

    private void setCodice(String codice) {
        if (codice == null) {
            throw new NullPointerException("codice non può essere nullo");
        }
        this.codice = codice;
    }

    public double getPrezzo() {
        return prezzo;
    }

    private void setPrezzo(double prezzo) {
        if (prezzo <= 0) {
            throw new IllegalArgumentException("Il prezzo non può essere negativo o zero");
        }
        this.prezzo = prezzo;
    }

    @Override
    public int hashCode() {
        return Objects.hash(codice);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        // Per i tipi primitivi dobbiamo fare il boxin nel suo tipo Wrapper
//        Double p = (Double) obj;
//        return p.equals(((Articolo) obj).prezzo);

        // Controlliamo solo "codice"
         return Objects.equals(this.codice, ((Articolo) obj).codice);
    }

    @Override
    public int compareTo(Articolo o) {
        return this.getCodice().compareTo(o.getCodice());
    }

    @Override
    public String toString() {
        return "[" + this.getClass().getSimpleName()
                + "] Codice: " + this.codice
                + ", Prezzo: " + this.prezzo + "€";
    }
}
