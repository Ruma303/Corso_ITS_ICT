Costruisci una pagina **nuova e scollegata dalla dashboard**: la vetrina di una piccola libreria. Una navbar di navigazione + una griglia di 3 card-libro responsive. Usa **solo** le classi viste finora in questo blocco (CDN, griglia, breakpoint, gutter, palette, navbar con toggler, card con badge e bottone in fondo). Niente immagini, niente form, niente alert/modal: arrivano nei blocchi dopo.

### Consegna
Crea `libreria.html` (pagina a parte, NON toccare la dashboard) con:
- Bootstrap collegato via **CDN** (CSS nell'`<head>`, JS bundle in fondo al `<body>`) + **meta viewport**
- Una **navbar** `bg-dark`/`navbar-dark`, `sticky-top`, `navbar-expand-lg`, con brand, 3 voci di menu, un bottone a destra e il **toggler** hamburger funzionante
- Un **titolo** di sezione e una **griglia** `row g-4` con 3 card in `col-12 col-md-6 col-lg-4`
- Ogni **card**: badge in alto a destra (su 2 card: una `bg-success` "Novità" e una `bg-danger` "Esaurimento"; la terza senza badge), `card-body` con `card-title` (titolo), `card-text` (autore + descrizione + prezzo), bottone `btn-primary` **in fondo** alla card

### Criteri di accettazione
- [ ] Su **desktop** (≥992px): 3 card **affiancate**, tutte della **stessa altezza**, bottoni allineati in fondo.
- [ ] Su **tablet** (768–991px): **2 card sopra + 1 sotto**.
- [ ] Su **mobile** (<768px): card **impilate**, navbar diventata **hamburger** e il menu si **apre** cliccando.
- [ ] I badge stanno **ancorati in alto a destra** della loro card.
- [ ] I colori vengono dalla **palette Bootstrap** (`bg-dark`, `btn-primary`, `bg-success`, `bg-danger`) — niente nomi inventati (`bg-green`, ecc.).
- [ ] **Zero CSS custom**: tutto con le classi Bootstrap.

### Svolgimento (30 min, può sforare)

### Regole
- **Niente copia/incolla** dalla mia versione: ricostruisci dalle tue note + la doc.
- Una pagina **a parte**, non la dashboard.

[Documentazione](https://getbootstrap.com/docs/5.3/getting-started/introduction/)