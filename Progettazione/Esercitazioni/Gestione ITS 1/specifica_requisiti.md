# Obiettivi 1

I dati di interesse per il sistema sono gli studenti, i corsi, i docenti e i moduli didattici offerti dall’ITS. 

Di ogni studente il sistema deve rappresentare il nome, il codice fiscale, il numero di matricola (una stringa alfanumerica), la data di nascita, il luogo di nascita (città, regione, nazione), il corso ITS (unico) in cui è iscritto ed i moduli didattici che ha superato. 

Dei docenti il sistema deve rappresentare il nome, la data di nascita, il codice fiscale, il luogo di nascita ed i moduli didattici insegnati. 

Di ogni corso ITS il sistema deve rappresentare il nome, l’edizione (ovvero l’anno nel quale iniziano, ad es. 2025) e l’area disciplinare (informatica, turismo, cybersecurity, etc.). Nuove aree disciplinari devono poter essere aggiunte in futuro dagli amministratori del sistema. 

Di ogni modulo interessa il codice, il nome, i corsi ITS nei quali sono inclusi, ed il numero di ore di lezione previsto.


# Obiettivi 2

Estendere lo schema concettuale del progetto “Gestione ITS” definendo le operazioni di classe necessarie a modellare i requisiti ulteriori indicati di seguito. 

# Specifica dei requisiti aggiuntivi

1. Per ogni studente ‘s’ il sistema deve restituire tutti i moduli nei quali ‘s’ ha preso il voto più alto tra quelli di cui ha sostenuto l’esame. Ad esempio, se ‘s’ ha superato il modulo “M1” con 27, i moduli “M2” ed “M3” con 28 ed il modulo “M4” con 25, l’operazione deve restituire “M2” ed “M3”. 

2. Per ogni corso ‘c’, il sistema deve calcolare il numero medio di esami registrati per i diversi moduli. 
