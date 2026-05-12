# Obiettivi 1

## Specifica della classe CodiceFiscale

CodiceFiscale: String ~ /^[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]$/i

### Approfondimenti Regex Codice Fiscale
^
[A-Z]{6}          → cognome (3) + nome (3)
\d{2}             → anno nascita
[ABCDEHLMPRST]    → mese (solo queste 12 lettere, una per mese)
\d{2}             → giorno/sesso (01-31 o 41-71)
[A-Z]             → lettera del codice comune (es. F=Roma, L=Milano)
\d{3}             → cifre del codice comune
[A-Z]             → check digit
$


# Obiettivi 2

Estendere lo schema concettuale del progetto “Gestione ITS” definendo le operazioni di classe necessarie a modellare i requisiti ulteriori indicati di seguito. 

## Specifica dei requisiti aggiuntivi

1. Per ogni studente ‘s’ il sistema deve restituire tutti i moduli nei quali ‘s’ ha preso il voto più alto tra quelli di cui ha sostenuto l’esame. Ad esempio, se ‘s’ ha superato il modulo “M1” con 27, i moduli “M2” ed “M3” con 28 ed il modulo “M4” con 25, l’operazione deve restituire “M2” ed “M3”. 

```md
Specifica della classe Studente

ottieni_esami_con_voti_più_alti(s: Studente): {Modulo}

	# pre-condizioni:
	# per ogni s deve esistere almeno un esame superato
	
	# ogni esame è un dizionario che contiene il voto dell'esame e il nome del modulo
	esami_superati: {(this, m).voto, m.nome} = {} 
	
	for esame in (this, m: Modulo): esame:
		esami_superati += (this, m).voto
		esami_superati += this.nome
		
	se non esiste almeno un (this, m): esame -> return {}
		
		
	# algoritmo
	moduli = {}
	max_voto = 0
	
	for esame in esami_superati:
		voto_corrente = (this, m).voto
		
		se max_voto non è definito oppure se voto_corrente > max_voto:
			max_voto = voto_corrente
			moduli = { m } # reset del nuovo modulo con voto massimo trovato

		altrimenti, se voto_corrente == max_voto:
			moduli += { m } # aggiunta modulo con voto massimo trovato

		altrimenti:
			ignora
	
	return moduli
	
```


2. Per ogni corso ‘c’, il sistema deve calcolare il numero medio di esami registrati per i diversi moduli.

```md
Specifica della classe Corso

# un corso è in relazione con più moduli
# ogni modulo è in relazione con studenti creando una classe associativa "esame"
# prendere il numero di esami di ogni modulo e fare una media con il numero di moduli del corso


numero_medio_esami(): Real >= 0

    # pre-condizione:
    # se non esiste almeno un (this, m: Modulo): mod_corso → return 0

    # algoritmo
    totale_esami = 0
    num_moduli = 0

    per ogni (this, m: Modulo): mod_corso:
        num_moduli += 1

        per ogni (m, s: Studente): esame:
            totale_esami += 1

    se num_moduli == 0:
        return 0

    return totale_esami / num_moduli
	
```