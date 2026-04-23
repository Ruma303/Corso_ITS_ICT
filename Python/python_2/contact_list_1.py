import sys

"""
Contact list 1: implementing objects as dictionaries

Scrivere un programma Python che permetta di rappresentare e manipolare
dati di un insieme di persone (ovvero una rubrica di contatti).

Di ogni contatto, il programma deve rappresentare:
 - nome
 - cognome
 - telefono
 - indirizzo email

Il programma deve permettere all'utente di:

1) inserire i dati di un nuovo contatto
2) mostrare il contenuto della rubrica
3) cercare un contatto per nome e/o per cognome
4) eliminare un contatto.


Suggerimenti:

Rappresentare ogni contatto come un dizionario con le entry:
 - "nome"
 - "cognome"
 - "telefono"
 - "email"

Ad esempio, il dizionario seguente:

anna = {
	"nome": "Anna",
	"cognome": "Bianchi",
	"telefono": "3353922342",
	"email": "annabianchi@mymail.com"
}

rappresenta i dati del contatto Anna Bianchi.


L'elenco di contatti memorizzati nell'applicazione è una collezione di dizionari.
Quale tipo di collezione adoperare? set, list, dict, tuple, ...?

Si fornisce uno scheletro per il programma, da completare. In particolare:
  * la funzione main() chiede ripetutamente all'utente quale azione vuole effettuare:
 	* inserimento di una nuovo contatto
 	* stampa della rubrica
 	* ricerca di un contatto

 * Le funzioni il cui nome inizia per "ui_" definiscono l'interfaccia utente, ovvero
   si occupano di chiedere dati all'utente oppure di mostrare il risultato di una operazione.

 * Le funzioni il cui nome inizia per "contact_" si occupano invece di eseguire un'azione su
   un singolo contatto.


Esercizio 1.
Implementare la funzione contact_search() che restituisce la
collezione dei contatti che hanno il nome e il cognome dati (se dati!)

Esercizio 2.
Estendere il programma per permettere ad ogni contatto di appartenere ad un gruppo.
Il programma dovrà permettere all'utente di:

   1) Creare un nuovo gruppo. Di ogni gruppo interessa il nome ed una descrizione
   2) Assegnare ogni nuovo contatto ad uno dei gruppi esistenti, lasciando la possibilità che alcuni contatti non appartengano ad alcun gruppo
   3) Estendere la funzionalità di ricerca per cercare solo all'interno di un gruppo

"""

# Variabile globale: viene inizializzata all'avvio del programma e resta
# in vita fino alla terminazione del programma.
contacts = list() # valutare l'uso di altre tipologie di collezioni
groups = set() # I gruppi saranno tuple composte da (nome, desc)

# restituisce una stringa che mostra il contatto c
def contact_to_str(c):
  gruppo_str = c['gruppo'] if c['gruppo'] else "Nessuno"
  return f"* {c['cognome']}, {c['nome']}:\n" + \
    f"   - telefono: {c['telefono']}\n" + \
    f"   - email: {c['email']}\n" + \
    f"   - gruppo: {gruppo_str}\n"

def contact_add(n, c, t, e, g=None):
	global contacts # dichiariamo che questa funzione vuole modificare la variabile globale "contacts"

	# Crea il nuovo contatto
	new_contact = {
		"nome":     n,
		"cognome":  c,
		"telefono": t,
		"email":    e,
		"gruppo":   g
	}
	# Aggiungilo in contacts
	contacts.append(new_contact)

def contact_search(n, c, g=None):
    global contacts
    found = []

    for contact in contacts:
        match_n = (not n) or (contact['nome'].lower() == n.lower())
        match_c = (not c) or (contact['cognome'].lower() == c.lower())
        match_g = (not g) or (contact['gruppo'] == g)

        if match_n and match_c and match_g:
            found.append(contact)
    return found


## --- User interface (UI) del programma

def ui_add_contact():
	print("\nAggiunta di un nuovo contatto")
	nome =     input(" - nome? ")
	cognome =  input(" - cognome? ")
	telefono = input(" - telefono? ")
	email =    input(" - email? ")
	gruppo =   input(" - gruppo? ")
	contact_add(nome, cognome, telefono, email, gruppo)

def ui_show_contacts():
	print(f"In rubrica ci sono i seguenti {len(contacts)} contatti:")
	for c in contacts:
		print(contact_to_str(c))
	print("Fatto.")

def ui_search_contact():
	print("\nRicerca contatti per nome e/o cognome")
	# chiedere nome e/o cognome e restituire tutti i contatti corrispondenti
	nome =    input(" - nome (o stringa vuota)? ")
	cognome = input(" - cognome (o stringa vuota)? ")
	result = contact_search(nome, cognome)
	print(f"\nIn rubrica ci sono le seguenti {len(result)} corrispondenze:")
	for c in result:
		print(contact_to_str(c))
	print("Fatto.")


## --- Groups

def create_group(n, d):
  global groups
  if n is not None and d is not None:
    new_group = n, d
    return groups.add(new_group)

def ui_search_in_group():
  target_group = input("Inserisci il nome del gruppo in cui cercare: ").strip()
  # Possiamo riutilizzare contact_search passando solo il gruppo
  result = contact_search(None, None, target_group)

  print(f"\nContatti nel gruppo {target_group}:")
  for c in result:
      print(contact_to_str(c))

## --- Menu

def ui_ask_what_to_do():
  while True:
    print(  "\nScegli un'azione:\n" + \
    "1. add: Aggiungi un nuovo contatto\n" + \
    "2. show: Mostra tutta la contacts\n" + \
    "3. search: Cerca un contatto\n" + \
    "4. group_C: Crea un gruppo\n" + \
    "5. group_S: Cerca contatto in un gruppo\n" + \
    "6. exit: Esci"
    )

    choice = input("Scrivi l'azione oppure digita il numero corrispondente:\n").strip().lower()

    if choice == 'add' or choice == '1':
      ui_add_contact()
    elif choice == 'show' or choice == '2':
      ui_show_contacts()
    elif choice == 'search' or choice == '3':
      ui_search_contact()
    elif choice == 'group_C' or choice == '4': create_group(
      input("Indica il nome del gruppo:\n").strip(),
      input("Scrivi una descrizione del gruppo:\n").strip()
    )
    elif choice == 'group_s' or choice == '5':
      ui_search_in_group()
    elif choice == 'exit' or choice == '6':
      print("Arrivederci!")
      break
    else:
      print(f"{choice}? mmm, non capisco...")


def main():
    hardcoded_contacts = [
        {'nome': 'mario', 'cognome': 'rossi', 'telefono': '157347', 'email': 'mario@gmail.com', 'gruppo': 'IT'},
        {'nome': 'ugo', 'cognome': 'bianchi', 'telefono': '9999', 'email': 'ugo@gmail.com', 'gruppo': None},
        {'nome': 'elena', 'cognome': 'gialli', 'telefono': '222222', 'email': 'elena@gmail.com', 'gruppo': 'HR'},
    ]

    for persona in hardcoded_contacts:
        # Accediamo ai valori usando le chiavi tra parentesi quadre
        contact_add(
            persona['nome'],
            persona['cognome'],
            persona['telefono'],
            persona['email'],
            persona['gruppo']
        )

    ui_ask_what_to_do()

if __name__ == '__main__':
  sys.exit( main() )
