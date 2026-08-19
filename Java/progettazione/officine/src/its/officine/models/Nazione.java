package its.officine.models;

import java.util.*;

public class Nazione {
    final private String nome;
    private Set<String> regex_targa;

    public String getNome() {
        return nome;
    }

    public Set<String> getRegex_targa() {
        return regex_targa;
    }

    public void setRegex_targa(Set<String> regex_targa) {
        this.regex_targa = regex_targa;
    }

    private Nazione(
            String nome,
            Set<String> regex_targa
    ) {
        this.nome = nome;
        this.setRegex_targa(new HashSet<>(regex_targa)); // 1..* garantito alla nascita
    }

    @Override
    public String toString() {
        return this.getNome();
    }
}