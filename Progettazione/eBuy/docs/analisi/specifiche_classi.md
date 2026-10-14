# Specifica operazioni Post

scadenza(): DataOra
  - pre: 
	  - p. tipologia dev'essere di tipo Asta
  - post:
    - result = this.istante_pubbl + this.durata


prezzo_finale(p: Post): RealGEZ
	- pre:
	  - p.tipologia dev'essere un'Asta
	  - p.prezzo dev'essere >= 0
	  - p.rialzo dev'essere >= 0
	
	- post:
	  - l'operazione NON modifica il livello estensionale dell'istanza p
		- Ogni invocazione di questa operazione incrementa un contatore di classe "numero_rialzi"
	  - result = p.prezzo + SOMMA(numero_rialzi)