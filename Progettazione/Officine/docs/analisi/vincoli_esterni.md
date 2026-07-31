# Vincoli esterni

[V.RiparazioneTerminata.riconsegna_dopo_accettazione]
  Per ogni r: RiparazioneTerminata, deve essere:
    r.riconsenga > r.accettazione


[V.Veicolo.targa_legale]
	Per ogni v:Veicolo,
		sia n:Nazione la nazione associata a v (dal link di assoc. naz_veic)

		deve essere:
			v.targa ~ n.regex_targa