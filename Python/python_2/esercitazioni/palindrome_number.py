"""
Nome file: palindrome_number.py

Scrivere un programma che, dato un intero non negativo n,
stampa True se n è palindromo (cioè si legge allo stesso modo
da sinistra a destra e da destra a sinistra), False altrimenti.

Ad esempio, se n = 12321, il programma stampa True;
se n = 1234, il programma stampa False.

La verifica deve essere effettuata operando su n come intero
(ad esempio confrontando n con il suo inverso, calcolato
esclusivamente tramite operazioni aritmetiche), senza convertire
n in stringa.

Un numero con un'unica cifra è palindromo per definizione, ma in questo
esercizio il vincolo è che vi siano almeno due cifre uguali per 
poter dire che il numero è palindromo.

BONUS: l'algoritmo NON DEVE RIMUOVERE le cifre iniziali e finali mentre si sposta
verso l'interno per eseguire i confronti. Deve solo spostarsi di cifra in cifra
senza modificarle.
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
        number = number // 10
        if not number:
            break

    return result


def get_digit_at(number: int, pos: int) -> int:
    """A partire da un numero intero, ottiene la cifra alla posizione indicata"""
    
    # INFO: Il valore non viene consumato in quanto non è riassegnato
    # Es: number = 75357, pos = 2
    # 10 ** 2 = 100
    # 75357 // 100 = 753 (tronca le ultime due cifre)
    # 753 % 10 prende solo l'ultima cifra, restituendo il resto = 3

    return (number // (10 ** pos)) % 10


def palindrome_number_1(number: int) -> bool:
    assert (len_digits := num_digits(number)) > 1, "Il numero deve avere almeno 2 cifre"

    # INFO: non possiamo verificare i valori dei singoli numeri.
    # Verificando 746, il primo numero 7 è > di 6, quindi il ciclo terminerebbe
    # Bisogna verificare le posizioni con degli indici, come qualsiasi iterabile

    i = 0
    while i < len_digits - 1 - i:
      
        left  = get_digit_at(number, len_digits - 1 - i)
        right = get_digit_at(number, i)

        if left != right:
            return False
        i += 1
            
    return True


def main() -> int:
    tests = [75357, 73639043, 666, 32, 22, 343]
    # print(get_digit_at(tests[0], 2))

    for test in tests:
      # Controlli centralizzati nel chiamante
      assert isinstance(test, int), (
          "Il valore non è un numero. Dev'essere un numero intero"
      )
      assert test >= 0, "Il numero dev'essere NON negativo"

      if palindrome_number_1(test):
          print(f"\nIl numero {test} è palindromo")
      else:
          print(f"\nIl numero {test} NON è palindromo")

    return 0


if __name__ == "__main__":
    exit(main())
