package it.exercise;

public class Main {

    public static void main(String[] args) {
        Rifugio rifugio = new Rifugio(30);

        Animale[] animali = {
            new Cane("Piero"),
            new Gatto("Andrea"),
            new Uccello("Alfredo"),
            new Uccello("Nicola"),
            new Gatto("Ugo")
        };
        
        double costoComplessivo = 0;

        for (Animale a : animali) {
            // Comportamenti comuni
            a.verso();
            System.out.println("Costo giornaliero: " + a.costoCuraGiornaliero());
            costoComplessivo += a.costoCuraGiornaliero();

            // Comportamenti specifici
            if (a instanceof Cane)
                ((Cane) a).scodinzola();
            else if (a instanceof Gatto)
                ((Gatto) a).faLeFusa();
            else if (a instanceof Uccello)
                ((Uccello) a).vola();

            System.out.println(a.toString());
            System.out.println();
        }

        // Altri test
        System.out.println("[Budget Rifugio] iniziale: +" + rifugio.getBudget());

        // rifugio.cura(animali[0], 2); // OK
        rifugio.cura(animali[1], 3);
        try {
            rifugio.aggiungiFondi(-3); // OK
        } catch (IllegalArgumentException e) {
            System.out.println("Errore: " + e.getMessage());
        }
        rifugio.cura(animali[2], 2);
        // rifugio.cura(animali[2], -2); // Ok
        // rifugio.cura(null, 3); // Ok
    }
}
