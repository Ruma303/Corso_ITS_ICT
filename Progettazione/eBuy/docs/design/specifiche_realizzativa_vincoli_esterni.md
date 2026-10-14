# Specifica realizzativa vincoli esterni - Design

## Specifiche per classe Utente

[V.Utente.Acquirente_o_venditore_complete]
- Descrizione: Realizzazione del vincolo di generalizzazione {complete}
- Nota bene: le istanze di Utente possono cambiare la loro specializzazione a runtime in quanto non sono disjoint. Un acquirente può diventare un Venditore e viceversa.
- Invarianti:
  - u is-a Venditore se e solo se u.garanzia è valorizzato
  - u is-a Veditore se e solo se u è coinvolto in un link (u, p: Post) : popolarita
  - u is-a Acquirente se e solo se u è coinvolto in un link (u, p: Post) : acquista 
  - u is-a Acquirente se e solo se u è coinvolto in un link (u, p: Post) : bid
  - u is-a Acquirente se e solo se u è coinvolto in un link (u, met_pag: MetodoPagamento) : paga_con


[V.Utente.Venditore_o_venditore_professionale]
- Descrizione: Realizzazione del vincolo di generalizzazione tra le classi Venditore e VenditoreProfessionale
- u is-a VenditoreProfessionale se u.garanzia è int >= 2 anni
- u is-a VenditoreProfessionale se e solo se u.url è valorizzato



## Specifiche per classe Post

[V.Post.scadenza_non_inferiore_a_pubblicazione]
- Descrizione: La data di scadenza non può essere inferiore o uguale all'istante di pubblicazione del post
- p.ist_pubbl < p.scadenza()

[V.Post.asta_o_compralo_subito]
- Descrizione: Tutte le istanze p devono essere specializzate in post con tipologia "Asta" o "CompraloSubito"
- p is-a Asta se e solo se p.durata è valorizzato
- p is-a Asta se e solo se p.rialzo è valorizzato
- p is-a Asta se e solo se ha un'operazione p.ammontare()
- p is-a Asta se e solo se ha un'operazione p.ottieni_vincitore()
- p is-a Asta se e solo se ha un'operazione p.scadenza()
- p is-a Asta se e solo se è coinvolto in un link di associazione (p, u: Utente) : bid
-- quando posso dire che p is-a CompraloSubito? Mi basta != tutte le condizioni sopra?

[V.Post.nuovo_o_usato]
- Descrizione: Un post può avere soltanto due stati: nuovo oppure usato
- p.stato = Usato XOR Nuovo

[V.Post.condizioni_se_usato]
- Realizzazione del vincolo {disjoint} 
- Descrizione: Soltanto per i Post Usati va specificata la condizione
- Se e solo se p.stato è "Usato", p.condizione è valorizzato con un valore dell'enumerazione Condizione


## Specifiche per classe MetodoPagamento

[V.MetodoPagamento.bonifico_o_carta_credito]
- Realizzazione del vincolo {disjoint} 
- Descrizione: I metodi di pagamento accettati possono essere soltanto Bonifico o CartaDiCredito
- p is-a Bonifico XOR CartaDiCredito
