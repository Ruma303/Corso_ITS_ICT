package com.orchestra.model;

public class Chitarra extends Strumento {
    private Integer numeroCorde;

    public Chitarra(Integer anno, String marca, Integer numeroCorde) {
        super(anno, marca);
        this.numeroCorde = numeroCorde;
    }

    public Integer getNumeroCorde() {
        return numeroCorde;
    }

    public void setNumeroCorde(Integer numeroCorde) {
        this.numeroCorde = numeroCorde;
    }

    @Override
    public void suona() {
        System.out.println("Una chitarra a " + this.getNumeroCorde() + " corde suona.");
    }
}
