# Avance 2 U3: control de versiones e integración continua

## Repositorio

Sistema: Sistema Inteligente de Monitoreo Agrícola mediante IoT para Smart Farming.

Módulo: recepción, validación y almacenamiento de datos IoT.

Integrante: José Antonio Álvarez Lema.

Repositorio: https://github.com/Jalvarez2380/smart-farming-iot

## Estructura inicial

- `README.md`: descripción, trazabilidad, stack y forma de ejecución.
- `.gitignore`: exclusión de archivos temporales y entornos de Python.
- `src/`: código fuente de la API REST.
- `tests/`: pruebas automatizadas.
- `.github/workflows/ci.yml`: pipeline de integración continua.

## Flujo de ramas

Se aplica un flujo basado en GitHub Flow:

1. `main` conserva la versión estable.
2. Cada cambio se desarrolla en una rama `feature/*`.
3. Los cambios se guardan mediante commits con mensajes claros.
4. La rama se propone mediante un pull request.
5. GitHub Actions verifica el proyecto antes de fusionarlo.
6. El cambio aprobado se integra a `main`.

## Evidencia de este cambio

- Rama: `feature/documentar-flujo-git`.
- Commit: `Documentar flujo Git y CI del módulo`.
- Pull request: creado para integrar esta documentación a `main`.
- CI: configurado para ejecutarse en cada `push` y `pull_request`.

## Funcionamiento del CI

El workflow configura Python 3.12, instala las dependencias y ejecuta las pruebas de la carpeta `tests`. Un check verde indica que el módulo superó la verificación automática.
