# Esercizio: fibonacci ricorsivo con dizionario

## Analisi del problema

Il codice dell'esercizio costruisce una soluzione ricorsiva che calcola la successione di Fibonacci memorizzando ogni valore intermedio in un dizionario globale (`fib_cache`). Ogni volta che viene calcolato un nuovo valore, questo viene aggiunto al dizionario con una nuova chiave.

- Input: un numero intero `N` che rappresenta la posizione nella sequenza di Fibonacci.
- Output: il valore di Fibonacci corrispondente alla posizione `N`.
- Criteri di accettazione: la funzione deve restituire il valore corretto di Fibonacci per qualsiasi `N` non negativo, utilizzando un dizionario per memorizzare i valori calcolati.


## Descrizione tecnica

### Elementi iniziali

 - La funzione utilizza un dizionario per memorizzare i valori calcolati dinamicamente.
 - Il dizionario viene inizializzato con i primi tre valori della sequenza di Fibonacci: `fib_cache = {0: 1, 1: 1}`.

### Algoritmo della funzione ricorsiva

- La funzione gestisce automaticamente i casi base per `n = 0` e `n = 1` in quanto già presenti nel dizionario. In questi casi, la funzione restituisce semplicemente `1`.
- Se il valore non è presente nel dizionario, il programma calcola il valore di Fibonacci per `n` calcolando la somma dell'ultimo valore `n - 1` e il penultimo `n - 2` .
- Infine, la funzione restituisce l'ultimo valore di Fibonacci salvato prelevandolo dal dizionario.

## Codice della soluzione

Nel codice seguente è implementata la soluzione descritta:
- per mostrare l'efficacia dell'algoritmo ottimizzato, viene confrontato con una versione tradizionale non ottimizzata della funzione di Fibonacci.
- vengono misurati i tempi di esecuzione per entrambi gli approcci utilizzando il modulo `time`.

```python
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
```