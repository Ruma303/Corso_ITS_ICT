package com.composition.es1.model;

import com.composition.es1.performance.Performance;

public class CPU implements Performance {
    private String marca;
    private int potenzaGHz;

    public CPU(String marca, int potenzaGHz) {
        this.marca = marca;
        this.potenzaGHz = potenzaGHz;
    }

    @Override
    public String toString() {
        return "{" +
                "marca='" + marca + '\'' +
                ", potenzaGHz=" + potenzaGHz +
                '}';
    }

    @Override
    public void verificaPerformace() {
        System.out.println("CPU verifica performace");
    }
}
