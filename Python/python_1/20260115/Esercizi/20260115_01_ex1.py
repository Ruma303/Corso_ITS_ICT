"""
Sia dato un piano cartesiano e due punti su di esso
p1=(30, 40)
p2=(27, 89)
Si ricordi che il primo elemento della coppia è la posizione sull'asse x del punto e il secondo elemento della coppia è la posizione sull'asse y del punto
Calcolare la distanza euclidea tra i due punti
"""

from math import sqrt

p1=(30, 40)
p2=(27, 89)

p1x= p1[0]
p2x= p2[0]
p1y= p1[1]
p2y= p2[1]

# Versione 1: come ipotenusa
ipo = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
print(ipo)

# Versione 2: formula della distanza euclidea
distanza_euclidea = sqrt(abs(p1x - p2x)**2 + abs(p1y -p2y)**2)
print(distanza_euclidea)