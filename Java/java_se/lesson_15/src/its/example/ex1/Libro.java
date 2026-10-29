package its.example.ex1;

public class Libro extends Articolo implements Vendibile {

    private final double iva = 4;
    private String titolo;

    public Libro(String codice, double prezzo, String titolo) {
        super(codice, prezzo);
        this.setTitolo(titolo);
    }

    private void setTitolo(String titolo) {
        if (titolo == null) {
            throw new NullPointerException("Il titolo non può essere nullo");
        }
        this.titolo = titolo;
    }

    public String getTitolo() {
        return titolo;
    }

    public double getIva() {
        return iva;
    }

    @Override
    public String toString() {
        String formattedPrice = String.format("%.2f", prezzoFinale());

        return super.toString()
                + ", Titolo: " + titolo
                + ", IVA: " + iva + "%"
                + ", Prezzo finale: " + formattedPrice + "€";
    }

    @Override
    public String descrizione() {
        return this.toString();
    }

    @Override
    public double prezzoFinale() {
        return getPrezzo() * (1 + getIva() / 100);
    }
}