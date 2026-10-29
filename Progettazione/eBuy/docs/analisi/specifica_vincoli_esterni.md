# Specifica vincoli esterni - Analisi

## Specifiche per classe Utente

[V.Utente.Acquirente_o_venditore_complete]
- Descrizione: Realizzazione del vincolo di generalizzazione {complete}
- Invarianti:
  - u is-a Venditore se e solo se u.garanzia è valorizzato
  - u is-a Veditore se e solo se u è coinvolto in un link (u, p: Post) : popolarita
  - u is-a Acquirente se e solo se u è coinvolto in un link (u, p: Post) : acquista 
  - u is-a Acquirente se e solo se u è coinvolto in un link (u, p: Post) : bid


[V.Utente.Venditore_o_venditore_professionale]
- Descrizione: Realizzazione del vincolo di generalizzazione tra le classi Venditore e VenditoreProfessionale
- u is-a VenditoreProfessionale se u.garanzia è int >= 2 anni
- u is-a VenditoreProfessionale se e solo se u.url è valorizzato


[V.Utente.pubblica_singolo_post]
TODO: Un utente può pubblicare un singolo Post alla volta


## Specifiche per classe Post

[V.Post.scadenza_non_inferiore_a_pubblicazione]
- Descrizione: La data di scadenza non può essere inferiore o uguale all'istante di pubblicazione del post
- Contesto: per ogni istanza p di Post
- Invariante: p.istante_pubbl < p.scadenza()

[V.Post.asta_o_compralo_subito]
- Descrizione: Non esistono istanze di Post a se stanti. Tutte le istanze p devono essere specializzate in post con tipologia "Asta" o "CompraloSubito"
- Contesto: per ogni p: Post
- Invariante: p is-a Asta oppure CompraloSubito

[V.Post.nuovo_o_usato]
- Descrizione: Un post può avere soltanto due stati: nuovo oppure usato
- Contesto: per ogni p: Post
- Invariante: p.stato può essere esclusivamente Usato XOR Nuovo

[V.Post.condizioni_se_usato]
- Descrizione: Soltanto per i Post usati va specificata la condizione
- Contesto: per ogni p: Post
- Invariante: se p.stato è "Usato", va specificata la condizione dell'oggetto con un valore dell'enumerazione Condizione


## Specifiche per classe MetodoPagamento

[V.MetodoPagamento.bonifico_o_carta_credito]
- Descrizione: I metodi di pagamento accettati possono essere soltanto Bonifico o CartaDiCredito
- Contesto: per ogni istanza mp di MetodoPagamento
- Invariante: p is-a Bonifico oppure CartaDiCredito
