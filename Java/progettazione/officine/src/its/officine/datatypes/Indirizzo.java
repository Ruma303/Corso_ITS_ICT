package its.officine.datatypes;

public class Indirizzo {
    final private String via;
    final private String civico;
    final private String cap;

    public Indirizzo(String via, String civico, String cap) {
        this.via = via;
        this.civico = civico;
        this.cap = cap;
    }

    @Override
    public String toString() {
        return "Indirizzo {" +
                "via='" + via + '\'' +
                ", civico='" + civico + '\'' +
                ", cap='" + cap + '\'' +
                '}';
    }

    public String getVia() {
        return via;
    }

    public String getCivico() {
        return civico;
    }

    public String getCap() {
        return cap;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Indirizzo indirizzo = (Indirizzo) o;
        return via.equals(indirizzo.via) && civico.equals(indirizzo.civico) && cap.equals(indirizzo.cap);
    }

    @Override
    public int hashCode() {
        int result = via.hashCode();
        result = 31 * result + civico.hashCode();
        result = 31 * result + cap.hashCode();
        return result;
    }
}
