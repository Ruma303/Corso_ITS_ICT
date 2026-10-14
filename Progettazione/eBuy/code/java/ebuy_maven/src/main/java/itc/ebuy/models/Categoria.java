package itc.ebuy.models;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.util.Objects;

// TODO Non final, future sotto-categorie da aggiungere
public class Categoria {
    private final String nome;

    public Categoria(String nome) {
        if (nome == null || nome.isBlank()) {
            throw new VincoloViolatoException("Il nome non può essere vuoto, ricevuto: " + nome);
        }
        this.nome = nome.strip();
    }
    public String getNome() {
        return nome;
    }

    @Override
    public String toString() {
        return "[" + getClass().getSimpleName() + "]"
                + " nome: " + nome;
    }

    @Override
    public int hashCode() {
        return Objects.hash(nome);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        return Objects.equals(this.nome, ((Categoria) obj).nome);
    }
}
