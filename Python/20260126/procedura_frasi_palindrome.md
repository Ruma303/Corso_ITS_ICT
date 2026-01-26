# Esercizio: parole palindrome

## Analisi del problema

- Input: Il programma accetta una stringa di caratteri come input.
- Output: Il programma ha diverse funzioni (versioni diverse del programma) che restituiscono un valore booleano. Questo valore verrà utilizzato per indicare se la stringa di input è una parola palindroma o meno.
- Criteri di accettazione:
  - Una parola palindroma è una parola che si legge allo stesso modo da sinistra a destra e da destra a sinistra.
  - Esempi di parole palindrome: "anna", "osso", "radar", "level".
  - Esempi di parole non palindrome: "ciao", "python", "esempio".
  - Il programma accetta qualsiasi stringa di caratteri come input, inclusi spazi e punteggiatura. Questi verranno rimossi con metodi di sanitizzazione offerti da Python.

Esempi:

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

## Nota sulla sanitizzazione

- Per scelta progettuale, la sanitizzazione viene effettuata esternamente alla funzione che verifica se la parola è palindroma o meno. In questo modo, la funzione può essere riutilizzata in altri contesti senza dover ripetere la sanitizzazione ogni volta.
- Un'ulteriore miglioramento potrebbe essere quello di includere la sanitizzazione all'interno della funzione stessa, ma per semplicità in questo esercizio è stata evitata questa complessità aggiuntiva.
- Inoltre, la sanitizzazione potrebbe essere facilmente implementabile in ulteriori metodi custom, ma per brevità si è scelto di eseguire la sanitizzazione sulla stringa inline.

## Scelta della tecnica

### Funzione Versione 1: Utilizzo di slicing
Questa versione utilizza lo slicing delle stringhe per confrontare la stringa originale con la sua versione invertita utilizzando l'operatore di slicing `[::-1]`.

Questa tecnica è molto concisa e sfrutta le funzionalità integrate di Python per manipolare le stringhe in modo efficiente. Tuttavia, l'utilizzo dello slicing può essere meno intuitivo per chi non ha familiarità con questa sintassi. Inoltre, questo operatore non è disponibile in tutti i linguaggi di programmazione, quindi questa soluzione è specifica per Python.

Per questo motivo è stata implementata una seconda funzione che utilizza un approccio algoritmico più generale.

### Funzione Versione 2: Algoritmo iterativo

#### Inizializzazione e parametri di ingresso
- La funzione prende in ingresso una stringa già validata e sanitizzata (caratteri speciali rimossi, tutto in minuscolo).
- Il confronto avviene su due liste. Sarà quindi necessario convertire la stringa in una lista di caratteri, in modo da poter accedere facilmente ai singoli caratteri ed utilizzare eventualmente metodi delle liste.
- Viene inizializzata una lista vuota `test` che conterrà i caratteri della stringa di input ma al contrario.
- Viene inizializzata una variabile booleana `is_palindrome` a `False`, che presuppone che la parola non sia palindroma fino a prova contraria.

#### Primo ciclo: costruzione della lista invertita
- Si utilizza un ciclo `for` per iterare sugli indici della stringa di input, partendo dall'ultimo indice fino al primo.
- Tra le numerose tecniche offerte in Python, viene utilizzato il metodo `enumerate()` che fornisce un contatore automatico insieme agli elementi della stringa.
- L'indice `i` viene utilizzato per calcolare l'indice dell'elemento da prelevare dalla lista originale, partendo dall'ultimo elemento e procedendo verso il primo.

```python
for i, _ in enumerate(phrase):
    # Rimuovo ogni elemento dall'ultimo e lo inserisco in test
    ele = phrase_list[len(phrase) -1 - i] # Ultimo elemento
    # Oppure, usando il metodo pop()
    test.append(ele)
```

- Notare che per accedere all'ultimo elemento della lista si possono utilizzare:
  - il metodo `pop()` che rimuove e restituisce l'ultimo elemento della lista. Questo però è specifico di Python e non è applicabile in tutti i linguaggi di programmazione.
  - l'indicizzazione negativa, ad esempio `phrase_list[len(phrase) -1 - i]` per ottenere l'elemento desiderato. Questo è calcolato sfruttando la lunghezza della lista - 1 (per l'ultimo indice) meno l'indice `i` del ciclo.
  - Ad esempio, per la stringa "anna":
    - Quando `i = 0`, si preleva l'elemento in posizione `4 - 1 - 0 = 3` (ultimo elemento 'a').
    - Quando `i = 1`, si preleva l'elemento in posizione `4 - 1 - 1 = 2` (secondo elemento 'n').
    - Quando `i = 2`, si preleva l'elemento in posizione `4 - 1 - 2 = 1` (terzo elemento 'n').
    - Quando `i = 3`, si preleva l'elemento in posizione `4 - 1 - 3 = 0` (primo elemento 'a').

#### Secondo ciclo: confronto delle liste
Una volta costruita la lista invertita `test`, si procede al confronto con la lista originale `phrase_list`.

- Si utilizza un doppio ciclo `for` per confrontare ogni elemento della lista originale con ogni elemento della lista invertita.
- Se gli elementi corrispondenti sono uguali, la variabile `is_palindrome` viene impostata a `True`.
- Se viene trovato un elemento che non corrisponde, `is_palindrome` viene impostata a `False`.

```python
for i, _ in enumerate(phrase_list):
    for j, _ in enumerate(test):
      if phrase_list[i] == test[j]:
        is_palindrome = True
      else:
        is_palindrome = False
```

#### Conclusione
Al termine del confronto, la funzione restituisce il valore della variabile `is_palindrome`, che indica se la parola è palindroma o meno.

```python
if is_palindrome:
    return True
  else:
    return False
```

## Implementazione delle funzioni
Entrambe le versioni hanno lo stesso tipo di implementazione:

```python
t1v1 = check_palindrome(frase_test_1_validated)
if t1v1 == True: print(f"La frase {frase_test_1} è palindroma")
else: print(f"La frase {frase_test_1} non è palindroma")
```

### Esempi di input e output

#### Versione 1: Utilizzo di slicing
La frase I topi non avevano nipoti è palindroma
La frase Amo Roma è palindroma
La frase Ai lati d'Italia è palindroma
La frase E la sete sale è palindroma

#### Versione 2: Algoritmo iterativo
La frase I topi non avevano nipoti è palindroma
La frase Amo Roma è palindroma
La frase Ai lati d'Italia è palindroma
La frase E la sete sale è palindroma