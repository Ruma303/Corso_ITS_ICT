-- accademia5.sql

-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’ ? 

select wp.nome, wp.inizio, wp.fine
from wp, progetto as p
where wp.progetto = p.id
and p.nome = 'Pegasus';

select distinct p.nome, p.cognome, p.posizione
from persona p, progetto pr, attivitaprogetto a
where p.id = a.persona
and pr.id = a.progetto
and pr.nome = 'Pegasus'
order by p.cognome desc;


-- 2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente? 


-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di una attività nel progetto ‘Pegasus’ ? 


-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto almeno una assenza per malattia? 


-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto più di una assenza per malattia? 


-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno un impegno per didattica? 


-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un impegno per didattica? 


-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali? 



-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di entrambe le attività. 

SELECT DISTINCT p.nome, p.cognome, ap.giorno, pr.nome, anp.tipo, anp.oredurata "Ore durata attività non progettuale",
	ap.oredurata "Ore durata attività progettuale"
FROM attivitaprogetto ap, attivitanonprogettuale anp, persona p, progetto pr
WHERE ap.persona = anp.persona
AND ap.giorno = anp.giorno
AND p.id = ap.persona
AND ap.progetto = pr.id;
-- 1 row Anna Bianchi


-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali? 

SELECT DISTINCT p.nome, p.cognome
FROM Persona p, Assenza a, AttivitaProgetto ap
WHERE a.persona = p.id
AND (ap.persona = p.id AND ap.giorno = a.giorno);
-- 1 row Anna Bianchi


-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, la causa di assenza e la durata in ore della attività progettuale. 

SELECT DISTINCT p.nome, p.cognome, ap.giorno, pr.nome, a.tipo, ap.oreDurata 
FROM Persona p, AttivitaProgetto ap, Assenza a, Progetto pr
WHERE ap.persona = p.id
AND ap.progetto = pr.id
AND (ap.persona = p.id AND ap.giorno = a.giorno);


-- 12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?


