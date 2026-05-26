"""
azienda_1.py

Prerequisiti:
Aver svolto l'Esercitazione "Azienda 1" (modulo "Progettazione").


Si consideri lo schema concettuale prodotto dagli analisti
per il progetto "Azienda 1".

Si scriva un programma Python orientato agli oggetti che permetta di:

1) rappresentare impiegati con:
        - nome (str)
        - cognome (str),
        - stipendio attuale in Euro (float, impedendo che possano essere inseriti valori <= 0)
        - data di nascita (un valore del tipo Python datetime.date, v. seguito)

2) rappresentare dipartimenti con:
        - nome (str)
        - telefono (str)

3) il singolo dipartimento di afferenza di ogni impiegato e la
   sua data di afferenza.

4) l'impiegato direttore di ogni dipartimento.

Questi requisiti sono un frammento di quelli gestiti durante
la fase di Analisi concettuale di "Azienda 1", con le seguenti
semplificazioni, necessarie per permettere l'implementazione Python
con i costrutti che conosciamo già:
        - un impiegato può dirigere anche più dipartimenti
          (l'analista ha invece imposto "al massimo uno")
        - ignoriamo i progetti aziendali.


Gestire la persistenza dei dati tramite un file JSON.

# Importiamo la class 'date' dal modulo 'datetime'.
# Le istanze di 'date' rappresentano valori del tipo 'Data'.
# https://docs.python.org/3/library/datetime.html#datetime.date

"""

import json
import sys
from datetime import date
from typing import Self

# Class di interesse per il programma


class Department:
    all_departments: dict = dict()
    next_i = 0

    # Non ci aspettiamo più che l'utente invochi direttamente il
    # costruttore (e quindi che invocato direttamente __init__ con gli
    # argoment i, n, p).
    # Forniamo invece @classmethod opportuni
    # per creare nuovi oggetti (factory methods)
    # Il metodo __init__(self, i,n,p) sarà utilizzato in modo
    # appropriato dai factory methods.
    def __init__(self, i: int, name: str, phone: str) -> None:

        assert type(self).next_i not in type(self).all_departments, (
            "Error, this should NEVER happen!"
        )

        self.i = i
        self.name = name
        self.phone = phone

        # Aggiungo il nuovo oggetto al dizionario di tutti gli oggetti della classe esistenti
        type(self).all_departments[self.i] = self

    @classmethod
    # Crea un nuovo oggetto, assegnandogli un id ('i') automaticamente
    def create(cls, name: str, phone: str) -> Self:
        result = cls(cls.next_i, name, phone)
        cls.next_i += 1
        return result

    @classmethod
    # Crea un nuovo oggetto, con id 'i' e dati nel dizionario 'd'
    # ('d' sarà ottenuto dal database JSON)
    def create_from_dict(cls, i: int, d: dict) -> Self:
        result = cls(i, d["name"], d["phone"])

        if cls.next_i <= i:
            cls.next_i = (
                i + 1
            )  # evitiamo che l'auto-creazione di nuovi ID diventi problematica

        return result

    @classmethod
    def search(cls, n: str | None, p: str | None) -> list[Self]:
        result = []
        for d in cls.all_departments.values():
            if (n != "" and n is not None and d.name != n) or (
                p != "" and p is not None and d.phone != p
            ):
                continue

            result.append(d)
        return result

    @classmethod
    def get(cls, i: int) -> Self:
        # print(f"Getting department {i}. All departments: {cls.all_departments}")
        return cls.all_departments[i]

    def to_str(self) -> str:
        return f"{self.i}: {self.name} (phone: {self.phone})"


class Employee:
    # attributi di classe (condivisi tra tutti gli oggetti)
    all_employees: dict = dict()
    next_i = 0

    # Gestione del tutto analoga a Department.
    # Per creare gli uggetti l'utente userà i factory methods
    # che, a loro volta, useranno __init__() in modo corretto
    def __init__(
        self,
        i: int,
        name: str,
        surname: str,
        wage: float,
        birth_date: date,
        # il link, con il suo attributo!
        department: Department | None,
        emp_date: date | None,
    ) -> None:

        assert type(self).next_i not in type(self).all_employees, (
            "Error, this should NEVER happen!"
        )

        assert wage > 0, "Error, wage cannot be zero or negative"

        self.i = i
        self.name = name
        self.surname = surname
        self.wage = wage
        self.birth_date = birth_date

        self.department = department
        self.emp_date = emp_date

        type(self).all_employees[self.i] = self

    @classmethod
    # Crea un nuovo oggetto, assegnandogli un id ('i') automaticamente
    def create(
        cls,
        name: str,
        surname: str,
        wage: float,
        birth_date: date,
        department: Department | None,
        emp_date: date | None,
    ) -> Self:

        if department is None:
            emp_date = None

        result = cls(cls.next_i, name, surname, wage, birth_date, department, emp_date)
        cls.next_i += 1
        return result

    @classmethod
    # Crea un nuovo oggetto, con id 'i' e dati nel dizionario 'd'
    # ('d' sarà ottenuto dal database JSON)
    def create_from_dict(cls, i: int, d: dict) -> Self:
        result = cls(
            i,
            d["name"],
            d["surname"],
            d["wage"],
            date.fromisoformat(d["birth date"]),
            Department.get(d["department"]) if d["department"] is not None else None,
            (
                date.fromisoformat(d["employment date"])
                if d["employment date"] is not None
                else None
            ),
        )
        if cls.next_i <= i:
            cls.next_i = (
                i + 1
            )  # evitiamo che l'auto-creazione di nuovi ID diventi problematica

        return result

    @classmethod
    def search(cls, n: str | None, s: str | None, d: Department | None):
        result = []
        for e in cls.all_employees.values():
            if (
                (n != "" and n is not None and e.name != n)
                or (s != "" and s is not None and e.surname != s)
                or (d is not None and e.department != d)
            ):
                continue

            result.append(e)

        return result

    def to_str(self):
        department_str = (
            f"{self.department.to_str()} (from {self.emp_date})"
            if self.department is not None
            else "None"
        )
        return f"{self.surname}, {self.name}\n\r\t- wage = {self.wage}\n\r\t- birth_date = {self.birth_date}\n\r\t- department = {department_str}"


def input_date(msg: str):
    result = None
    while result is None:
        try:
            result = date.fromisoformat(input(f"{msg} "))
        except ValueError:
            print("date in wrong format, please use YYYY-MM-DD")
    return result


def input_department(msg: str, allow_none: bool) -> Department | None:
    result = None

    print("Department? ")
    for d in Department.search(None, None):
        print(f" - {d.to_str()}")

    while result is None:
        dept_id_str = input("ID? ")
        if dept_id_str == "" and allow_none is True:
            break

        try:
            dept_id = int(dept_id_str)
            result = Department.get(dept_id)
        except Exception:
            print("Write the ID of a department")

    return result


def ui_add_employee():
    n = input("Name? ")
    s = input("Surname? ")
    w = input("Wage? ")

    bdate = input_date("Birth date? ")
    d = input_department("Department? ", True)

    emp_date = None
    if d is not None:
        emp_date = input_date("Employment date? ")

    return Employee.create(n, s, float(w), bdate, d, emp_date)


def ui_search_employees():
    n = input("Name?")
    s = input("Surname?")
    d = input_department("Department? ", True)
    for e in Employee.search(n, s, d):
        print(f" - {e.to_str()}")


def ui_add_department():
    n = input("Name?")
    p = input("Phone?")
    d = Department.create(n, p)
    print(f"Created department {d.to_str()}")


def ui_search_departments():
    n = input("Name?")
    p = input("Phone?")
    for d in Department.search(n, p):
        print(f" - {d.to_str()}")


def ui_ask_what_to_do():
    while True:
        print(
            "\n\n\n----------\n\nChoose an action:\n"
            + " - add department: Add a new department\n"
            + " - search departments: Search departments\n"
            + " - add employee: Add a new employee\n"
            + " - search employees: Search employees\n"
            + " - exit: Exit"
        )

        choice = input("Action? ")

        if choice == "add department":
            ui_add_department()
        elif choice == "search departments":
            ui_search_departments()
        elif choice == "add employee":
            ui_add_employee()
        elif choice == "search employees":
            ui_search_employees()
        elif choice == "exit":
            print("Arrivederci!")
            break
        else:
            print(f"{choice}? mmm, unknown command...")


# Costante globale: nome del file che mantiene i dati
datafile = "data.json"


def load_all():
    print(f"Loading data file '{datafile}':")
    try:
        fp = open(datafile, "rt")
        data: dict = json.load(fp)

        # Leggi l'entry 'Department' del database
        print(" - Departments")
        try:
            for i, obj in data["Department"].items():
                try:
                    print(f"   - Found data for department {i}: {obj}")
                    d = Department.create_from_dict(int(i), obj)
                    print(f"     --> Created department object: {d.to_str()}")
                except Exception as ex:
                    print(
                        f"Error while reading department {obj} in database. Detailed error: {ex}"
                    )
        except KeyError:
            print("Error: misformed data file: entry 'Department' does not exist")

        # Leggi l'entry 'Employee' del database
        print(" - Employees")
        try:
            for i, obj in data["Employee"].items():
                print(f"   - Found data for employee {i}: {obj}")
                try:
                    e = Employee.create_from_dict(int(i), obj)
                    print(f"     --> Created employee object: {e.to_str()}")
                except Exception as ex:
                    print(
                        f"Error while reading employee {obj} in database. Detailed error: {ex}"
                    )
        except KeyError:
            print("Error: misformed data file: entry 'Employee' does not exist")

        # Chiude lo stream del file
        fp.close()

    except FileNotFoundError:
        print(f"File '{datafile}' not found. Starting with an empty database.")
    except Exception as ex:
        print(f"Error: cannot open data file. Error: {ex}")


def save_all():
    print(f"Saving data to file '{datafile}'...")

    # Costruiamo la struttura dati che verrà salvata nel JSON
    data_to_save = {"Department": {}, "Employee": {}}

    # Serializziamo i dipartimenti
    for dept_id, dept in Department.all_departments.items():
        data_to_save["Department"][str(dept_id)] = {
            "name": dept.name,
            "phone": dept.phone,
        }

    # Serializziamo gli impiegati
    for emp_id, emp in Employee.all_employees.items():
        data_to_save["Employee"][str(emp_id)] = {
            "name": emp.name,
            "surname": emp.surname,
            "wage": emp.wage,
            "birth date": emp.birth_date.isoformat(),
            "department": emp.department.i if emp.department is not None else None,
            "employment date": emp.emp_date.isoformat()
            if emp.emp_date is not None
            else None,
        }
    try:
        # Scriviamo il dizionario sul file convertendolo in JSON
        with open(datafile, "wt") as fp:
            json.dump(data_to_save, fp, indent=4)
        # indent=4 rende il file JSON formattato in modo leggibile
        print("Data successfully saved!")
    except Exception as e:
        print(f"Error while saving data. {e.__class__.__name__}: ", e)


def main():
    try:
        load_all()
        ui_ask_what_to_do()
        save_all()
    except Exception as e:
        print(f"Error type: {e.__class__.__name__}\nmessage: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
