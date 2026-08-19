import datetime
import re
import sys

# Da rivedere e completare... continua tu!

# INFO: DATATYPES

class CodiceFiscale(str):
    def __new__(cls, v: str):
        if v is None:
            raise ValueError("Un codice fiscale non può essere None")
        v = v.strip().upper()

        if not re.fullmatch("[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z0-9]{4}[A-Z]", v):
            raise ValueError(
                f"La stringa '{v}' non è un codice fiscale sintatticamente legale"
            )

        return super().__new__(cls, v)


class Int_GE0(int):
    def __new__(cls, v: int):
        if v is None:
            raise ValueError("Un Int_GE0 non può essere None")

        if not isinstance(v, int):
            raise ValueError(f"'{v}' non è un int")

        if v < 0:
            raise ValueError(f"'{v}' non è >= 0")

        return super().__new__(cls, v)


class Telefono(str):
    def __new__(cls, v: str):
        if v is None:
            raise ValueError("Un numero di telefono non può essere None")
        v = v.replace(" ", "")

        if not re.fullmatch("\\+[0-9 ]{0,15}", v):
            raise ValueError(
                f"La stringa '{v}' non è un numero di telefono sintatticamente legale"
            )

        return super().__new__(cls, v)


class Targa(str):
    def __new__(cls, v: str):
        if v is None:
            raise ValueError("Un numero di targa non può essere None")
        v = v.upper().replace(" ", "")

        if not re.fullmatch("[A-Z]{2}[0-9]{3}[A-Z]{2}", v):
            raise ValueError(
                f"La stringa '{v}' non è un numero di targa sintatticamente legale"
            )

        return super().__new__(cls, v)


class Indirizzo:
    __via: str
    __civico: str
    __cap: str

    def __init__(self, v: str, civ: str, cap: str):
        if v is None:
            raise ValueError("La via non può essere None")
        if civ is None:
            raise ValueError("Il civico non può essere None")
        if cap is None:
            raise ValueError("Il cap non può essere None")
        if not re.fullmatch("[0-9]+(/[a-zA-Z]+)?", civ):
            raise ValueError(f"Il valore '{civ}' non è un numero civico legale")
        if not re.fullmatch("[0-9]{5}", cap):
            raise ValueError(f"Il valore '{cap}' non è un numero CAP legale")

        self.__via = v
        self.__civico = civ
        self.__cap = cap

    def __hash__(self) -> int:
        return hash((self.via(), self.civico(), self.cap()))

    def __eq__(self, o: Any) -> bool:
        if o is None or type(o) != type(self) or hash(self) != hash(o):
            return False
        return (
            self.civico() == o.civico()
            and self.cap() == o.cap()
            and self.via() == o.via()
        )

    def get_via(self) -> str:
        return self.__via

    def get_civico(self) -> str:
        return self.__civico

    def get_cap(self) -> str:
        return self.__cap

    def __str__(self) -> str:
        return f"{self.get_via()} {self.get_civico()}, {self.get_cap()}"

# INFO: CLASSES

class Nazione:
    __nome: str  # <<imm>> {id}
    __regex_targa: set[str]  # [1..*]

    __objects_by_name: dict[str, Self] = dict()

    @classmethod
    def all_objects(cls) -> set[Self]:
        return set(cls.__objects_by_name.values())

    def nome(self) -> str:
        return self.__nome

    def regex_targa(self) -> frozenset[str]:
        return frozenset(self.__regex_targa)

    def __set_nome(self, n: str):
        if n is None:
            raise ValueError(f"nome non può essere None")
        if not isinstance(n, str):
            raise ValueError(f"nome essere una str")

        if n in type(self).__objects_by_name:
            raise ValueError(f"Il nome {n} è già assegnato")

        if self.nome():
            del type(self).__objects_by_name[self.nome()]

        self.__nome = n
        type(self).__objects_by_name[n] = self

    def add_regex_targa(self, re: str):
        if re is None or len(re) == 0:
            raise ValueError(f"regex_targa non può avere elementi None o vuoti")
        if not isinstance(re, str):
            raise ValueError(f"regex_targa deve avere elementi di tipo str")

        self.__regex_targa.add(re)

    def remove_regex_targa(self, re: str):
        if len(self.__regex_targa) == 1:  # implementa [1..*]
            raise ValueError(f"L'oggetto {self} ha un solo valore per regex_targa")
        self.__regex_targa.remove(re)

    def __str__(self) -> str:
        return self.nome()

    def __init__(self, nome: str, re: str):
        self.__nome = None
        self.__regex_targa = set()

        self.add_regex_targa(re)
        self.__set_nome(nome)


class Citta:
    __nome: str  ## <<imm>>
    __nazione: Nazione  # <<imm>>

    __citta_off: set[citta_off]  # 0..*

    def nome(self) -> str:
        return self.__nome

    def nazione(self) -> Nazione:
        return self.__nazione

    def __set_nome(self, n: str):
        if not n or not isinstance(n, str):
            raise TypeError(f"n illegale: {n}")
        self.__nome = n

    def __set_nazione(self, n: Nazione):
        if not n or not isinstance(n, Nazione):
            raise TypeError(f"n illegale: {n}")
        self.__nazione = n

    def _add_citta_off(self, l: citta_off):
        if not l or not isinstance(l, citta_off):
            raise TypeError(f"l illegale: {l}")
        if l.citta() != self:
            raise ValueError(f"il link non mi appartiene")

        print(f"Adding link ({l.citta().nome()}, {l.officina().nome()}):citta_off")
        self.__citta_off.add(l)

    def _remove_citta_off(self, l: citta_off):
        if not l or not isinstance(l, citta_off):
            raise TypeError(f"l illegale: {l}")
        if l.citta() != self:
            raise ValueError(f"il link non mi appartiene")

        self.__citta_off.remove(l)

    def __init__(self, nome: str, nazione: Nazione):
        self.__citta_off = set()
        self.__set_nome(nome)
        self.__set_nazione(nazione)

    def __str__(self) -> str:
        return f"{self.nome()} ({self.nazione()})"


class Officina:
    __nome: str  # <<imm>>
    __indirizzo: Indirizzo
    __telefono: Telefono

    __lavora: set[lavora]

    __dirige: dirige

    __citta_off: citta_off  # 1..1

    def _add_citta_off(self, l: citta_off):
        assert self.__citta_off is None

        if not l or not isinstance(l, citta_off):
            raise TypeError(f"l illegale: {l}")
        if l.officina() != self:
            raise ValueError(f"il link non mi appartiene")
        self.__citta_off = l

    def _remove_citta_off(self, l: citta_off):
        assert self.__citta_off == l

        if not l or not isinstance(l, citta_off):
            raise TypeError(f"l illegale: {l}")
        if l.officina() != self:
            raise ValueError(f"il link non mi appartiene")

        self.__citta_off = None

    def nome(self) -> str:
        return self.__nome

    def indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def telefono(self) -> Telefono:
        return self.__telefono

    def dirige(self) -> dirige:
        return self.__dirige

    def lavora(self) -> frozenset[lavora]:
        return frozenset(self.__lavora)

    def citta(self) -> Citta:
        return (
            self.__citta_off.citta()
            if self.__citta_off
            else "(Officina.__citta is None)"
        )

    def __set_nome(self, v: str):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, str):
            raise ValueError("v deve essere una str")
        self.__nome = v

    def set_indirizzo(self, v: Indirizzo):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, Indirizzo):
            raise ValueError("v deve essere un Indirizzo")
        self.__indirizzo = v

    def set_telefono(self, v: Telefono):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, Telefono):
            raise ValueError("v deve essere un Telefono")

        self.__telefono = v

    def _add_dirige(self, l: dirige):
        assert self.__dirige == None
        self.__dirige = l

    def _remove_dirige(self):
        self.__dirige = None

    def cambia_direttore(self, p: Persona):
        dirige._create(self, p)

    def cambia_citta(self, c: Citta):
        citta_off._remove(self.citta_off())
        citta_off._create(c, self)

    def _add_lavora(self, l: lavora):
        if l is None:
            raise ValueError("l non può essere None")
        if not isinstance(l, lavora):
            raise ValueError("l deve essere di class lavora")
        if not l.is_valid():
            raise ValueError("l non è valido!")
        if l.officina() != self:
            raise ValueError("l non mi appartiene")

        self.__lavora.add(l)

    def _remove_lavora(self, l: lavora):
        assert self.is_dipendente(), "self non è un dipendente"
        if l is None:
            raise ValueError("l non può essere None")
        if l.officina() != self:
            raise ValueError("l non mi appartiene")

        self.__lavora.remove(l)

    def __init__(
        self,
        nome: str,
        indirizzo: Indirizzo,
        citta: Citta,
        telefono: Telefono,
        direttore: Persona,
    ):
        self.__citta_off = None
        self.__dirige = None
        self.__lavora = set()

        self.__set_nome(nome)
        self.set_indirizzo(indirizzo)
        self.set_telefono(telefono)
        dirige._create(self, direttore)
        citta_off._create(citta, self)

    def __str__(self) -> str:
        return f"{self.nome()} | {self.indirizzo()}, {self.citta()}"

    def text(self) -> str:
        result = (
            f"{self.nome()}:\n"
            + f" - indirizzo: {self.indirizzo()}, {self.citta()}\n"
            + f" - telefono: {self.telefono()}\n"
            + f" - direttore: {self.dirige().persona()}\n"
            + f" - dipendenti: {len(self.lavora())}"
        )

        if len(self.lavora()) > 0:
            dipendenti_as_list = list()
            for l in self.lavora():
                dipendenti_as_list.append(str(l.persona()))
            result += ", che sono: " + ",".join(dipendenti_as_list)
        return result


class Persona:
    __cf: CodiceFiscale  # <<imm>> {id}
    __nome: str  # <<imm>>
    __cognome: str  # <<imm>>
    __indirizzo: Indirizzo
    __citta: Citta
    __tel: Telefono
    __nascita: datetime.date | None  # <<imm>> <<poss noto alla nascita>>
    __is_cliente: bool
    __is_dipendente: bool
    __is_direttore: bool

    __lavora: set[lavora]  # 0..*
    __dirige: set[dirige]  # 0..*

    # Vincoli esterni
    # IMPLEMENTATO [V.Persona.nascita_sse_direttore]
    # Per ogni p:Persona, deve essere:
    # 	- p.nascita ha un valore se e solo se p.is_direttore = TRUE

    # **DA IMPLEMENTARE [V.Persona.lavora_sse_dipendente]
    # Per ogni p:Persona, deve essere:
    # 	- p ha un link di assoc. "lavora" se e solo se p.is_dipendente = TRUE

    # **DA IMPLEMENTARE IN CLASSS OFFICINA [V.Persona.se_dirige_allora_direttore]
    # Per ogni p:Persona, deve essere:
    # 	- se p ha un link di assoc. "dirige" allora p.is_direttore = TRUE

    # **DA IMPLEMENTARE IN CLASS VEICOLO [V.Persona.se_proprietario_allora_cliente]
    # Per ogni p:Persona, deve essere:
    # 	- se p ha un link di assoc. "proprietario" allora p.is_cliente = TRUE

    # IMPLEMENTATO [V.Persona.complete]
    # Per ogni p:Persona, deve essere:
    # 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE

    def cf(self) -> CodiceFiscale:
        return self.__cf

    def nome(self) -> str:
        return self.__nome

    def cognome(self) -> str:
        return self.__cognome

    def indirizzo(self) -> Indirizzo:
        return self.__indirizzo

    def citta(self) -> Citta:
        return self.__citta

    def telefono(self) -> Telefono:
        return self.__telefono

    def lavora(self) -> frozenset[lavora]:
        return frozenset(self.__lavora)

    # ...

    def nascita(self) -> datetime.date:
        return self.__nascita

    def is_cliente(self) -> bool:
        return self.__is_cliente

    def is_direttore(self) -> bool:
        return self.__is_direttore

    def is_dipendente(self) -> bool:
        return self.__is_dipendente

    def dirige(self) -> frozenset[dirige]:
        return frozenset(self.__dirige)

    def __set_cf(self, v: CodiceFiscale):
        if v is None:
            raise ValueError(f"v non può essere None")
        if not isinstance(v, CodiceFiscale):
            raise ValueError(f"v deve essere una istanza di CodiceFiscale")
        self.__cf = v

    def __set_nome(self, v: CodiceFiscale):
        if v is None:
            raise ValueError(f"v non può essere None")
        if not isinstance(v, str):
            raise ValueError(f"v deve essere una istanza di str")
        self.__nome = v

    def __set_cognome(self, v: CodiceFiscale):
        if v is None:
            raise ValueError(f"v non può essere None")
        if not isinstance(v, str):
            raise ValueError(f"v deve essere una istanza di str")
        self.__cognome = v

    def set_indirizzo(self, i: Indirizzo, c: Citta):
        if i is None:
            raise ValueError(f"i non può essere None")
        if not isinstance(i, Indirizzo):
            raise ValueError(f"i deve essere una istanza di Indirizzo")
        if c is None:
            raise ValueError(f"c non può essere None")
        if not isinstance(c, Citta):
            raise ValueError(f"c deve essere una istanza di Citta")
        self.__indirizzo = i
        self.__citta = c

    def set_telefono(self, v: Telefono):
        if v is None:
            raise ValueError(f"v non può essere None")
        if not isinstance(v, Telefono):
            raise ValueError(f"v deve essere una istanza di Telefono")
        self.__telefono = v

    def set_direttore(self, v: datetime.date):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, datetime.date):
            raise ValueError(f"v deve essere una istanza di date")

        self.__is_direttore = True
        self.__nascita = v

        # [V.Persona.nascita_sse_direttore]
        # Per ogni p:Persona, deve essere:
        # 	- p.nascita ha un valore se e solo se p.is_direttore = TRUE
        assert (self.__nascita is not None) == (self.__is_direttore == True)

    def reset_direttore(self):
        if not self.is_dipendente() and not self.is_cliente():
            raise ValueError(
                f"Non puoi eliminare il ruolo di direttore della persona {self}"
            )

        self.__is_direttore = False
        self.__nascita = None

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        # 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.is_cliente() or self.is_direttore() or self.is_dipendente()

        # [V.Persona.nascita_sse_direttore]
        # Per ogni p:Persona, deve essere:
        # 	- p.nascita ha un valore se e solo se p.is_direttore = TRUE
        assert (self.nascita() is not None) == (self.is_direttore())

    def set_is_cliente(self, v: bool):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, bool):
            raise ValueError("v deve essere bool")

        if not v and not self.is_direttore() and not self.is_dipendente():
            raise ValueError(f"Non puoi togliere la caratteristica di cliente a {self}")

        self.__is_cliente = v

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        # 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.is_cliente() or self.is_direttore() or self.is_dipendente()

    def set_is_dipendente(self, v: bool):
        if v is None:
            raise ValueError("v non può essere None")
        if not isinstance(v, bool):
            raise ValueError("v deve essere bool")
        if v == False and len(self.__lavora) > 0:
            raise ValueError("ho dei link lavora")

        if not v and not self.is_direttore() and not self.is_cliente():
            raise ValueError(
                f"Non puoi togliere la caratteristica di dipendente a {self}"
            )

        self.__is_dipendente = v

        # [V.Persona.complete]
        # Per ogni p:Persona, deve essere:
        # 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
        assert self.is_cliente() or self.is_direttore() or self.is_dipendente()

    def _add_lavora(self, l: lavora):
        if not self.is_dipendente():
            raise ValueError("self non è un dipendente")
        if l is None:
            raise ValueError("l non può essere None")
        if not isinstance(l, lavora):
            raise ValueError("l deve essere di class lavora")
        if l.persona() != self:
            raise ValueError("l non mi appartiene")
        if not l.is_valid():
            raise ValueError("l non è valido!")

        self.__lavora.add(l)

    def _remove_lavora(self, l: lavora):
        if not self.is_dipendente():
            raise ValueError("self non è un dipendente")
        if l is None:
            raise ValueError("l non può essere None")
        if l.persona() != self:
            raise ValueError("l non mi appartiene")

        self.__lavora.remove(l)

    def _add_dirige(self, l: dirige):
        if not l or not isinstance(l, dirige):
            raise ValueError(f"l è illegale: {l}")
        self.__dirige.add(l)

    def remove_dirige(self, l: dirige):
        if not l or not isinstance(l, dirige):
            raise ValueError(f"l è illegale: {l}")
        self.__dirige.remove(l)

    def __init__(
        self,
        cf: CodiceFiscale,
        nome: str,
        cognome: str,
        indirizzo: Indirizzo,
        c: Citta,
        tel: Telefono,
        nascita: datetime.date | None,
        is_cliente: bool,
        is_dipendente: bool,
        is_direttore: bool,
    ):
        # [V.Persona.nascita_sse_direttore] p.nascita ha un valore se e solo se p.is_direttore = TRUE
        if (nascita is not None) != (is_direttore):
            raise ValueError(
                f"I valori degli argomenti 'nascita' e 'is_direttore' non sono coerenti tra di loro"
            )

        self.__lavora = set()
        self.__dirige = set()

        self.__set_cf(cf)
        self.__set_nome(nome)
        self.__set_cognome(cognome)
        self.set_indirizzo(indirizzo, c)
        self.set_telefono(tel)
        self.__is_cliente = is_cliente
        self.__is_dipendente = is_dipendente
        if is_direttore:
            self.set_direttore(nascita)
        else:
            self.reset_direttore()

    def __str__(self) -> str:
        return f"{self.cognome()}, {self.nome()} ({self.cf()})"

    def text(
        self,
    ) -> str:  # Decidiamo di usare questa funzione quando vorremo restituire una stringa con tutti i dettagli
        result = (
            f"{self.cognome()}, {self.nome()} ({self.cf()}):"
            + f"\n - indirizzo: {self.indirizzo()}, {self.citta()}"
            + f"\n - telefono: {self.telefono()}"
            + f"\n - È cliente? {self.is_cliente()}"
            + f"\n - È dipendente? {self.is_dipendente()}"
        )

        if self.is_dipendente():
            result += f", di {len(self.lavora())} officine"
            officine_as_list = list()
            for l in self.lavora():
                officine_as_list.append(l.officina().nome())

            if len(officine_as_list) > 0:
                result += ": " + ",".join(officine_as_list)

        result += f"\n - È direttore? {self.is_direttore()}"
        if self.is_direttore():
            result += f", di {len(self.dirige())} officine"
            officine_as_list = list()
            for l in self.dirige():
                officine_as_list.append(l.officina().nome())

            if len(officine_as_list) > 0:
                result += ": " + ",".join(officine_as_list)

        return result


# INFO: ASSOCIATIONS

class dirige:
    __officina: Officina
    __persona: Persona

    __is_valid: bool

    def officina(self) -> Officina:
        if not self.__is_valid:
            raise Exception("Attenzione: il link non è più valido")
        return self.__officina

    def persona(self) -> Persona:
        if not self.__is_valid:
            raise Exception("Attenzione: il link non è più valido")
        return self.__persona

    def __hash__(self) -> int:
        if not self.__is_valid:
            raise Exception("Attenzione: il link non è più valido")
        return hash((self.officina(), self.persona()))

    def __eq__(self, o: Any) -> bool:
        if not self.__is_valid:
            raise Exception("Attenzione: il link non è più valido")
        if not o or not isinstance(o, type(self)):
            return False

        return self.officina() == o.officina() and self.persona() == o.persona()

    def __init__(self, o: Officina, p: Persona):
        if not o or not isinstance(o, Officina):
            raise ValueError(f"o è illegale: {o}")
        if not p or not isinstance(p, Persona):
            raise ValueError(f"p è illegale: {p}")

        self.__officina = o
        self.__persona = p
        self.__is_valid = False  # v. commento qui sotto.

    @classmethod
    def _create(cls, o: Officina, p: Persona):
        l = cls(o, p)
        l.__is_valid = True
        old_l = o.dirige()
        if old_l:
            dirige.remove(old_l)

        o._add_dirige(l)
        p._add_dirige(l)

    # Nota. Il metodo __init__() assegna self.__is_valid = False,
    # mentre _create() lo riassegna a True.
    # Difatti, non vogliamo che i clienti delle nostre classi creino istanze
    # di citta_off invocando in autonomia il costruttore,
    # ma vogliamo costringerli ad usare questa factory.
    # Con questo stratagemma, se un programmatore creasse un link citta_off invocando
    # direttamente il costruttore (che invoca __init__() e basta), allora si ritroverebbe
    # con un link non valido!

    @classmethod
    def _remove(cls, l: dirige):
        l.officina()._remove_dirige()
        l.persona()._remove_dirige(l)
        l.__officina = None
        l.__persona = None
        l.__is_valid = False


class citta_off:
    __citta: Citta  # <<imm>>
    __officina: Officina  # <<imm>>

    __is_valid: bool

    def citta(self) -> Citta:
        if not self.is_valid():
            raise Exception("Il link è invalido")
        return self.__citta

    def officina(self) -> Officina:
        if not self.is_valid():
            raise Exception("Il link è invalido")
        return self.__officina

    def is_valid(self) -> bool:
        return self.__is_valid

    def __set_citta(self, c: Citta):
        if not c or not isinstance(c, Citta):
            raise TypeError(f"c illegale: {c}")
        self.__citta = c

    def __set_officina(self, o: Officina):
        if not o or not isinstance(o, Officina):
            raise TypeError(f"o illegale: {o}")
        self.__officina = o

    def __hash__(self) -> int:
        if not self.is_valid():
            raise Exception("Il link è invalido")
        return hash((self.citta(), self.officina()))

    def __eq__(self, o: Any) -> bool:
        if not self.is_valid():
            raise Exception("Il link è invalido")
        if not o or not isinstance(o, type(self)):
            return False
        return self.citta() == o.citta() and self.officina() == o.officina()

    def __init__(self, c: Citta, o: Officina):
        self.__set_citta(c)
        self.__set_officina(o)
        self.__is_valid = False

    @classmethod
    def _create(cls, c: Citta, o: Officina):
        l = cls(c, o)
        l.__is_valid = True
        c._add_citta_off(l)
        o._add_citta_off(l)

    @classmethod
    def _remove(cls, l: citta_off):
        if not l or not isinstance(l, cls):
            raise TypeError(f"l illegale: {l}")
        l.citta()._remove_citta_off(l)
        l.officina()._remove_citta_off(l)
        self.__is_valid = False

    def __str__(self) -> str:
        return f"(citta={self.citta()}, officina={self.officina()}):citta_off"


class lavora:
    __officina: Officina  # <<imm>> per costruzione
    __persona: Persona  # <<imm>  per costruzione
    __assunzione: datetime.date  # <<imm>>

    __is_valid: bool

    @classmethod
    def create(cls, p: Persona, o: Officina, a: datetime.date):
        l = cls(p, o, a)
        l.__is_valid = True
        p._add_lavora(l)
        o._add_lavora(l)

    @classmethod
    def remove(cls, l: lavora):
        l.persona()._remove_lavora(l)
        l.officina()._remove_lavora(l)
        l.__is_valid = False

    def is_valid(self) -> bool:
        return self.__is_valid

    def officina(self) -> Officina:
        if not self.is_valid():
            raise Exception("arg, stai usando un link invalido")

        return self.__officina

    def persona(self) -> Persona:
        if not self.is_valid():
            raise Exception("arg, stai usando un link invalido")

        return self.__persona

    def assunzione(self) -> datetime.date:

        if not self.is_valid():
            raise Exception("arg, stai usando un link invalido")

        return self.__assunzione

    def anni_servizio(self) -> Int_GE0:
        if not self.is_valid():
            raise Exception("arg, stai usando un link invalido")

        pass  # per esercizio
        # return "data corrente" - self.assunzione()

    def __set_officina(self, o: Officina):
        if o is None or not isinstance(o, Officina):
            raise ValueError(f"o deve essere una Officina")
        self.__officina = o

    def __set_persona(self, p: Persona):
        if p is None or not isinstance(p, Persona):
            raise ValueError(f"p deve essere una Persona")
        if not p.is_dipendente():
            raise ValueError(f"p deve essere un dipendente")
        self.__persona = p

    def __set_assunzione(self, d: datetime.date):
        if d is None or not isinstance(d, datetime.date):
            raise ValueError(f"d deve essere una datetime.date")
        self.__assunzione = d

    def __init__(self, p: Persona, o: Officina, assunzione: datetime.date):
        self.__set_persona(p)
        self.__set_officina(o)
        self.__set_assunzione(assunzione)
        self.__is_valid = False

    def __hash__(self) -> int:
        return hash((self.officina(), self.persona()))

    def __eq__(self, other: Any) -> bool:
        if other is None or not isinstance(other, type(self)):
            return False
        return self.officina() == other.officina() and self.persona() == other.persona()

# INFO: MAIN

def main():
    cf = CodiceFiscale("   slvfvn00r29h501j     ")
    print(f"cf è di tipo {type(cf)} ed ha valore '{cf}'")

    tel = Telefono("+39443 29385 323")
    print(f"tel è di tipo {type(tel)} ed ha valore '{tel}'")

    tar = Targa("aB   540 xd")
    print(f"tar è di tipo {type(tar)} ed ha valore '{tar}'")

    ind = Indirizzo("Via di casa mia", "28/bis", "00452")
    print(f"ind è di tipo {type(ind)} ed ha valore '{ind}'")

    italia = Nazione("Italia", "[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}")
    print(f"ita è di tipo {type(italia)} ed ha valore '{italia}'")

    roma = Citta("Roma", italia)
    milano = Citta("Milano", italia)

    alice = Persona(
        CodiceFiscale("bbbaaa55a34rrtgh"),
        "Alice",
        "Bianchi",
        Indirizzo("Via di casa di Alice", "28/bis", "00100"),
        roma,
        Telefono("+39263388463"),
        datetime.date.fromisoformat("2000-01-01"),
        False,  # is_cliente
        True,  # is_dipendente
        True,  # is_direttore
    )
    print(f"\nOggetto alice (class Persona):\n{alice.text()}\n\n")

    riparami = Officina(
        "riparaMI",
        Indirizzo("via Brembate", "15", "20135"),
        milano,
        Telefono("+39 02 87445912"),
        alice,
    )
    print(f"\nOggetto riparami (class Officina):\n{riparami.text()}\n\n")

    print(f"\nOra alice è:\n{alice.text()}\n\n")

    biagio = Persona(
        CodiceFiscale("cccbbb98d12edt4h"),
        "Biagio",
        "Corallo",
        Indirizzo("Via di casa di Biagio", "28/bis", "20100"),
        milano,
        Telefono("+39023094455"),
        None,  # data di nascita
        False,  # is_cliente
        True,  # is_dipendente
        False,  # is_direttore
    )
    lavora.create(biagio, riparami, datetime.date.fromisoformat("2015-04-01"))

    print(f"\nbiagio è:\n{biagio.text()}\n\n")
    print(f"\nAdesso riparami è:\n{riparami.text()}\n\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
