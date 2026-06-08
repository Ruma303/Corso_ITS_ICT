"""
Leggere una sequenza di numeri utilizzando la forma
while True:
       # qui le istruzioni di lettura ...
1) Per ogni numero stampare se è pari o se è dispari
2) stampare il valor medio dei valori letti finora
"""

numeri = [1, 5, 6, 743, 2, 45, 7, 7356, 8, 845, 34, 256, 7, 84]
# numeri = [1, 2, 3]
posizione = 0
somma = 0.0

while True:
    if posizione >= len(numeri):
        break

    valore = numeri[posizione]

    if valore % 2 == 0:
        print(f"{valore} è pari")
    else:
        print(f"{valore} è dispari")

    somma += valore

    if posizione > 0:
        media = somma / (posizione + 1)
        print(f"Media finora ({posizione + 1} valori): {media}")

    posizione += 1

print(f"Media finale su {len(numeri)} valori: {media}")
