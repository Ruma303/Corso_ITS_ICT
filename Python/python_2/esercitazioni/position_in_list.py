'''
Position in list

Scrivere un programma che, legge da input:
 - una lista 'l' di stringhe e
 - una singola stringa 's'

e scrive a schermo la posizione di 's' nella lista 'l'.

In particolare se 's' occorre (ovvero compare) nella lista 'l' scrive:

	f"La stringa {s} occorre in {l} alla posizione ..."

Se invece 's' non occorre nella lista 'l' scrive:

	f"La stringa {s} non occorre in {l}".

Organizzare il programma in opportune funzioni.
'''

def get_strings():
  """
  Legge una lista di stringhe da input e una stringa di ricerca.
  Restituisce la lista e la stringa.
  """
  result = []

  while True:
    string = input("Digita una stringa o premi invio per interrompere: ")

    if not string:
      break
    result.append(string)

  s = input("Scrivi la stringa di ricerca: ")
  if not s:
    raise ValueError("La stringa di ricerca non può essere vuota")

  return result, s


def find_in_list(lista, s, case_insensitive=False, remove_whitespaces=True):
  """
  Cerca la stringa s come elemento nella lista l.
  Stampa la posizione se presente; altrimenti segnala che non occorre.
  """

  if len(lista) <= 0:
    raise IndexError("La lista non può essere vuota!")

  # Condizioni progressive per flessibilità
  def normalize(val):
    res = val
    if remove_whitespaces:
      res = res.strip()

    if case_insensitive:
      res = res.lower()
    return res

  # Pre-elabora la stringa da cercare una volta sola
  s_norm = normalize(s)

  for i in range(len(lista)):
      el_norm = normalize(lista[i])
      # Confronto con le stringhe normalizzate nella lista
      if el_norm == s_norm:
          return f"La stringa {s} occorre in {lista} alla posizione {i}"

  return f"La stringa {s} non occorre in {lista}"


if __name__ == "__main__":
  lista, s = get_strings()

  # Ricerca base
  match1 = find_in_list(lista, s)
  print(match1)

  # Ricerca case-insensitive e senza spazi
  match2 = find_in_list(lista, s, case_insensitive=True, remove_whitespaces=True)
  print(match2)

  # Ricerca case-sensitive e con spazi ammessi
  match3 = find_in_list(lista, s, case_insensitive=False, remove_whitespaces=False)
  print(match3)

"""
Esempi:

Digita una stringa o premi invio per interrompere: una
Digita una stringa o premi invio per interrompere: ROSA .
Digita una stringa o premi invio per interrompere:  per
Digita una stringa o premi invio per interrompere: me
Digita una stringa o premi invio per interrompere:
Scrivi la stringa di ricerca: me
La stringa me occorre in ['una', 'ROSA . ', ' per ', 'me    '] alla posizione 3
La stringa me occorre in ['una', 'ROSA . ', ' per ', 'me    '] alla posizione 3
La stringa me non occorre in ['una', 'ROSA . ', ' per ', 'me    ']
"""