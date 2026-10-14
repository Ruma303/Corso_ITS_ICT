# Pattern di implementazione di associazione Doppia

Tieni presente il PDF delle associazioni a responsabilità doppia. quello è il pattern suggerito dal prof che ho riscritto e si può applicare in Python e Java. Concentriamoci su Python. 

Considerando il diagramma UML di design, ci sono diverse associazioni doppie. 

Concentriamoci ESCLUSIVAMENTE sull'associazione pubblica tra Post e Utente. L'interfaccia pubblica è in Post, perché i vincoli di molteplicità indicano che essa è la responsabile per creare le associazioni. D'altra parte, ho creato un metodo statico in Utente.create_pubblica() che richiama l'interfaccia Post.create_pubblica() in quanto per me ha senso che sia l'utente che crea il post. 

In ogni caso, quel che ti chiedo è di analizzare le varie classi per verificare se questa associazione è definita correttamente. NON analizzare altre associazioni come create_post_cat(), non analizzare i vari TODO da completare perché la classe Post non è ancora completa.

Inoltre, nelle classi concrete non era richiesto creare dei set di classe dei vari link, ma vorrei crearli per tenerne traccia, in quanto saranno utili per operazioni successive. Quel che realmente serve sono che:

- se l'associazione è unica (es. 1..1): va impostata con un metodo comunemente chiamato _set_nomelink_link(), e _remove_nomelink_link()
	- Aggiunta: come avviene in Post.__nomelink_link = link per crearlo 
	- Rimozione: impostando Post.__nomelink_link = None per rimuoverlo (in Python non si possono distruggere oggetti, quindi vanno invalidati)

- se l'associazione è un'insieme (es. 0..*): i link vengono aggiunti al set di istanza (di solito uno alla volta) che contiene i link usando un metodo comunemente chiamato _add_nomelink_links(), e _remove_nomelink_links()
	- Aggiunta: il Post.__nomelinks_links.add() in un set o, ancora meglio, un frozenset dato che i link per definizione sono immutabili
	- Rimozione: avviene ricreando il set o usando del / discard(). In maniera identica se si usano altre strutture dati come frozenset o dizionari.

# Navigabilità 
La linea continua in un’associazione - come post_cat - indica navigabilità doppia. Le categorie possono conoscere quali post hanno (insieme di post 0..* per singola categoria).

La navigabilità singola è designata dalla freccia. In questo caso si usa l’aggregazione, ovvero una semplice dipendenza nel costruttore della classe che ha visibilità/responsabilità sull'altra. Non serve una classe per associazione doppia. 
