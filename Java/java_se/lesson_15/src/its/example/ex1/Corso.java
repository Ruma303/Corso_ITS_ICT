package its.example.ex1;

public class Corso extends Articolo implements Vendibile {

    private final double iva = 22;
    private int ore;

    public Corso(String codice, double prezzo, int ore) {
        super(codice, prezzo);
        this.setOre(ore);
    }

    private void setOre(int ore) {
        if (ore <= 0) {
            throw new IllegalArgumentException(
                    "Le ore del corso devono essere maggiori di zero"
            );
        }
        this.ore = ore;
    }

    public int getOre() {
        return ore;
    }

    public double getIva() {
        return iva;
    }

    @Override
    public String toString() {
        String formattedPrice = String.format("%.2f", prezzoFinale());

        return super.toString()
                + ", Ore: " + ore
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