import re
from sys import exit
from typing import Any

class Targa(str):
    __patterns = [r'[A-Z0-9]{3,7}', r'[A-Z]{1,2}\s*[\d]{1,6}']

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, targa: str):
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

    __patterns = [
        r'^(?:(?:\+|00)39)?\s?[3]\d{2}(?:\s?\d{3,4}){2,3}$', 
        r'^\+?\s?[\d]{6,10}$'
    ]

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, numero: str|int):
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
    __patterns = [
        r"[A-Z0-9]{0,16}", 
        r"[A-Z]{6}[0-9]{2}[A-EHLMPRST][0-9]{2}[A-Z][0-9]{3}[A-Z]", 
        r"[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[0-9A-Z]{5}"
    ]

    @classmethod
    def get_patterns(cls):
        return cls.__patterns

    def __new__(cls, cf: str):
        result = False

        for pattern in cls.get_patterns():
            if re.fullmatch(pattern, cf):
                result = True
                break

        if not result:
            patterns_str = ", ".join(cls.get_patterns())
            raise ValueError(
                f"\nIl codice fiscale '{cf}' non è valido. Deve seguire almeno uno di questi pattern:\n{patterns_str}"
            )

        return super().__new__(cls, cf)


    def __str__(self):
        return self

    def __repr__(self):
        return f"CodiceFiscale('{self}')"


class CAP(str):

    def __new__(cls, cap: str):
        str_cap = str(cap)
        if not re.fullmatch(r'[0-9]{5}', str_cap):
            raise ValueError(f"Il cap '{cap}' inserito non è valido.")
        
        return super().__new__(cls, str_cap)

    def __str__(self):
        return self

    def __repr__(self):
        return f"CAP('{self}')"


class Indirizzo: 

    __civico_patterns = [r"\d+[\w\W\d\s/.-]*"]

    @classmethod
    def get_civico_patterns(cls):
        return cls.__civico_patterns


    # Alternativa all'init. 

    # def __new__(cls, via: str, civico: str, cap: CAP):
    #     if not isinstance(cap, CAP):
    #         raise ValueError("Il parametro 'cap' deve essere un'istanza valida della classe CAP.")

    #     result = False

    #     for pattern in cls.get_civico_patterns():
    #         if re.fullmatch(pattern, str(civico)):
    #             result = True
    #             break

    #     if not result:
    #         raise ValueError(f"Il numero civico '{civico}' non è valido.")

    #     instance = super().__new__(cls)
    #     instance.via = via
    #     instance.civico = civico
    #     instance.cap = cap

    #     return instance


    # Oppure, usare soltanto l'init. 
    def __init__(self, via: str, civico: str, cap: CAP):
        # 1. Controlli e Validazioni
        if not isinstance(cap, CAP):
            raise ValueError("Il parametro 'cap' deve essere un'istanza valida della classe CAP.")

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
        self.cap = cap


    def get_via(self):
        return self.via

    def get_civico(self):
        return self.civico

    def get_cap(self):
        return self.cap


    def __str__(self):
        return f"{self.via} {self.civico}, {self.cap}"

    def __repr__(self):
        return f"Indirizzo(via='{self.get_via()}', civico='{self.get_civico()}', cap={repr(self.get_cap())})"


    # Per i dati composti ridefiniamo i metodi di uguaglianza

    def __hash__(self) -> int:
        return hash((self.via, self.civico, str(self.cap)))

    def __eq__(self, other: Any) -> bool:
        # type() verifica la classe esatta, mentre isinstance() verifica anche le sottoclassi
        if other is None or type(other) is not type(self) or hash(self) != hash(other):
            return False
        return (self.get_via(), self.get_civico(), str(self.get_cap())) == (other.get_via(), other.get_civico(), str(other.get_cap()))



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
    codici = ["RSSMRA80A01H501U", "A1B2C3D4E5", "RSSMRA80A01H501UX", "RSS-MRA-80A01-H"]
    for cf_test in codici:
        try:
            cf = CodiceFiscale(cf_test)
            print(f"Successo: {cf}")
        except ValueError as e:
            print(f"Errore: {e}")

    print("\n=== TEST: CAP ===")
    caps = ["12345", "0", "ABC/a", "3-a. "]
    for cap_test in caps:
        try:
            cf = CodiceFiscale(cap_test)
            print(f"Successo: {cap_test}")
        except ValueError as e:
            print(f"Errore: {e}")

    print("\n=== TEST: INDIRIZZO ===")
    # Prepariamo un cap valido e uno invalido per i test composti
    cap_roma = CAP("00153")
    
    # 1. Indirizzo Standard Valido
    try:
        ind1 = Indirizzo("Via Trastevere", "12/A", cap_roma)
        print(f"Successo: {ind1}")
    except ValueError as e:
        print(f"Errore: {e}")
        
    # 2. Indirizzo Civico Alternativo Valido (es. Interno o scala)
    try:
        ind2 = Indirizzo("Corso Vittorio Emanuele", "154 - Scala B", cap_roma)
        print(f"Successo: {ind2}")
    except ValueError as e:
        print(f"Errore: {e}")

    # 3. ERRORE: Civico non valido (non inizia con un numero)
    try:
        ind_err1 = Indirizzo("Via Roma", "Senza Numero", cap_roma)
        print(f"Successo: {ind_err1}")
    except ValueError as e:
        print(f"Errore atteso: {e}")

    # 4. TEST UGUAGLIANZA (Uguaglianza strutturale ed equivalenza hash)
    print("\n-> Sotto-test Uguaglianza Indirizzi:")
    ind_a = Indirizzo("Via Garibaldi", "10", cap_roma)
    ind_b = Indirizzo("Via Garibaldi", "10", cap_roma)
    ind_c = Indirizzo("Via Garibaldi", "11", cap_roma)
    
    print(f"ind_a == ind_b? {ind_a == ind_b} (Atteso: True)")
    print(f"ind_a == ind_c? {ind_a == ind_c} (Atteso: False)")
    print(f"Gli hash di ind_a e ind_b coincidono? {hash(ind_a) == hash(ind_b)} (Atteso: True)")

    return 0

if __name__ == "__main__":
    exit(execute_tests())

