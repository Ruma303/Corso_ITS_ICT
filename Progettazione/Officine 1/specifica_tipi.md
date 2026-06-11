Specifica dei tipi di dato

Telefono: String ~ ^(?:(?:\+|00)39)?\s?[3]\d{2}(?:\s?\d{3,4}){2,3}$
- Regex volutamente molto ampia


Targa : String ~ [A-Z0-9]{3,7}
- Le targhe possono essere molto varie e sono cambiate costantemente dagli anni '30 in poi
- Questa è una regex appositamente molto ampia
- La targa da sola non consente l'univocità del veicolo. Quindi fa parte di un vincolo d'integrità composto


CodiceFiscale : String ~ [A-Z0-9]{0,16} {id}
- Anche questa è una regex tenuta volutamente molto ampia


StatoRiparazione : { non_iniziata, in_lavorazione, conclusa }
-  Esempi di stati di una riparazione definiti come simboli di un'enumerazione


Indirizzo : (
	via: String {id}
	civico: String {id}
	cap: String ~ [0-9]{5} {id}
)
- È necessario introdurre il campo composto "indirizzo" in quanto possono esistere più officine con lo stesso nome e nella stessa città.
- Il vincolo d'integrità sarà quindi condiviso tra la classe Officina e Città
- Il campo composto contiene dei sotto-campi via, civico e cap. Insieme, costituiscono il vincolo d'integrità della classe.