"""
Contact list 1: implementing objects as dictionaries

Scrivere un programma Python che permetta di rappresentare e manipolare
dati di un insieme di persone (ovvero una rubrica di contatti).

Di ogni contatto, il programma deve rappresentare:
\r\tnome
\r\tcognome
\r\ttelefono
\r\tindirizzo email

Il programma deve permettere all'utente di:

1) inserire i dati di un nuovo contatto
2) mostrare il contenuto della rubrica
3) cercare un contatto per nome e/o per cognome
4) eliminare un contatto.


Suggerimenti:

Rappresentare ogni contatto come un dizionario con le entry:
\r\t"nome"
\r\t"cognome"
\r\t"telefono"
\r\t"email"

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
Implementare la funzione Contact.search() che restituisce la
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

from __future__ import annotations

import json
from pathlib import Path
from sys import exit
from typing import Self


class Group:
    groups: dict[int, Self] = dict()
    current_group = 0

    def __init__(self, name: str, description: str, idx: int | None = None):
        if idx is None:
            idx = type(self).current_group

        assert idx not in type(self).groups, f"Error, group id already '{idx}' exists"

        self.idx = idx
        self.name = name
        self.description = description

        type(self).groups[self.idx] = self
        if type(self).current_group <= self.idx:
            type(self).current_group = self.idx + 1

    @classmethod
    def search(cls, name: str | None) -> list[Self]:
        found = []
        for group in cls.groups.values():
            if name and group.name.lower() != name.lower():
                continue
            found.append(group)
        return found

    @classmethod
    def get(cls, idx: int) -> Self:
        return cls.groups[idx]

    def __str__(self):
        return (
            f"{self.idx}: {self.name}\n" + f"Description: {self.description}"
            if self.name is not None and self.name != ""
            else f"WARNING! Group '{self.name}' NOT FOUND"
        )


class Contact:
    contacts: dict[int, Self] = dict()
    current_contact = 0

    def __init__(
        self,
        name: str,
        lastname: str,
        phone: str,
        email: str,
        group: Group | None,
        idx: int | None = None,
    ):
        if idx is None:
            idx = type(self).current_contact

        assert idx not in type(self).contacts, f"Error, contact id '{idx}' already exists"

        self.idx = idx
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.group = group or None

        type(self).contacts[self.idx] = self
        if type(self).current_contact <= self.idx:
            type(self).current_contact = self.idx + 1

    def __str__(self):
        gruppo_str = self.group.name if self.group else "Nessuno"
        return (
            f"* {self.idx}: {self.lastname}, {self.name}:\n"
            f"\t- telefono: {self.phone}\n"
            f"\t- email: {self.email}\n"
            f"\t- gruppo: {gruppo_str}\n"
        )

    @classmethod
    def search(cls, nome, cognome, gruppo=None):
        found = []

        for contact in cls.contacts.values():
            match_n = (not nome) or contact.name.lower() == nome.lower()
            match_c = (not cognome) or contact.lastname.lower() == cognome.lower()
            match_g = (not gruppo) or (
                contact.group and contact.group.name.lower() == gruppo.lower()
            )

            if match_n and match_c and match_g:
                found.append(contact)

        return found

    @classmethod
    def delete(cls, contact):
        contact_id_to_delete = None
        for contact_id, c in cls.contacts.items():
            if c == contact:
                contact_id_to_delete = contact_id
                print(f"Contatto {c.lastname} {c.name} rimosso\n")
                break
        if contact_id_to_delete is not None:
            del cls.contacts[contact_id_to_delete]
        return

    @classmethod
    def create(cls, nome, cognome, telefono, email, gruppo=None) -> Self:
        """
        Factory Method da usare al posto del costruttore (invoca il costruttore)
        """
        return cls(nome, cognome, telefono, email, gruppo)

    @classmethod
    def create_from_dict(cls, idx: int, d: dict) -> Self:
      """
      Crea un contatto da un dizionario
      """ 
      pass # lo completo io dopo
      

# --- User interface (UI) del programma

yes = ("s", "si", "y", "yes")


def ui_add_contact():
    print("\nAggiunta di un nuovo contatto\n")
    nome = input("\r\tnome?\n>\t")
    cognome = input("\r\tcognome?\n>\t")

    contatto_esistente = None
    verifica_contatto = Contact.search(nome, cognome)

    if verifica_contatto:
        contatto_esistente = verifica_contatto[0]
        # Mi basta mostrare il primo contatto
        print(
            f"\nIl contatto con Nome: {nome} e Cognome: {cognome} esiste già.\n{verifica_contatto[0]}\n"
        )
        choice = (
            input("Vuoi aggiornare le sue informazioni? (Y/N):\n>\t").strip().lower()
        )
        if choice not in yes:
            print(
                "\nNon è possibile proseguire con l'aggiunta del contatto. Riprova.\n"
            )
            return

    telefono = input("\r\ttelefono?\n>\t")
    email = input("\r\temail?\n>\t")
    gruppo = None

    groups = Group.groups

    if len(groups) > 0:
        print("\r\tgruppi disponibili:")
        for g in groups.values():
            print(f"\t{g.name}")
        scelta = input("\r\tgruppo? (invio per nessuno)\n>\t").strip()
        if scelta:
            found = False
            for g in groups.values():
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
                if creare in yes:
                    desc = input(f"\tDescrizione per '{scelta}':\n>\t").strip()
                    gruppo = ui_add_group(scelta, desc)
                else:
                    print("\tContatto aggiunto senza gruppo.")

    # Se il gruppo non esiste, chiedere se crearlo
    else:
        scelta = (
            input("\r\tnessun gruppo disponibile. Vuoi crearne uno? (Y/N):\n>\t")
            .strip()
            .lower()
        )
        if scelta in yes:
            nome_g = input("\tNome del gruppo:\n>\t").strip()
            desc = input("\tDescrizione:\n>\t").strip()
            gruppo = ui_add_group(nome_g, desc)
        else:
            print("\tContatto aggiunto senza gruppo.")

    if contatto_esistente:
        contatto_esistente.phone = telefono
        contatto_esistente.email = email
        contatto_esistente.group = gruppo
    else:
        Contact.create(nome, cognome, telefono, email, gruppo)


def ui_show_contacts():
    print(f"\nIn rubrica ci sono i seguenti {len(Contact.contacts)} contatti:\n")
    for c in Contact.contacts.values():
        print(c)


def ui_search_contact():
    print("\nRicerca contatti per nome e/o cognome")

    # chiedere nome e/o cognome e restituire tutti i contatti corrispondenti
    nome = input("\r\tnome (o stringa vuota)?\n>\t")
    cognome = input("\r\tcognome (o stringa vuota)?\n>\t")

    result = Contact.search(nome, cognome)
    print(f"\nIn rubrica ci sono le seguenti {len(result)} corrispondenze:\n")

    for c in result:
        print(c)
    return


def ui_delete_contact():
    print("\nEliminazione contatto")
    nome = input("\r\tnome (o stringa vuota)?\n>\t")
    cognome = input("\r\tcognome (o stringa vuota)?\n>\t")
    result = Contact.search(nome, cognome)
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
            Contact.delete(result[idx])
        else:
            print("\nNumero non valido.")
    except ValueError:
        print("\nInput non valido.")


## --- Groups


def ui_add_group(name, description):
    if name.strip() == "":
        print("\nNome del gruppo è obbligatorio. Riprova.\n")
        return None

    for group in Group.groups.values():
        if name.lower() == group.name.lower():
            print(f"\nIl gruppo {name} esiste già. Riprovare con un altro nome\n")
            return None

    new_group = Group(name, description)
    print(f"\nGruppo aggiunto con successo!\n{new_group}\n")
    return new_group


def ui_search_in_group():
    target_group_name = input(
        "\nInserisci il nome del gruppo in cui cercare:\n>\t"
    ).strip()

    found_group = None
    for group in Group.groups.values():
        if group.name.lower() == target_group_name.lower():
            found_group = group
            break

    if not found_group:
        print(f"\nIl gruppo '{target_group_name}' non esiste.")
        return

    print(f"\nStai cercando nel gruppo: {found_group}\n")
    result = Contact.search(None, None, target_group_name)

    if not result:
        print(f"\nNessun contatto trovato nel gruppo {target_group_name}")
    else:
        print(f"\nContatti nel gruppo {target_group_name}:")
        for c in result:
            print(c)


def ui_show_groups():
    if len(Group.groups) == 0:
        choice = (
            input("\nIn rubrica non ci sono ancora gruppi. Vuoi crearne uno? Y/N\n>\t")
            .strip()
            .lower()
        )
        if choice == "y" or choice == "yes" or choice == "s" or choice == "si":
            ui_add_group(
                input("\nIndica il nome del gruppo:\n>\t").strip(),
                input("\nScrivi una descrizione del gruppo:\n>\t").strip(),
            )
        else:
            print("\nOk. Prosegui pure\n")
    else:
        print(f"\nIn rubrica ci sono i seguenti {len(Group.groups)} gruppi:")
        for g in Group.groups.values():
            print(g)


## --- Menu


def ui_ask_what_to_do():
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
                    ui_add_contact()
                elif user_choice == "show" or user_choice == "2":
                    ui_show_contacts()
                elif user_choice == "search" or user_choice == "3":
                    ui_search_contact()
                elif user_choice == "delete" or user_choice == "4":
                    ui_delete_contact()
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
                        input("\nIndica il nome del gruppo:\n>\t").strip(),
                        input("\nScrivi una descrizione del gruppo:\n>\t").strip(),
                    )
                elif group_choice == "show" or group_choice == "2":
                    ui_show_groups()
                elif group_choice == "search" or group_choice == "3":
                    ui_search_in_group()
                elif group_choice == "exit" or group_choice == "4":
                    print("\nRicevuto! Tornerai al menu principale\n")
                    break
                else:
                    print(f"{group_choice}? non è una scelta valida. Riprova\n")


def load_all(): ...


def save_all(): ...


def main():

    try:
        data_dir = Path.cwd() / "data"
        load_all()
        ui_ask_what_to_do()
        save_all()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
