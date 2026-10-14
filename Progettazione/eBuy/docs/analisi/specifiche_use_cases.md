# Specifica use-case Pubblicazione post

L'utente può creare un post che sarà di tipologia Asta oppure CompraloSubito

pubblica(
	vend: Utente,
	istante_pubbl: DataOra,
	desc: Stringa,
	prezzo: RealGEZ,
	val: Valuta,
	cat: Categoria,
	met_pagam: MetodoPagamento [1..*],
	tipologia: Tipologia,
	rialzo: RealGZ [0..1],
	durata: Durata [0..1],
	stato: Stato,
	condizione: Condizione,
	is_venduto = Boolean
): Post

    pre:
    	tipologia=asta se e solo se rialzo ha un valore
    	and
    	tipologia=asta se e solo se durata ha un valore;

    post:
    	- result.istante_pubbl = istante_pubbl;
    	- result.descrizione = desc;
    	- result.prezzo = prezzo;
    	- result.stato = stato;
    	- result.condizione = condizione;
    	- result.is_venduto = FALSE; // default

    	Se tipologia = asta, allora:
    		- viene creato result: Asta;
    		- result.rialzo = rialzo;
    		- result.durata = durata;

     altrimenti viene creato
     		- result: CompraloSubito;

    	Viene creato il link (vend, result): pubblica;
    	Viene creato il link (result, cat): post_cat;
    	Viene creato il link (result, val): post_valuta;
    	Per ogni m in met_pagam:
    		viene creato un link (result, m): post_metodo_pag


# Specifica use-case Acquista - Compra Subito di Acquirente

Il primo utente che acquista in modalità compralo subito si aggiudica già l'oggetto

acquista(
	u: Utente,
	p: Post,
	is_ venduto : Boolean
): void // Non ritorna nulla, esegue un'operazione

    pre:
    	- p dev'essere di tipologia = CompraloSubito
    	- p.is_venduto dev'essere FALSE

    post:
    	- p.is_venduto diventa TRUE
    	- Creazione del link (u, p): acquista


# Specifica use-case offerta ("bid") da Acquirente

Un utente può piazzare un'offerta che aumenta il prezzo con il rialzo indicato nel Post
Un utente può piazzare 0..* bid

bid(
	u: Utente,
	p: Post,
	istante_pubbl: DateTime
): bid

- pre:
  - p.tipologia dev'essere di tipo Asta
  - p.scadenza() non dev'essere 0. L'asta dev'essere ancora attiva
  - l'utente (bidder) dev'essere di tipo Acquirente. Non può essere un Venditore
  - istante_pubbl: dev'essere compreso tra gli intervalli (p.istante_pubbl, p.scadenza()]

- post:
  - il risultato modifica il livello estensionale dell'istanza corrente del post
  - viene creato un link (u, p): bid
  - viene invocata l'operazione p.prezzo_totale() che aggiunge un nuovo rialzo prestabilito


# Specifica use-case Chiusura Asta

Le aste vengono automaticamente chiuse alla data/ora specificata dal venditore. L'ultimo utente che ha effettuato il bid si aggiudica l'oggetto in vendita al prezzo del bid. Recuperare anche il prezzo finale.

# Da completare

chiusura_asta(
	p: Post,
	b: bid [0..1],
	u: Utente,
	prezzo: RealGEZ
): (Utente, RealGEZ) // tupla (insieme) di valori

- pre:
  - se b DEVE esistere
  - p dev'essere di tipologia = Asta
  - b dev'essere coinvolto in un link (p, u): bid
  - u è l'ultimo utente in ordine di tempo (calcolato dagli insieme B di link bid.istante_pubbl)

- post:
  // recuperare sia l'utente vincitore che il prezzo
  - il prezzo_finale che l'utente pagherà è p.prezzo_totale() del Post
  - il risultato è un'insieme (u, prezzo_finale), ovvero l'utente vincitore e il prezzo complessivo del post



# Specifica use-case Feedback


# Specifica use-case Affidabilità