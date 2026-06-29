'''
Scrivere un programma che, letta una stringa 'string' ed un carattere 'c'
da tastiera, restituisca la posizione dell'ultima occorrenza di 'c' in
'string', e -1 se 'c' non occorre in 'string'.

Organizzare il programma in opportune funzioni che effettuino il calcolo.
'''
import sys

def find_last_char(string, char):

  if type(char) is not str:
    raise TypeError("Il valore non è una stringa. Inserire una stringa.")

  if len(char) != 1:
    raise ValueError("Puoi inserire soltanto un carattere di ricerca: ")

  if char not in string:
    print(f"{char = } non appare nella {string = }")
    return -1

  else:
    last_idx = 0
    for idx, c in enumerate(string):
      if c in string:
        # assegno l'ultima posizione in cui appare c 
        last_idx = idx
    return last_idx


def main():
  string = input("Inserisci una stringa: ").strip()
  char = input("Inserisci un carattere di ricerca: ").strip()

  pos = find_last_char(string, char)
  if pos != -1:
    print(f"Ultima posizione di {char} è {pos}")

  return 0


if __name__ == "__main__":
  sys.exit(main())