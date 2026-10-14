# Classi, attributi, vincoli (V), operazioni (O), associazioni (A), use-case (U)

1. Degli utenti registrati interessa:
  1.1 nome utente univoco
  1.2 data di registrazione
  V.1.3 poter pubblicare un singolo oggetto per ogni annuncio
  1.4 ogni utente può essere sia un Acquirente che un Venditore
  1.5 ogni Venditore può essere anche un VenditoreProfessionale
    1.5.1 i venditori professionali possono vendere oggetti in condizione Nuovo
    V.1.5.2 i venditori prof. interessa l'url della loro vetrina on-line
  V.1.6 ogni venditore deve prevedere una garanzia 
    V.1.6.1 minima di 0 anni se condizione Post è Usato
    V.1.6.2 minima di 2 anni se condizione Post è Nuovo
  V.1.7 solo gli utenti Acquirenti possono acquistare o proporre bid
  V.1.8 gli utenti Venditori possono solo vendere (pubblicare)
  1.9 dei venditori professionali è interesse conoscere la popolarità

2. Dei post interessa:
  2.1 il venditore (v. req. 1)
  2.2 la data di pubblicazione (istante)
  2.3 la descrizione
  2.4 categoria (v. req. 3)
  2.5 prezzo di vendita
    V.2.5.1 prezzo da specificare alla creazione del post
  2.6 stato ("nuovo" oppure "usato")
  2.7 tipologia ("asta" o "compra subito")
  2.8 dei post di tipologia "asta" interessa:
    2.8.1 prezzo iniziale
    2.8.2 ammontare rialzo 
    2.8.3 istante scadenza dell'asta
    V.2.8.4 rialzo fisso per le aste
    O.2.8.5 Le aste vengono automaticamente chiuse alla data/ora specificata dal venditore (v. req. U.2.4)
  2.9 della tipologia "compra subito" interessa:
    2.9.1 solo il prezzo di partenza (v. V.2.5.1)
  2.10 metodi di pagamento (v. req. 4)
  2.11 di ogni asta conclusa interessa conoscere 
    2.11.1 il bid che si è aggiudicato l'oggetto (se esiste) 
    2.11.2 il prezzo del bid
  2.12 per gli oggetti con stato "Usato" è necessario conoscere la loro condizione:
    - ottimo, buono, discreto, da sistemare

3. Delle categorie interessa:
	3.1 nome
  3.2 gerarchia (v. req. U.2.6) 

4. Dei metodi di pagamento interessa:
  4.1 nome
	V.4.2 possono essere esclusivamente "Bonifico" o "Carta di Credito"


Il sistema deve consentire di:
- U.1 agli utenti via web di pubblicare post di tipo "asta" XOR "compra subito"
  - U.1.1 il primo utente che compra da un post di tipologia "compra subito" si aggiudica l'articolo
  - U.1.2 i post che di tipologia "asta" sono soggette a offerte (bid) - (v. req. A.1)
  - U.1.3 l'utente che offre un post di tipo "asta" si offre ad acquistarlo al prezzo che è l'ultimo prezzo fino a quel momento + p.rialzo
  - U.1.4 l'ultimo utente che ha effettuato un bid si aggiudica l'oggetto al prezzo del bid. 

- U.2 il sistema organizza gli articoli tramite categorie in ordine gerarchico ad albero
  - U.2.1 da una categoria dev'essere possibile ricavare l'insieme delle sottocategorie

- U.3 gli utenti possono esprimere giudizi (feedback) dopo aver acquistato articoli in modalità CompraloSubito
  - U.3.1 I feedback sono un voto numerico tra 0 (non soddisfatto) e 5 (molto soddisfatto)
  - si può aggiungere un commento testuale
- U.4 l'affidabilità di un vendtore si calcola a partire dai suoi feedback
  - U.4.1 media di tutti i feedback meno un fattore
  - U.4.2 il fattore è tanto più grande quanto è maggiore il numero di feedback negativi (<= 2). 
  - U.4.3 Il fattore z è calcolato come somma(feedback negativi) / somma(feedback totali)
  - U.4.4 l'affidabilità è m(1 - z) / 5. È quindi un valore reale tra 0 e 1


A.1 l'associazione "bid" è composta da (u: Utente, p: Post):
  - A.1.1 il post dev'essere di tipo "asta"
  - A.1.2 di ogni bid interessa:
    - A.1.2.1: istante in cui è stato creata l'offerta
    - A.1.2.2: l'utente u offerente (bidder)

A.2 l'utente di tipo "venditore" può mettere in vendita un p: Post, creando l'associazione (u, p): pubblicazione

A.3 la popolarità dei venditori professionali è così calcolato:
  - insieme di utenti che hanno effettuato bid per i loro articoli negli ultimi 12 mesi
  - oppure, numero utenti che hanno acquistato articoli in modalità compralo subito.
  - popolarità bassa < 50, 50>= media <=300, alta > 300