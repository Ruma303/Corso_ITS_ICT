# Esercizio: fibonacci ricorsivo con dizionario

## Analisi del problema

Il codice dell'esercizio costruisce una soluzione ricorsiva che calcola la successione di Fibonacci memorizzando ogni valore intermedio in un dizionario globale (`fib_dict`). Ogni volta che viene calcolato un nuovo valore, questo viene aggiunto al dizionario con una nuova chiave.

- Input:
  - Il programma accetta un numero intero `n` come input, che rappresenta la posizione nella sequenza di Fibonacci.
  - Nella versione personale prende anche una variabile contatore `count` che parte da 2 (per accedere al terzo elemento del dizionario).
- Output: Il programma restituisce il valore di Fibonacci corrispondente alla posizione `n`.

- Criteri di accettazione:
  - La funzione deve essere implementata in modo ricorsivo.
  - La funzione deve accettare un numero intero `n` maggiore o uguale a 0.

## Descrizione tecnica

### Elementi iniziali

 - La funzione utilizza un dizionario per memorizzare i valori calcolati dinamicamente.
 - Il dizionario viene inizializzato con i primi tre valori della sequenza di Fibonacci: `fib_dict = {0: 1, 1: 1, 2: 1}`.

### Algoritmo della funzione ricorsiva

- La funzione gestisce i casi base per `n = 0` e `n = 1`. In questi casi restituirà 1, interrompendo la ricorsione.
- Nel caso ricorsivo, invece, calcola il valore di Fibonacci per `n` utilizzando i valori memorizzati nel dizionario.
- Nel farlo, vengono memorizzati dinamicamente l'ultimo e il penultimo valore calcolato nel dizionario, in modo da evitare calcoli ridondanti.
- Questi due valori vengono sommati per ottenere il nuovo valore di Fibonacci per `n`.
- Non resta che memorizzare questo nuovo valore nel dizionario:
  - Per memorizzare il nuovo valore nel dizionario, si utilizza la chiave e si assegna il valore calcolato.
  - La chiave corrisponde a `count`, che viene incrementata ad ogni chiamata ricorsiva.
- Avviene quindi la ricorsione chiamando la funzione stessa con `n - 1` e `count + 1` (già incrementato precedentemente per inserire il nuovo elemento nel dizionario).
- Infine, la funzione restituisce l'ultimo valore di Fibonacci per `n` prelevandolo dal dizionario.


```python
# Dizionario di partenza
fib_dict = {
    0: 0,
    1: 1,
    2: 1
}

count = 2

def Fib(N, count):

    # Casi base di uscita
    if N == 0 or N == 1:
        return 1

    else:
        prev1 = fib_dict[count] # Ultimo elemento del dizionario
        prev2 = fib_dict[count - 1] # Penultimo elemento

        # Somma dell'ultimo e penultimo elemento
        curr = prev1 + prev2

        # Aumentiamo il count per accedere al prossimo posto nel dizionario
        count += 1

        # Inserimento del nuovo elemento curr nel dizionario
        fib_dict[count] = curr

        # Ricorsione calcolando il prossimo Fibonacci (N - 1), count +1
        Fib(N - 1, count)

    # Ritorna l'ultimo elemento del dizionario
    return fib_dict[len(fib_dict) - 1]

print("Fib di 10: ", Fib(10, count))
print("Fib di 20: ", Fib(20, count))
print("Fib di 30: ", Fib(30, count))
print("Fib di 40: ", Fib(40, count))
print("Fib di 100: ", Fib(100, count))
print(fib_dict)
```