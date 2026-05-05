s1 = set()

s1.add("Uno"); s1.add("Due"); s1.add("Tre"); s1.add("Quattro"); s1.add("Uno")

# L'ordine di inserimento non è garantito, ma ottimizzato per tempi di accesso
print(s1) # Esempio: {'Uno', 'Quattro', 'Due', 'Tre'}
# L'univocità è garantita in quanto ogni elemento è univoco. I doppioni non vengono inseriti

t1 = (1, 2, 3)
s1.add(t1) # Ogni volta che si aggiunge un elemento il set viene riorganizzato per efficienza
print(s1)  # {'Uno', 'Due', 'Quattro', (1, 2, 3), 'Tre'}

s2 = s1 | {"Cinque", "Nove", "Tre"}
print(s2)

"""
def string_ascii(stringa):
  ord_string = 0
  for c in stringa:
    ord_string += ord(c)
  return ord_string

stringa1 = string_ascii("Hello")
print(stringa1)
"""
