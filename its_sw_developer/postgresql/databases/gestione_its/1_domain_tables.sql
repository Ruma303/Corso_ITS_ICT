CREATE DATABASE GestioneITS;



CREATE DOMAIN String AS VARCHAR(100);

CREATE DOMAIN CodiceFiscale AS String;

CREATE DOMAIN Int_GE0 AS INTEGER
    CHECK (VALUE >= 0);

CREATE DOMAIN Int_GT0 AS INTEGER
    CHECK (VALUE > 0);

CREATE DOMAIN Voto AS INTEGER
    CHECK (VALUE BETWEEN 6 AND 10);


-- tables
CREATE TABLE Nazione (
    nome String PRIMARY KEY
);

CREATE TABLE Regione (
    nome String,
    nazione String,
    PRIMARY KEY(nome, nazione),
    FOREIGN KEY (nazione) REFERENCES Nazione(nome)
);

CREATE TABLE Citta (
    id SERIAL PRIMARY KEY,
    nome String NOT NULL,
    regione String NOT NULL,
    nazione String NOT NULL,
    FOREIGN KEY (regione, nazione) REFERENCES Regione(nome, nazione)
);

CREATE TABLE Persona (
    cf CodiceFiscale PRIMARY KEY,
    nome String NOT NULL,
    cognome String NOT NULL,
    citta_nascita INTEGER NOT NULL,
    FOREIGN KEY(citta_nascita) REFERENCES Citta(id)
);

CREATE TABLE Docente (
    cf CodiceFiscale PRIMARY KEY,
    FOREIGN KEY(cf) REFERENCES Persona(cf)
);

CREATE TABLE AreaDisciplinare (
    nome String PRIMARY KEY
);

CREATE TABLE CorsoITS (
    nome String,
    edizione Int_GT0,
    area String NOT NULL,
    PRIMARY KEY(nome, edizione),
    FOREIGN KEY(area) REFERENCES AreaDisciplinare(nome)
);

CREATE TABLE Studente (
    cf CodiceFiscale PRIMARY KEY,
    matricola String UNIQUE NOT NULL,
    nascita DATE NOT NULL,
    corso_nome String NOT NULL,
    corso_edizione Int_GT0 NOT NULL,
    FOREIGN KEY(cf) REFERENCES Persona(cf),
    FOREIGN KEY(corso_nome, corso_edizione) REFERENCES CorsoITS(nome, edizione)
);

CREATE TABLE Modulo (
    codice String PRIMARY KEY,
    nome String NOT NULL,
    ore Int_GT0 NOT NULL
);

CREATE TABLE doc_insegna_modulo (
    docente CodiceFiscale,
    modulo String,
    PRIMARY KEY(docente, modulo),
    FOREIGN KEY(docente) REFERENCES Docente(cf),
    FOREIGN KEY(modulo) REFERENCES Modulo(codice)
);

CREATE TABLE esame_superato (
    studente CodiceFiscale,
    modulo String,
    voto Voto NOT NULL,
    PRIMARY KEY(studente, modulo),
    FOREIGN KEY(studente) REFERENCES Studente(cf),
    FOREIGN KEY(modulo) REFERENCES Modulo(codice)
);

CREATE TABLE modulo_in_corso (
    modulo String,
    corso_nome String,
    corso_edizione Int_GT0,
    PRIMARY KEY(modulo, corso_nome, corso_edizione),
    FOREIGN KEY(modulo) REFERENCES Modulo(codice),
    FOREIGN KEY(corso_nome, corso_edizione) REFERENCES CorsoITS(nome, edizione)
);
