package lesson.uguaglianza;

import java.util.Objects;

class Studente {
    private String matricola;
    private String nome;

    public Studente(String matricola, String nome) {
        this.matricola = matricola;
        this.nome = nome;
    }

    public String getMatricola() {
        return matricola;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public int hashCode() {
        return Objects.hash(matricola);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == null || !(obj instanceof Studente) || getClass() != obj.getClass() || this != obj) {
            return false;
        }
        if (this ==  obj) {
            return true;
        }
        Studente studente = (Studente) obj;
        // Verifichiamo solo la matricola in quanto da design è un identificatore univoco
        return matricola .equals(studente.matricola);
    }
}

