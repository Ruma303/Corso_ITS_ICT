"""
Nome file: num_digits.py

Scrivere un programma che, dato un intero non negativo n, stampa il numero di cifre di n.

Ad esempio, se n = 356, il programma stampa 3.

Il conteggio deve essere effettuato operando su n come intero (tramite operazioni aritmetiche), senza convertirlo in stringa.
"""

from sys import exit

def num_digits(number: int) -> int:
  assert isinstance(number, int), "Il valore non è un numero. Dev'essere un numero intero"
  assert number >= 0, "Il numero dev'essere NON negativo"

  result = 0

  # WARNING: Se mettessimo while number == 0 il ciclo si bloccherebbe alla prima cifra 0 che incontra
  while True:

    result += 1
    number = number // 10 # Rimuove l'ultima cifra
    
    # INFO: il controllo in coda consente di evitare che il ciclo si blocchi se la cifra in esame == 0
    # Verifichiamo esclusivamente se non sono rimaste più cifre
    if not number: 
      break 

  return result


def main() -> int:
    test1 = 736394239012347500043
    test1_digits = num_digits(test1)
    print(f"Il numero {test1} ha {test1_digits} cifre")

    test2 = 0
    test2_digits = num_digits(test2)
    print(f"Il numero {test2} ha {test2_digits} cifre")

    return 0

if __name__ == "__main__":
    exit(main())
