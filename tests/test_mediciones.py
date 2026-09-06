from fastapi.testclient import TestClient

from src.main import app, mediciones


client = TestClient(app)


def setup_function() -> None:
    mediciones.clear()


def test_registra_medicion_iot_valida() -> None:
    """CP-01 crítico: valida y almacena una lectura correcta del gateway."""
    entrada = {
        "sensor_id": "HUM-001",
        "parcela": "P-01",
        "tipo": "humedad",
        "valor": 45.5,
        "fecha": "2026-09-06T14:30:00",
    }

    respuesta = client.post("/mediciones", json=entrada)

    assert respuesta.status_code == 201
    assert respuesta.json()["mensaje"] == "Medición almacenada"
    assert len(mediciones) == 1
    assert mediciones[0]["sensor_id"] == "HUM-001"


def test_rechaza_humedad_fuera_de_rango() -> None:
    entrada = {
        "sensor_id": "HUM-002",
        "parcela": "P-02",
        "tipo": "humedad",
        "valor": 140,
        "fecha": "2026-09-06T14:35:00",
    }

    respuesta = client.post("/mediciones", json=entrada)

    assert respuesta.status_code == 422
    assert respuesta.json()["detail"] == "Valor fuera del rango permitido"
    assert mediciones == []
