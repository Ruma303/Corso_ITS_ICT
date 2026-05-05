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

Si fornisce uno scheletro per il programma, da completare.
In particolare:
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
   2) Assegnare ogni nuovo contatto ad uno dei gruppi esistenti, lasciando la possibilità
      che alcuni contatti non appartengano ad alcun gruppo
   3) Estendere la funzionalità di ricerca per cercare solo all'interno di un gruppo

"""

# --- Variabili globali ---
contacts = list()
groups = list()


# --- Contact actions ---
def contact_to_str(c):
    # Gestiamo il caso in cui il gruppo sia None o vuoto
    gruppo_str = c["gruppo"] if c["gruppo"] else "Nessun gruppo"
    return (
        f"* {c['cognome'].upper()}, {c['nome']}:\n"
        + f"    - telefono: {c['telefono']}\n"
        + f"    - email: {c['email']}\n"
        + f"    - gruppo: {gruppo_str}"
    )


def contact_add(n, c, t, e, g=None):
    global contacts
    new_contact = {
        "nome": n.strip(),
        "cognome": c.strip(),
        "telefono": t.strip(),
        "email": e.strip(),
        "gruppo": g.strip() if g else None,
    }
    contacts.append(new_contact)


def contact_search(n=None, c=None, g=None):
    """
    Esercizio 1 & 2: Cerca contatti per nome, cognome e/o gruppo.
    Se un parametro è vuoto, non viene usato per il filtraggio.
    """
    results = []
    for contact in contacts:
        # Verifichiamo se il contatto soddisfa TUTTI i criteri inseriti
        match_nome = not n or n.lower() == contact["nome"].lower()
        match_cognome = not c or c.lower() == contact["cognome"].lower()
        match_gruppo = not g or (
            contact["gruppo"] and g.lower() == contact["gruppo"].lower()
        )

        if match_nome and match_cognome and match_gruppo:
            results.append(contact)
    return results


# --- Group actions ---
def create_group(n, d):
    global groups
    if n:  # Verifichiamo almeno che il nome non sia vuoto
        new_group = {"nome": n.strip(), "descrizione": d.strip()}
        groups.append(new_group)
        print(f"Gruppo '{n}' creato con successo.")
    else:
        print("Errore: Il nome del gruppo non può essere vuoto.")


def show_groups():
    if not groups:
        print("Non ci sono gruppi creati.")
    for g in groups:
        print(f"* {g['nome']}: {g['descrizione']}")


# --- User interface (UI) ---
def ui_add_group():
    print("\nCreazione nuovo gruppo")
    nome = input(" - nome gruppo? ").strip()
    descrizione = input(" - descrizione? ").strip()
    create_group(nome, descrizione)


def ui_show_contacts():
    print(f"\nIn rubrica ci sono {len(contacts)} contatti:")
    for c in contacts:
        print(contact_to_str(c))
    print("-" * 20)


def ui_add_contact():
    print("\nAggiunta di un nuovo contatto")
    nome = input(" - nome? ")
    cognome = input(" - cognome? ")
    telefono = input(" - telefono? ")
    email = input(" - email? ")

    # Mostra i gruppi disponibili per aiutare l'utente
    if groups:
        print(" Gruppi disponibili:", [g["nome"] for g in groups])
    gruppo = input(" - gruppo (lascia vuoto per nessuno)? ")

    contact_add(nome, cognome, telefono, email, gruppo)


def ui_search_contact():
    print("\nRicerca contatti")
    nome = input(" - nome (invio per saltare)? ").strip()
    cognome = input(" - cognome (invio per saltare)? ").strip()
    gruppo = input(" - gruppo (invio per saltare)? ").strip()

    result = contact_search(nome, cognome, gruppo)
    print(f"\nRisultati trovati ({len(result)}):")
    for c in result:
        print(contact_to_str(c))


def ui_ask_what_to_do():
    while True:
        print("\n--- RUBRICA PYTHON ---")
        print("1. Aggiungi contatto")
        print("2. Mostra tutti i contatti")
        print("3. Cerca contatto (per nome/cognome/gruppo)")
        print("4. Crea nuovo gruppo")
        print("5. Mostra gruppi esistenti")
        print("6. Esci")

        choice = input("\nScegli un'azione (1-6): ").strip()

        if choice == "1":
            ui_add_contact()
        elif choice == "2":
            ui_show_contacts()
        elif choice == "3":
            ui_search_contact()
        elif choice == "4":
            ui_add_group()
        elif choice == "5":
            show_groups()
        elif choice == "6":
            print("Arrivederci!")
            break
        else:
            print(f"'{choice}' non è un'opzione valida.")


def main():
    ui_ask_what_to_do()
    return 0


if __name__ == "__main__":
    sys.exit(main())
