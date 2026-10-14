import pytest

from python_code.models.categoria import Categoria

@pytest.fixture(autouse=True)
def pulisci_registro():
    """Il registro è stato di classe: va azzerato prima di ogni test."""
    Categoria._clear_registry()
    yield
    Categoria._clear_registry()


# ---------- Creazione ----------


def test_creazione_valida():
    c = Categoria("Libri")
    assert c.get_nome() == "Libri"


def test_nome_viene_normalizzato():
    c = Categoria("   Categoria di test    ")
    assert c.get_nome() == "Categoria di test"


@pytest.mark.parametrize("nome", ["", "   ", "\t\n"])
def test_nome_vuoto_rifiutato(nome):
    with pytest.raises(ValueError):
        Categoria(nome)


@pytest.mark.parametrize("nome", [None, 42, 3.14, ["Libri"]])
def test_tipo_errato_rifiutato(nome):
    with pytest.raises(TypeError):
        Categoria(nome)


def test_nome_duplicato_rifiutato():
    Categoria("Libri")
    with pytest.raises(KeyError):
        Categoria("Libri")


def test_duplicato_dopo_strip_rifiutato():
    Categoria("Libri")
    with pytest.raises(KeyError):
        Categoria("  Libri  ")


def test_creazione_fallita_non_inquina_registro():
    with pytest.raises(ValueError):
        Categoria("")
    assert Categoria.get_by_nome("") is None


# ---------- Modifica ----------


def test_rinomina():
    c = Categoria("Libri")
    c.set_nome("Fumetti")
    assert c.get_nome() == "Fumetti"


def test_rinomina_aggiorna_indice():
    c = Categoria("Libri")
    c.set_nome("Fumetti")
    assert Categoria.get_by_nome("Libri") is None
    assert Categoria.get_by_nome("Fumetti") is c


def test_vecchio_nome_riutilizzabile_dopo_rinomina():
    c = Categoria("Libri")
    c.set_nome("Fumetti")
    c2 = Categoria("Libri")  # non deve sollevare
    assert c2 is not c


def test_rinomina_con_nome_gia_usato_da_altra():
    Categoria("Libri")
    c2 = Categoria("Fumetti")
    with pytest.raises(KeyError):
        c2.set_nome("Libri")
    # lo stato non deve essere cambiato
    assert c2.get_nome() == "Fumetti"
    assert Categoria.get_by_nome("Fumetti") is c2


def test_rinomina_con_stesso_nome_e_noop():
    c = Categoria("Libri")
    c.set_nome("Libri")
    assert c.get_nome() == "Libri"
    assert Categoria.get_by_nome("Libri") is c


# ---------- Uguaglianza e hash ----------


def test_uguaglianza_per_nome():
    c = Categoria("Libri")
    assert c == c
    assert c != Categoria("Fumetti")


def test_non_uguale_a_altri_tipi():
    c = Categoria("Libri")
    assert c != "Libri"
    assert c != None  # noqa: E711


def test_hash_coerente_con_nome():
    c = Categoria("Libri")
    assert hash(c) == hash("Libri")
