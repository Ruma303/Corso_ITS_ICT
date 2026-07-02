"""
Nome file: reverse_digits.py

Scrivere un programma che, dato un intero non negativo n,
stampa l'intero ottenuto invertendo l'ordine delle cifre di n.

Ad esempio, se n = 356, il programma stampa 653.

Se n termina con una o più cifre 0, queste non devono comparire
come cifre iniziali del risultato (es. n = 1200 -> 21).

L'inversione deve essere effettuata operando su n come intero,
senza convertirlo in stringa.
"""

from sys import exit


def num_digits(number: int) -> int:
    assert isinstance(number, int), (
        "Il valore non è un numero. Dev'essere un numero intero"
    )
    assert number >= 0, "Il numero dev'essere NON negativo"

    result = 0

    while True:
        result += 1
        number = number // 10  # Rimuove l'ultima cifra

        if not number:
            break

    return result


def reverse_digits(number: int) -> int:
    # Invariante: il numero è intero positivo

    len_digits = num_digits(number)
    assert len_digits > 1, "Il numero ha una sola cifra o nessuna. Non è invertibile."
    
    power = len_digits - 1
    # Se la lunghezza del numero iniziale è di 3 cifre (es in 356)
    # Quando ricostruirò il numer al contrario non posso
    # elevare ogni numero a potenze di 10 partendo da 3
    # perché 10 ** 3 = 1000. Mi troverei uno 0 in più.
    
    digit = 0
    result = 0
    copy_of_number = number  # evitiamo di consumare il numero

    while True:
        # 1. Estrarre l'ultima cifra
        digit = copy_of_number % 10
        # print(f"{digit = }")

        # 2. Moltiplicarla per 10 * numero cifre (che decrementa)
        curr_digit = digit * (10**power)
        power -= 1

        # 3. Sommare le cifre man mano
        result += curr_digit

        # 4. Togliere l'ultima cifra
        copy_of_number //= 10

        # 5. Se l'ultima cifra non c'è, uscire
        if not copy_of_number:
            break

    return result


def main() -> int:
    tests = [73639043, 356, 0]

    for test in tests:
        test_revert = reverse_digits(test)
        if test_revert == 1:
            print(f"Il numero {test} ha {test_revert} cifre, non è invertibile")
        else:
            print(f"Il numero {test} invertito è {test_revert}")

    return 0


if __name__ == "__main__":
    exit(main())
