Specifica associazione lavora


  anni_servizio(): Intero >= 0
  	pre: 
  		nessuna
  
  	post:
  
  		Sia oggi:Data la data corrente.
  
  		result = oggi - this.assunzione espressa in anni.


Specifica della classe Officina

numero_dipendenti() : Integer >= 0
	# pre
	-- nessuna

	# post
	result = 0

	per ogni associazione (this, dip: Dipendente): Impiego
		result aggiungi 1

	return result

