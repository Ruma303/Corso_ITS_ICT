Specifica use-case Accettazione riparazioni

	nuova_riparazione(cod:Stringa, o:Officina, v:Veicolo)
	 	pre:

	 	post:
	 		crea un nuovo oggetto r:RiparazioneInCorso con:

	 			- r.codice = cod
	 			- r.accettazione = l'istante corrente


	 		crea il link
	 			(o,r):off_rip

	 		crea il link
	 			(r,v):rip_veic
