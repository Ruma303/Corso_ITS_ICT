package com.composition.es1.model;

import com.composition.es1.performance.Performance;

public class RAM implements Performance {
    private int CapacityGB;

    public RAM(int CapacityGB) {
        this.CapacityGB = CapacityGB;
    }

    @Override
    public String toString() {
        return "{" +
                "CapacityGB=" + CapacityGB +
                '}';
    }

    @Override
    public void verificaPerformace() {
        System.out.println("RAM verificaPerformace");
    }
}
