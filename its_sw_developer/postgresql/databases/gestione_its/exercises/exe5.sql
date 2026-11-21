-- 20261119

/* Esercizio 1

Visualizzare:
• matricola
• nome
• cognome
• corso frequentato

degli studenti che soddisfano contemporaneamente le seguenti condizioni:
• iscritti ai corsi:
o Full Stack Developer
o Data Analyst
• cognome che inizia per "B" oppure per "R"
• nati dopo il 01/01/1999
Ordinare per cognome crescente e nome crescente.
*/

SELECT s.matricola "Matricola Modulo", p.nome, p.cognome, s.corso_nome
FROM Studente s, Persona p, CorsoITS c
WHERE s.cf = p.cf
AND s.corso_nome = c.nome
AND s.corso_edizione = c.edizione
AND c.nome IN ('Full Stack Developer', 'Data Analyst')
AND (p.cognome ILIKE 'B%' OR p.cognome ILIKE 'R%')
AND s.nascita > '1999-01-01'
ORDER BY p.cognome, p.nome;

-- 2


/* Esercizio 2

Visualizzare:
• codice modulo
• nome modulo
• ore
• docente (nome e cognome)
per i moduli che soddisfano tutte le seguenti condizioni:
• durata compresa tra 40 e 70 ore
• codice diverso da:
o DB01
o JAVA01
• docente con cognome che contiene la lettera "i"
Ordinare per ore decrescente
*/

SELECT m.codice, m.nome, m.ore, p.nome, p.cognome
FROM Modulo m, Persona p, Docente d, doc_insegna_modulo dim
WHERE d.cf = p.cf
AND dim.docente = d.cf
AND dim.modulo = m.codice
AND m.ore >= 40 AND m.ore <= 70 
-- > e = sono due controlli che fa. 
-- è possibile usare > 39 oppure
-- AND m.ore BETWEEN 40 AND 70 variante
AND m.codice NOT IN ('DB01', 'JAVA01')
AND p.cognome ILIKE '%i%'
ORDER BY m.ore DESC;

-- 8

/* Esercizio 3

Visualizzare:
• matricola studente
• nome studente
• cognome studente
• modulo
• voto
per tutti gli esami che soddisfano le seguenti condizioni:
• voto maggiore o uguale a 8
• modulo appartenente a:
o DB01
o JAVA01
o SPR01
o PY01
• cognome dello studente che NON inizia per:
o B
o V
• nome dello studente contenente la lettera "a"
Ordinare:
1. per voto decrescente
2. a parità di voto per cognome crescente
*/

SELECT s.matricola, p.nome, p.cognome, m.nome, es.voto
FROM Studente s, Persona p, Modulo m, esame_superato es
WHERE s.cf = p.cf 
AND es.studente = s.cf
AND es.modulo = m.codice
AND es.voto >= 8
AND m.codice IN ('DB01', 'JAVA01', 'SPR01', 'PY01')
AND (p.cognome NOT ILIKE 'B%' AND p.cognome NOT ILIKE 'V%')
AND p.nome LIKE '%a%'
ORDER BY es.voto DESC, p.cognome ASC;

-- 35

-- Funzioni di aggregazioni e GROUP BY devono comparire sempre
-- non è possibile creare una query con l'una senza l'altra


/* Esercizio 4

Visualizzare, per ogni corso ITS:
• nome corso
• edizione
• numero di studenti iscritti
Ordinare per numero di studenti decrescente.
*/

SELECT c.nome, c.edizione, COUNT(*) AS "Numero studenti"
FROM CorsoITS c, Studente s
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione
GROUP BY c.nome, c.edizione
ORDER BY "Numero studenti" DESC;

-- Senza GROUP BY
SELECT c.nome, c.edizione, s.matricola
FROM CorsoITS c, Studente s
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione
ORDER BY c.nome, c.edizione;


-- 3


/*
Quello che vuoi davvero è raggruppare per **corso + edizione** (la chiave che identifica ogni corso), e poi contare quante righe (= quanti studenti) cadono in ogni gruppo.

**Nota sull'`ORDER BY`:** qui `ORDER BY "Numero studenti"` funziona correttamente, perché l'alias definito nella `SELECT` **può** essere riusato nell'`ORDER BY` (è una comodità che PostgreSQL permette, dato che l'`ORDER BY` viene eseguito logicamente *dopo* la `SELECT`). Questo è diverso dal `GROUP BY`, che viene eseguito *prima* della `SELECT`, motivo per cui lì l'alias dell'aggregazione non è ancora disponibile/sensato.

**Riassumendo l'ordine logico di esecuzione** (utile da tenere a mente):
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY 
```
Ogni fase "vede" solo i risultati delle fasi precedenti — ecco perché `GROUP BY` non può usare alias definiti nella `SELECT` (non è ancora stata eseguita), mentre `ORDER BY` sì.
*/


/* Esercizio 5

Visualizzare, per ogni modulo:
• codice
• nome
• voto medio ottenuto negli esami
Mostrare solo i moduli per cui esiste almeno un esame superato.
*/

SELECT m.codice, m.nome, AVG(es.voto) "Voto medio"
FROM Modulo m, esame_superato es
WHERE es.modulo = m.codice
GROUP BY m.codice, m.nome;

-- 10


/*
Qui raggruppi solo per modulo (codice + nome, che insieme identificano univocamente il modulo — anche se basterebbe solo m.codice essendo la PK, Postgres richiede comunque che ogni colonna non aggregata in SELECT sia nel GROUP BY).

Una riga per modulo, con la media calcolata su tutti gli esami superati per quel modulo.

La regola d’oro: il GROUP BY deve contenere esattamente le colonne che identificano “l’unità” per cui vuoi un risultato aggregato — né più (altrimenti spezzetti troppo i gruppi, come nel tuo tentativo), né meno (altrimenti SQL non sa cosa fare con le colonne non aggregate).
*/


/* Esercizio 6
Visualizzare, per ogni docente:
• nome
• cognome
• numero di moduli insegnati
Ordinare per numero di moduli decrescente.
*/

SELECT p.nome, p.cognome, COUNT(m.codice) "Numero moduli"
FROM Docente d, Persona p, Modulo m, doc_insegna_modulo dim
WHERE d.cf = p.cf 
AND dim.docente = d.cf
AND dim.modulo = m.codice
GROUP BY p.nome, p.cognome
ORDER BY "Numero moduli" DESC;

-- 7

/*
Ottima domanda, è un punto che genera molta confusione. Chiariamo cosa succede davvero "sotto il cofano".

## Cosa fa `COUNT()` davvero

`COUNT(espressione)` conta **quante righe del gruppo hanno un valore NON NULL per quell'espressione**. Punto. Non è magia, è letteralmente questo: scorre le righe del gruppo, per ognuna valuta l'espressione tra parentesi, e se il risultato non è `NULL` incrementa il contatore.

`COUNT(*)` invece è un caso speciale: conta **tutte le righe del gruppo**, senza guardare nessuna colonna specifica, quindi senza nessun rischio di escludere righe per via di `NULL`.

## Nel tuo caso specifico

```sql
COUNT(m.codice)
```

Qui stai contando, per ogni gruppo (= ogni docente, dato il tuo `GROUP BY p.nome, p.cognome`), quante righe hanno `m.codice` **non nullo**. Dato che `m.codice` è la PK di `Modulo` e la query fa un join (`dim.modulo = m.codice`), ogni riga del gruppo ha necessariamente un `m.codice` valido (mai NULL, altrimenti il join l'avrebbe scartata). Quindi in questo caso specifico, `COUNT(m.codice)` e `COUNT(*)` danno **esattamente lo stesso risultato**.

## Allora quando scegliere uno o l'altro?

**Usa `COUNT(*)`** quando vuoi semplicemente "quante righe ci sono in questo gruppo", senza preoccuparti di valori NULL — è il caso più comune con gli inner join classici, dove ogni riga del gruppo rappresenta già un'entità completa e valida (es. "un modulo insegnato da questo docente").

**Usa `COUNT(colonna)`** quando la colonna può contenere `NULL` e vuoi escludere quei casi dal conteggio. Esempio tipico: un `LEFT JOIN` dove alcune righe non hanno corrispondenza nella tabella di destra, quindi quella colonna risulta `NULL` per quelle righe — lì `COUNT(colonna)` ti dà "quanti hanno effettivamente un valore", mentre `COUNT(*)` conterebbe anche le righe senza corrispondenza.

**Esempio concreto per capire la differenza:** immagina di voler sapere quanti studenti hanno sostenuto almeno un esame, usando un `LEFT JOIN` per includere anche chi non ne ha sostenuti:

```sql
SELECT s.matricola, COUNT(es.modulo) AS esami_sostenuti
FROM Studente s
LEFT JOIN esame_superato es ON es.studente = s.cf
GROUP BY s.matricola;
```

Qui, per uno studente senza esami, il `LEFT JOIN` produce comunque una riga, ma con `es.modulo = NULL`. Se usassi `COUNT(*)`, quella riga conterebbe comunque come "1", dandoti il risultato sbagliato (`1` invece di `0`). Usando `COUNT(es.modulo)`, quel `NULL` viene ignorato, e ottieni correttamente `0`.

## Usare colonne diverse dentro `COUNT`: `DISTINCT`

C'è un'altra sfumatura: `COUNT(DISTINCT colonna)` conta i **valori distinti** non nulli, non le righe. Utile quando il join può introdurre righe duplicate per la stessa entità e vuoi contare entità uniche. Esempio: se un docente insegnasse lo stesso modulo due volte per qualche motivo nei dati (riga duplicata), `COUNT(m.codice)` lo conterebbe 2 volte, mentre `COUNT(DISTINCT m.codice)` lo conterebbe 1 volta sola.

## Verdetto sulla tua query

La tua query con `COUNT(m.codice)` **è corretta** per questo esercizio, perché grazie all'inner join non ci sono righe con `m.codice` nullo da preoccuparsi — ma in questo caso specifico avresti potuto scrivere anche semplicemente `COUNT(*)` ottenendo lo stesso risultato, perché ogni riga del gruppo rappresenta esattamente un modulo insegnato dal docente, senza ambiguità.
*/


/*
Esercizio 7

Visualizzare, per ogni docente:
• Nome
• Cognome
• numero di moduli insegnati
considerando solamente i moduli che:
• hanno almeno 50 ore
• non hanno codice:
o DB01
o JAVA01
Ordinare per numero di moduli decrescente.
*/

SELECT p.nome, p.cognome, COUNT(*) "Numero moduli"
FROM Persona p, Docente d, Modulo m, doc_insegna_modulo dim
WHERE p.cf = d.cf
AND dim.docente = d.cf
AND dim.modulo = m.codice
AND m.ore >= 50
AND m.codice NOT IN ('DB01', 'JAVA01')
GROUP BY p.nome, p.cognome
ORDER BY 3 DESC;

-- 3

/*Esercizio 8

Visualizzare, per ogni corso:
• nome corso
• edizione
• numero di studenti iscritti
considerando solamente gli studenti:
• nati dopo il 01/01/1999
• con cognome che contiene la lettera "a"
Ordinare per nome corso.
*/

SELECT c.nome, c.edizione, COUNT(*) AS "Num Studenti"
FROM CorsoITS c, Studente s, Persona p
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione 
AND s.cf = p.cf
AND s.nascita > '1999-01-01'
AND p.cognome ILIKE '%a%'
GROUP BY c.nome, c.edizione
ORDER BY c.nome;

-- 3


/* Esercizio 9

Visualizzare, per ogni modulo:
• codice
• nome
• voto medio
considerando solamente gli esami:
• con voto maggiore o uguale a 8
• sostenuti da studenti iscritti ai corsi:
o Full Stack Developer
o Data Analyst
Ordinare per voto medio decrescente.
*/

SELECT m.codice, m.nome, AVG(es.voto) "Voto medio"
FROM Modulo m, esame_superato es, Studente s, CorsoITS c
WHERE es.modulo = m.codice 
AND es.studente = s.cf
AND s.corso_nome = c.nome AND s.corso_edizione = c.edizione
AND es.voto >= 8
AND c.nome IN ('Full Stack Developer', 'Data Analyst')
GROUP BY m.codice
ORDER BY "Voto medio" DESC;

-- 10

-- FILTRARE SUI RAGGRUPPAMENTI 

/* Uguale alla 4 ma con studenti < 10 */
SELECT c.nome, c.edizione, COUNT(*) AS "Numero studenti"
FROM CorsoITS c, Studente s
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione
GROUP BY c.nome, c.edizione
HAVING COUNT(*) < 10
ORDER BY "Numero studenti" DESC;

/*
HAVING invece filtra i gruppi già formati, dopo che l’aggregazione è stata calcolata. Per questo esiste una clausola separata.

Nota: in HAVING devi ripetere l’espressione COUNT(*) per esteso — non puoi usare l’alias "Numero studenti" definito nella SELECT, perché (come visto prima nell’ordine logico di esecuzione FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY) HAVING viene valutato prima della SELECT, quindi l’alias non esiste ancora a quel punto. È per questo che ORDER BY "Numero studenti" invece funziona: viene eseguito dopo la SELECT.
*/