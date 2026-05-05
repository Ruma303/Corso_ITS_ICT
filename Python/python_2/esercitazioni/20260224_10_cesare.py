'''
Svetonio nella "Vita dei dodici Cesari" racconta che Giulio Cesare
usava per le sue corrispondenze riservate un codice di sostituzione
molto semplice, nel quale ogni lettera alfabetica del testo veniva
sostituita dalla lettera che le segue di tre posti nell'alfabeto:
la lettera 'A' veniva sempre sostituita con la 'D', la 'B' con la 'E'
e così; via fino alle ultime lettere che venivano cifrate con le
prime, come nella tabella che segue (che fa riferimento
all'odierno alfabeto internazionale).

  Lettera          a b c d e f g h i j k l m n o p q r s t u v w x y z
  Lettera cifrata  d e f g h i j k l m n o p q r s t u v w x y z a b c

Più in generale, si dice "Codice di Cesare" un codice nella quale ogni
lettera del messaggio in chiaro (il messaggio prima della codifica)
viene spostata di un numero fisso 'x' di posti (la chiave del codice),
non necessariamente tre.

Si scriva un programma che prenda in input un messaggio
(stringa) 'messaggio' ed una chiave 'x' (un intero positivo) e lo traduca
nel corrispondente messaggio cifrato secondo il codice di Cesare
con chiave 'x'.

La funzione deve lasciare inalterati tutti i caratteri del messaggio che
non siano lettere, e deve rispettare la differenza tra maiuscole e minuscole.

Suggerimenti:

I possibili caratteri rappresentabili nel computer sono ordinati.
Dunque, ad ogni carattere corrisponde un codice numerico (int), che è
il numero d'ordine nell'ordinamento.

Python offre due funzioni che saranno cruciali per questo esercizio:
 - ord(c) che, dato un carattere c, ne restituisce il codice numerico (int)
 - chr(i) che, dato un intero i, restituisce il carattere corrispondente.

Ad esempio:
	- ord('A') = 65
	- chr(65) = 'A'

Nell'ordine dei caratteri, le lettere maiuscole sono una di seguito all'altra:
	- ord('A') = 65
	- ord('B') = 66
	...
	- ord('Z') = 90

La stessa cosa vale per le lettere minuscole:
	- ord('a') = 97
	...
	- ord('z') = 122

Dunque, per ogni carattere c del messaggio in chiaro, il corrispondente
carattere del messaggio cifrato (con codice intero x) sarà:
	chr( ord(c) + x ) se c è una lettera (maiuscola o minuscola)
	  				  che non è tra le ultime x dell'alfabeto

Vanno gestiti però tutti i casi: che succede se c = 'Y' e x = 5?
Il corrispondente carattere cifrato dovrebbe essere 'D'!

Buon divertimento!
'''

from sys import exit

def cesare_encryption(chiave, messaggio, alfabeto):

  """
  Cifra il messaggio usando il Codice di Cesare con chiave 'chiave'.
  Mantiene inalterati caratteri non alfabetici.
  Rispetta la differenza tra maiuscole e minuscole.
  """
  try:
    if chiave <= 0:
        raise ValueError(f"La chiave {chiave} deve essere positiva e maggiore di zero.")

    maiuscole = alfabeto[0]
    minuscole = alfabeto[1]
    result = ""

    for char in messaggio:

      # Calcolo posizione circolare per le MAIUSCOLE
      if 'A' <= char <= 'Z':
          carattere_trasposto = (ord(char) - ord('A') + chiave)
          nuovo_car = chr(carattere_trasposto % len(maiuscole) + ord('A'))
          result += nuovo_car
      # Calcolo posizione circolare per le MINUSCOLE
      elif 'a' <= char <= 'z':
          carattere_trasposto = (ord(char) - ord('a') + chiave)
          nuovo_car = chr(carattere_trasposto % len(minuscole) + ord('a'))
          result += nuovo_car
      else:
          # Caratteri non alfabetici restano invariati
          result += char

    return result

  except ValueError:
    print("Cattivo")
    return messaggio
  finally:
    pass


def cesare_multi(chiave, messaggio, /, *alfabeti):
    """
    Cifra il messaggio usando il Codice di Cesare con chiave 'chiave'.
    Mantiene inalterati caratteri non appartenenti ad alcun alfabeto.
    È possibile passare più alfabeti dal terzo parametro in poi.
    """
    result = ""

    for char in messaggio:
        cifrato = False

        for alfabeto in alfabeti:
            # Non tutti gli alfabeti sono contigui in Unicode
            # Per questo verifichiamo direttamente se il carattere
            # appartiene all'alfabeto in analisi

            # scansione lineare: nessun metodo built-in tipo index()
            idx = 0
            trovato = False

            for c in alfabeto:
                if c == char:
                    trovato = True
                    break
                idx += 1              # idx cresce solo se c != char

            if trovato:
                nuovo_idx = (idx + chiave) % len(alfabeto)
                result += alfabeto[nuovo_idx]
                cifrato = True
                break  # trovato l'alfabeto di appartenenza: nessun altro va controllato

        if not cifrato:
            result += char

    return result


def main():
  # Alfabeti
  maiuscole = [chr(x) for x in range(65, 91)]
  minuscole = [chr(x) for x in range(97, 123)]
  numeri = [str(n) for n in range(10)]
  simboli = list('!@#$%^&*')
  greche = list('αβγδεζηθικλμνξοπρστυφχψω')
  kanji = ['日', '本', '語', '学']  # esempio (stringhe Unicode)

  # Input
  # messaggio = input("Inserisci una stringa da codificare: ")
  chiave = int(input("Inserisci una chiave numerica di spostamento: "))
  messaggio1 = "_abcxyz ABC!XYZ . "
  alfabeto1 = [maiuscole, minuscole]

  messaggio2 = "hello ELITE 987 ! αβγ 日語"

  # Tests
  cesare1 = cesare_encryption(chiave, messaggio1, alfabeto1)
  print(f"Messaggio originario: {messaggio1 = }\nMessaggio codificato: {cesare1 = }")
  cesare2 = cesare_multi(chiave, messaggio2,
      minuscole, maiuscole, numeri, simboli, greche, kanji
  )
  print(f"Messaggio originario: {messaggio2 = }\nMessaggio codificato: {cesare2 = }")
  return 0


if __name__ == "__main__":
  exit(main())
