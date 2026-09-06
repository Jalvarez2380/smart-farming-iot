from datetime import datetime
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Smart Farming IoT API", version="1.0.0")
mediciones: list[dict] = []


class MedicionIoT(BaseModel):
    sensor_id: str = Field(min_length=1)
    parcela: str = Field(min_length=1)
    tipo: Literal["humedad", "temperatura", "radiacion"]
    valor: float
    fecha: datetime


def validar_medicion(medicion: MedicionIoT) -> bool:
    """Valida los rangos físicos aceptados para cada sensor."""
    rangos = {
        "humedad": (0.0, 100.0),
        "temperatura": (-20.0, 80.0),
        "radiacion": (0.0, 2000.0),
    }
    minimo, maximo = rangos[medicion.tipo]
    return minimo <= medicion.valor <= maximo


@app.get("/salud")
def comprobar_salud() -> dict:
    return {"estado": "activo"}


@app.post("/mediciones", status_code=201)
def registrar_medicion(medicion: MedicionIoT) -> dict:
    if not validar_medicion(medicion):
        raise HTTPException(status_code=422, detail="Valor fuera del rango permitido")
    registro = medicion.model_dump(mode="json")
    mediciones.append(registro)
    return {"mensaje": "Medición almacenada", "medicion": registro}


@app.get("/mediciones")
def consultar_mediciones() -> list[dict]:
    return mediciones
