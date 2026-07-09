package com.its.lesson;

import java.math.BigInteger;

public class ContoRisparmio extends ContoBancario {
    private final Float tassoInteresse = 10.0f;

    public ContoRisparmio(String titolare, String banca) {
        super(titolare, banca);
    }

    public ContoRisparmio(ContoBancario contoBancario) {
        super(
            contoBancario.getSaldo(),
            contoBancario.getTitolare(),
            contoBancario.getNumOp(),
            contoBancario.getBanca()
        );
    }

    public void applicaInteressi() {

        double interessiGuadagnati = super.getSaldo() * tassoInteresse / 100;

        // Aggiorno il saldo sommandoli
        this.setSaldo(this.getSaldo() + interessiGuadagnati);

        // Incrementare il numero di operazioni
        this.setNumOp(this.getNumOp().add(BigInteger.ONE));
    }

    public Float getTassoInteresse() {
        return tassoInteresse;
    }
}
