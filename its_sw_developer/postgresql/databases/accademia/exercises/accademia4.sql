
-- accademia5.sql
select distinct cognome from persona;

select nome, cognome from persona where posizione = 'Ricercatore';

select nome, cognome from persona where posizione = 'Professore Associato' and cognome like 'V%';

select nome, cognome from persona 
where posizione in ('Professore Associato', 'Professore Ordinario')
/* 
oppure 
where (posizione = 'Professore Associato' or posizione = 'Professore Ordinario')
*/
and cognome like 'V%';

select * from progetto where fine < CURRENT_DATE;

select nome from progetto order by inizio asc;

select nome from wp order by nome asc;  

select distinct tipo from assenza;

select distinct tipo from attivitaprogetto;

select distinct giorno from public.attivitanonprogettuale where tipo = 'Didattica' order by giorno asc;
