package its.officine.datatypes;

public class CodiceFiscale {
    final private String codice_fiscale;
    public CodiceFiscale(String codice_fiscale) {
        if (codice_fiscale == null) {
            throw new NullPointerException("codice_fiscale == null");
        }
        if (codice_fiscale // non è uguale alla regex) {

        }
        // this.codice_fiscale = codice_fiscale;
    }

    // Implementa correttamente
    public int hashCode() {
        return this.hashCode();
    }

    public boolean equals(Object obj) {
        return obj instanceof CodiceFiscale;
    }

}