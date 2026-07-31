Specifica dei tipi di dato

Telefono: String ~ (?:(?:\+|00)39)?\s?[3]\d{2}(?:\s?\d{3,4}){2,3}
- Regex volutamente molto ampia


Targa : String ~ [A-Z0-9]{3,7} | [\W]{1,2}\s*[\d]{1,6}
- Le targhe possono essere molto varie e sono cambiate costantemente dagli anni '30 in poi
- La targa da sola non consente l'univocità del veicolo. Quindi fa parte di un vincolo d'integrità composto


CodiceFiscale : String ~ [A-Z0-9]{0,16} 
- Usiamo un paio di regex: una volutamente molto ampia e un'altra più precisa


Indirizzo : (
	via: String
	civico: String ~ [0-9]+(/[A-Za-z]+)?
	cap: CAP
)
- È necessario introdurre il campo composto "indirizzo" in quanto possono esistere più officine con lo stesso nome e nella stessa città
- Il vincolo di integrità sarà composto tra il nome dell'officina unito al campo indirizzo
- Il sistema quindi ammetterà due officine con lo stesso nome e nella stessa via, ma non con lo stesso civico


CAP : String ~ [0-9]{5}
- Una città può avere più cap, quindi serve una molteplicità [1..*]
 