package com.composition.es1.model;

import com.composition.es1.performance.Performance;

public class Storage implements Performance {
    private String tipo;
    private int CapacityGB;

    public Storage(String tipo, int CapacityGB) {
        this.tipo = tipo;
        this.CapacityGB = CapacityGB;
    }

    @Override
    public String toString() {
        return "{" +
                "tipo='" + tipo + '\'' +
                ", CapacityGB=" + CapacityGB +
                '}';
    }

    @Override
    public void verificaPerformace() {
        System.out.println("Storage verificato");
    }
}
