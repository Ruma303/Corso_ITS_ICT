package exercise2;

import java.util.InputMismatchException;
import java.util.Scanner;

public class TestCalcolatrice {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    menu(sc);
    sc.close();
    System.exit(0);
  }

  public static void divisione(Scanner sc) {
    while (true) {
      try {
        // Prendere un input con due numeri e separarli
        System.out.print(
          "Inserisci un numeratore e denominatore separati da spazio: "
        );
        // Svuotare il buffer di out per pulizia in console
        System.out.flush();

        String input = sc.nextLine();
        if (input.equals("") || input.isBlank()) {
          throw new InputMismatchException(
            "Inserire due numeri separati da spazio"
          );
        }
        String[] inputs = input.split(" ");

        if (inputs.length != 2) {
          throw new InputMismatchException(
            "Inserire due numeri separati da spazio"
          );
        }

        double num1 = Double.parseDouble(inputs[0]);
        double num2 = Double.parseDouble(inputs[1]);

        if (num2 == 0) {
          throw new ArithmeticException();
        }

        double divisione = num1 / num2;

        String result = String.format(
          "Divisione tra Numeratore %.2f e Denominatore %.2f = %.2f",
          num1,
          num2,
          divisione
        );
        System.out.println(result);
        break;
      } catch (InputMismatchException | NumberFormatException e) {
        System.out.println(
          "[" +
            e.getClass().getSimpleName() +
            "] Gli input inseriti non sono numeri!"
        );
      } catch (ArithmeticException e) {
        System.out.println(
          "[" +
            e.getClass().getSimpleName() +
            "]: non è possibile dividere per zero"
        );
        break;
      }
    }
  }

  public static void moltiplicazione(Scanner sc) {
    while (true) {
      try {
        // Prendere un input con due numeri e separarli
        System.out.print("Inserisci due fattori da moltiplicare separati da spazio: ");
        // Svuotare il buffer di out per pulizia in console
        System.out.flush();

        String input = sc.nextLine();
        if (input.equals("") || input.isBlank()) {
          throw new InputMismatchException(
            "Inserire due numeri separati da spazio"
          );
        }
        String[] inputs = input.split(" ");

        if (inputs.length != 2) {
          throw new InputMismatchException(
            "Inserire due numeri separati da spazio"
          );
        }

        double num1 = Double.parseDouble(inputs[0]);
        double num2 = Double.parseDouble(inputs[1]);

        if (num1 == 0 || num2 == 0) {
          return;
        }

        double moltiplicazione = num1 * num2;
        String result = String.format(
          "Moltiplicazione tra %.2f e %.2f = %.2f",
          num1,
          num2,
          moltiplicazione
        );
        System.out.println(result);
        break;
      } catch (InputMismatchException | NumberFormatException e) {
        System.out.println(
          "[" +
            e.getClass().getSimpleName() +
            "] Gli input inseriti non sono numeri!"
        );
      } catch (ArithmeticException e) {
        System.out.println(
          "[" +
            e.getClass().getSimpleName() +
            "]: non è possibile dividere per zero"
        );
        break;
      }
    }
  }

  public static void menu(Scanner sc) {
    System.out.println(
      """
      === Benvenuto nell'app Calcolatrice! ===

      Digita uno dei seguenti numeri per attivare la corrispondente azione
      
      0 = esci
      1 = divisione
      2 = moltiplicazione
      """
    );
    while (true) {
      
      System.out.print("Inserisci un numero corrispondente all'azione: ");

      String input = sc.nextLine();
      
      try {
        int scelta = Integer.parseInt(input.trim());
        
        switch (scelta) {
          case 0:
            System.out.println("Grazie per aver usato la nostra applicazione!");
            return;
          case 1:
            System.out.println("Hai scelto divisione");
            divisione(sc);
            break;
          case 2:
            System.out.println("Hai scelto moltiplicazione");
            moltiplicazione(sc);
            break;
          default:
            System.out.println("Scelta non valida. Riprovare.\n");
        }
      } catch (InputMismatchException | NumberFormatException e) {
        System.out.println(
          "[" +
            e.getClass().getSimpleName() +
            "] Gli input inseriti non sono numeri!"
        );
      } catch (ArithmeticException e) {
        System.out.println("[" + e.getClass().getSimpleName() + e.getMessage());
        break;
      } 
      System.out.println("\n======= Operazione conclusa =======\n");
    }
  }
}
