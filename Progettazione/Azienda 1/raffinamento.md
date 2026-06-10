## Analisi dei requisiti - Raffinamento

### 1. Requisiti sugli impiegati

Di ogni impiegato interessa rappresentare:
	1.1 nome;
	1.2 cognome;
	1.3 data di nascita;
	1.4 stipendio attuale;
	1.5 dipartimento di afferenza.

	911. Ogni impiegato afferisce a esattamente un dipartimento.
	912. Per ogni afferenza di un impiegato a un dipartimento interessa conoscere:
		912.1 data di afferenza.
	913. Ogni impiegato può partecipare a un numero qualsiasi di progetti aziendali, anche nessuno.


### 2. Requisiti sui dipartimenti

Di ogni dipartimento interessa rappresentare:
	2.1 nome;
	2.2 numero di telefono del centralino.

	921. Ogni dipartimento può avere zero o più impiegati afferenti.
	922. Di ogni dipartimento interessa conoscere il direttore.
	923. Il direttore di un dipartimento è un impiegato dell’azienda.
	924. Ogni dipartimento ha al più un direttore.
	925. Ogni impiegato dirige al più un dipartimento.


### 3. Requisiti sui progetti

Di ogni progetto aziendale interessa rappresentare:
	3.1 nome;
	3.1 budget.

	931. Ogni progetto può coinvolgere zero o più impiegati.
	932. Ogni impiegato può partecipare a zero o più progetti.
