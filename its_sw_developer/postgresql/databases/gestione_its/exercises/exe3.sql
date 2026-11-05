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


-- Raggruppamenti (esempi)

SELECT es.modulo AS modulo_superato, COUNT(*)
FROM Studente s, Persona p, esame_superato es, Modulo m, 
Docente d, doc_insegna_modulo dim
WHERE s.cf = p.cf
	AND s.cf = es.studente 
	AND m.codice = es.modulo
	AND m.codice = dim.modulo 
	AND d.cf = dim.docente
GROUP BY modulo_superato;

-- Conteggio per modulo (es. “quanti esami superati per ogni modulo”)

SELECT m.nome AS modulo_superato, COUNT(*) AS numero_esami
FROM esame_superato es
JOIN Modulo m ON m.codice = es.modulo
GROUP BY m.nome;

-- Lista di studenti/docenti per modulo, ma su un’unica riga per modulo (usando STRING_AGG per concatenare i valori)

SELECT m.nome AS modulo_superato,
       STRING_AGG(DISTINCT s.matricola, ', ') AS studenti,
       STRING_AGG(DISTINCT pd.nome || ' ' || pd.cognome, ', ') AS docenti
FROM Studente s
JOIN esame_superato es ON es.studente = s.cf
JOIN Modulo m ON m.codice = es.modulo
JOIN doc_insegna_modulo dim ON dim.modulo = m.codice
JOIN Docente d ON d.cf = dim.docente
JOIN Persona pd ON pd.cf = d.cf
GROUP BY m.nome;

SELECT s.matricola, 
       p.nome, 
       p.cognome,
       m.nome AS modulo_superato,
       STRING_AGG(DISTINCT pd.nome || ' ' || pd.cognome, ', ') AS docente
FROM Studente s
JOIN Persona p ON s.cf = p.cf
JOIN esame_superato es ON es.studente = s.cf
JOIN Modulo m ON m.codice = es.modulo
JOIN doc_insegna_modulo dim ON dim.modulo = m.codice
JOIN Docente d ON d.cf = dim.docente
JOIN Persona pd ON pd.cf = d.cf
GROUP BY s.matricola, p.nome, p.cognome, m.nome
ORDER BY s.matricola, m.nome;