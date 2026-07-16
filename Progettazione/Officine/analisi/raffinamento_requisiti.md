# Raffinamento dei requisiti - Officine 1

## Potenziali classi

- Persona (superclasse)
	- Dipendente
	- Direttore
	- Proprietario
- Officina
- Riparazione (possibile classe associativa)
- Veicolo
- Nazione
- Regione
- Città

## Note sui vincoli

1. Le targhe possono essere cambiate. Per identificare univocamente un veicolo si usa un **Identificativo Unico Internazionale** (VIN - Vehicle Identification Number).
2. Il vincolo di integrità viene spostato sulla targa, ma potrebbe essere un vincolo composto da tutti gli altri campi dell'istanza veicolo.
3. Nel mondo reale sia Dipendente che Direttore possono essere comunque Proprietari di un Veicolo e beneficiare di servizi di Riparazione.


## Legenda

- A: **association**, indica associazioni tra classi
- C: **constraint**, indica ulteriori vincoli sul singolo elemento o tra gli elementi
- Op: **operation**, indica che il valore è derivato a seguito di un'operazione


# Classi Autonome

## 1. Requisiti sulle persone

	1.1 nome
	1.2 codice fiscale
	1.3 indirizzo
	1.4 numero telefono

	C1.1 codice fiscale diventa il vincolo d'integrità
	C1.2 il codice fiscale ha una sua regex
	C1.3 il numero di telefono ha una sua regex

	C1.4 questa classe sarà estesa da altre tre classi:
		C1.4.1 Dipendente
		C1.4.2 Direttore
		C1.4.3 Proprietario

	A1.1 Ogni sottoclasse prende l'indirizzo dall'associazione con Città


## 2. Requisiti sui dipendenti (Persona)

	A2.1 Associazione con officina dove lavorano

	Op2.1 gli anni di servizio verranno calcolati da un'operazione (Dipendente, Officina) che conterrà il numero di anni


## 3. Requisiti sui direttori (Persona)

	3.1 data di nascita

	A3.1 associazione con l'officina che un Direttore dirige


## 4. Requisiti sulle officine

	4.1 nome
	4.2 indirizzo
	4.3 numero dipendenti
	4.4 direttore

	A4.1 associazione con i dipendenti
	A4.2 associazione con i direttori
	A4.3 l'indirizzo è un'associazione con Città

	Op4.1 Il numero dei dipendenti può essere ottenuto da un'operazione sommando i link (Officina, Dipendente)

	C4.1 la coppia nome e indirizzo può fungere da vincolo d'integrità di classe in relazione con la città dove si trova


## 5. Requisiti sui veicoli

	5.1 modello
	5.2 tipo
	5.2 targa
	5.3 anno di immatricolazione

	A5.1 associazione con il/i proprietario/i
	A5.2 associazione con l'officina per mezzo di una Riparazione

	C5.1 il vincolo d'integrità può essere rappresentato da una tupla di tutti i valori (modello, tipo, targa, anno di immatricolazione), non potendo contare sul VIN
	C5.2 le tipologie di veicoli sono prestabilite, quindi va usata un'enumerazione
	C5.3 la targa utilizza sicuramente uno standard, servirà quindi una regex


## 6. Requisiti sui proprietari (Persona)

	A6.1 associazione con Officina come cliente per mezzo del servizio di Riparazione
	A6.2 associazione con Veicolo come possessore


## 7.Requisiti sulle nazioni

	7.1 nome

	C7.1 le nazioni sono identificate dal nome che funge da chiave univoca


## 8. Requisiti sulle regioni

	8.1 nome

	A8.1 associati con le nazioni di cui fanno parte

	C8.1 le regioni sono identificate dal nome proprio e dal nome della nazione. Ammettiamo che possano esistere più regioni con lo stesso nome in nazioni diverse, ma sono identificate univocamente dalla coppia (Regione, Nazione)


## 9. Requisiti sulle città

	9.1 nome
	9.2 CAP

	A9.1 associati con le regioni di cui fanno parte
	A9.2 associazione con le officine in merito alla loro sede
	A9.3 associazione con le persone in merito alla loro residenza

	C9.1 le città sono identificate dalla tupla (nome proprio, nome regione, nome nazione)
		C9.1.1 Il sistema ammette due città omonime che si trovano nella stessa regione
		C9.1.2 Il sistema impedisce due città omonime, nella stessa regione e stessa nazione
	C9.2 le grandi città possono avere più CAP. Questo campo deve contenere un vincolo di molteplicità => 1


## 10. Requisiti sulle riparazioni

	10.1 codice
	10.2 veicolo
	10.3 data ora accettazione
	10.4 data ora riconsegna
	10.5 stato della riparazione

	A10.1 associazione con il Veicolo da riparare
		A10.1.1 dall'istanza del veicolo recuperare modello, tipo, targa, anno di immatricolazione
	A10.2 associazione con il Proprietario a cui è intestata la riparazione

	C10.1 l'attributo veicolo è l'associazione con la classe Veicolo
	C10.2 una riparazione può esser appena stata presa in carico, in lavorazione, oppure terminata. È il caso quindi di creare un'enumerazione con questi valori
	C10.3 il codice è univoco, diventerà il vincolo d'integrità
