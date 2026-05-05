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
groups = list() # I gruppi saranno tuple composte da (nome, desc)

# restituisce una stringa che mostra il contatto c
def contact_to_str(c):
  gruppo_str = c['gruppo'] if c['gruppo'] else "Nessuno"
  return f"* {c['cognome']}, {c['nome']}:\n" + \
    f"   - telefono: {c['telefono']}\n" + \
    f"   - email: {c['email']}\n" + \
    f"   - gruppo: {gruppo_str}\n"

def contact_add(n, c, t, e, g=None):
	global contacts

	new_contact = {
		"nome":     n,
		"cognome":  c,
		"telefono": t,
		"email":    e,
		"gruppo":   g or None
	}
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
	print(f"\nIn rubrica ci sono i seguenti {len(contacts)} contatti:\n")
	for c in contacts:
		print(contact_to_str(c))
	print("Fatto.")

def ui_search_contact():
	print("\nRicerca contatti per nome e/o cognome")
	# chiedere nome e/o cognome e restituire tutti i contatti corrispondenti
	nome =    input(" - nome (o stringa vuota)? ")
	cognome = input(" - cognome (o stringa vuota)? ")
	result = contact_search(nome, cognome)
	print(f"\nIn rubrica ci sono le seguenti {len(result)} corrispondenze:\n")
	for c in result:
		print(contact_to_str(c))
	print("Fatto.")


## --- Groups

def group_to_str(g):
  # nome : descrizione
  return f"* {g['nome']}: {g['descrizione']}"


def ui_add_group(n, d):
  global groups

  if n.strip() is None or n.strip() == "":
    print("\nNome del gruppo è obbligatorio. Riprova.\n")
    return

  else:
    # Se non ci sono gruppi, crea
    if len(groups) <= 0:
      new_group = {'nome': n, 'descrizione': d}
      groups.append(new_group)
      print(f"\nGruppo '{group_to_str(new_group)}' aggiunto con successo!\n")

    # Se ci sono gruppi, verifica che il nome non esista già
    else:
      for group in groups:
        if n.lower() == group['nome'].lower():
          print(f"\nIl gruppo {n} esiste già. Riprovare con un altro nome\n")
          return

      # In caso contrario, aggiungi il gruppo
      new_group = {'nome': n, 'descrizione': d}
      groups.append(new_group)
      print(f"\nGruppo '{group_to_str(new_group)}' aggiunto con successo!\n")



def ui_search_in_group():
  target_group = input("\nInserisci il nome del gruppo in cui cercare:\n>\t").strip()
  group_to_str(target_group)
  result = contact_search(None, None, target_group)

  print(f"\nContatti nel gruppo {target_group}:")
  found_contacts = []
  for c in result:
      found_contacts.append(c)

  if len(found_contacts) == 0:
    print(f"\nNessun conttatto trovato nel gruppo {target_group}")

  else:
    for c in found_contacts:
      print(contact_to_str([c]))


def ui_show_groups():
  global groups
  if len(groups) == 0:
    choice = input("\nIn rubrica non ci sono ancora gruppi. Vuoi crearne uno? Y/N\n>\t").strip().lower()
    if choice == "y" or choice == "yes" or choice == "s" or choice == "si":
      ui_add_group(
        input("\nIndica il nome del gruppo:\n>\t").strip(),
        input("\nScrivi una descrizione del gruppo:\n>\t").strip()
      )
    else:
      print("\nOk. Prosegui pure\n")
  else:
    print(f"\nIn rubrica ci sono i seguenti {len(groups)} gruppi:")
    for g in groups:
      print(group_to_str(g))


## --- Menu

def ui_ask_what_to_do():
  while True:
    menu_choice = 3

    print( "\nScegli che tipo di azioni vuoi effettuare\n" + \
      "\r\t1. contatti: Azioni sui contatti\n" + \
      "\r\t2. gruppi: Azioni sui gruppi\n" + \
      "\r\t3. exit: Esci\n"
    )

    choice_type = input("\nScrivi l'azione oppure digita il numero corrispondente:\n>\t").strip().lower()

    match choice_type:
      case "1" | "contatti":
          menu_choice = 1
      case "2" | "gruppi":
          menu_choice = 2
      case "3" | "exit":
          print("Arrivederci!")
          break
      case _:
          print("\nScelta non valida, riprova.")

    if menu_choice == 1:
      while True:

        print(  "\nScegli un'azione:\n" + \
          "\r\t1. add: Aggiungi un nuovo contatto\n" + \
          "\r\t2. show: Mostra tutta la contacts\n" + \
          "\r\t3. search: Cerca un contatto\n" + \
          "\r\t4. exit: Esci\n"
        )
        user_choice = input("\nScrivi l'azione oppure digita il numero corrispondente:\n>\t").strip().lower()


        if user_choice == 'add' or user_choice == '1':
          ui_add_contact()
        elif user_choice == 'show' or user_choice == '2':
          ui_show_contacts()
        elif user_choice == 'search' or user_choice == '3':
          ui_search_contact()
        elif user_choice == 'exit' or user_choice == '4':
          print("\nRicevuto! Tornerai al menu principale\n")
          break
        else:
          print(f"{user_choice}? non è una scelta valida. Riprova\n")


    if menu_choice == 2:
      while True:

        print(  "\nScegli un'azione:\n" + \
          "\r\t1. add: Aggiungi un nuovo gruppo\n" + \
          "\r\t2. show: Mostra tutti i gruppi\n" + \
          "\r\t3. search: Cerca contatti in un gruppo\n" + \
          "\r\t4. exit: Esci\n"
        )
        group_choice = input("\nScrivi l'azione oppure digita il numero corrispondente:\n>\t").strip().lower()


        if group_choice == 'add' or group_choice == '1':
          ui_add_group(
            input("\nIndica il nome del gruppo:\n>\t").strip(),
            input("\nScrivi una descrizione del gruppo:\n>\t").strip()
          )
        elif group_choice == 'show' or group_choice == '2':
          ui_show_groups()
        elif group_choice == 'search' or group_choice == '3':
          ui_search_in_group()
        elif group_choice == 'exit' or group_choice == '4':
          print("\nRicevuto! Tornerai al menu principale\n")
          break
        else:
          print(f"{group_choice}? non è una scelta valida. Riprova\n")


def main():
    hardcoded_contacts = [
        {'nome': 'mario', 'cognome': 'rossi', 'telefono': '157347', 'email': 'mario@gmail.com', 'gruppo': 'IT'},
        {'nome': 'ugo', 'cognome': 'bianchi', 'telefono': '9999', 'email': 'ugo@gmail.com', 'gruppo': None},
        {'nome': 'elena', 'cognome': 'gialli', 'telefono': '222222', 'email': 'elena@gmail.com', 'gruppo': 'HR'},
    ]

    for persona in hardcoded_contacts:
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
