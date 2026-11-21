
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