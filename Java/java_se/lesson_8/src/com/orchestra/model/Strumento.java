package com.orchestra.model;

public abstract class Strumento {

    private Integer anno;
    private String marca;

    public abstract void suona();

    public Strumento(Integer anno, String marca) {
        this.anno = anno;
        this.marca = marca;
    }

    public Integer getAnno() {
        return anno;
    }

    public void setAnno(Integer anno) {
        this.anno = anno;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }
}
