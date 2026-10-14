# Specifiche realizzative di classi ristrutturata

## Classe Asta

scadenza() : datetime
  - algoritmo:
    - result = this.ist_pubbl + this.durata

  
ammontare(p: Post) : FloatGEZ
  - pre:
    - p.prezzo >= 0
    - p.tipologia = Asta
    - p.rialzo >= 0

  - algoritmo:
    - result = p.prezzo + p.rialzo


ottieni_vincitorer() # non so se è uno use-case