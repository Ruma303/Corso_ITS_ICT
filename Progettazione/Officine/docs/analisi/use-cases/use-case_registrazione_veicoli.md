Specifica use-case Registrazione Veicoli

	nuovo_veicolo(ta:Targa, imm:Intero, m:Modello, c:Cliente)
		pre:

		post:
			crea un oggetto v:Veicolo con:
				v.targa = ta
				v.immatricolazione = imm

			creare il link 
				(v, m):mod_veic

			creare il link
				(v, c):proprietario