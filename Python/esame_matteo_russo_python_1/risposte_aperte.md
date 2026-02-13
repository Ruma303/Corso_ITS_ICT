# Domande aperte

## 1. Strutture dati
Differenze tra le principali strutture dati composte in Python sono:
1. Una lista è un dato che può contenere molteplici dati di ogni natura. La sua particolarità sta nel fatto che la lista è completamente modificabile; ogni elemento può essere riassegnato, cambiare di tipo, essere rimosso.
2. Una tupla è una struttura dati molto simile ad una lista ma ha la particolarità di essere immutabile. Gli elementi interni, una volta assegnati, non possono essere modificati. È possibile comunque cambiare una tupla in una lista, modificare la lista, poi riconvertirla in una tupla.
3. Un set è un dato composto che contiene un insieme di dati distinti. L'inserimento di dati duplicati viene ignorato senza lanciare errori.
4. Un dizionario è un dato composto dove i dati sono indicizzati per mezzo di una chiave. Mentre tutti gli altri dati composti precedenti potevano essere acceduti tramite indice numerico [n], i valori dei dizionari possono essere acceduti esclusivamente tramite la loro chiave (intera o stringa).
  - Esempio dizionario['nome_chiave'].
  - L'inserimento di più chiavi identiche viene ignorato. Ogni chiave dev'essere distinta. Ciò che cambia è il valore interno che viene riassegnato.
  - I dizionari sono particolarmente efficienti in quanto la ricerca non è lineare ma utilizza una funzione di ricerca più avanzata. Questo consente una ricerca lineare estremamente veloce O(1)
  - Le chiavi vengono hashate tramite una funzione di hashing. Ciò rende più difficile eventuali collisioni tra nomi delle chiavi.
  - L'ordine delle chiavi dei dizionari non è garantito. Inserire ad esempio dizionario['uno'], dizionario['due'], non garantisce l'ordine alfabetico. In realtà, da Python 3.7 l'ordine è garantito.

### Scenari di utilizzo
1. Liste: insiemi di valori che devono essere manipolabili, esempio per tenere traccia di coordinate di un percorso che vengono costantemente modificate.
2. Tuple: insiemi di valori immutabili, fondamentali per record e logging di operazioni fatte da server (web server, application server, database, accessi ai sistemi) e scoprire eventuali vulnerabilità o accessi non autorizzati.
3. Set: insieme di valori distinti, come le materie di un corso scolastico.
4. Dizionari: insiemi di valori mappati chiave-valore, fondamentali per profilazione di persone con tutti i loro dati personali, ma anche per creare delle API in formato JSON o YAML.

## 2. Controllo di flusso
- Il ciclo for in Python può essere utilizzato esclusivamente su un oggetto iterabile (stringhe, liste, dizionari, range, etc.).
- I ciclo for è un ciclo finito dove sappiamo qual è l'iterazione iniziale e quella finale, diversamente dal ciclo while che, se non gestito correttamente, rischia di iterare all'infinito.
- La funzione range() in Python è un generatore, una funzione particolare che genera dei numeri quando richiesti. In particolare, la funzione range infine ritorna una lista di numeri interi. Può prendere diversi parametri:
1. inizio (opzionale): se non indicato la funzione partirà dal valore 0 INCLUSIVO
2. fine: numero intero obbligatorio ESCLUSIVO.
3. step (opzionale): indica lo spostamento tra i numeri.

Esempi:
- range(4): [0, 1, 2, 3]
- range(3, 5): [3, 4]
- range(2, 6, 2): [2, 4]

## 3. Modularità
- L'utilizzo delle funzioni diventa fondamentale per ridurre la ridondanza del codice. Lo scopo delle funzioni è quello di definire un algoritmo una sola volta e riutilizzarlo invocando la funzione quando serve, generalmente con argomenti diversi.
- Un "parametro" è una variabile che viene creata quando la funzione viene chiamata. Esiste esclusivamente all'interno della funzione (function scope) e non può essere utilizzato esternamente, si può ritornare esclusivamente il suo valore se serve.
- Un parametro diventa utile quando il suo valore può essere assegnato da un'altra variabile all'esterno della funzione. Questo viene passato come "argomento" della funzione, assegnato al parametro e poi utilizzato all'interno della funzione.
- Le funzioni in realtà si dividono in funzioni e procedure.
    - Le procedure sono blocchi di codice che non ritornano valori ma eseguono altre operazioni (banalmente, eseguire dei print nella funzione), ma alla fine la funzione non ritorna alcun valore. In Python, funzioni che non ritornano esplicitamente valori ritorneranno il tipo di dato NoneType, con valore None.
    - Le funzioni vere e proprie sono blocchi di codice riutilizzabili che ritornano dei valori. Questo viene eseguito in Python utilizzando la keyword "return" seguito dal / dai valori che vogliamo ritornare.

## 4. Gestione delle eccezioni
I blocchi try except gestiscono delle eccezioni che possono capitare runtime, quando il programma è in esecuzione. Se non gestite, queste eccezioni si propagano salendo in maniera gerarchica fino a lanciare un'eccezione della classe Except (se non gestite prima) e comportano l'interruzione del programma.

L'utilizzo del costrutto try except consente di gestire l'eccezione runtime senza interrompere il programma.

Esempio, divisione aritmetica per 0:

try:
  num = int(input("Inserisci un numero intero: ").strip())
  ris = num / 0 # Genera un errore

except AritmeticError as err:
  print("Non è possibile dividere un numero intero per 0", err)

Senza il blocco try except il programma si sarebbe interrotto, mentre con questo codice gestiamo l'eccezione (che in questo caso è un eccezione aritmetica), lanciando solo un messaggio personalizzato al client. Il programma potrà proseguire nella sua esecuzione.