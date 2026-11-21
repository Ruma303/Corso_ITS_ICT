/* Esercizio 16

Visualizzare tutti i moduli il cui nome contiene la parola:
"Data"
Mostrare:
• codice
• nome
• ore
*/

SELECT codice, nome, ore FROM Modulo WHERE nome LIKE '%Data%';
-- 1

/* Esercizio 17

Visualizzare:
• matricola
• nome
• cognome
degli studenti il cui cognome inizia per:
"B"
Ordinare per cognome crescente.
*/

SELECT s.matricola, p.nome || ' ' || p.cognome as full_name
FROM Studente s, Persona p
WHERE s.cf = p.cf 
AND p.cognome LIKE 'B%'
ORDER BY p.cognome ASC;
-- 1

/* Esercizio 18

Visualizzare tutti i moduli che NON contengono la parola:
"Java"
Mostrare:
• codice
• nome
*/

SELECT codice, nome FROM Modulo WHERE nome NOT LIKE '%Java%';
-- 11 


/* Esercizio 19

Visualizzare:
• nome docente
• cognome docente
• nome modulo
per tutti i docenti il cui cognome termina con: "i"
*/

SELECT p.nome || ' ' || p.cognome as docente, m.nome
FROM Docente d, Persona p, Modulo m, doc_insegna_modulo dim
WHERE d.cf = p.cf AND dim.docente = d.cf AND dim.modulo = m.codice
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
*/

SELECT codice, nome, ore FROM Modulo
WHERE codice in ('DB01', 'JAVA01', 'SPR01');
-- 3



/* Esercizio 21

Visualizzare:
• matricola
• corso frequentato
degli studenti iscritti ad uno dei seguenti corsi:
• Full Stack Developer
• Data Analyst
*/

SELECT matricola, corso_nome
FROM Studente s, CorsoITS c
WHERE s.corso_nome = c.nome AND s.corso_edizione = c.edizione
AND c.nome IN ('Full Stack Developer', 'Data Analyst');
-- 21


/* Esercizio 22

Visualizzare:
• codice modulo
• nome modulo
dei moduli che NON appartengono ai corsi:
• Full Stack Developer
• Cyber Security Specialist
*/

SELECT m.codice, m.nome 
FROM Modulo m, modulo_in_corso mic, CorsoITS c
WHERE m.codice = mic.modulo 
AND mic.corso_nome = c.nome
AND mic.corso_edizione = c.edizione
AND c.nome NOT IN ('Full Stack Developer', 'Cyber Security Specialist');

-- 4

/* Esercizio 23

Visualizzare:
• matricola studente
• nome studente
• cognome studente
• nome corso
per tutti gli studenti:
• il cui cognome contiene la lettera "a"
• iscritti ai corsi:
o Full Stack Developer
o Data Analyst
Ordinare per cognome e nome.
*/

SELECT s.matricola, p.nome, p.cognome ,
	c.nome FROM Studente s, Persona p, CorsoITS c
WHERE s.cf = p.cf 
AND s.corso_edizione = c.edizione 
AND s.corso_nome = c.nome
AND c.nome IN ('Full Stack Developer', 'Data Analyst')
ORDER BY p.cognome, p.nome;
-- 21