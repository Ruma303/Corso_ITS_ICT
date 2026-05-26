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


# Un contatto non crea altri contatti, un gruppo non cerca altri gruppi.
# Le operazioni CRUD verranno spostate rimangono in funzioni separate fuori dalle classi.

# --- Classi

from sys import exit

class Group:
    name: str
    description: str

    def __init__(self, n: str, desc: str):
        self.name = n
        self.description = desc

    def to_str(self):
        if self.name is not None and self.name != "":
            return f"Title: {self.name}\n" + f"Description: {self.description}"


class Contact:
    name: str
    lastname: str
    phone: str
    email: str
    group: Group | None

    def __init__(self, n: str, ln: str, p: str, e: str, g: Group | None):
        self.name = n
        self.lastname = ln
        self.phone = p
        self.email = e
        self.group = g or None

    def to_str(self):
        gruppo_str = self.group.name if self.group else "Nessuno"
        return (
            f"* {self.lastname}, {self.name}:\n"
            f"\t- telefono: {self.phone}\n"
            f"\t- email: {self.email}\n"
            f"\t- gruppo: {gruppo_str}\n"
        )


# --- Operazioni


def contact_add(contacts, nome, cognome, telefono, email, gruppo=None):
    new_contact = Contact(nome, cognome, telefono, email, gruppo)
    contacts.append(new_contact)


def contact_search(contacts, nome, cognome, gruppo=None):
    found = []

    for contact in contacts:
        match_n = (not nome) or contact.name.lower() == nome.lower()
        match_c = (not cognome) or contact.lastname.lower() == cognome.lower()
        match_g = (not gruppo) or (
            contact.group and contact.group.name.lower() == gruppo.lower()
        )

        if match_n and match_c and match_g:
            found.append(contact)

    return found


# --- User interface (UI) del programma


def ui_add_contact(contacts, groups):
    print("\nAggiunta di un nuovo contatto")
    nome = input(" - nome?\n>\t")
    cognome = input(" - cognome?\n>\t")

    contatto_esistente = None
    verifica_contatto = contact_search(contacts, nome, cognome)

    if verifica_contatto:
        contatto_esistente = verifica_contatto[0]
        print(f"Il contatto con Nome: {nome} e Cognome: {cognome} esiste già.\n{verifica_contatto[0].to_str()}")
        choice = input("Vuoi aggiornare le sue informazioni? (Y/N):\n>\t").strip().lower()
        if choice not in ("s", "si", "y", "yes"):
          print("Non è possibile proseguire con l'aggiunta del contatto. Riprova.\n")
          return

    telefono = input(" - telefono?\n>\t")
    email = input(" - email?\n>\t")
    gruppo = None

    if len(groups) > 0:
        print(" - gruppi disponibili:")
        for g in groups:
            print(f"\t{g.name}")
        scelta = input(" - gruppo? (invio per nessuno)\n>\t").strip()
        if scelta:
            found = False
            for g in groups:
                if g.name.lower() == scelta.lower():
                  gruppo = g
                  found = True
                  break
            if not found:
                creare = (
                    input(f"Gruppo '{scelta}' non trovato. Vuoi crearlo? (Y/N):\n>\t")
                    .strip()
                    .lower()
                )
                if creare in ("s", "si", "y", "yes"):
                    desc = input(f"\tDescrizione per '{scelta}':\n>\t").strip()
                    gruppo = ui_add_group(groups, scelta, desc)
                else:
                    print("   Contatto aggiunto senza gruppo.")

    # Se il gruppo non esiste, chiedere se crearlo
    else:
        scelta = (
            input(" - nessun gruppo disponibile. Vuoi crearne uno? (Y/N):\n>\t")
            .strip()
            .lower()
        )
        if scelta in ("s", "si", "y", "yes"):
            nome_g = input("\tNome del gruppo:\n>\t").strip()
            desc = input("\tDescrizione:\n>\t").strip()
            gruppo = ui_add_group(groups, nome_g, desc)
        else:
            print("\tContatto aggiunto senza gruppo.")


    if contatto_esistente:
        contatto_esistente.phone = telefono
        contatto_esistente.email = email
        contatto_esistente.group = gruppo
    else:
        contact_add(contacts, nome, cognome, telefono, email, gruppo)


def ui_show_contacts(contacts):
    print(f"\nIn rubrica ci sono i seguenti {len(contacts)} contatti:\n")
    for c in contacts:
        print(c.to_str())


def ui_search_contact(contacts):
    print("\nRicerca contatti per nome e/o cognome")

    # chiedere nome e/o cognome e restituire tutti i contatti corrispondenti
    nome = input(" - nome (o stringa vuota)?\n>\t")
    cognome = input(" - cognome (o stringa vuota)?\n>\t")

    result = contact_search(contacts, nome, cognome)
    print(f"\nIn rubrica ci sono le seguenti {len(result)} corrispondenze:\n")

    for c in result:
      print(c.to_str())
    return


def contact_delete(contacts, contact):
    for c in contacts:
        if c == contact:
            contacts.remove(c)
            print(f"Contatto {c.lastname} {c.name} rimosso\n")
            break
    return


def ui_delete_contact(contacts):
    print("\nEliminazione contatto")
    nome = input(" - nome (o stringa vuota)?\n>\t")
    cognome = input(" - cognome (o stringa vuota)?\n>\t")
    result = contact_search(contacts, nome, cognome)
    if not result:
        print("\nNessun contatto trovato.\n")
        return
    print(f"\nTrovati {len(result)} contatti:\n")
    for i, c in enumerate(result):
        print(f"\t{i + 1}. {c.name} {c.lastname}")
    scelta = input("\nQuale vuoi eliminare? (posizione, o 'annulla'):\n>\t").strip()
    if scelta == "annulla":
        return
    try:
        idx = int(scelta) - 1
        if 0 <= idx < len(result):
            contact_delete(contacts, result[idx])
        else:
            print("\nNumero non valido.")
    except ValueError:
        print("\nInput non valido.")


## --- Groups


def ui_add_group(groups, nome, descrizione):
    if nome.strip() == "":
        print("\nNome del gruppo è obbligatorio. Riprova.\n")
        return None

    for group in groups:
        if nome.lower() == group.name.lower():
            print(f"\nIl gruppo {nome} esiste già. Riprovare con un altro nome\n")
            return None

    new_group = Group(nome, descrizione)
    groups.append(new_group)
    print(f"\nGruppo aggiunto con successo!\n{new_group.to_str()}\n")
    return new_group


def ui_search_in_group(contacts, groups):
    target_group_name = input(
        "\nInserisci il nome del gruppo in cui cercare:\n>\t"
    ).strip()

    found_group = None
    for group in groups:
        if group.name.lower() == target_group_name.lower():
            found_group = group
            break

    if not found_group:
        print(f"\nIl gruppo '{target_group_name}' non esiste.")
        return

    print(f"\nStai cercando nel gruppo: {found_group.to_str()}\n")
    result = contact_search(contacts, None, None, target_group_name)

    if not result:
        print(f"\nNessun contatto trovato nel gruppo {target_group_name}")
    else:
        print(f"\nContatti nel gruppo {target_group_name}:")
        for c in result:
            print(c.to_str())


def ui_show_groups(contacts, groups):
    if len(groups) == 0:
        choice = (
            input("\nIn rubrica non ci sono ancora gruppi. Vuoi crearne uno? Y/N\n>\t")
            .strip()
            .lower()
        )
        if choice == "y" or choice == "yes" or choice == "s" or choice == "si":
            ui_add_group(
                groups,
                input("\nIndica il nome del gruppo:\n>\t").strip(),
                input("\nScrivi una descrizione del gruppo:\n>\t").strip(),
            )
        else:
            print("\nOk. Prosegui pure\n")
    else:
        print(f"\nIn rubrica ci sono i seguenti {len(groups)} gruppi:")
        for g in groups:
            print(g.to_str())


## --- Menu


def ui_ask_what_to_do(contacts, groups):
    while True:
        menu_choice = 3

        print(
            "\nScegli che tipo di azioni vuoi effettuare\n"
            + "\r\t1. contatti: Azioni sui contatti\n"
            + "\r\t2. gruppi: Azioni sui gruppi\n"
            + "\r\t3. exit: Esci\n"
        )

        choice_type = (
            input("\nScrivi l'azione oppure digita il numero corrispondente:\n>\t")
            .strip()
            .lower()
        )

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
                print(
                    "\nScegli un'azione:\n"
                    + "\r\t1. add: Aggiungi un nuovo contatto\n"
                    + "\r\t2. show: Mostra tutti i contatti\n"
                    + "\r\t3. search: Cerca un contatto\n"
                    + "\r\t4. delete: Elimina un contatto\n"
                    + "\r\t5. exit: Esci\n"
                )
                user_choice = (
                    input(
                        "\nScrivi l'azione oppure digita il numero corrispondente:\n>\t"
                    )
                    .strip()
                    .lower()
                )

                if user_choice == "add" or user_choice == "1":
                    ui_add_contact(contacts, groups)
                elif user_choice == "show" or user_choice == "2":
                    ui_show_contacts(contacts)
                elif user_choice == "search" or user_choice == "3":
                    ui_search_contact(contacts)
                elif user_choice == "delete" or user_choice == "4":
                    ui_delete_contact(contacts)
                elif user_choice == "exit" or user_choice == "5":
                    print("\nRicevuto! Tornerai al menu principale\n")
                    break
                else:
                    print(f"{user_choice}? non è una scelta valida. Riprova\n")

        if menu_choice == 2:
            while True:
                print(
                    "\nScegli un'azione:\n"
                    + "\r\t1. add: Aggiungi un nuovo gruppo\n"
                    + "\r\t2. show: Mostra tutti i gruppi\n"
                    + "\r\t3. search: Cerca contatti in un gruppo\n"
                    + "\r\t4. exit: Esci\n"
                )
                group_choice = (
                    input(
                        "\nScrivi l'azione oppure digita il numero corrispondente:\n>\t"
                    )
                    .strip()
                    .lower()
                )

                if group_choice == "add" or group_choice == "1":
                    ui_add_group(
                        groups,
                        input("\nIndica il nome del gruppo:\n>\t").strip(),
                        input("\nScrivi una descrizione del gruppo:\n>\t").strip(),
                    )
                elif group_choice == "show" or group_choice == "2":
                    ui_show_groups(contacts, groups)
                elif group_choice == "search" or group_choice == "3":
                    ui_search_in_group(contacts, groups)
                elif group_choice == "exit" or group_choice == "4":
                    print("\nRicevuto! Tornerai al menu principale\n")
                    break
                else:
                    print(f"{group_choice}? non è una scelta valida. Riprova\n")


def main():
    contacts: list[Contact] = []
    groups: list[Group] = []

    it = Group("IT", "Information Technology")
    hr = Group("HR", "Human Resources")

    groups.append(it)
    groups.append(hr)

    contacts.append(Contact("mario", "rossi", "157347", "mario@gmail.com", it))
    contacts.append(Contact("ugo", "bianchi", "9999", "ugo@gmail.com", None))
    contacts.append(Contact("elena", "gialli", "222222", "elena@gmail.com", hr))

    ui_ask_what_to_do(contacts, groups)
    return 0


if __name__ == "__main__":
    exit(main())
