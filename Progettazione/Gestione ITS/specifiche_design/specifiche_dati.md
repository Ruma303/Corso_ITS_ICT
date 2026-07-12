# Specifica dei dati

```md
CodiceFiscale(input: str) -> this:
		pattern: '[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[0-9A-Za-z]{5}'

    se input non corrisponde a pattern
      return error

    # istanziare il costruttore str per tornare un'istanza di
    # str, poi valorizzarla nel costruttore di CodiceFiscale
		return super(input.upper())


IntGZ(v:int|float)->this: ## Maggiore di 0
    int(v) # casting esplicito int
		se v <= 0:
			ritorna errore
		return super(v)


IntGEZ(v:int|float)->this: ## Maggiore o uguale a 0
    int(v) # casting esplicito int
		se v < 0:
			ritorna errore
		return super(v)


Voto(v:int|float)->this:
    int(v) # casting esplicito int
	  se non (v >= 6 e v <= 10):
			ritorna errore
		return super(v)


RealGEZ(v:int|float)->this:
    float(v) # casting esplicito float (opzionale)
		se v < 0:
			ritorna errore
		return super(v)
```