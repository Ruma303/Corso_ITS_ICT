# test/api/conftest.py
import pytest
from fastapi.testclient import TestClient

from python_code.api.app import create_app
from python_code.api.dependencies import get_utente_repository
from python_code.repositories.in_memory import InMemoryUtenteRepository


@pytest.fixture
def client():
    app = create_app()
    repo = InMemoryUtenteRepository()
    app.dependency_overrides[get_utente_repository] = lambda: repo
    with TestClient(app) as c:
        yield c