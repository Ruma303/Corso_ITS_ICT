# Specifica Classi

```
Direttore
	nome: String
	cognome: String
	codice_fiscale: CodiceFiscale 
	data_nascita: Date
	luogo_nascita: (this, Città) # relazione con Città
	anni_servizio: Integer >=0
```

```
Dipartimento
	nome: String
	indirizzo: (this, Città) # relazione con Città
	direttore: Direttore [0..1]
```

```
Fornitore
	ragione_sociale: String
	partita_iva: PartitaIVA
	indirizzo: (this, Città) # relazione con Città
	telefono: String
	email: Email [0..*]
```

```
Città
	nome: String
```

```
Regione
	nome: String
```

```
Nazione
	nome: String
```

```
Ordine
	tipologia: Bene | Servizio
	dipartimento: Dipartimento
	data: Data
	fornitore: Fornitore
	descrizione: String
	imponibile: Integer >= 0
	aliquota: Percentuale (Reale) >= 0
	stato: {in_preparazione, inviato, da_saldare, saldato}
```

```
Fattura
	ordine: (this, Ordine) # relazione con Ordine
```

```
Bene
	nome: String
```

```
Servizio
	nome: String
```

---

# Classi di supporto

```
CodiceFiscale: String ~ /^[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]$/i
```

```
PartitaIVA: String ~ /^IT\d{11}$/i
```

```
Email: String ~ /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$/
```

---

# Associazioni

```
Direttore 0..1 -- dirige -- 0..1 Dipartimento
```

```
Dipartimento 0..* -- ordine -- 0..* Fornitore
```

```
Ordine 1..* -- ordine_fattura -- 0..* Fattura
```

```
Ordine 0..* -- tipologia_bene -- 0..* Bene
```

```
Ordine 0..* -- tipologia_servizio -- 0..* Servizio
```

```
Direttore 0..* -- luogo_nascita -- 0..1 Città
```

```
Dipartimento 0..* -- dip_citta -- 0..1 Città
```

```
Fornitore 0..* -- citta_fornitore -- 0..1 Città
```

```
Città 0..* -- città_reg -- 0..1 Regione
```

```
Regione 0..* -- reg_naz -- 0..1 Nazione
```
