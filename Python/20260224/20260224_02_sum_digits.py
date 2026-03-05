'''
Sum digits

Scrivere un programma che, dato un intero non negativo n,
stampa la somma delle cifre di n.

Ad esempio, se n = 356, il programma stampa 14 (ovvero l'intero
ottenuto come 3+5+6).

Modificare il programma di modo che:

 - definisca una opportuna funzione sum_digits(n:int)->int
 - prenda l'input dell'utente da tastiera.
'''


def sum_digits(num):

  if int(num) < 0:
    print("Il numero non può essere negativo")
    return

  dig_sum = 0

  for i, digit in enumerate(num):
    dig_sum += int(digit)

  return dig_sum


if __name__ == "__main__":
  num = input("Scrivi un numero con più cifre non negativo: ").strip()
  print(sum_digits(num))