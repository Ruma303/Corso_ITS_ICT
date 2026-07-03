Specifica della classe Dipendente

anni_servizio() : Integer >= 0
	# pre
	-- l'associazione (this, o: Officina): Impiego deve esistere

	# post
	anno_corrente = ottenere l'anno attuale
	data_inizio_impiego = estrarre anno da (this, o: Officina).data_assunzione
	result = anno_corrente - data_inizio_impiego
	return result


---------------------


Specifica della classe Officina

numero_dipendenti() : Integer >= 0
	# pre
	-- nessuna

	# post
	result = 0

	per ogni associazione (this, dip: Dipendente): Impiego
		result aggiungi 1

	return result