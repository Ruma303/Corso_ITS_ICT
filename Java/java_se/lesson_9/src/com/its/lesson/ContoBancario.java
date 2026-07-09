package com.its.lesson;

import java.math.BigInteger;

public class ContoBancario {
    private Double saldo;
    private String titolare;
    private BigInteger numOp;
    private String banca;

    public void deposita(double ammontare) {
        if (ammontare > 0) {
           this.saldo += ammontare;
            this.numOp = this.numOp.add(BigInteger.ONE);
        }
        else {
            System.err.println("Impossibile depositare. L'ammontare dev'essere positivo");
        }
    };

    public String informazioniBanca() {
        return "Banca: " + this.getBanca();
    };

    // Costruttore completo
    public ContoBancario(Double saldo, String titolare, BigInteger numOp, String banca) {
        this.saldo = saldo;
        this.titolare = titolare;
        this.numOp = numOp;
        this.banca = banca;
    }

    // Costruttore minimale: saldo e numOp inizializzati a valori di default sicuri
    public ContoBancario(String titolare, String banca) {
        this.titolare = titolare;
        this.banca = banca;
        this.saldo = 0.0;           // evita NullPointerException in deposita()
        this.numOp = BigInteger.ZERO; // evita NullPointerException in add()
    }

    public Double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public String getTitolare() {
        return titolare;
    }

    public void setTitolare(String titolare) {
        this.titolare = titolare;
    }

    public BigInteger getNumOp() {
        return numOp;
    }

    public void setNumOp(BigInteger numOp) {
        this.numOp = numOp;
    }

    public String getBanca() {
        return banca;
    }

    public void setBanca(String banca) {
        this.banca = banca;
    }

    @Override
    public String toString() {
        return "ContoBancario {" +
                "saldo=" + this.getSaldo() +
                ", titolare='" + this.getTitolare() + '\'' +
                ", numOp=" + this.getNumOp() +
                ", banca='" + this.getBanca() + '\'' +
                '}';
    }
}
