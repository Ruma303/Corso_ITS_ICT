Specifica use-case Termine riparazione


	termina_riparazione(r:RiparazioneInCorso)
		pre: 

		post:
			r diventa di sottoclasse RiparazioneTerminata con:
				r.riconsegna = istante corrente


	riapri_riparazione(r:RiparazioneTerminata)
		pre: 

		post:
			r diventa di sottoclasse RiparazioneInCorso ignorando il valore dell'attributo riconsegna
