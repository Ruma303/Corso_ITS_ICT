from src.ebuy_py.datatypes.datatypes import Float_GEZ
from src.ebuy_py.models.categoria import Categoria
from src.ebuy_py.models.met_pag import MetodoPagamento
from src.ebuy_py.models.utente import Utente
from src.ebuy_py.models.valuta import Valuta
from src.ebuy_py.ui.utilities import input_validated


def ui_search_post_by_categoria():

    utente: Utente | str
    categoria: Categoria | str
    utente = input_validated("Inserisci il nome dell'utente : ", Utente)
    categoria = input_validated("Inserisci categoria: ", Categoria)
    Utente.search_by_categoria(utente, categoria)


def ui_search_post():

    categoria: Categoria | str
    inizio: Float_GEZ | str
    fine: Float_GEZ | str
    met_pag: MetodoPagamento | str
    valuta: Valuta | str

    categoria = input_validated("Inserisci categoria: ", Categoria)

    inizio = input_validated("Inserisci valore iniziale: ", Float_GEZ)

    fine = input_validated("Inserisci valore finale: ", Float_GEZ)

    met_pag = input_validated("Inserisci metodo di pagamento: ", MetodoPagamento)

    valuta = input_validated("Inserisci valuta: ", Valuta)

    Utente.search(categoria, inizio, fine, met_pag, valuta)
