# Esercizio: parole palindrome

## Analisi del problema

- Input: Il programma accetta una stringa di caratteri come input.
- Output: Il programma ha diverse funzioni (versioni diverse del programma) che restituiscono un valore booleano. Questo valore verrà utilizzato per indicare se la stringa di input è una parola palindroma o meno.
- Criteri di accettazione:
  - Una parola palindroma è una parola che si legge allo stesso modo da sinistra a destra e da destra a sinistra.
  - Esempi di parole palindrome: "anna", "osso", "radar", "level".
  - Esempi di parole non palindrome: "ciao", "python", "esempio".
  - Il programma accetta qualsiasi stringa di caratteri come input, inclusi spazi e punteggiatura. Questi verranno rimossi con metodi di sanitizzazione offerti da Python.

Esempi di sanitizzazione:

```python
# Frase da test
frase_test_1 = "I topi non avevano nipoti"

# Sanitizzazione della frase
frase_test_1_validated = frase_test_1.strip().lower().replace(" ", "").replace("'", "")
```

i metodi di sanitizzazione utilizzati sono:
- `strip()`: rimuove gli spazi vuoti all'inizio e alla fine
- `lower()`: converte tutti i caratteri in minuscolo
- `replace(" ", "")`: rimuove tutti gli spazi all'interno della string
- `replace("'", "")`: rimuove gli apostrofi singoli all'interno della stringa

### Terminologia

Il termine “sanitizzazione” è frequentemente utilizzato nel contesto informatico per indicare l’insieme delle operazioni volte a ripulire o modificare dati in ingresso, eliminando o trasformando caratteri o elementi potenzialmente pericolosi.
L’azione di sanitizzare riguarda tipicamente l’input utente per proteggerlo da rischi come iniezioni di codice (ad esempio SQL injection, XSS) o per adeguarlo a uno standard elencato.

## Nota sulla sanitizzazione

- Per scelta progettuale, la sanitizzazione viene effettuata esternamente alla funzione, in modo da avere un algoritmo che verifica esclusivamente se la parola è palindroma.
- In questo modo, la funzione può essere riutilizzata in altri contesti senza dover ripetere la sanitizzazione ogni volta.
- Un ulteriore miglioramento potrebbe essere quello di includere la sanitizzazione all'interno della funzione stessa, ma per semplicità in questo esercizio è stata evitata questa complessità aggiuntiva. Sarebbe meglio definire una funzione di sanitizzazione separata.

## Scelta della tecnica

### Funzione Versione 1: Utilizzo di slicing
Questa versione utilizza lo slicing delle stringhe di Python per confrontare la stringa originale con la sua versione invertita utilizzando l'operatore di slicing `[::-1]`.

Questa tecnica è molto concisa e sfrutta le funzionalità integrate di Python per manipolare le stringhe in modo efficiente. Tuttavia, l'utilizzo dello slicing può essere meno intuitivo per chi non ha familiarità con questa sintassi. Inoltre, questo operatore non è disponibile in tutti i linguaggi di programmazione, quindi questa soluzione è specifica per Python.

Per questo motivo è stata implementata una seconda versione che utilizza un approccio algoritmico più generale e riutilizzabile in ogni linguaggio.

### Funzione Versione 2: Verifica con due puntatori
Questa versione utilizza due puntatori: uno che parte dall'inizio della stringa e l'altro che parte dalla fine della stringa. I due puntatori si muovono verso il centro della stringa, confrontando i caratteri corrispondenti. Se i caratteri non corrispondono, la funzione restituisce `False`. Se i puntatori si incontrano o si superano senza trovare differenze, la funzione restituisce `True`.

```python
def check_palindrome_v2(phrase):
  n = len(phrase)
  for i in range(n // 2):
    print("Verifica: ", phrase[i], phrase[n - i - 1])
    if phrase[i] != phrase[n - i - 1]:
      return False
  return True
```

### Esempio di confronti in entrambe le versioni

```
I topi non avevano nipoti

Verifica:  i i
Verifica:  t t
Verifica:  o o
Verifica:  p p
Verifica:  i i
Verifica:  n n
Verifica:  o o
Verifica:  n n
Verifica:  a a
Verifica:  v v
```