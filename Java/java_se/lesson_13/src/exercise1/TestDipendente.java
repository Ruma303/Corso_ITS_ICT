package exercise1;

public class TestDipendente {

  public static void main(String[] args) {
    Dipendente[] dipendenti = {
      new Manager("Rossi", 3000, 12),
      new Operaio("Bianchi", 1800, 5),
      new Manager("Verdi", 3500, 3),
      new Operaio("Neri", 1650),
      new Apprendista("Gialli", 1200, 8),
      new Apprendista("Rosa", 1600, 6),
    };

    double totBonus = 0.0;
    System.out.println("=== TEAM ===");
    for (Dipendente d : dipendenti) {
      System.out.println(d);
      totBonus += d.calcolaBonus();
    }

    System.out.println("\nTotale bonus:  " + totBonus + " euro");

    Dipendente migliore = getBonusPiuAlto(dipendenti);
    System.out.println("\tIl dipendente con il bonus più alto è: " + migliore);

    System.out.println();
    Dipendente[] opResult = getDipendentiByClassName(dipendenti, "Operaio");
    for (Dipendente d : opResult) {
      System.out.println(d);
    }

    System.out.println();
    getDipendentiByObj(dipendenti, dipendenti[0]);

    System.out.println();
    getManagers(dipendenti);

    System.out.println();
    getOperai(dipendenti);

    System.out.println();
    getApprendisti(dipendenti);

    System.out.println();
    System.out.println("\nIl migliore appartiene alla classe: " + migliore.getClass().getSimpleName() + "\n" + migliore);

    System.out.println();
    sortBonusDecr(dipendenti);
  }

  public static Dipendente getBonusPiuAlto(Dipendente[] dipendenti) {
    Dipendente result = dipendenti[0];
    for (Dipendente d : dipendenti) {
      if (d.calcolaBonus() > result.calcolaBonus()) {
        result = d;
      }
    }
    return result;
  }

  public static Dipendente[] getDipendentiByClassName(Dipendente[] dipendenti, String filtro) {

    if (filtro.equals("") || filtro.isBlank() || filtro.length() == 0) {
      throw new IllegalArgumentException("La classe di ricerca non può essere vuota");
    }
    int tizi = 0;

    for (Dipendente d : dipendenti) {
      // Oppure con instanceof
      if (d.getClass().getSimpleName().equalsIgnoreCase(filtro)) {
        tizi++;
      }
    }
    if (tizi == 0) {
      return null;
    }

    Dipendente[] results = new Dipendente[tizi];
    int resultCount = 0;
    for (int i = 0; i < dipendenti.length; i++) {
       if (dipendenti[i].getClass().getSimpleName().equalsIgnoreCase(filtro)) {
        results[resultCount] = dipendenti[i]; 
        resultCount++;
       }
    }
    
    return results;
  }

  public static void getDipendentiByObj(Dipendente[] dipendenti, Dipendente obj) {
    if (dipendenti.length == 0) {
      return;
    }

    if (obj == null) {
      throw new IllegalArgumentException("L'oggetto da cercare non può essere nullo");
    }

    // Non creiamo l'array ma facciamo il downcasting
    for (Dipendente d : dipendenti) {
      if (d instanceof Manager) {
          System.out.println(d + " | manager coordina " + ((Manager) d).getNumPersone() + " persone");
      } else if (d instanceof Operaio) {
        System.out.println(d + " | operaio lavora " + ((Operaio) d).getOreStraordinario() + " ore extra");
      } else if (d instanceof Apprendista) {
        System.out.println(d + " | apprendista ha " + ((Apprendista) d).getMesiFormazione() + " mesi di formazione");
      } else {
        System.err.println("Il dipendente non appartiene ad alcuna classe nota");
      }
    }
  }

  // Fare 3 metodi separati. Per ogni tipo di classe eseguire il suo metodo
  public static void getManagers(Dipendente[] dipendenti) {
    if (dipendenti.length == 0) {
      return;
    }

    for (Dipendente dipendente : dipendenti) {
        // Uso del downcasting implicito + istanziazione 
        if (dipendente instanceof Manager d) 
          System.out.println(d + " | manager coordina " + ((Manager) d).getNumPersone() + " persone");
    }
  }

  public static void getOperai(Dipendente[] dipendenti) {
    if (dipendenti.length == 0) {
      return;
    }

    for (Dipendente dipendente : dipendenti) {
        // Uso del downcasting implicito + istanziazione 
        if (dipendente instanceof Operaio d) 
          System.out.println(d + " | operaio lavora " + ((Operaio) d).getOreStraordinario() + " ore extra");
    }
  }


  public static void getApprendisti(Dipendente[] dipendenti) {
    if (dipendenti.length == 0) {
      return;
    }

    for (Dipendente dipendente : dipendenti) {
        // Uso del downcasting implicito + istanziazione 
        if (dipendente instanceof Apprendista d) 
          System.out.println(d + " | apprendista ha " + ((Apprendista) d).getMesiFormazione() + " mesi di formazione");
    }
  }

  public static void sortBonusDecr(Dipendente[] dipendenti) {
    if (dipendenti.length == 0) {
      return;
    }
  
    // Bubble Sort
    for (int i = 0; i < dipendenti.length - 1; i++) {
      // Salvare posizione visitata di bonus + alto per evitare di rifarlo
      for (int j = 0; j < dipendenti.length - i - 1; j++) {
        if (dipendenti[j].calcolaBonus() < dipendenti[j + 1].calcolaBonus()) {
          Dipendente temp = dipendenti[j];
          dipendenti[j] = dipendenti[j+1];
          dipendenti[j+1] = temp;        
        }
      }      
    }

    for (Dipendente d: dipendenti)
      System.out.println(d.calcolaBonus());
  }
}
