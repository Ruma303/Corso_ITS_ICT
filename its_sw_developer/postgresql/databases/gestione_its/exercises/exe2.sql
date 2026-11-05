-- Esercitazioni con JOIN

/* Ex 6

Visualizzare:
• matricola
• nome corso
• area disciplinare
per ogni studente. 
*/

SELECT s.matricola, s.corso_nome, a.nome
FROM Studente s, CorsoITS c, AreaDisciplinare a
WHERE s.corso_nome = c.nome AND s.corso_edizione = c.edizione
AND c.area = a.nome;


/* Ex 7

Visualizzare:
• docente
• modulo insegnato
per tutti i docenti che insegnano almeno un modulo.
*/

SELECT * FROM doc_insegna_modulo 
WHERE docente IS NOT NULL 
AND modulo IS NOT NULL;

-- oppure, se necessario recuperare altri campi che non sono PK

SELECT cf AS "CF Docente", nome AS "Nome modulo"
FROM Docente d, Modulo m, doc_insegna_modulo dim
WHERE dim.docente = d.cf 
AND dim.modulo = m.codice;


/* Ex 8

Visualizzare:
• matricola studente
• modulo
• voto
per tutti gli esami sostenuti. 
*/

SELECT s.matricola, e.modulo, e.voto
FROM Studente s, esame_superato e
WHERE e.studente = s.cf;


/* Ex 9

Visualizzare:
• codice modulo
• nome modulo
• nome docente
per tutti i moduli che hanno un docente assegnato.
*/


SELECT m.codice, m.nome, p.nome
FROM Modulo m, doc_insegna_modulo dim, Docente d, Persona p
WHERE m.codice = dim.modulo AND dim.docente = d.cf AND d.cf = p.cf;

-- Sintassi con JOIN e ON
SELECT m.codice, m.nome, p.nome
FROM Modulo m 
JOIN doc_insegna_modulo dim 
	ON m.codice = dim.modulo 
JOIN Docente d
	ON dim.docente = d.cf
JOIN Persona p
	ON d.cf = p.cf;


/* Ex 10

Visualizzare:
• matricola
• corso frequentato
• area disciplinare
solo per gli studenti appartenenti all'area: Informatica
*/

SELECT s.matricola, s.corso_nome, a.nome
FROM Studente s, CorsoITS c, AreaDisciplinare a
WHERE s.corso_nome = c.nome 
AND s.corso_edizione = c.edizione 
AND c.area = a.nome 
AND a.nome = 'Informatica';
