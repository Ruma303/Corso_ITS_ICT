# Analisi dei requisiti - Gestione ITS 1 - Raffinamento


## Legenda

In questa specifica sono stati aggiunti:

- C: **constraints**, indica la specifica dei vincoli o associazioni da aggiungere ad ogni entità
- E: **evalutations**, sono degli elementi non ancora chiari che devono essere valutati man mano, rappresentate come checkbox 


## 1. Requisiti sulle persone (entità astratta)

	1.1 nome;
	1.2 codice fiscale;
	1.3 data nascita;
	1.4 luogo nascita;
	
	C1.2 il codice fiscale italiano ha una regex fissa
	C1.3 per la data di nascita utilizzare un formato italiano che esprime solo il giorno-mese-anno
	C1.4 il luogo di nascita è un'associazione con l'entità LuogoNascita


## 2. Requisiti sugli studenti : Persona (specializzazione di Persona, eredita i suoi campi)

	2.1 numero matricola;
	2.2 corso ITS iscritto;
	2.3 moduli superati;

	C2.1 il numero matricola è una stringa alfanumerica. Escludere caratteri speciali
	C2.2 il corso ITS dev'essere univoco
	C2.3 dei moduli didattici ci interessa inserire soltanto quelli che ha superato, non tutti quelli del programma
	C2.4 il luogo di nascita è un'associazione con la classe "LuogoNascita"


## 3. Requisiti sui docenti : Persona (specializzazione di Persona, eredita i suoi campi)

	3.1 moduli didattici insegnati;

	C3.1 un docente può insegnare più moduli didattici contemporaneamente 


## 4. Requisiti sui corsi

	4.1 nome;
	4.2 edizione;

	C4.2 l'edizione è un numero che indica l'anno di partenza
		B3.1.1 Gli ITS in italia sono stati costituiti dal 2021, quindi questo è il valore minimo
	C4.3 le aree disciplinari sono stringhe che indicano il nome dell'area
		C4.3.1 Il campo dev'essere opzionale o consentire stringhe vuoto per poter essere aggiunto in futuro

	E4.1 [ ] le aree disciplinari potrebbero essere dei campi appartenenti all'entità Modulo, o anche associazioni. Se non è necessario rappresentarle esternamente, è possibile inserirle come semplice campo
	E4.2 [ ] valutare la presenza di amministratori nel sistema con poteri decisionali


## 5. Requisiti sui moduli

	5.1 codice;
	5.2 nome;
	5.3 corso ITS;
	5.4 numero ore;

Specifica dei vincoli:
	B5.1 il codice è presumibilmente alfanumerico e facoltativo
	B5.3 vi è un vincolo di associazione con i corsi che possiamo chiamare "appartiene a"
		B5.3.1 l'associazone sarà facoltativa. Un modulo può appartenere o no ad un corso
	B5.3. il numero di ore verrà indicato come un intero positivo ma con default 0, per consentire la creazione di corsi non ancora avviati.


## 6. Luogo di nascita

	6.1 città;
	6.2 regione;
	6.3 nazione;
	
	C6.1 il luogo di nascita è in relazione con le entità Persona	
	C6.2 ogni campo - città, regione, nazione - potrebbe essere rappresentata con una classe separata. In questo sistema brevità rappresentiamo tutto in un'unica classe
	C5.3 le entità in relazioni potranno avere un vincolo si / no. Una persona può esser nata soltanto una volta in una città oppure no. 
		C5.3.1 dal punto di vista del luogo di nascita, la relazione sarà sicuramente molteplice in quanto in una città possono nascere un numero multiplo di persone.


## 7. Superamento moduli: classe associativa con campi

	7.1 data in formato italiano
	7.2 voto 
	
	C7.1 Il voto deve essere espresso con numero intero
		C7.1.1 La base scelta sono i trentesimi
		C7.1.2 un voto può essere soltanto >= 18 e <= 30, altrimenti è considerato non superato
	C7.2 l'associazione sarà con la classe Studente


## 8. Requisiti Area disciplinare 


## 9. Requisiti Amministratore
