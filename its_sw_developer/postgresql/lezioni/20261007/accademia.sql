-- TODO: completare e correggere

-- Tipi
create type enum as Strutturato('Ricercatore', 'Professore Associato', 'Professore Ordinario');

create type enum as LavoroProgetto('Ricerca e Sviluppo', 'Dimostrazione', ' Management', 'Altro');

create type enum as LavoroNonProgettuale('Didattica', 'Ricerca', ' Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');


-- Domini
create domain PosInteger as integer (
	default 0,
	check (value >= 0)
);

-- Dominio specializzato senza check (alias)
create domain StringaM as varchar(100);

create domain NumeroOre as integer check(0>= value <=8);

create domain Denaro as real 
	check (value >= 0.0);

create table Persona(
	id PosInteger not null,
	nome StringaM not null,
	cognome StringaM not null,
	posizione Strutturato not null,
	stipendio Denaro not null,
	primary key (id)
);
