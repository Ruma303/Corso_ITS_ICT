package com.orchestra.model;

public class Flauto extends Strumento {
    private String materiale;

    // Il costruttore ora accetta direttamente il Builder
    private Flauto(Builder builder) {
        super(builder.anno, builder.marca); // Passa i dati al costruttore di Strumento
        this.materiale = builder.materiale;
    }

    @Override
    public void suona() {
        System.out.println("Il flauto di " + materiale + " (" + getMarca() + ") sta suonando!");
    }

    // Getter e Setter per materiale (opzionali, se ti servono fuori dalla classe)
    public String getMateriale() {
        return materiale;
    }

    public void setMateriale(String materiale) {
        this.materiale = materiale;
    }

    // --- IL BUILDER ---
    public static class Builder {
        // Il builder ha bisogno di replicare temporaneamente i campi per accumulare i dati
        private Integer anno;
        private String marca;
        private String materiale;

        // Costruttore vuoto del Builder
        public Builder() {
        }

        // Metodi "Fluent" (restituiscono Builder invece di void)
        public Builder setAnno(Integer anno) {
            this.anno = anno;
            return this; // Permette il concatenamento
        }

        public Builder setMarca(String marca) {
            this.marca = marca;
            return this;
        }

        public Builder setMateriale(String materiale) {
            this.materiale = materiale;
            return this;
        }

        // Il metodo build() crea e restituisce l'istanza finale di Flauto
        public Flauto build() {
            return new Flauto(this);
        }
    }
}