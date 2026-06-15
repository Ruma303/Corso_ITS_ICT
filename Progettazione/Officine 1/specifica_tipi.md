Specifica dei tipi di dato

Telefono: String ~ ^(?:(?:\+|00)39)?\s?[3]\d{2}(?:\s?\d{3,4}){2,3}$
- Regex volutamente molto ampia

TipoVeicolo : { Autovettura, Motociclo, Autocarro, Furgone, Altro }
- Il simbolo Altro serve a racchiudere qualsiasi altro tipo di veicolo non inserito nell'enumerazione per conferire maggiore flessibilità


Targa : String ~ [A-Z0-9]{3,7}
- Le targhe possono essere molto varie e sono cambiate costantemente dagli anni '30 in poi
- Questa è una regex appositamente molto ampia
- La targa da sola non consente l'univocità del veicolo. Quindi fa parte di un vincolo d'integrità composto


CodiceFiscale : String ~ [A-Z0-9]{0,16}
- Anche questa è una regex tenuta volutamente molto ampia


StatoRiparazione : { PRESO_IN_CARICO, IN_LAVORAZIONE, CONCLUSO }
-  Esempi di stati di una riparazione definiti come simboli di un'enumerazione


Indirizzo : (
	via: String
	civico: String
)
- È necessario introdurre il campo composto "indirizzo" in quanto possono esistere più officine con lo stesso nome e nella stessa città
- Il vincolo di integrità sarà composto tra il nome dell'officina unito al campo indirizzo
- Il sistema quindi ammetterà due officine con lo stesso nome e nella stessa via, ma non con lo stesso civico


CAP : String ~ [0-9]{5}
- Una città può avere più cap, quindi serve una molteplicità [1..*]
