"""
Istruzioni
La serie numerica detta di Fibonacci è:
1 1 2 3 5 8 13 21 ...
dove ogni cifra, a partire dalla terza, è pari alla somma delle due cifre precedenti
Una caratteristica notevole della serie di Fibonacci è che il rapporto tra n-esimo elemento e n-1-esimo elemento tende al rapporto aureo

Un esempio ricorsivo per il calcolo della serie di Fibonacci è il seguente:
def Fib(N):
  if N == 0 or N == 1:
    return 1
  else:
    return Fib(N-1)+Fib(N-2)

Questa definizione funziona molto bene MA per N troppo grandi impiega un tempo enorme poiché ricalcola continuamente i valori di fibonacci per uno specifico valore.
Esempio: Fib(10) = Fib(9)+Fib(8)
ma Fib(9)=Fib(8)+Fib(7) e Fib(8) = Fib(7)+Fib(6)
come si vede da questo semplice esempio, per calcolare Fib(10), calcola due volte Fib(9), due volte Fib(8) , tre volte Fib(7), ecc.

Utilizzare un dizionario per archiviare i valori già calcolati e, rima di calcolare un nuovo valore, verificare se è già presente nel dizionario.

Verificare l'incremento di efficienza dell'algoritmo.
"""

fib_dict = {
    0: 0,
    1: 1,
    2: 1
}

count = 2

def Fib(N, count):

    if N == 0 or N == 1:
        return 1

    else:
        prev = fib_dict[count]
        prev2 = fib_dict[count - 1]
        curr = prev + prev2
        count += 1
        fib_dict[count] = curr
        Fib(N - 1, count)

    return fib_dict[len(fib_dict) - 1]


print("Fib di 10: ", Fib(10, count))
print("Fib di 20: ", Fib(20, count))
print("Fib di 30: ", Fib(30, count))
print("Fib di 40: ", Fib(40, count))
print("Fib di 100: ", Fib(100, count))
# print(fib_dict)