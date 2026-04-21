"""
Insertion sort 1

Scrivere un programma che legge una lista 'list' di interi e ne
calcola il suo ordinamento (in ordine crescente).

Sebbene Python offra già questa funzionalità (funzione sorted()),
in questo esercizio si richiede di sviluppare esplicitamente
l'algoritmo di ordinamento chiamato "insertion sort".

L'algoritmo "insertion sort" funziona in questo modo.

1. Si crea una lista 'risultato', inizialmente vuota.
2. Si considerano, in ordine, tutti gli elementi della lista in input
('list') e si inserisce ognuno di essi nella posizione corretta in 'risultato'.

Ad esempio, supponiamo che l'utente dia in input:
        list = [5, 2, 7, 3]

L'algoritmo si comporterebbe nel modo seguente:

Passo 1: risultato = [] (lista vuota).

Passo 2: si considera list[0] = 5 e lo si inserisce nella posizione corretta
                 in 'risultato'. A questo punto risultato = [5].

Passo 3: si considera list[1] = 2 e lo inserisce nella posizione corretta
                 in 'risultato'. A questo punto risultato = [2, 5].

Passo 4: si considera list[2] = 7 e lo inserisce nella posizione corretta
                 in 'risultato'. A questo punto risultato = [2, 5, 7].

Passo 5: si considera list[3] = 3 e lo inserisce nella posizione corretta
                 in 'risultato'. A questo punto risultato = [2, 3, 5, 7].

"""

from sys import exit


def insertion_sort(lista: list[int]) -> list[int]:
    result: list[int] = []

    # TODO: Completa
    for idx, ele in enumerate(lista):
        result.append(ele)
        # Ultima posizione
        j = len(result) - 1

        while j > 0 and result[j] < result[j - 1]:
            temp = result[j]
            result[j] = result[j - 1]
            result[j - 1] = temp

            # Spostamento a sinistra per verificare se
            # result[j] è ancora minore in altre posizioni

            j -= 1  # Errore di indentazione intenzionale.
            # Da aggiustare con formattatori

    return result


def main() -> int:
    test1 = [5, 2, 7, 3]
    result = insertion_sort(test1)
    print(result)
    return 0


if __name__ == "__main__":
    exit(main())
