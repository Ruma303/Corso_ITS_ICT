Partire dalla classe astratta Animale
abstract class Animale
 
abstract class Animale {
   protected String nome;
   public Animale(String nome) {
       this.nome = nome;
   }
   public abstract void verso();
   public String descrizione() {
       return "Animale di nome: " + nome;
   }
}
// TODO: creare la classe Cane
// TODO: creare la classe Gatto
// TODO: creare la classe Uccello
public class Main {
   public static void main(String[] args) {
       // Il progetto verrà sviluppato
       // attraverso i cinque esercizi.
   }
}
 
- Il rifugio ospita tre specie di animali: cani, gatti e uccelli.
- Ogni animale possiede un nome e può emettere un verso, ma ogni specie lo fa in maniera differente.
- Inoltre, il rifugio deve conoscere il costo giornaliero necessario per prendersi cura di ciascun animale.

- Crea tre classi che estendano Animale:
  - Cane
    - Implementa il costruttore.
    - Ridefinisci verso() affinché stampi Bau!.
    - Implementa un metodo costoCuraGiornaliero() che restituisca 8.0.

  - Gatto
    - Implementa il costruttore.
    - Ridefinisci verso() affinché stampi Miao!.
    - Implementa costoCuraGiornaliero() che restituisca 5.0.

  - Uccello
    - Implementa il costruttore.
    - Ridefinisci verso() affinché stampi Cip cip!.
    - Implementa costoCuraGiornaliero() che restituisca 3.0.

- Per rendere obbligatoria l'implementazione del costo in tutte le sottoclassi, aggiungi il metodo alla classe astratta Animale

  public abstract double costoCuraGiornaliero();
 
Nel main, crea un array Animale[] contenente almeno cinque animali di specie differenti.

Utilizzando un unico ciclo:
- Stampa la descrizione dell'animale.
- Fagli emettere il proprio verso.
- Stampa il costo giornaliero della sua cura.
- Calcola il costo complessivo giornaliero per tutti gli animali.
- Non utilizzare instanceof né controlli sulla specie per determinare il verso o il costo di cura.
 
 
Oltre a emettere un verso, alcune specie possiedono comportamenti specifici.

Aggiungi alle sottoclassi:
- Cane: scodinzola() → stampa "Il cane scodinzola!"
- Gatto: faLeFusa() → stampa "Il gatto fa le fusa!"
- Uccello: vola() → stampa "L'uccello vola!"

- Nel main, utilizza l'array creato nell'esercizio precedente.
- Per ogni animale, esegui il comportamento specifico della sua specie.
- Il rifugio vuole stampare automaticamente le informazioni di ogni animale.
- Nella classe Animale, ridefinisci il metodo toString().
- Il metodo deve restituire una stringa contenente la specie dell'animale e il suo nome.getClass().getSimpleName()
 
- Il rifugio dispone di un budget economico per prendersi cura degli animali.
- Ogni volta che viene effettuata una cura, il costo deve essere sottratto dal budget disponibile.

- Il programma deve gestire correttamente anche operazioni non valide.

- Crea una nuova classe Rifugio con:
  - Un attributo privato budget, di tipo double.
  - Un costruttore che riceve il budget iniziale.
  - Un metodo getBudget() che restituisce il budget disponibile.

- Implementa metodo: public void aggiungiFondi(double importo)
  - Il metodo deve aggiungere fondi al budget.
  - Se l'importo è minore o uguale a zero, deve lanciare un'IllegalArgumentException con un messaggio significativo.

- Implementa metodo: public void cura(Animale animale, int giorni). Il metodo deve: 
  - Verificare che l'animale non sia null.
  - Verificare che il numero di giorni sia maggiore di zero.

- Calcolare il costo totale utilizzando costoCuraGiornaliero().
  - Verificare che il budget sia sufficiente.
  - Sottrarre il costo dal budget e stampare un messaggio di conferma.
  - Se l'animale è null oppure i giorni non sono validi, lancia un'IllegalArgumentException.
  - Se il budget non è sufficiente, lancia un'IllegalStateException.
  - In caso di errore, il budget non deve essere modificato.
 
 
Nel main, crea un rifugio con un budget iniziale di 30 € ed esegui queste operazioni nell'ordine:
 
 
Rifugio rifugio = new Rifugio(30);
Animale cane = new Cane("Fido");
Animale gatto = new Gatto("Micio");
Animale uccello = new Uccello("Titti");
// Operazione 1
rifugio.cura(cane, 2);
// Operazione 2
rifugio.cura(gatto, 3);
// Operazione 3
rifugio.aggiungiFondi(-3);
// Operazione 4
rifugio.cura(uccello, 2);
 