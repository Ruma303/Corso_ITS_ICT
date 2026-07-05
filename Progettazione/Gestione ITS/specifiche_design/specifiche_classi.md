## Specifica delle classi

Notare che Python è estremamente vicino allo pseudocodice. Quindi va bene utilizzare anche qualche 

```
Specifica classe CorsoITS

num_medio_esami_per_modulo(): RealGEZ
	algoritmo:

		tot_esami = 0
		num_moduli = 0

		per ogni m in self.modulo_in_corso:
			num_moduli = num_moduli + 1
			tot_esami = tot_esami + m.num_esami()

		try:
			result = tot_esami / num_moduli
		except ZeroDivisionError as e:
			e.add_note(f"Il CorsoITS {self} non ha moduli")
			raise e

```

```
Specifica della classe Studente

moduli_con_voto_piu_alto() : set[Modulo]
	algoritmo: 
		# i moduli per i quali lo studente 'this' ha preso voto_max
		result = {}
		voto_max = None
		
		per ogni link (this, m) in this.esame_superato:
			se voto_max is None or (this, m).voto > voto_max:
				result = { m }
		
		return result
```

- ignora al momento in quanto serve un'associazione bidirezionale.

```
Specifica della classe Modulo

num_esami() : IntGEZ
	algoritmo:
		return |len(this.esame_superato)|
```

```
Specifica della classe Docente

verbalizza_esame(m: Modulo, s: Studente) -> Voto:
	# pre: 
		- deve esistere il modulo associato m
		- deve esistere lo Studente s
		- deve esistere l'associazione esame_superato (m, s)
	
	# post:
		il docente crea v: Voto
		il docente inserisce un Voto v in (m, s): esame_superato
		return v
		

ottenere_voti_studente(s: Studente) -> voti[0..*]:
	# pre: 
		- deve esistere il modulo associato m
		- deve esistere lo Studente s
		- deve esistere l'associazione esame_superato (m, s)
	
	# post:
		result = {}
		se (m, docente) contiene docente # modulo di sua competenza
			per ogni associazione (m, s): esame_superato
				dall'associazione recupera v: Voto 
				a result aggiunge v
		return result 
```

```
Specifica della classe Segreteria

crea_corsi() -> CorsoITS[0..*]:
	
	# pre: 
		- il corso non deve già esistere (nome e edizione)
		  
	# post:
		result = {}
		se presenti altri corsi, inserirli in result
		per ogni input crea un nuovo corso:
			corso: CorsoITS = ottieni valori (nome: String, edizione: IntGEZ)
			se la coppia (nome, edizione) non è presente in result:
				result aggiungi il nuovo corso
		return result


crea_moduli() -> Modulo[0..*]
	
	# pre: 
		- il modulo non deve già esistere (codice univoco)
		  
	# post:
		result = {}
		se presenti altri moduli, inserirli in result
		per ogni input crea un nuovo corso:
			modulo: Modulo = ottieni valori (codice: String, nome: String, ore: IntGZ)
			se il codice non è presente in result:
				result aggiungi il nuovo modulo
		return result


registrare_docenti() -> Docente[0..*]:
	
	# pre: 
		- i docenti non devono già esistere (codice_fiscale univoco)
		  
	# post:
		result = {}
		se presenti altri docenti, inserirli in result
		per ogni input crea un nuovo docente:
			docente: Docente = ottieni valori (nome: String, conome: String, codice_fiscale: CodiceFiscale)
			se il codice_fiscale non è presente in result:
				result aggiungi il nuovo docente
		return result


somma_voti_studente(s: Studente) -> Integer:

	# pre:
		- deve esistere almeno un m: Modulo
		- deve esistere almeno uno s: Studente associato al modulo (m, s)
	
	result: Integer = 0
	
	per ogni m: Modulo in (m, s): 
		se esiste (s, m).esame_superato:
			v: Voto = (s, m).esame_superato.voto
			result += v
	
	return result


numero_voti_studente(s: Studente) -> Integer:
	
	# pre:
		- deve esistere almeno un m: Modulo
		- deve esistere almeno uno s: Studente associato al modulo (m, s)
	
	result: Integer = 0
	
	per ogni m: Modulo in (c, m).modulo_in_corso:   
		se esiste (s, m).esame_superato:
			result += 1
	
	return result


media_studente(s: Studente) -> Float:
	
	# pre:
		- deve esistere almeno un'associazione con un m: Modulo
		  
	# post:
		result: Float = 0.0
		somma = somma_voti_studente(s)
		numero = numero_voti_studente(s)
		
		# numero > 0 è sufficiente
		# somma non può essere 0 in quanto è un insime di voti
		# di tipo Voto che vale 18..30
		se numero > 0:
			result = somma / numero
			return result
			
		else:
			lancia eccezione, lo studente non ha ancora conseguito esami
 

voti_moduli_in_corso(c: CorsoITS) -> Voto[0..*]:
	
	# pre:
		- deve esistere il corso c
		- deve esistere almeno un m: Modulo
		- deve esistere almeno uno s: Studente associato al modulo (m, s)
	
	result: Voto[0..*] = {}
	
	per ogni s in (s, c):
		per ogni m in (m, c):
			se esiste (s, m).esame_superato:
				v: Voto = (s, m).esame_superato.voto
				result.aggiungi(v)
				
	return v



numero_iscritti_con_media(c: CorsoITS, x: Voto) -> Integer:
	
    # pre:
        - Il corso c deve esistere
	
    # post:
        result: Integer = 0

        per ogni s: Studente in (c, s).stud_corso:      # studenti iscritti a c
            media = media_studente(s)
            			
            se media_studente >= x:
                result += 1
		
        return result
        

numero_iscritti_corso(c: CorsoITS) -> Integer:
	
	# pre: 
		- deve esistere almeno un CorsoITS
		- deve esistere almeno uno Studente in quel corso (s, c)
		  
	# post:
		result: Integer = 0
		per ogni (s, c):
			result += 1
		retunr result


numero_iscritti_citta(c: Citta) -> Integer:

	# pre:
		- la c: Citta deve esistere 
		- la città deve avere almeno uno s: Studente associato (s, c)
		  
	# post:
		result: Integer = 0
		per ogni (s, c): citta_nascita:
			result += 1
		
		return result


numero_iscritti_regione(r: Regione) -> Integer:
	
	# pre:
		- La r: Regione deve esistere

	# post:
		result: Integer = 0
		per ogni (c: Citta, r):
			studenti_per_citta = numero_iscritti_citta(c)
			result += 1
		
		return result
		  

regione_maggior_numero_iscritti() -> Regione[0..1]:
	
	# pre:
		- deve esistere almeno una regione
		
	# post:
		result: Regione [0..*] = nullo
		max_iscritti = 0
		pre ogni r:
			curr_reg_iscritti = numero_iscritti_regione(r)
			if curr_reg_iscritti > max_iscritti:
				max_iscritti = curr_reg_iscritti
				result = r
		return result

```

```
Specifica della classe Amministratore

def crea_nazione

def crea_regione

def crea_citta

def crea_area_disciplinare
```