package it.prova.test;

import it.prova.model.Nazione;

/*
denominazione (String),superficie (double - km²),abitanti (int)
Italia, 301.340, 58_850_000
Francia, 551.695, 67_750_000
Germania, 357.022, 83_200_000
Spagna, 505.990, 47_450_000
Giappone, 377.975, 125_700_000
*/

public class TestNazione {
  public static void main(String[] args) {

    Nazione italia = new Nazione("Italia", 301.340, 58_850_000);
    Nazione francia = new Nazione("Francia", 551.695, 67_750_000);
    Nazione germania = new Nazione("Germania", 357.022, 83_200_000);
    Nazione spagna = new Nazione("Spagna", 505.990, 47_450_000);
    Nazione giappone = new Nazione("Giappone", 377.97, 125_700_000);

    Nazione[] listaNazioniEuropee = new Nazione[] {italia, francia, germania, spagna};

    System.out.println(menu());

    System.out.println(
      spagna.piuEstesaDi(germania)
      ? "La spagna è più estesa della germania"
      : "La spagna NON è più estesa della germania"
    );

    System.out.println(
      giappone.piuPopolosaDi(germania)
      ? "Il giappone è più popoloso della germania"
      : "Il giappone NON è più popoloso della germania"
    );

     System.out.println(
      giappone.esisteAlmenoUnaPiuEstesa(listaNazioniEuropee)
      ? "Esiste almeno una nazione più grande del giappone"
      : "Il giappone è più esteso delle nazioni europee"
    );
  }






  private static String menu() {
    return """
        {
            HELLO GENTE!
            Welcome to Nazioni games!
        }
        """;
  }
}
