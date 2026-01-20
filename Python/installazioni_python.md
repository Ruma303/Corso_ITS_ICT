# Installazione e autocompletamento Python in Visual Studio Code in Windows

1. Installare l'interprete Python da terminale: `winget install 9NQ7512CXL7T`

2. Trovare il percorso dov'è installato l'interprete:
  1. Aprire il menu Windows e digitare *CMD* oppure *Prompt dei comandi*, preferibilmente non *Powershell*
  2. Digitare innanzitutto `cd\`
  3. Subito dopo digitare `dir/s python.exe`
  4. Dopo un po' di tempo vengono mostrati vari percorsi dove sono installati i vari eseguibili di Python.
  5. Copiare soltanto il percorso simile a:
    `
    C:\Users\nome.utente\AppData\Local\Python\pythoncore-3.14-64
    `
  6. Per copiare va nei terminali premere *Ctrl + Shift + C* (per incollare *Ctrl + Shift + V*)

3. Aprire il menu Windows e digitare "*env*" e selezionare "*Modifica le variabili d'ambiente per l'account*". **ATTENZIONE, NON selezionare "per il sistema" perché servirebbero i permessi di amministratore**.
  1. Nella finestra che si apre selezionare "*Variabili d'ambiente...*" doppio click su "*Path*"
  2. Nella tabella che si apre cliccare su "*Nuovo*" e incollare il percorso copiato in precedenza.
  3. Per sicurezza portare in cima alla lista la nuova voce selezionandola e cliccando su "*Sposta su*" più volte. Infine salvare ed uscire.

4. Aprire **Visual Studio Code** e installare l'estensione **Python**
5. Andare nelle impostazioni digitando *Ctrl + ,*
6. Nella barra di ricerca scrivere *Python Default Interpreter*. Troveremo una casella dove sarà possibile incollare il percorso precedentemente copiato.
7. Per sicurezza, salvare con *Ctrl + s*, chiudere e riaprire VSCode.
8. Riaperto VSCode testiamo in un file Python l'autocompletamento.

Provare ad importare la libreria random:

`
import random
random.
`

Durante la digitazione, dopo il punto dovrebbe comparire l'autocompletamento con le varie funzioni disponibili per ogni modulo importato, esempio: randint, shuffle, etc...