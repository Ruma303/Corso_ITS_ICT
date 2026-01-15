"""
Scrivere una funzione con un parametro di tipo stringa
la funzione deve tornare la lettera più frequente nella stringa e il numero di occorrenze
Esempio: Realizzare => a è la più frequente e la sua frequenza è occorre 2 volte. Quindi la funzione torna
return carattere, occorrenze
"""

# Versione 1 senza count ma con dizionario
"""
def most_present_char(word):

  if not word:
    return None, 0

  frequency = {}
  for char in word:
    # Somma +1 ogni carattere trovato. Es: Precipitevolissimevolmente
    # Il dizionario inizializzato sarà:
    # 1 1 1 1 1 1 2 1 2 1 1 1 3 1 2 4 1 3 2 2 2 2 4 1 2 5
    frequency[char] = frequency.get(char, 0) + 1

  max_char = None
  max_count = 0

  for char in word:
    count = frequency[char]
    if count > max_count:
      max_char = char
      max_count = count

  return max_char, max_count

char, num = most_present_char("Precipitevolissimevolmente")
print(f"La lettera {char} è presente più volte: {num}")

char, num = most_present_char(input("Inserisci una parola: "))
print(f"La lettera {char} è presente più volte: {num}")
"""

# Versione 2 con count
"""
def word_count(word):
    max_num = 0
    max_char = None

    for char in word:
        occurrences = word.count(char)
        if occurrences > max_num:
            max_num = occurrences
            max_char = char

    return max_char, max_num

char, num = word_count("Precipitevolissimevolmente")

print(f"La lettera '{char}' è presente più volte: {num}")

char, num = word_count(input("Inserisci una parola: "))
print(f"La lettera {char} è presente più volte: {num}")
"""

# Versione 3 senza count e dizionari
"""
def double_for(word):
    max_num = 0
    max_char = None

    for char in word:
        num = 0
        for c in word:
          if c == char:
            num += 1
            max_num = num
            max_char = c

    return max_char, max_num

char, num = double_for("Precipitevolissimevolmente")
print(f"La lettera '{char}' è presente più volte: {num}")
"""