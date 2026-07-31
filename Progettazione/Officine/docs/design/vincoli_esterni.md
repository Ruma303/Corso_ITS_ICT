# Vincoli esterni - Livello 1

[V.Riparazione.in_corso_o_terminata]
Per ogni istanza r di Riparazione:
  r.is_terminata = TRUE se e solo se r.riconsegna è valorizzato  


[V.MembroStaff.dipendente_o_direttore]
Per ogni istanza m di MembroStaff:
  m.is_dipendente = TRUE se e solo se è conivolto in un'associazione "lavora"
  m.is_dipendente = TRUE se e solo se m.data_assunzione è valorizzato
  m.is_direttore = TRUE se e solo se è conivolto in un'associazione "dirige"
  m.is_direttore = TRUE se e solo se m.data_nascita è valorizzato


[V.Persona.cliente_o_membro_staff]
Per ogni istanza p di Persona:
  p è coinvolto in un link "lavora" --> p.is_membro_staff = TRUE
  p è coinvolto in un link "dirige" --> p.is_membro_staff = TRUE
  p è coinvolto in un link "proprietario" --> p.is_cliente = TRUE
  p.is_membro_staff = TRUE se e solo se p.data_nascita è valorizzato


---

# Vincoli esterni - Livello 2

[V.Persona.cliente_o_dipendente_o_direttore]
Per ogni istanza p di Persona:
  p è coinvolto in un link "proprietario" --> p.is_cliente = TRUE
  p.is_dipendente = TRUE se e solo se p è coinvolto in un link è "lavora"
  p.is_direttore = TRUE se p è coinvolto in un link "dirige"
  p.is_direttore = TRUE se e solo se p.data_nascita è valorizzato

  # Vincolo di completezza
  p.is_cliente = TRUE or p.is_dipendente = TRUE or p.is_direttore = TRUE