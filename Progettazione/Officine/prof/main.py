import sys
import re
import datetime


class CodiceFiscale(str):
	def __new__(cls, v:str):
		if v is None:
			raise ValueError("Un codice fiscale non può essere None")
		v = v.strip().upper()

		if not re.fullmatch('[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z0-9]{4}[A-Z]', v):
			raise ValueError(f"La stringa '{v}' non è un codice fiscale sintatticamente legale")

		return super().__new__(cls, v)


class Int_GE0(int):
	def __new__(cls, v:int):
		if v is None:
			raise ValueError("Un Int_GE0 non può essere None")

		if not isinstance(v, int):
			raise ValueError(f"'{v}' non è un int")

		if v < 0:
			raise ValueError(f"'{v}' non è >= 0")

		return super().__new__(cls, v)


class Telefono(str):
	def __new__(cls, v:str):
		if v is None:
			raise ValueError("Un numero di telefono non può essere None")
		v = v.replace(" ", "")

		if not re.fullmatch('\\+[0-9 ]{0,15}', v):
			raise ValueError(f"La stringa '{v}' non è un numero di telefono sintatticamente legale")

		return super().__new__(cls, v)


class Targa(str):
	def __new__(cls, v:str):
		if v is None:
			raise ValueError("Un numero di targa non può essere None")
		v = v.upper().replace(" ", "")

		if not re.fullmatch('[A-Z]{2}[0-9]{3}[A-Z]{2}', v):
			raise ValueError(f"La stringa '{v}' non è un numero di targa sintatticamente legale")

		return super().__new__(cls, v)


class Indirizzo:
	__via: str
	__civico: str
	__cap: str

	def __init__(self, v:str, civ:str, cap:str):
		if v is None:
			raise ValueError("La via non può essere None")
		if civ is None:
			raise ValueError("Il civico non può essere None")
		if cap is None:
			raise ValueError("Il cap non può essere None")
		if not re.fullmatch('[0-9]+(/[a-zA-Z]+)?', civ):
			raise ValueError(f"Il valore '{civ}' non è un numero civico legale")
		if not re.fullmatch('[0-9]{5}', cap):
			raise ValueError(f"Il valore '{cap}' non è un numero CAP legale")

		self.__via = v
		self.__civico = civ
		self.__cap = cap


	def __hash__(self)->int:
		return hash( (self.via(), self.civico(), self.cap()) )

	def __eq__(self, o:Any)->bool:
		if o is None or type(o) != type(self) or hash(self) != hash(o):
			return False
		return 	self.civico() == o.civico() and \
				self.cap() == o.cap() and \
				self.via() == o.via()


	def get_via(self)->str:
		return self.__via
	def get_civico(self)->str:
		return self.__civico
	def get_cap(self)->str:
		return self.__cap

	def __str__(self)->str:
		return f"{self.get_via()} {self.get_civico()}, {self.get_cap()}"


class Nazione:
	__nome:str # <<imm>> {id}
	__regex_targa: set[str] # [1..*] 

	__objects_by_name:dict[str, Self] = dict()

	@classmethod
	def all_objects(cls)->set[Self]:
		return set(cls.__objects_by_name.values())

	def nome(self)->str:
		return self.__nome

	def regex_targa(self)->frozenset[str]:
		return frozenset(self.__regex_targa)

	def __set_nome(self, n:str):
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

	def add_regex_targa(self, re:str):
		if re is None or len(re) == 0:
			raise ValueError(f"regex_targa non può avere elementi None o vuoti")
		if not isinstance(re, str):
			raise ValueError(f"regex_targa deve avere elementi di tipo str")

		self.__regex_targa.add(re)

	def remove_regex_targa(self, re:str):
		if len(self.__regex_targa) == 1: # implementa [1..*]
			raise ValueError(f"L'oggetto {self} ha un solo valore per regex_targa")
		self.__regex_targa.remove(re)

	def __str__(self)->str:
		return f"{self.nome()}"

	def __init__(self, nome:str, re:str):
		self.__nome = None
		self.__regex_targa = set()

		self.add_regex_targa(re)		
		self.__set_nome(nome)
	


class Officina:
	__nome:str # <<imm>>
	__indirizzo:Indirizzo
	__telefono:Telefono
	__dirige:Persona

	__lavora:set[lavora]

	def nome(self)->str:
		return self.__nome

	def indirizzo(self)->Indirizzo:
		return self.__indirizzo

	def telefono(self)->Telefono:
		return self.__telefono

	def dirige(self)->Persona:
		return self.__dirige

	def lavora(self)->frozenset[lavora]:
		return frozenset(self.__lavora)

	def __set_nome(self, v:str):
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, str):
			raise ValueError("v deve essere una str")
		self.__nome = v

	def set_indirizzo(self, v:Indirizzo):
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, Indirizzo):
			raise ValueError("v deve essere un Indirizzo")
		self.__indirizzo = v

	def set_telefono(self, v:Telefono):
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, Telefono):
			raise ValueError("v deve essere un Telefono")

		self.__telefono = v

	def set_dirige(self, v:Persona):
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, Persona):
			raise ValueError("v deve essere un Persona")
		if not v.is_direttore():
			raise ValueError("v deve essere un direttore")

		self.__dirige = v

		# [V.Persona.se_dirige_allora_direttore]
		# 	- se p ha un link di assoc. "dirige" allora p.is_direttore = TRUE
		assert v.is_direttore()

	def _add_lavora(self, l:lavora):
		if l is None:
			raise ValueError("l non può essere None")
		if not isinstance(l, lavora):
			raise ValueError("l deve essere di class lavora")
		if not l.is_valid():
			raise ValueError("l non è valido!")
		if l.officina() != self:
			raise ValueError("l non mi appartiene")

		self.__lavora.add(l)



	def _remove_lavora(self, l:lavora):
		if not self.is_dipendente():
			raise ValueError("self non è un dipendente")
		if l is None:
			raise ValueError("l non può essere None")
		if l.officina() != self:
			raise ValueError("l non mi appartiene")

		self.__lavora.remove(l)
	
	def __init__(self, nome:str, indirizzo:Indirizzo, telefono:Telefono, dirige:Persona):
		self.__set_nome(nome)
		self.set_indirizzo(indirizzo)
		self.set_telefono(telefono)
		self.set_dirige(dirige)
		self.__lavora = set()


class lavora:
	__officina:Officina # <<imm>> per costruzione
	__persona:Persona # <<imm>  per costruzione
	__assunzione:datetime.date # <<imm>>

	__is_valid:bool

	@classmethod
	def create(cls, p:Persona, o:Officina, a:datetime.date):
		l = cls(p, o, a)
		p._add_lavora(l)
		o._add_lavora(l)

	@classmethod
	def remove(cls, l:lavora ):
		l.persona()._remove_lavora(l)
		l.officina()._remove_lavora(l)
		l.__is_valid = False

	def is_valid(self)->bool:
		return self.__is_valid

	def officina(self)->Officina:
		if not self.is_valid():
			raise Exception("arg, stai usando un link invalido")

		return self.__officina
	def persona(self)->Persona:
		if not self.is_valid():
			raise Exception("arg, stai usando un link invalido")

		return self.__persona
	def assunzione(self)->datetime.date:

		if not self.is_valid():
			raise Exception("arg, stai usando un link invalido")

		return self.__assunzione
	def anni_servizio(self)->Int_GE0:
		if not self.is_valid():
			raise Exception("arg, stai usando un link invalido")

		pass # per esercizio
		#return "data corrente" - self.assunzione()

	def __set_officina(self, o:Officina):
		if o is None or not isinstance(o, Officina):
			raise ValueError(f"o deve essere una Officina")
		self.__officina = o

	def __set_persona(self, p:Persona):
		if p is None or not isinstance(p, Persona):
			raise ValueError(f"p deve essere una Persona")
		if not p.is_dipendente():
			raise ValueError(f"p deve essere un dipendente")
		self.__persona = p
	def __set_assunzione(self, d:datetime.date):
		if d is None or not isinstance(d, datetime.date):
			raise ValueError(f"d deve essere una datetime.date")
		self.__assunzione = d

	def __init__(self, p:Persona, o:Officina, assunzione:datetime.date):
		self.__set_persona(p)
		self.__set_officina(o)
		self.__set_assunzione(assunzione)
		self.__is_valid = True


	def __hash__(self)->int:
		return hash(self.officina(), self.persona())

	def __eq__(self, other:Any)->bool:
		if other is None or not isinstance(other, type(self)):
			return False
		return self.officina() == other.officina() and self.persona() == other.persona()

class Persona:
	__cf:CodiceFiscale # <<imm>> {id}
	__nome:str # <<imm>>
	__cognome:str # <<imm>>
	__indirizzo:Indirizzo
	__citta:Citta
	__tel:Telefono
	__nascita: datetime.date|None # <<imm>> <<poss noto alla nascita>>
	__is_cliente:bool
	__is_dipendente:bool
	__is_direttore:bool

	__lavora:set[lavora] # 0..*

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


	def cf(self)->CodiceFiscale:
		return self.__cf
	def nome(self)->str:
		return self.__nome
	def cognome(self)->str:
		return self.__cognome
	def indirizzo(self)->Indirizzo:
		return self.__indirizzo
	def citta(self)->Citta:
		return self.__citta
	def lavora(self)->frozenset[lavora]:
		return frozenset(self.__lavora)

	#...

	def nascita(self)->datetime.date:
		return self.__nascita  ???
	def is_cliente(self)->bool:
		return self.__is_cliente
	def is_direttore(self)->bool:
		return self.__is_direttore
	
	# ...

	def __set_cf(v:CodiceFiscale):
		if v is None:
			raise ValueError(f"v non può essere None")
		if not isinstance(v, CodiceFiscale):
			raise ValueError(f"v deve essere una istanza di CodiceFiscale")
		self.__cf = v

	def __set_nome(v:CodiceFiscale):
		if v is None:
			raise ValueError(f"v non può essere None")
		if not isinstance(v, str):
			raise ValueError(f"v deve essere una istanza di str")
		self.__nome = v

	def __set_cognome(v:CodiceFiscale):
		if v is None:
			raise ValueError(f"v non può essere None")
		if not isinstance(v, str):
			raise ValueError(f"v deve essere una istanza di str")
		self.__cognome = v

	def set_indirizzo(self, i:Indirizzo, c:Citta):
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

	def set_direttore(self, v:datetime.date):	
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, datetime.date):
			raise ValueError(f"v deve essere una istanza di date")
		
		self.__is_direttore = True
		self.__nascita = v

		# [V.Persona.nascita_sse_direttore]
		# Per ogni p:Persona, deve essere:
		# 	- p.nascita ha un valore se e solo se p.is_direttore = TRUE
		assert (self.__nascita is not None) == (self.is_direttore == True)

	def reset_direttore(self):
		if not self.is_dipendente() and not self.is_cliente():
			raise ValueError(f"Non puoi eliminare il ruolo di direttore della persona {self}")

		self.__is_direttore = False
		self.__nascita = None


		# [V.Persona.complete]
		# Per ogni p:Persona, deve essere:
		# 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
		assert (self.is_cliente() or self.is_direttore() or self.is_dipendente())

		# [V.Persona.nascita_sse_direttore]
		# Per ogni p:Persona, deve essere:
		# 	- p.nascita ha un valore se e solo se p.is_direttore = TRUE
		assert (self.nascita() is not None) == (self.is_direttore())


	def set_is_cliente(self, v:bool):
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
		assert (self.is_cliente() or self.is_direttore() or self.is_dipendente())	

	def set_dipendente(self, v:bool):
		if v is None:
			raise ValueError("v non può essere None")
		if not isinstance(v, bool):
			raise ValueError("v deve essere bool")
		if v == False and len(self.__lavora) > 0:
			raise ValueError("ho dei link lavora")

		if not v and not self.is_direttore() and not self.is_cliente():
			raise ValueError(f"Non puoi togliere la caratteristica di dipendente a {self}")

		self.__is_dipendente = v

		# [V.Persona.complete]
		# Per ogni p:Persona, deve essere:
		# 	p.is_cliente = TRUE or p.is_direttore = TRUE or p.is_dipendente = TRUE
		assert (self.is_cliente() or self.is_direttore() or self.is_dipendente())

	def _add_lavora(self, l:lavora):
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


	def _remove_lavora(self, l:lavora):
		if not self.is_dipendente():
			raise ValueError("self non è un dipendente")
		if l is None:
			raise ValueError("l non può essere None")
		if l.persona() != self:
			raise ValueError("l non mi appartiene")

		self.__lavora.remove(l)

	def __init__(self, cf:CodiceFiscale, nome:str, cognome:str, indirizzo:Indirizzo, c:Citta, tel:Telefono, nascita:datetime.date|None, is_cliente:bool, is_dipendente:bool, is_direttore:bool):

		# [V.Persona.nascita_sse_direttore] p.nascita ha un valore se e solo se p.is_direttore = TRUE
		if (nascita is not None) != (is_direttore):
			raise ValueError(f"I valori degli argomenti 'nascita' e 'is_direttore' non sono coerenti tra di loro")

		self.__set_cf(cf)
		self.__set_nome(nome)
		self.__set_cognome(cognome)
		self.set_indirizzo(indirizzo, c)
		self.set_telefono(tel)
		
		self.__lavora = set()


def main():
	# c = CodiceFiscale('   slvfvn00r29h501j     ')
	# print(f"c è di tipo {type(c)} ed ha valore '{c}'")

	# tel = Telefono('+39443 29385 323')
	# print(f"tel è di tipo {type(tel)} ed ha valore '{tel}'")

	# tar = Targa('aB   540 xd')
	# print(f"tar è di tipo {type(tar)} ed ha valore '{tar}'")

	#ind = Indirizzo("Via di casa mia", "28/bis", "00452")
	#print(f"ind è di tipo {type(ind)} ed ha valore '{ind}'")

	naz = Nazione("Italia", "[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}")
	print(f"naz è: '{naz}'")

	o = Officina(...)
	p = Persona(...)
 	l1 = lavora(o, p, ...)
 	l2 = lavora(o, p, ...)


if __name__ == '__main__':
	sys.exit( main() )