from src.ebuy_py.models.categoria import Categoria
from src.ebuy_py.models.post import DataValidator, Post, Valuta
from src.ebuy_py.models.utente import Utente


# Meglio non passare gli oggetti (es Utente e Categoria) ma gli indici
@staticmethod
def get_all_post_utente_by_categoria(utente: str, categoria: str):
    u = Utente.get_by_nome(utente)
    c = Categoria.get_by_nome(categoria)

    results = set()

    for link in Utente.get_all_pubblica_links():
        post = link._get_post()
        if post.get_categoria() == categoria:
            results.add(post)

    return results


def get_post_utente_by_categoria(): ...


def post_prezzo_alto(categoria: Categoria, valuta: Valuta):
    """Data una categoria, trovare i post con il prezzo più alto della categoria, data una valuta in input"""
    # Effettuare ricerca da categoria verso Post

    DataValidator._require_type(categoria, Categoria)
    DataValidator._require_type(valuta, Valuta)

    # Ritornare un dizionario categoria: set[Post]
    results: dict[Categoria, set[Post]] = dict()


    for k, c in Categoria.get_all_categories():
        # Filtro le categorie non None
        if c is not None:
          posts = set()  # Set di Post per singola categoria

          # Cerco i post con valuta più alta
          prezzo_max = None
          for i, post in enumerate(posts):
              if post.get_valuta() == valuta:
                if i == 0:
                  # Valorizzo la prima volta il prezzo e continua
                  prezzo_max = post.get_prezzo()
                  posts = {post} # Aggiungo il primo
                  continue
                # Ora possiamo confrontare

                # Se il prezzo del post > di quello attuale
                if post.get_prezzo() > prezzo_max:
                    posts = {post}  # Svota il vecchio e aggiungi i nuovi
                    prezzo_max = post.get_prezzo() # Riassegna il prezzo più alto

                # Se sono uguali, aggiungere al set della categoria
                elif post.get_prezzo() == prezzo_max:
                    posts.add(post)
                else:
                  continue

        results[c] = posts # qui c è str, non Categoria. Perché?

    return results
