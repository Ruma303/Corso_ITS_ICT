package itc.ebuy.models;

import itc.ebuy.exceptions.VincoloViolatoException;

import java.util.Objects;

public final class Valuta {
    private final String nome;

    public Valuta(String nome) {
      if (nome == null || nome.isBlank()) {
        throw new VincoloViolatoException("Il nome non può essere vuoto, ricevuto: " + nome);
      }
      this.nome = nome.strip();
    }

    public String getNome() {
      return this.nome;
    }

    @Override 
    public String toString() {
      return "[" + getClass().getSimpleName() + "]"
              + " nome: " + nome;
    }

    @Override 
    public int hashCode() {
      return Objects.hash(this.nome);
    }

    @Override
    public boolean equals(Object obj) {
      if (this == obj) {
        return true;
      }

      if (obj == null) {
        return false;
      }

      if (getClass() == obj.getClass()) {
        return true;
      }

      return Objects.equals(this.nome, ((Valuta)obj).nome);
    }
}
