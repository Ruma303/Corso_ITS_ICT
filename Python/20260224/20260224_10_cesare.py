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

# ascii da 65 a 90 per lettere maiuscole
maiuscole = [chr(x) for x in range(65, 91)]

# ascii da 97 a 122 lettere minuscole
minuscole = [chr(x) for x in range(97, 123)]

def cesare_encryption(messaggio, chiave, alfabeto):

  """
  Cifra il messaggio usando il Codice di Cesare con chiave 'chiave'.
  Mantiene inalterati caratteri non alfabetici.
  Rispetta la differenza tra maiuscole e minuscole.
  """

  if chiave <= 0:
      raise ValueError(f"La chiave {chiave} deve essere positiva e maggiore di zero.")

  maiuscole = alfabeto[0]
  minuscole = alfabeto[1]
  result = ""

  for char in messaggio:
    # print(ord(char))
    carattere_trasposto = (ord(char) - ord('A') + chiave)
    # print(f"DEBUG: Posizione carattere {ord(char) - ord('A')} | {carattere_trasposto = }")
    if 'A' <= char <= 'Z':
        # Calcolo posizione circolare per le MAIUSCOLE
        nuovo_car = chr(carattere_trasposto % len(maiuscole) + ord('A'))
        # print(f"DEBUG: {carattere_trasposto % len(maiuscole)}")
        # print(f"DEBUG: {carattere_trasposto % len(maiuscole)} + {ord('A')}")
        result += nuovo_car
    elif 'a' <= char <= 'z':
        # Calcolo posizione circolare per le MINUSCOLE
        nuovo_car = chr(carattere_trasposto % len(minuscole) + ord('a'))
        result += nuovo_car
    else:
        # Caratteri non alfabetici restano invariati
        result += char

  return result


if __name__ == "__main__":
  messaggio = input("Inserisci una stringa da codificare: ")
  chiave = int(input("Inserisci una chiave numerica di spostamento: "))
  alfabeto = [maiuscole, minuscole]
  result = cesare_encryption(messaggio, chiave, alfabeto)
  print(f"messaggio codificato: {result= }")


"""
Esempio con maiuscole: YELLOW

Calcolo posizione carattere Y
pos = ord(char) - ord('A')
pos = 89 - 65 = 24

Si aggiunge la chiave di spostamento, es 5:
24 + 5 = 29

Per restare nel range A..Z si usa il modulo % 26 ovvero, len(maiuscole)
nuova_pos = pos % 26 = 3 (29 / 26 = 1 con resto di 3)

e si converte in ASCII
chr(nuova_pos + ord('A')),
quindi chr(3 + 65) = D

result= 'DJQQTB'
"""