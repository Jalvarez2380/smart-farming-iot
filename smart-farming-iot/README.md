# Smart Farming IoT

Módulo de recepción, validación y almacenamiento de datos IoT para el Sistema Inteligente de Monitoreo Agrícola mediante IoT para Smart Farming.

## Trazabilidad

- Epic de Jira: SF-12.
- Historia de usuario: SF-13.
- Tarea: SF-15, implementar recepción de datos IoT.
- RF-05: validar y procesar mediante una API REST los datos enviados por el gateway.
- RF-06: almacenar el histórico por fecha, sensor y parcela.

## Stack tecnológico

- Python 3.12.
- FastAPI para la API REST.
- Pydantic para validación.
- pytest para automatización de pruebas.
- GitHub Actions para integración continua.

## Estructura

```text
src/main.py                 API y reglas de validación
tests/test_mediciones.py    pruebas automatizadas
.github/workflows/ci.yml    pipeline de CI
requirements.txt            dependencias
```

## Ejecución local

```bash
python -m venv .venv
pip install -r requirements.txt
uvicorn src.main:app --reload
```

La documentación interactiva queda disponible en `http://127.0.0.1:8000/docs`.

## Pruebas

```bash
pytest -v
```

El caso crítico `test_registra_medicion_iot_valida` comprueba de punta a punta que una lectura válida recibida desde el gateway sea aceptada por la API y almacenada con sensor, parcela y fecha. El pipeline ejecuta las pruebas en cada `push` y `pull_request`.

## Flujo de ramas

Se propone `main` como rama estable, `develop` para integración y ramas `feature/*` para funcionalidades. Los cambios se revisan mediante pull request antes de integrarse.
