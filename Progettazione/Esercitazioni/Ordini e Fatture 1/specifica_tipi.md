# Specifica tipi di dato

```md
Indirizzo: (
  via: String
  civico: String ~ '[0-9]+(/[a-z]+){0,1}'
)
```

```md
CodiceFiscale: String ~ /^[A-Z]{6}\d{2}[ABCDEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]$/i
```

```md
PartitaIVA: String ~ /^IT\d{11}$/i
```

```md
Email: String ~ /^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$/
```

```md
Telefono: String ~ \+?[0-9]{0,15}
```

```md
Real_0_1: Real >= 0 and <= 1
```

```md
StatoOrdine: = { in_preparazione, inviato, da_saldare, saldato }
```

```md
RagioneSociale = String ~ /^.{2,255}$/
```