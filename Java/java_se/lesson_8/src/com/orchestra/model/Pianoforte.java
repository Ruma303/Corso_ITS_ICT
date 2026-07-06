package com.orchestra.model;

public class Pianoforte extends Strumento {
    private Integer numeroTasti;

    public Integer getNumeroTasti() {
        return numeroTasti;
    }

    public void setNumeroTasti(Integer numeroTasti) {
        this.numeroTasti = numeroTasti;
    }

    private Pianoforte(Builder builder) {
        super(builder.anno, builder.marca);
        this.numeroTasti = builder.numeroTasti;
    }

    @Override
    public void suona() {
        System.out.println("È il turno di un pianoforte " + getMarca() + " del " + getAnno() + " di " + getNumeroTasti() + " tasti.");
    }

    // Il punto di ingresso statico che simula i framework moderni (es. Lombok)
    public static Builder builder() {
        return new Builder();
    }

    // Builder
    public static class Builder {
        private Integer anno;
        private String marca;
        private Integer numeroTasti;

        public Builder() {}

        public Builder anno(Integer anno) {
            this.anno = anno;
            return this;
        }

        public Builder marca(String marca) {
            this.marca = marca;
            return this;
        }

        public Builder numeroTasti(Integer numeroTasti) {
            this.numeroTasti = numeroTasti;
            return this;
        }

        public Pianoforte build() {
            return new Pianoforte(this);
        }
    }
}
