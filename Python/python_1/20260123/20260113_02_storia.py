"""
lista = [3, 4, 1, 5, 5, 2, 9, 7, 7, 8, 9, 10]
n = 0
curr = lista[n]
prev = lista[n - 1]
sorted = True

for i in lista:
  if curr > prev:
    sorted = False
    break
  prev = curr

if sorted:
  print(f"Lista ordinata: {lista}")
"""

# Oppure con for-else

# Trovare i picchi in una lista
# Un picco è un numero che è circondato da due numeri più piccoli
# Uno che lo precede, e uno che lo segue

from random import randint

lista2 = [randint(1, 1001) for _ in range(1000)]

"""
lista_picchi = []
for i in range(1, len(lista2) - 1):
    prev = lista2[i - 1]
    curr = lista2[i]
    next = lista2[i + 1]
    if curr > prev and curr > next:
        lista_picchi.append(curr)
print(f"Lista picchi: {lista_picchi}")
"""

# Oppure con list comprehension
lista_picchi2 = [(lista2[i-1], lista2[i], lista2[i+1])  for i in range(1, len(lista2) - 1) if lista2[i] > lista2[i-1] and lista2[i] > lista2[i+1]]

print(f"Lista picchi 2: {lista_picchi2}")
print(f"Numero lista picchi 2: {len(lista_picchi2)}")


# picchi sarà una lista di tuple (indice, valore)

"""
O ancora, basta conoscere soltanto i primi due numeri
"""

"""
picchi = 0
if len(lista2) <= 2:
  print("La lista ha due o meno elementi")
else:
  curr = lista2[1]
  prev = lista2[0]

  for next in lista2[2:]:
    if curr > prev and curr > next:
      print(prev, curr, next)
      picchi += 1
    prev = curr
    curr = next

print(f"Versione 3, Numero di picchi: {picchi}")
"""