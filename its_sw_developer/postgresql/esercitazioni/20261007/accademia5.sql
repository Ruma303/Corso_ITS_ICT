-- accademia5.sql

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

