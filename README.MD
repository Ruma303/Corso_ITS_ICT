# Note iniziali

Questo è un file di guida per l'installazione degli strumenti necessari per seguire il corso di programmazione accademico.

Queste note sono scritte in Markdown, un linguaggio di markup leggero che consente di formattare il testo in modo semplice. Potete visualizzare questo file in modo più leggibile utilizzando un visualizzatore di Markdown, come ad esempio l'estensione "Markdown Preview" di Visual Studio Code.

In alto a destra di questo file, potete trovare un'icona con una lente di ingrandimento e la scritta "Open Preview to the Side" oppure "Apri anteprima laterale". Cliccando su questa icona, potrete vedere il file formattato accanto al codice sorgente.

---

## Utility varie

### Charmap e caratteri speciali

Premere il tasto di Windows + R per aprire la finestra di Esegui. Digitare Charmap e premere su OK per visualizzare a schermo la mappa dei caratteri di Windows.

In Visualizzazione avanzata; digita Grave Accent in “Cerca” o (Accento grave) per selezionare il BackTick.

### Cambiare layout da tastiera

Non sempre si riesce a scrivere caratteri speciali con una tastiera italiana. Per cambiare il layout della tastiera in inglese (USA).

1. Andare su Impostazioni > Data/Ora e lingua > Lingua e area geografica
2. Cliccare su "Aggiungi una lingua" ed installare "Inglese (Stati Uniti d'America)". A noi interessa solo la digitazione, volendo potete installare tutti i pacchetti.
3. Al termine potete cambiare il layout della tastiera cliccando sull'icona della lingua in basso a destra vicino all'orologio di Windows, oppure premendo la combinazione di tasti Windows + Barra spaziatrice.
4. Ora potete digitare i caratteri speciali che per il layout ANSII (USA):
    - BackTick (Accento grave) ` : si trova sopra il tasto Tab, a sinistra del numero 1
    - Tilde ~ : si ottiene premendo Shift + BackTick
    - Pipe | : si ottiene premendo Shift + BackSlash (il tasto con la barra rovesciata \ che si trova sopra Invio/Enter)
    - BackSlash \ : si trova sopra Invio/Enter
    - At @ : si ottiene premendo Shift + 2
    - Hash # : si ottiene premendo Shift + 3
    - Dollar $ : si ottiene premendo Shift + 4
    - Percent % : si ottiene premendo Shift + 5
    - Accento circonflesso ^ : si ottiene premendo Shift + 6
    - Ampersand & : si ottiene premendo Shift + 7
    - Asterisco \* : si ottiene premendo Shift + 8
    - Parentisi tonde ( ) : si ottengono premendo Shift + 9 e Shift + 0
    - Parentesi quadre [ ] : si ottengono premendo BackSlash + 8 e BackSlash + 9
    - Graffe { } : si ottengono premendo Shift + BackSlash +

---

### PowerToys - Utility di Windows avanzate

PowerToys è una raccolta di utilità avanzate per utenti esperti di Windows 10 e Windows 11, che consente di migliorare la produttività e personalizzare l'esperienza utente.

1. Scaricare PowerToys dal Microsoft Store.
2. Installare e avviare PowerToys. Da qui esplorare le numerose funzionalità offerte, come ad esempio:
    - FancyZones: per creare layout di finestre personalizzati.
    - PowerToys Run: un launcher rapido per avviare applicazioni e cercare file.
    - Keyboard Manager: per rimappare i tasti della tastiera.
    - Image Resizer: per ridimensionare rapidamente le immagini tramite il menu contestuale di Esplora file.

---

# Git - versionamento del codice

Git è uno strumento fondamentale per il versionamento del codice sorgente. Permette di tenere traccia delle modifiche apportate al codice nel tempo, facilitando la collaborazione tra più sviluppatori.

1. Installare Git: https://git-scm.com/install/windows
2. Su questa macchina potete farlo solo da terminale. Esempio, aprite PowerShell e digitate:

winget install --id Git.Git -e --source winget

3. Alla fine verificate che Git sia installato con il comando: git --version
4. Configurate Git con il vostro nome e email (quelli che appariranno nei commit):

    git config --global user.name "Your Name"
    git config --global user.email "

(email possibilmente quella dell'accademia)

Volendo, potete vedere il mio codice che si trova su https://github.com/Ruma303/Corso_ITS_ICT.git

---

# Python

1. Installare Python: https://www.python.org/downloads/
2. Verificare l'installazione aprendo il terminale e digitando: python --version
3. Python di solito abilita degli alias come py o python3. Potete utilizzare anche questi al posto di python.
4. Inoltre, Python include già il gestore di pacchetti pip, che useremo per installare le librerie necessarie.

---

## Installare librerie Python localmente con ambienti virtuali

1. Aprire il terminale
2. Eseguire il comando `python -m venv .venv` creare un ambiente virtuale locale. Le librerie installate in questo ambiente non influenzeranno il sistema globale Python, ma si troveranno in una cartella chiamata `.venv`.
3. Attivare l'ambiente virtuale:
    - Su Windows: `.\.venv\Scripts\activate`
    - Su macOS/Linux: `source .venv/bin/activate`
4. Ora nel terminale staremo utilizzando il Python e le librerie installate nell'ambiente virtuale. Ciò è indicato dal prefisso `(.venv)` nella riga di comando.
5. Eseguire il comando `pip install pyfiglet termcolor` per installare le librerie necessarie.
6. Ora è possibile eseguire lo script Python con le librerie installate nell'ambiente virtuale.
7. Per disattivare l'ambiente virtuale, eseguire il comando `deactivate` nel terminale.
