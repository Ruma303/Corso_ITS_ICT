# Raffinamento dei requisiti - Ordini e fatture

## Legenda

- A: **associations**, indica associazioni e/o classi associative definite separatamente dalle classi autonome
- C: **constraints**, indica la specifica dei vincoli o associazioni da aggiungere ad ogni elemento


# Classi Autonome


## 1. Requisiti sui direttori
	1.1 nome
	1.2 cognome
	1.3 codice fiscale
	1.4 data nascita
	1.5 luogo nascita
	1.6 anni servizio in azienda
	
	A.1.1 relazione con Dipartimenti 
	
	C.1.1 dirige al più un dipartimento


## 2. Requisiti sui dipartimenti
	2.1 nome
	2.2 indirizzo
	2.3 direttore
	
	A.2.1 relazione con i direttori 
	A.2.2 un dipartimento può effettuare ordini ad uno o più fornitori per mezzo di un ordine
	
	C.2.1 un dipartimento è diretto al più da un direttore
	C.2.2 un dipartimento può eseguire una molteplicità di ordini
  

## 3. Requisiti sui fornitori
	3.1 ragione sociale
	3.2 partita iva
	3.3 indirizzo
	3.4 numero telefono
	3.5 indirizzo email
	
	A.3.1 relazione con gli ordini
	
	C.3.1 possono ricevere uno o più ordini stipulati dai vari dipartimenti


## 4. Requisiti sulle Città
	4.1 nome
	
	A.4.1 in relazione con i direttori per determinare il luogo di nascita
	A.4.2 in relazione con i dipartimenti per indicare il loro indirizzo
	A.4.3 in relazione con i fornitori per indicare la loro sede
	A.4.4 in relazione con le regioni in cui si trovano


## 5. Requisiti sulle regioni
	5.1 nome
	
	A.5.1 in relazione con le città con che hanno al loro interno
	A.5.2 in relazione con le nazioni dove si trovano


## 6. Requisiti sulle nazioni
	6.1 nome
	
	A.6.1 in relazione con le regioni che contengono


## 7. Requisiti sulle fatture
	7.1 ordine
	
	A.7.1 relazione con gli ordini
	
	C.7.1 una fattura esiste esclusivamente se esiste l'ordine corrispondente
	C.7.2 l'ordine dev'essere con stato "da saldare" o "saldato"


## 8. Requisiti sui beni
	8.1 nome
	
	A.8.1 in relazione con gli ordini


## 9. Requisiti sui servizi
	9.1 nome
	
	A.9.1 in relazione con gli ordini
	

# Classi associative


## 10. Requisiti sugli ordini
	10.1 tipologia
	10.2 dipartimento
	10.3 data stipula
	10.4 fornitore
	10.5 descrizione 
	10.6 imponibile
	10.7 aliquota
	10.8 stato
	
	A.10.1 relazione con il dipartimento che emette l'ordine
	A.10.2 relazione con le fatture
	A.10.3 relazione con beni per via del campo tipologia
	A.10.4 relazione con servizi per via del campo tipologia
	
	C.10.1 le tipologie possono essere beni o servizi in cui questa classe è in relazione
	C.10.2 l'imponibile è una somma reale >=0 
	C.10.3 l'aliquota è una percentuale >=0
	C.10.4 lo stato è un campo enumerativo da più simboli
		C.10.4.1 solo uno stato alla volta può esistere
		C.10.4.2 può esistere la relazione con le fatture solo dagli stati "da_saldare" e "saldato"
