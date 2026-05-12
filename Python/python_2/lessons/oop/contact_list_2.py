from sys import exit


class Group:
    name: str
    description: str

    def __init__(self, n: str, desc: str):
        self.name = n
        self.description = desc

    def to_str(self, name: str, desc: str):
        if name is not None and name != "":
            return f"Title: {self.name}\n" + f"Description: {self.description}"

    def add(self): ...

    def show(self): ...

    def search(self): ...

    def delete(self): ...


class Contact:
    name: str
    lastname: str
    phone: str
    email: str
    group: str

    def __init__(self, n: str, l: str, p: str, e: str, g: str):
        self.name = n
        self.lastname = l
        self.phone = p
        self.email = e
        self.group = g

    def to_str(self, name: str, lastname: str, phone: str, email: str, group: Group):
        if self.name == "" or self.name is None:
            return ""

        g = group.name if not None else ""
        return (
            f"* {self.lastname}, {self.name}:\n"
            + f"{self.phone}\n"
            + f"{self.email}\n"
            + f"{self.g.name}"
        )


class Agenda:
    """Classe 'Contenitore' che gestisce la logica dei dati"""

    def __init__(self):
        self.contacts = []
        self.groups = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def search_contact(self, query: str):
        # Logica di ricerca qui
        return [c for c in self.contacts if query.lower() in c.name.lower()]

    def show_contacts(self):
        print(f"\nIn rubrica ci sono i seguenti {len(self.contacts)} contatti:\n")
        for c in self.contacts:
            print(self.contacts.to_str(c))
        print("Fatto.")

    def add_group(): ...

    def show_group(): ...

    def search_group(): ...



class UI:
    def __init__(self, agenda: Agenda):
        self.agenda = agenda

    @staticmethod
    def main_menu():
        while True:
            menu_choice = 3

            print(
                "\nScegli che tipo di azioni vuoi effettuare\n"
                + "\r\t1. contatti: Azioni sui contatti\n"
                + "\r\t2. gruppi: Azioni sui gruppi\n"
                + "\r\t6. exit: Esci\n"
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
                        + "\r\t2. show: Mostra tutta la contacts\n"
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
                        self.agenda.add()
                    elif user_choice == "show" or user_choice == "2":
                        show()
                    elif user_choice == "search" or user_choice == "3":
                        search()
                    elif user_choice == "delete" or user_choice == "4":
                        delete()
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
                        add(
                            input("\nIndica il nome del gruppo:\n>\t").strip(),
                            input("\nScrivi una descrizione del gruppo:\n>\t").strip(),
                        )
                    elif group_choice == "show" or group_choice == "2":
                        show()
                    elif group_choice == "search" or group_choice == "3":
                        search()
                    elif group_choice == "exit" or group_choice == "4":
                        print("\nRicevuto! Tornerai al menu principale\n")
                        break
                    else:
                        print(f"{group_choice}? non è una scelta valida. Riprova\n")


def main():

    c1 = Contact("Mario", "Rossi", "+3976237438", "mario@gmail.com", "IT")
    c2 = Contact("Ugo", "Bianchi", "+3986190354", "ugo@gmail.com", "")
    c3 = Contact("Elena", "Gialli", "+3921357560", "elena@gmail.com", "HR")

    g1 = Group("IT", "Information Technology")
    g2 = Group("HR", "Human Resources")

    contacts = [c1, c2, c3]
    groups = {g1, g2}

    try:
        UI.main_menu()
        return 0
    except Exception as e:
        raise Exception(f"Errore generico: {e}")


if __name__ == "__main__":
    exit(main())
