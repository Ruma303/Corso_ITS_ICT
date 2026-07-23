# Vincoli esterni - Livello 1

[V.Persona.cliente_o_dipendente_o_direttore]

Vincoli esterni: per ogni istanza p di Persona:
  p è coinvolto in un link "proprietario" --> p.is_cliente = TRUE
  p.is_dipendente = TRUE se e solo se p è coinvolto in un link è "lavora"
  p.is_direttore = TRUE se p è coinvolto in un link "dirige"
  p.is_direttore = TRUE se e solo se p.data_nascita è valorizzato
   