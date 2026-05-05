'''
Dato un intero positivo n, il fattoriale di n (denotato da "n!") è
l'intero calcolato come segue:

n! = n * (n-1) * (n-2) * ... * 2 * 1.

Ad esempio:

4! = 4 * 3 * 2 *1

Scrivere un programma che, letto un intero positivo 'n' ne calcoli il fattoriale

Organizzare il programma in opportune funzioni che effettuino il calcolo.
'''
from sys import exit

def factorial(n) -> int | ValueError:
  if n < 0:
    raise ValueError("Il numero non può essere negativo")
  if n == 1 or n == 0:
    return 1
  else:

    return factorial(n - 1) * n


def main():
  test1 = factorial(4)
  print("Il fattoriale di 4 è", test1)
  test2 = factorial(1)
  print("Il fattoriale di 1 è", test2)
  test3 = factorial(int(input("Inserisci un numero intero positivo: ")))
  print("Il tuo fattoriale è", test3)

  return 0

if __name__ == "__main__":
  exit(main())
