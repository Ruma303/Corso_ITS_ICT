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
import time

print("Fibonacci ottimizzato tramite dizionario")

# Dizionari iniziale
fib_cache = {0: 1, 1: 1}

def fib(N):
    # Evitiamo di calcolare Fibonacci di un numero
    # se già presente nel dizionario
    if N in fib_cache:
        return fib_cache[N]

    # Calcolo nuovo fibonacci del numero N
    # con la somma dei due precedenti
    fib_cache[N] = fib(N - 1) + fib(N - 2)
    return fib_cache[N]

# Test di vari valori di fibonacci
for N in (10, 20, 30, 40, 50, 100):
    # Misurazione tempo tramite il modulo time
    start = time.perf_counter()
    value = fib(N)
    duration = time.perf_counter() - start
    print(f"fib({N}) = {value}, tempo calcolo: {duration:.8f} secondi")


"""
Fibonacci ottimizzato tramite dizionario
fib(10) = 89, tempo calcolo: 0.00000520 secondi
fib(20) = 10946, tempo calcolo: 0.00000430 secondi
fib(30) = 1346269, tempo calcolo: 0.00000530 secondi
fib(40) = 165580141, tempo calcolo: 0.00000310 secondi
fib(50) = 20365011074, tempo calcolo: 0.00000570 secondi
fib(100) = 573147844013817084101, tempo calcolo: 0.00001390 secondi
"""

print("Fibonacci tradizionale non ottimizzato")

def Fib(N):
  if N == 0 or N == 1:
    return 1
  else:
    return Fib(N-1)+Fib(N-2)

# Test di vari valori di fibonacci
for N in (10, 20, 30, 40):
    # Misurazione tempo tramite il modulo time
    start = time.perf_counter()
    value = Fib(N)
    duration = time.perf_counter() - start
    print(f"Fib({N}) = {value}, tempo calcolo: {duration:.8f} secondi")


"""
Fib(10) = 89, tempo calcolo: 0.00001740 secondi
Fib(20) = 10946, tempo calcolo: 0.00080990 secondi
Fib(30) = 1346269, tempo calcolo: 0.10199260 secondi
Fib(40) = 165580141, tempo calcolo: 27.92206450 secondi
"""