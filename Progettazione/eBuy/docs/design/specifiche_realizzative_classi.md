# Specifiche realizzative di classi ristrutturata

## Classe Asta

scadenza() : datetime
  - algoritmo:
    - result = this.ist_pubbl + this.durata

  
prezzo_finale() : FloatGEZ
  - pre:
    p.tipologia = Asta
  	p.scadenza() != 0 # l'asta non dev'essere conclusa
    p.prezzo >= 0
    p.rialzo >= 0

  - algoritmo:
		# Ogni invocazione di questa operazione incrementa un contatore di classe "numero_rialzi"
    numero_rialzi = 0
    for b in SOMMA(bid) # insieme di associazioni (u: Utente, p: CompraloSubito): bid
  		numero_rialzi = numero_rialzi + 1
  
	  result = p.prezzo + (rialzo x numero_rialzi)

ottieni_vincitore() # non so se è uno use-case