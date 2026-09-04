import re
from pathlib import Path
from sys import exit
from typing import Any, Optional, Self


class Targa(str):
    __patterns = [r"[A-Z0-9]{3,7}", r"[A-Z]{1,2}\s*[\d]{1,6}"]

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, targa: str):
        if targa is None or targa == "":
            raise ValueError("La targa non può essere vuoto.")

        result = False

        for pattern in cls.get_patterns():
            if re.fullmatch(pattern, targa):
                result = True
                break

        if not result:
            patterns_str = ", ".join(cls.get_patterns())
            raise ValueError(
                f"\nLa targa '{targa}' non è valida. Deve seguire almeno uno di questi pattern: {patterns_str}"
            )

        return super().__new__(cls, targa)

    def __repr__(self):
        return f"Targa('{self}')"


class Telefono(str):
    __patterns = frozenset(
        [
            r"^(?:(?:\+|00)39)?\s?[3]\d{2}(?:\s?\d{3,4}){2,3}$",
            r"^\+?\s?[\d]{6,10}$",
        ]
    )

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, numero: str | int):
        if numero is None or numero == "":
            raise ValueError("Il numero di telefono non può essere vuoto.")

        result = False

        for pattern in cls.get_patterns():
            str_numero = str(numero)
            if re.fullmatch(pattern, str_numero):
                result = True
                break

        if not result:
            patterns_str = ", ".join(cls.get_patterns())
            raise ValueError(
                f"\nIl numero di telefono '{numero}' non è valido. Deve seguire almeno uno di questi pattern:\n{patterns_str}"
            )

        return super().__new__(cls, numero)

    def __str__(self):
        return self

    def __repr__(self):
        return f"Telefono('{self}')"


class CodiceFiscale(str):
    __patterns = frozenset(
        [
            r"[A-Z0-9]{0,16}",
            r"[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z][0-9]{3}[A-Z]",
            r"[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[0-9A-Z]{5}",
        ]
    )

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, cf: str):
        if cf is None or cf == "":
            raise ValueError("Il Codice Fiscale non può essere vuoto.")

        if len(cf) != 16:
            raise ValueError("Il Codice Fiscale deve contenere 16 caratteri.")

        cf_pulito = cf.strip().upper()
        result = False

        for pattern in cls.get_patterns():
            if re.fullmatch(pattern, cf_pulito):
                result = True
                break

        if not result:
            patterns_str = ", ".join(cls.get_patterns())
            raise ValueError(
                f"\nIl codice fiscale '{cf}' non è valido. "
                + f"Deve seguire almeno uno di questi pattern:\n{patterns_str}"
            )
        # Poiché le stringhe sono immutabili, dobbiamo intercettare
        # l'allocazione tramite __new__ invece di __init__
        return super().__new__(cls, cf_pulito)

    def __str__(self):
        return self

    def __repr__(self):
        return f"CodiceFiscale('{self}')"


# Creazione tipo composto
class Indirizzo:
    __civico_patterns = frozenset([r"\d+[\w\W\d\s/.-]*"])

    @classmethod
    def get_civico_patterns(cls):
        return cls.__civico_patterns

    # Oppure, usare soltanto l'init.
    def __init__(self, via: str, civico: str):
        if via is None or civico is None:
            raise TypeError(
                "Errore nell'Indirizzo: via e civico non possono essere vuoti."
            )

        # 1. Controlli e Validazioni
        civico_valido = False
        for pattern in self.get_civico_patterns():
            if re.fullmatch(pattern, str(civico)):
                civico_valido = True
                break

        if not civico_valido:
            raise ValueError(f"Il numero civico '{civico}' non è valido.")

        # 2. Creazione degli attributi (avviene qui in automatico)
        self.via = via
        self.civico = civico

    def get_via(self):
        return self.via

    def get_civico(self):
        return self.civico

    def __str__(self):
        return f"{self.via} {self.civico}"

    def __repr__(self):
        return f"Indirizzo(via='{self.get_via()}', civico='{self.get_civico()}')"

    # Per i dati composti ridefiniamo i metodi di uguaglianza

    def __hash__(self) -> int:
        return hash((self.via, self.civico))

    def __eq__(self, other: Any) -> bool:
        if other is None or type(other) is not type(self) or hash(self) != hash(other):
            return False
        return (self.get_via(), self.get_civico()) == (
            other.get_via(),
            other.get_civico(),
        )


class IntGZ(int):
    def __new__(cls, numero: int | float) -> Self:
        if type(numero) not in (int, float):
            raise TypeError("Il tipo del numero dev'essere un 'int' oppure un 'float'")
        if numero <= 0:
            raise ValueError("Il numero non può essere negativo o zero")
        return super().__new__(cls, numero)


class IntGEZ(int):
    def __new__(cls, numero: int | float) -> Self:
        if type(numero) not in (int, float):
            raise TypeError("Il tipo del numero dev'essere un 'int' oppure un 'float'")
        if numero < 0:
            raise ValueError("Il numero non può essere negativo")
        return super().__new__(cls, numero)


# TEST:
def execute_tests() -> int:

    print("\n=== TEST: TARGHE ===")
    targhe = ["129A", "AZ 1246", "", "ZAZHATT"]
    for t_test in targhe:
        try:
            t = Targa(t_test)
            print(f"Successo: {t}")
        except ValueError as e:
            print(f"Errore: {e}")

    print("\n=== TEST: TELEFONO ===")
    numeri = ["3331234567", "1234567", "", "(+0) 0"]
    for n_test in numeri:
        try:
            tel = Telefono(n_test)
            print(f"Successo: {tel}")
        except ValueError as e:
            print(f"Errore: {e}")

    print("\n=== TEST: CODICE FISCALE ===")
    cf_errati = [" ", "A1B2C3D4E5", "RSS-MRA-80A01-HA", ""]
    cf_corretti = []
    try:
        cf_file = Path("cf.example")
        content = cf_file.read_text().rstrip()
        cf_corretti = [line for line in content.splitlines()]
    except FileNotFoundError:
        cf_corretti = ["CNTLSN93R27D612V", "BRTGLI84B09H703M", "DLNGPP79L30F158N"]

    cf_da_testare = cf_errati + cf_corretti

    for cf_test in cf_da_testare:
        try:
            cf = CodiceFiscale(cf_test)
            print(f"Successo: {cf}")
        except ValueError as e:
            print(f"Errore: {e}")

    print("\n=== TEST: INDIRIZZO ===")
    # Prepariamo un cap valido e uno invalido per i test composti

    # 1. Indirizzo Standard Valido
    try:
        ind1 = Indirizzo("Via Trastevere", "12/A")
        print(f"Successo: {ind1}")
    except ValueError as e:
        print(f"Errore: {e}")

    # 2. Indirizzo Civico Alternativo Valido (es. Interno o scala)
    try:
        ind2 = Indirizzo("Corso Vittorio Emanuele", "154 - Scala B")
        print(f"Successo: {ind2}")
    except ValueError as e:
        print(f"Errore: {e}")

    # 3. ERRORE: Civico non valido (non inizia con un numero)
    try:
        ind_err1 = Indirizzo("Via Roma", "Senza Numero")
        print(f"Successo: {ind_err1}")
    except ValueError as e:
        print(f"Errore atteso: {e}")

    # 4. TEST UGUAGLIANZA (Uguaglianza strutturale ed equivalenza hash)
    print("\n-> Sotto-test Uguaglianza Indirizzi:")
    ind_a = Indirizzo("Via Garibaldi", "10")
    ind_b = Indirizzo("Via Garibaldi", "10")
    ind_c = Indirizzo("Via Garibaldi", "11")

    print(f"ind_a == ind_b? {ind_a == ind_b} (Atteso: True)")
    print(f"ind_a == ind_c? {ind_a == ind_c} (Atteso: False)")
    print(
        f"Gli hash di ind_a e ind_b coincidono? {hash(ind_a) == hash(ind_b)} (Atteso: True)"
    )

    return 0


if __name__ == "__main__":
    exit(execute_tests())
