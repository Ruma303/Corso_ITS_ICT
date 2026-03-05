'''
Scrivere un programma che legge da tastiera una sequenza di righe
(terminando quando legge la riga vuota) e stampa ogni riga letta in verticale,
una accanto all'altra (separate da spazi singoli), nello stesso ordine.

Ad esempio, se l'utente inserisce:

Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
(riga vuota)

allora il programma stamperà:

N m c
e i h
l   é
  r
m i l
e t a
z o
z v d
o a i
  i r
d   i
e p t
l e t
  r a
c
a u v
m n i
m a a
i
n s e
  e r
d l a
i v
  a s
n   m
o o a
s s r
t c r
r u i
a r t
  a a
v , .
i
t
a

Organizzare il programma in opportune funzioni.
'''

"""
phrase = input("Inserisci una frase. Metti una riga vuota per uscire")


"""

phrase = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura,
ché la diritta via era smarrita.

"""

def to_list():
    rows = []
    last_char = 0

    for i, char in enumerate(phrase):
        if char == "\n":
            # Preleva la sottostringa tra i newlines esclusi
            new_phrase = phrase[last_char:i]
            # Elimina eventuali newlines residui (per sicurezza)
            new_phrase = new_phrase.replace("\n", "")
            # Se non vuota, aggiungila
            if new_phrase.strip() != "":
                rows.append(new_phrase)
            last_char = i + 1  # Riparti subito dopo il newline

    # Gestisci la coda se il testo non termina con un newline
    if last_char < len(phrase):
        final_row = phrase[last_char:].replace("\n", "")
        if final_row.strip() != "":
            rows.append(final_row)
    return rows


"""
rows è
[
  'Nel mezzo del cammin di nostra vita',
  'mi ritrovai per una selva oscura,',
  'ché la diritta via era smarrita.',
]
"""

def transpose_v(rows):
  result = ""
  col = 0
  max_len = 0

  for row in rows:
    if len(row) > max_len:
      max_len = len(row)

  # Ciclare sulle colonne
  while col < max_len:

    new_row = ""

    try:

      # Iterazione sulle righe
      for row in rows:
        new_row += row[col] + " "

    except IndexError, Exception:
      new_row += " "

    result += new_row + "\n"
    new_row = ""
    col += 1

  return result

def main():
  rows = to_list()
  transposed_phrase = transpose_v(rows)
  print(transposed_phrase)
  return 0

import sys

if __name__ == "__main__":
  sys.exit(main())
