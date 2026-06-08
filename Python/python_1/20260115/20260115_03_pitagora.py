"""
dati due cateti, calcolare l'ipotenusa
"""

"""
from math import sqrt

cat1 = int(input("Inserire cateto 1: "))
cat2 = int(input("Inserire cateto 2: "))

def calcola_ipo(cat1, cat2):
  return sqrt(cat1**2 + cat2**2)

ipo = calcola_ipo(cat1, cat2)

# print(f"L'ipotenusa del triangolo è: {ipo}")
"""

"""
Trovare se tra i numeri compresi tra 1 e 1000, per i cateti, ci sono altre terne pitagoriche, in cui cioè l'ipotenusa è un numero intero
"""
from math import sqrt

def calcola_ipo(cat1, cat2):
  return sqrt(cat1**2 + cat2**2)

gap = range(1, 1001)
num = 0
tern = []
consecutive_num = 0
cons_terns = []

# def get_terns(num, tern, gap):
for i in gap:
    for j in gap:  # j parte da i per evitare duplicati
        ipo = calcola_ipo(i, j)
        #if ipo.is_integer(): # oppure
        if ipo == int(ipo):
            num += 1
            tern.append((i, j, int(ipo))) # tutte le terne
            if i+1 == j: # se i due cateti sono consecutivi
              consecutive_num += 1
              cons_terns.append((i, j, ipo))

# Tutte le terne pitagoriche
print(tern)
print(f"Sono state trovate {num} terne pitagoriche")

# Tutte le terne con cateti consecutivi
print(cons_terns)
print(f"Sono state trovate {consecutive_num} terne con cateti consecutivi")
