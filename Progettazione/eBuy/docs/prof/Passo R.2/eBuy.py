from enum import StrEnum, auto
from datetime import timedelta

class Float_GEZ(float):
	def __new__(cls, v:float):
		if not v or not isinstance(v, float):
			raise ValueError(f"{v} è di class {type(v)}, e non un float")
		if v < 0:
			raise ValueError(f"{v} non è un Float_GEZ")
		return super().__new__(cls, v)

class Float_GZ(Float_GEZ):
	def __new__(cls, v:float):
		if not v or not isinstance(v, float):
			raise ValueError(f"{v} è di class {type(v)}, e non un float")
		if v <= 0:
			raise ValueError(f"{v} non è un Float_GZ")
		return super().__new__(cls, v)

class TimeDelta_GZ(timedelta):
	def __new__(cls, v:timedelta):
		if not v or not isinstance(v, timedelta):
			raise ValueError(f"{v} è di class {type(v)}, e non un timedelta")
		if v <= timedelta(milliseconds=0):
			raise ValueError("timedelta can't be <= 0")
		return super().__new__(cls, 
			days=v.days,
			seconds=v.seconds, 
			microseconds=v.microseconds, 
			milliseconds=v.milliseconds, 
			minutes=v.minutes, 
			hours=v.hours, 
			weeks=v.weeks
		)

class StatoPost(StrEnum):
	nuovo = auto()
	usato = auto()

class StringaLecita(str):
	def __new__(cls, v:str):
		if not v or not isinstance(v, str):
			raise ValueError(f"{v} è di class {type(v)}, e non una str")
		
		v = v.strip()
		if len(v) == 0:
			raise ValueError(f"'{v}' non è una StringaLecita")
		return super().__new__(cls, v)



class Categoria:
	__nome:str # {id}

	# attributo di classe
	__all_objects:dict[str,Self] = dict() # nome -> Categoria

	@classmethod
	def get_object(cls, nome:str)->Categoria|None:
		return cls.__all_objects.get(nome, None)

	def nome(self)->str:
		return self.__nome

	def set_nome(self, v:str)->None:
		if v is None or type(v) != str:
			raise ValueError(f"Errore: il nome deve essere una stringa. Adesso è: '{v}'")
		v.strip()
		if v == "":
			raise ValueError(f"Errore: il nome non deve essere la stringa composta solo di spazi. Adesso è: '{v}'")
		
		if self.__nome is not None: # si sta modificando una categoria esistente
			del type(self).__all_objects[self.__nome]
		self.__nome = v
		type(self).__all_objects[self.__nome] = self

	def __init__(self, n:str):		
		self.__nome = None
		self.set_nome(n)
		
	def __str__(self)->str:
		return self.nome()

	def __repr__(self)->str:
		return f"Categoria({self.nome()})"


class pubblica:
	__utente:Utente
	__post:Post	

	__is_valid:bool

	# getter
	# setter privati

	def __init__(self, u:Utente, p:Post):
		self.set_utente(u)
		self.set_post(p)
		self.__is_valid = True

	def utente(self):
		if not self.__is_valid:
			raise ...

	def __eq__(self, other):
		if other is None or type(other) != type(self):
			return False

		return ( (self.utente(), self.post()) == (other.utente(), other.post()) ):
		
		# L'istruzione precedente è equivalente a:
		#
		# if self.utente() != other.utente():
		# 	return False
		# if self.post() != other.post():
		# 	return False
		# return True

	def __hash__(self)->int:
		return hash( (self.utente(), self.post()) )

	@classmethod
	def _create(cls, u:Utente, p:Post):
		link = cls(u,p)
		u._add_pubblica(link)
		p._set_pubblica(link)


	def _remove(cls, l:pubblica)
		l.utente()._remove_pubblica(l)
		l.post()._remove_pubblica(l)
		l.__is_valid == False

class Post(ABC):
	__istante_pubbl: datetime.datetime # <<imm>>
	__descrizione: str 
	__prezzo: Float_GEZ # <<imm>>
	__stato: StatoPost # <<imm>>

	# Aggregazioni
	__post_cat: Categoria # <<imm>>
	__valuta: Valuta # <<imm>
	__metodi_pagam: set[MetodoPagamento]

	# Associazione "pubblica" a resp. doppia
	__pubblica:pubblica # 1..1

	# getter
	def istante_pubbl(self)->datetime:
		return self.__istante_pubbl
	def descrizione(self)->str:
		return self.__descrizione
	def prezzo(self)->Float_GEZ:
		return self.__prezzo
	def stato(self)->StatoPost:
		return self.__stato
	def categoria(self)->Categoria:
		return self.__post_cat
	def valuta(self)->Valuta:
		return self.__valuta
	def metodi_pagam(self)->set[MetodoPagam]
		return frozenset(self.__metodi_pagam)

	# setter
	def __set_istante_pubbl(self, v:datetime):
		if not v or not isinstance(v, datetime):
			raise ValueError("not a datetime")
		self.__istante_pubbl = v

	def set_descrizione(self, v:str):
		if not v or not isinstance(v, str):
			raise ValueError("not a str")
		self.__descrizione = v 

	def __set_prezzo(self, v:Float_GEZ):
		if not v or not isinstance(v, Float_GEZ):
			raise ValueError("not a float >= 0")
		self.__prezzo = v

	def __set_stato(self, v :StatoPost):
		if not v or not isinstance(v, StatoPost):
			raise ValueError("not a StatoPost")
		self.__stato = v

	def __set_categoria(self, v:Categoria):
		if not v or not isinstance(v, Categoria):
			raise ValueError("not a Categoria")
		self.__post_cat = v	

	def __set_valuta(self, v:Valuta):
		if not v or not isinstance(v, Valuta):
			raise ValueError("not a Valuta")
		self.__valuta = v	

	def add_metodo_pagam(self, v:MetodoPagamento):
		if not v or not isinstance(v, MetodoPagamento):
			raise ValueError("not a MetodoPagamento")
		self.__metodi_pagam.add(v)

	def del_metodo_pagam(self, v:MetodoPagamento):
		if not v or not isinstance(v, MetodoPagamento):
			raise ValueError("not a MetodoPagamento")
		if len(self.__metodi_pagam) <= 1:
			raise Exception("this ha solo un metodo di pagamento, non puoi eliminarlo")
		self.__metodi_pagam.remove(v)

	@abstractmethod
	def __init__(self, i:datetime.datetime, descr:str, prezzo:Float_GEZ, stato:StatoPost, cat:Categoria, val:Valuta, m:MetodoPagamento, u:Utente):
		self.__istante_pubbl = None
		self.__descrizione = None
		self.__prezzo = None
		self.__stato = None
		self.__post_cat = None
		self.__valuta = None
		self.__metodo_pagam = set()

		self.__set_istante_pubbl(i)
		self.set_descrizione(descr)
		self.__set_prezzo(prezzo)
		self.__set_stato(stato)
		self.__set_categoria(cat)
		self.__set_valuta(val)
		self.add_metodo_pagam(m)
		pubblica._create(u, self)


	def add_link_pubblica(self, l:pubblica):
		self.__pubblica = l

	def del_link_pubblica(self, l:pubblica):
		if self.__pubblica == l:
			self.__pubblica = None
		else:
			raise Error("This is not my link")


class CompraloSubito(Post):
	def __init__(self, i:datetime.datetime, descr:str, prezzo:Float_GEZ, stato:StatoPost, cat:Categoria, val:Valuta):
		super().__init__(i, descr, prezzo, stato, cat, val)

class pubblica:
	__utente:Utente # <<imm>>
	__post:Post # <<imm>>
	__is_valid:bool

	def utente(self)->Utente:
		if not self.__is_valid:
			raise Exception("The link is invalid")
		return self.__utente
	def post(self)->Post:
		if not self.__is_valid:
			raise Exception("The link is invalid")
		return self.__post

	def is_valid(self)->bool:
		return self.__is_valid

	def __set_utente(self, v:Utente):
		if not v or not isinstance(v, Utente):
			raise ValueError("not a Utente")
		self.__utente = v
	def __set_post(self, v:Post):
		if not v or not isinstance(v, Post):
			raise ValueError("not a Post")
		self.__post = v

	def __eq__(self, other:pubblica)->bool:
		if not self.__is_valid:
			raise Exception("The link is invalid")

		if not other or not isinstance(other, pubblica) or hash(self) != hash(other):
			return False
		
		return (self.utente(), self.post()) == (other.utente(), other.post())

	def __hash__(self)->int:
		if not self.__is_valid:
			raise Exception("The link is invalid")
		return hash( (self.utente(), self.post()) )

	def __init__(self, u:Utente, p:Post):
		self.__set_utente(u)
		self.__set_post(p)
		self.__is_valid = True

	@classmethod
	def _create(cls, u:Utente, p:Post):
		l = pubblica(u,p)
		u._add_link_pubblica(l)
		p._add_link_pubblica(l)

	@classmethod
	def __remove(cls, l:pubblica)
		if not l:
			raise ValueError("l è none")
		l.utente()._del_link_pubblica(l)
		l.post()._def_link_pubblica(l)
		l.__is_valid = False

class Utente:
	__nomeutente:str
	__registrazione:datetime

	# Associazione "pubblica" a resp. doppia
	__pubblica:set[pubblica] # 0..*

	#__all_obj:set[Self]=set()

	def nomeutente(self):
		return self.__nomeutente
	def registrazione(self):
		return self.__registrazione
	def pubblica(self)->frozenset[pubblica]:
		return frozenset(self.pubblica)

	
	#def all_obj(self):
	#	return frozenset(self.__all_obj)

	def __set_nomeutente(self, v:str):
		if not v or not isinstance(v, str):
			raise ValueError("not a str")
		for c in self.__all_obj:
			if c.nomeutente() == v and c is not self:
				raise ValueError("Already exists")
		self.__nomeutente = v

	def __set_registrazione(self, v:datetime):
		if not v or not isinstance(v, datetime):
			raise ValueError("not a datetime")
		self.__registrazione = v

	def __init__(self, nomeutente:str):
		self.__pubblica = set()
		self.__set_nomeutente(nomeutente)
		self.__set_registrazione(datetime.now())

		#type(self).__all_obj.add(self)

	def __str__(self):
		return f"Utente: \nnome utente: {self.nomeutente()}\nregistered on: {self.registrazione()}"

	def _add_link_pubblica(self, l:pubblica):
		if not l or l.utente() is not self or not l.is_valid():
			raise Exception("Wrong link!")
		self.__pubblica.add(l)

	def _del_link_pubblica(self, l:pubblica):
		if not l or l.utente() is not self or not l.is_valid():
			raise Exception("Wrong link!")
		self.__pubblica.remove(l)

	def post_di_categoria(self, c:Categoria)->set[Post]:
		result = set()

		for l in self.pubblica():
			p = l.post()
			if p.categoria() == c:
				result.add(p)

		return result

def main():



if __name__ == '__main__':
	main()
	sys.exit(0)