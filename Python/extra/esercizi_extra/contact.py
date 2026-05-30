from typing import Self


class Contact:
    number: int = 0
    contacts: list = []

    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.number}. {self.name}"

    # Factory Method - spostiamo l'aggiornamento degli attributi di classe
    # in questo metodo, lasciando __init__ solo ad assegnare valori delle istanze
    @classmethod
    def create(cls, name, number) -> Self:
        contact = cls(name, number)
        cls.contacts.append(contact)
        cls.number += 1
        return contact


Contact.create("Angelo", Contact.number)
Contact.create("Piero", Contact.number)
Contact.create("Serena", Contact.number)

print(Contact.number)

for contact in Contact.contacts:
    print(contact)

print(Contact.number)
