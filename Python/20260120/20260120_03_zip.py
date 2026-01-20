# metodo zip

insieme1 = ('tizio', 'caio', 'sempronio', 'Marco')
insieme2 = (1, 2, 3)
insieme3 = (True, False, False)

# Zip aggrega un elemento per volta tra diverse sequenze.

gigatupla = tuple(zip(insieme1, insieme2, insieme3))

print(gigatupla)

gigalista = list(zip(insieme1, insieme2, insieme3))

print(gigalista)


# Altri parametri di zip