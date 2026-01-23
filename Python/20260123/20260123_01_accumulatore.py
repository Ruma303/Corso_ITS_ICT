# Creare una lista di 1000 numeri interi casuali compresi tra 67 e 135


from random import randint

lista1 = []

for _ in range(1001):
  lista1.append(randint(67, 136))
print("\nLista numeri random\n")
print(lista1)


# Costruire una nuova lista contenente esclusivamente i numeri pari presenti nella lista appena formata

# Esempio con le list comprehension
"""
Sintassi minima:
[ espressione for elemento in collezione ]

è possibile anche aggiungere condizioni alla fine:
[ espressione for elemento in collezione if condizione]

L'espressione indica di che natura sarà l'elemento, e può anche fare operazioni su di esso

"""


lista_pari = [ele for ele in lista1 if ele % 2 == 0]
print("\nLista pari\n")
print(lista_pari)

lista_random = [randint(67, 136) for _ in range(1000)]
print("\nLista pari comprehension\n")
print(lista_random)

lista_dispari_quadrato = [ele**2 for ele in lista1 if ele % 2 != 0]
print("\nLista dispari al quadrato comprehension\n")
print(lista_dispari_quadrato)