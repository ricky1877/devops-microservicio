from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenido al DevOps Microservice API"
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "UP"
    }


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1