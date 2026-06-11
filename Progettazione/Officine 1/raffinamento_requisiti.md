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

PS: le targhe possono essere cambiate. Per identificare univocamente un veicolo si usa un **Identificativo Unico Internazionale** (VIN - Vehicle Identification Number). Non avendo questo campo, identificheremo i veicoli in un altro modo.


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

	A1.1 Ogni sottoclasse ha il campo l'indirizzo che è un associazione con Città


## 2. Requisiti sui dipendenti (Persona)

	2.1 anni servizio

	A2.1 Associazione con officina dove lavorano

	Op2.1 gli anni di servizio verranno calcolati da un'operazione (Dipendente, Officina) che conterrà il numero di anni a partire dalla data di assunzione


## 3. Requisiti sui direttori (Persona)

	3.1 data di nascita

	A3.1 associazione con l'officina che un Direttore dirige


## 4. Requisiti sulle officine

	4.1 nome
	4.2 indirizzo
	4.3 numero dipendenti
	4.4 direttore

	A4.1 associazione con i dipendenti per:
		A4.1.1 ogni dipendente recuperare il numero di anni di servizio
		A4.1.2 recuperare il numero di dipendenti per officina
	A4.2 associazione con i direttori
	A4.3 l'indirizzo è un'associazione con Città

	Op4.1 Il numero dei dipendenti può essere ottenuto da un'operazione sommando i link (Officina, Persona)

	C4.1 la coppia nome e indirizzo può fungere da vincolo d'integrità di classe in relazione con la città dove si trova


## 5. Requisiti sui veicoli

	5.1 modello
	5.2 tipo
	5.2 targa
	5.3 anno di immatricolazione

	A5.1 associazione con il/i proprietario/i
	A5.2 associazione con l'officina diventa una riparazione, una associazione con attributi
	A5.3 associazione con i dipendenti per trovare il numero di impiegati
	A5.4 associazione con il direttore che dirige l'officina

	C5.1 il vincolo d'integrità può essere rappresentato da una tupla di tutti i valori (modello, tipo, targa, anno di immatricolazione), non potendo contare sul VIN
	C5.2 le tipologie di veicoli sono prestabilite, quindi va usata un'enumerazione
	C5.3 la targa utilizza sicuramente uno standard, servirà quindi una regex


## 6. Requisiti sui proprietari (Persona)

	A6.1 associazione con Officina come cliente
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

	A9.1 associati con le regioni di cui fanno parte

	C9.1 le città sono identificate dalla tupla (nome proprio, nome regione, nome nazione)


# Associazioni con attributi

## Requisiti sulle riparazioni (Possibile classe autonoma)

	1.1 codice
	1.2 veicolo (Veicolo)
	1.3 data ora accettazione
	1.4 data ora riconsegna
	1.5 stato della riparazione

	A1 associazione con il Veicolo da riparare quando si prende in consegna
		A1.1 dall'istanza del veicolo recuperare modello, tipo, targa, anno di immatricolazione
	A2 associazione con il Proprietario per prendere il veicolo da riparare
	A3 associazione con il Proprietario per riconsegnare il Veicolo

	C1 l'attributo veicolo è un'associazione verso la classe Veicolo
	C2 una riparazione può esser appena stata presa in carica, in manutenzione, oppure terminata. È il caso quindi di creare un'enumerazione con questi valori
	C3 il codice è univoco, diventerà il vincolo d'integrità

	Op1 il numero dipendenti è calcolato sommando il numero di dipendenti che lavorano in una determinata officina, quindi dalle associazioni (Dipendente, Officina)
