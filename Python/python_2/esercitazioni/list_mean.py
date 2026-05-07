'''
Scrivere un programma che legga da tastiera una lista "list" di numeri e
calcoli e restituisca il valor medio dei numeri in "list".

Ad esempio, se viene letta

list = [2, 5, 10]

il programma deve restituire (2+5+10)/3 = 17/3 = 5.666...

Organizzare il programma in opportune funzioni che effettuino il calcolo.
'''

from sys import exit

def converti_in_lista(inputs: str) -> list[int]:
  lista = []
  for c in inputs.split(','):
    num = c.strip()
    if num:
      try:
        lista.append(int(c))
      except Exception:
        continue

  return lista

def media(lista) -> float:
  somma = 0
  numeri = 0

  for ele in lista:
    somma += ele
    numeri += 1

  return somma/numeri

def main() -> int:

  test1 = [2,5,10]
  media1 = media(test1)
  print(f"La media della lista è {media1}")

  test2 = input("Inserisci dei numeri separati da virgole: ").strip()
  lista2 = converti_in_lista(test2)
  media2 = media(lista2)
  print(f"La media della lista è {media2}")
  return 0

if __name__ == "__main__":
  exit(main())
