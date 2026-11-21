/* Esercizio 11

Visualizzare:
• matricola studente
• nome studente
• cognome studente
• nome corso frequentato
• area disciplinare
*/

SELECT s.matricola, p.nome, p.cognome, s.corso_nome, a.nome
FROM Studente s, Persona p, AreaDisciplinare a, CorsoITS c
WHERE s.cf = p.cf 
AND s.corso_nome = c.nome AND s.corso_edizione = c.edizione
AND c.area = a.nome;
-- 30

/* Esercizio 12

Visualizzare:
• nome modulo
• docente che lo insegna (nome e cognome)
• numero di ore del modulo
per tutti i moduli che hanno un docente assegnato.
*/

SELECT m.nome as "Nome Modulo", p.nome || ' ' || p.cognome AS "Nome docente", m.ore "Ore Modulo"
FROM Modulo m, Persona p, doc_insegna_modulo dim, Docente d
WHERE m.codice = dim.modulo AND d.cf = dim.docente 
AND d.cf = p.cf;
-- 12


/* Esercizio 13

Visualizzare:
• matricola studente
• nome studente
• cognome studente
• nome modulo
• voto
per tutti gli esami sostenuti.
*/

SELECT s.matricola, p.nome, p.cognome, m.nome, es.voto
FROM Studente s, Persona p, Modulo m, esame_superato es
WHERE s.cf = p.cf 
AND es.studente = s.cf AND es.modulo = m.codice;
-- 126


/* Esercizio 14

Visualizzare tutti i moduli appartenenti al corso:
Full Stack Developer
Mostrare:
• codice modulo
• nome modulo
• ore
• edizione corso
Ordinare per ore decrescente.
*/

SELECT m.codice, m.nome, m.ore, c.edizione
FROM Modulo m, CorsoITS c, modulo_in_corso mic
WHERE m.codice = mic.modulo AND c.nome = mic.corso_nome
AND c.edizione = mic.corso_edizione
AND c.nome = 'Full Stack Developer'
ORDER BY m.ore DESC;
-- 6


/* Esercizio 15

Visualizzare:
• matricola studente
• nome studente
• cognome studente
• modulo superato
• docente che insegna quel modulo
Mostrare una riga per ogni esame superato per ogni studente. Non va mostrato lo stesso studente con lo stesso esame
*/

SELECT s.matricola, p.nome || ' ' || p.cognome AS docente, es.modulo AS modulo_superato, dim.docente AS docente
FROM Studente s, Persona p, esame_superato es, Modulo m, 
Docente d, doc_insegna_modulo dim
WHERE s.cf = p.cf
	AND s.cf = es.studente 
	AND m.codice = es.modulo
	AND m.codice = dim.modulo 
	AND d.cf = dim.docente;
-- AND p.cf = d.cf; Non è possibile. Servono 2 alias

SELECT s.matricola, 
       p.nome || ' ' || p.cognome AS docente_cf,
       pd.nome || ' ' || pd.cognome AS docente,
       m.nome AS modulo_superato
FROM Studente s
JOIN Persona p ON s.cf = p.cf
JOIN esame_superato es ON es.studente = s.cf
JOIN Modulo m ON m.codice = es.modulo
JOIN doc_insegna_modulo dim ON dim.modulo = m.codice
JOIN Docente d ON d.cf = dim.docente
JOIN Persona pd ON pd.cf = d.cf; -- Secondo alias su Persona
-- 153

/* Esercitazione 16

Visualizzare tutti i moduli il cui nome contiene la parola:
"Data"

Mostrare:
• codice
• nome
• ore
**/

SELECT nome, codice, ore
FROM Modulo
WHERE nome LIKE "%Data%";

-- "Data Analysis"	"DS01"	50


/* Esercitazione 17

Visualizzare:
• matricola
• nome
• cognome
degli studenti il cui cognome inizia per: "B"
Ordinare per cognome crescente.
**/

SELECT s.matricola, p.nome, p.cognome
FROM Studente s, Persona p
WHERE s.cf = p.cf
AND p.cognome LIKE 'B%'
ORDER BY cognome ASC;

-- "MAT019"	"Michela"	"Bruni"


/* Esercitazione 18

Visualizzare tutti i moduli che NON contengono la parola:
"Java"
Mostrare:
• codice
• nome
**/

SELECT codice, nome
FROM Modulo 
WHERE nome NOT LIKE 'Java';

-- 12

/* Esercizio 19

Visualizzare:
• nome docente
• cognome docente
• nome modulo
per tutti i docenti il cui cognome termina con: "i"
**/

SELECT p.nome, p.cognome, m.nome
FROM Docente d, Persona p, Modulo m, doc_insegna_modulo dim
WHERE d.cf = p.cf 
AND dim.docente = d.cf
AND dim.modulo = m.codice
AND p.cognome LIKE '%i';

-- 12

/* Esercizio 20

Visualizzare tutti i moduli con codice:
• DB01
• JAVA01
• SPR01

Mostrare:
• codice
• nome
• ore
**/

SELECT codice, nome, ore
FROM Modulo WHERE codice IN ('DB01', 'JAVA01', 'SPR01');

-- 3

/* Esercizio 21

Visualizzare:
• matricola
• corso 
frequentato degli studenti iscritti ad uno dei seguenti corsi:
• Full Stack Developer
• Data Analyst
**/

SELECT s.matricola, s.corso_nome
FROM Studente s, CorsoITS c
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione
AND c.nome IN ('Full Stack Developer', 'Data Analyst');

-- 21


/* Esercizio 22

Visualizzare:
• codice modulo
• nome modulo

dei moduli che NON appartengono ai corsi:
• Full Stack Developer
• Cyber Security Specialist
**/

SELECT mic.modulo, m.nome
FROM Modulo m, modulo_in_corso mic, CorsoITS c
WHERE mic.modulo = m.codice 
AND mic.corso_nome = c.nome
AND mic.corso_edizione = c.edizione
AND c.nome NOT IN ('Full Stack Developer', 'Cyber Security Specialist');

-- 4


SELECT s.matricola, p.nome, p.cognome, c.nome
FROM Studente s, Persona p, CorsoITS c
WHERE s.cf = p.cf
AND s.corso_nome = c.nome
AND s.corso_edizione = c.edizione
AND p.cognome ILIKE '%a%'
AND c.nome IN ('Full Stack Developer', 'Data Analyst')
ORDER BY p.cognome ASC, p.nome ASC;

-- 9
