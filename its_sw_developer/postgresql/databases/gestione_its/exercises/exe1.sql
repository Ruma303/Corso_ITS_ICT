
/* Ex 1

Visualizzare matricola e corso frequentato di tutti gli studenti.
Ordinare per matricola crescente.
*/

SELECT matricola, corso_nome
FROM Studente
ORDER BY matricola ASC;


/* Ex 2

Visualizzare tutti i moduli che hanno una durata superiore a 50 ore.
Mostrare:
• codice
• nome
• ore
*/

SELECT codice, nome, ore from Modulo WHERE ore > 50;


/* Ex 3

Visualizzare tutti gli esami con voto pari o superiore a 9.
Mostrare:
• studente
• modulo
• voto
*/

SELECT studente, modulo, voto FROM esame_superato WHERE voto >= 9;


/* Ex4

Visualizzare tutti gli studenti iscritti al corso: Full Stack Developer

Mostrare:
• matricola
• data di nascita
*/

SELECT matricola, nascita FROM Studente WHERE corso_nome = 'Full Stack Developer';


/* Ex 5

Visualizzare tutti i moduli ordinati:

1. per ore decrescente
2. a parità di ore, per nome crescente.
*/

SELECT * FROM Modulo ORDER BY ore DESC, nome ASC;
