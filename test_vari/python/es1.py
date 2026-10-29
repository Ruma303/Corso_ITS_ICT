"""
Scrivere una funzione che presa una lista di numeri, trova in un unico passaggio il massimo, minimo e medio, e li restituisca insieme.
"""

lista1 = [20, -3, 15, 72, 0]


def main(lista):
    massimo: int = lista[0]
    minimo: int = lista[0]
    media: float

    somma = 0
    numeri = len(lista1)

    contatore = 0
    while contatore < numeri:
        if lista[contatore] > massimo:
            massimo = lista[contatore]

        # trovare il minimo
        if lista[contatore] < minimo:
            minimo = lista[contatore]

        # sommare tutti i numeri in somma
        somma += lista[contatore]

        # incrementare numeri
        #numeri += 1

        contatore += 1

    if numeri == 0:
        raise ArithmeticError("Non puoi dividere per 0")
    media = somma / numeri

    return (massimo, minimo, media)

    # # trova in un unico passaggio il massimo, minimo e medio
    # for n in lista:
    #     # trovare il massimo
    #     if n > massimo:
    #         massimo = n

    #     # trovare il minimo
    #     if n < minimo:
    #         minimo = n

    #     # sommare tutti i numeri in somma
    #     somma += n

    #     # incrementare numeri
    #     numeri += 1

    # if numeri == 0:
    #     raise ArithmeticError("Non puoi dividere per 0")
    # media = somma / numeri

    # return (massimo, minimo, media)


print(main(lista1))
