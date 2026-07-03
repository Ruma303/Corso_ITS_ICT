# Classi

## 1. Requisiti sui Voli

Di ogni volo ci interessa rappresentare:
	1.1 codice_v;
	1.2 durata;
	
	911. Aeroporto di arrivo
	912. Aeroporto di partenza
	913. La durata sarà espressa come intero positivo che esprime il tempo in minuti
	914. Un volo appartiene ad una compagnia aerea. Sarà necessario un'associazione


## 2. Requisiti sugli Aeroporti
	2.1 codice_a;
	2.2 nome;
	
	921. Ogni aeroporto è situato con una Nazione. Serve un'associazione
	922. La città sarà un'entità autonoma espressa con
		922.1 nome città;
		922.2 numero_abitanti intero positivo;


## 3. Requisiti sulle CompagnieAeree
	3.1 nome;
	3.2 anno_fondazione;
	
	931. Sarà necessario definire l'associazione in una città per la sua sede direttiva


## 4. Città
	4.1 nome
	4.2 numero abitanti


## 5. Regione
	5.1 nome


## 6. Nazione
	6.1 nome


# Associazioni

	A1. Ogni Aeroporto è situato in una Città: 0..* -- aerop_città -- 0..1
	A2. Ogni CompagniaAerea ha sede in una Città: 0..* -- comp_città -- 0..1
	A3. Le città non esistono da sole, si trovano in regioni che si trovano in nazioni
		A3.1 0..* Città -- città_regione -- 0..1 Regione
		A3.2 0..* Regione -- reg_naz -- 0..1 Nazione
