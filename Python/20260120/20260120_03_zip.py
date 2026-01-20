# metodo zip

insieme1 = ('tizio', 'caio', 'sempronio')
insieme2 = (1, 2, 3)
insieme3 = (True, False, 20, 30)
stringa1 = "ABCDEFG"
stringa2 = "1234567"

# Zip aggrega un elemento per volta tra diverse sequenze.

gigatupla = tuple(zip(insieme1, insieme2))
print(gigatupla)
# (('tizio', 1), ('caio', 2), ('sempronio', 3))

gigalista = list(zip(insieme1, insieme2, insieme3))
print(gigalista)
# [('tizio', 1, True), ('caio', 2, False), ('sempronio', 3, 20)]

gigaset = set(zip('abcdefg', range(3), range(4)))
print(gigaset)
# {('a', 0, 0), ('b', 1, 1), ('c', 2, 2)}

gigastring = str(zip(stringa1, stringa2))
print(gigastring) # Oggetto zip da convertire <zip object at 0x1022affc0>

stringona = str(list(gigastring))
print(stringona)

stringona = ', '.join([f"({a}, {b})" for a, b in zip(stringa1, stringa2)])
print(stringona)