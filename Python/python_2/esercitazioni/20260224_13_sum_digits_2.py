'''
Sum digits 2

Scrivere un programma che, dato un intero non negativo n,
stampa la somma delle cifre di n.

Ad esempio, se n = 356, il programma stampa 14 (ovvero l'intero
ottenuto come 3+5+6).

A differenza dell'esercizio "Sum digits", si chiede esplicitamente che
il programma operi su n definito come intero, considerando
le sue singole cifre come numeri interi e non stringhe.
'''

from sys import exit

def sum_digits_2(n: int) -> int:

  if type(n) is not int: raise TypeError("L'input inserito deve essere un intero")
  if n < 0: raise ValueError("Il numero inserito non può essere negativo")

  result: int = 0

  while n > 0:
      # Prende l'ultima cifra a destra
      digit = n % 10

      # La aggiunge al totale
      result += digit

      # Rimuovere l'ultima cifra dal numero originale
      # Esempio: 64 // 10 diventa 6
      n = n // 10

  return result


def main() -> int:
  user_input = int(input("Inserisci un numero intero non positivo: ").strip())
  result = sum_digits_2(user_input)
  print(result)
  return 0

if __name__ == "__main__":
  exit(main())