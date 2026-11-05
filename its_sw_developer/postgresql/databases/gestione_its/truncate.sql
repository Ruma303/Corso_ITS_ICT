-- In caso di problemi con i dati corrotti, svuotare tutte le tabelle con il seguente comando:

TRUNCATE TABLE 
    esame_superato,
    doc_insegna_modulo,
    modulo_in_corso,
    studente,
    docente,
    persona,
    modulo,
    corsoits,
    areadisciplinare,
    citta,
    regione,
    nazione
RESTART IDENTITY CASCADE;

-- Poi ricaricare il file data.sql
