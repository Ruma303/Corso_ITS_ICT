Rifai sul tuo PC la stessa trasformazione da CSS-a-mano a Bootstrap che hai visto nel live coding — ma partendo dai tuoi file della Lezione 3 (centro-sportivo.html + style.css, la dashboard che già conoscete) ed evolvendoli in Bootstrap, sezione per sezione, sostituendo via via il CSS custom con le classi Bootstrap.

Partenza: apri i tuoi file L3 (centro-sportivo.html + style.css) nella cartella di progetto. Lavori su questi file (in luogo — se vuoi conservare la versione docente, fanne una copia prima). Non creare una nuova pagina scollegata: ripercorri lo stesso percorso visto nel live coding (CDN → griglia → navbar → card → form → modal → utility → immagini → tabella → pulizia style.css). L'obiettivo è consolidare esattamente i concetti di oggi, applicandoli da capo da soli.

Consegna (il compito principale)
Replica la dashboard Bootstrap che ho costruito io nel live coding, partendo dai file L3:

collega il CDN
ricostruisci la griglia con container/row/col
breakpoint, la navbar responsive con il toggler
le card con badge e bottone
il form a colonne
il modal di conferma sul bottone "Prenota"
la struttura del toast (il wiring JS lo faremo in L5 — oggi solo il markup)
i colori/varianti (bg-*/btn-*/text-*)
le utility di spaziatura/flex + l'immagine fluida (img-fluid)
la tabella degli orari in #info
#eventi e #info resi card (riusando griglia + card + tabella), con titoli di sezione allineati, sezioni in py-5 + container e sfondi alternati con bg-light
Alla fine riduci il tuo style.css.
Criteri di accettazione (cosa deve risultare)
Aprendo la pagina su desktop: navbar, hero, card allineate, form a colonne, alert.
Restringendo sotto 992px: la navbar diventa hamburger e si apre cliccandolo.
Restringendo sotto 768px: le card si impilano (una per riga) e il form diventa una colonna.
L'immagine è fluida (niente scroll orizzontale su mobile) e ha l'alt.
Il bottone "Prenota" apre il modal di conferma (senza scrivere JS).
La struttura del toast è presente (la riga di JS per mostrarlo arriverà in L5).
Gli orari di #info sono una tabella table table-striped.
#eventi e #info sono card in griglia (non più <article>/<p> nudi); i titoli di sezione sono allineati e le sezioni hanno py-5 + container (ritmo di pagina coerente, niente contenuto attaccato ai bordi).
I colori vengono dalla palette Bootstrap (bg-*/btn-*/text-* con i nomi tema), non da classi inventate.
Il tuo style.css contiene solo i colori del brand + al massimo un override minimo; nessuna regola di layout scritta a mano.
Svolgimento (può sforare)
L'esercizio non è time-boxed: completatelo in aula se finite prima, altrimenti a casa.
La prossima lezione (L5) aprirà con ~15 min di correzione di tutti gli esercizi: mostrerò bene/male per consolidare e spronare. È il momento per essere onesti su cosa non vi è chiaro.
Regole
Niente copia/incolla dalla mia versione finita: ricostruisci dal vivo (le tue note + la documentazione), non copiando il file di riferimento.
Se ti blocchi su una classe, cerca nella documentazione (link in fondo), non chiedere la soluzione al collega.
Chi finisce prima in aula: passa agli Extra / per casa.
