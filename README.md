# langraph_financial_agent

[![CI](https://github.com/bi0punk/langraph_financial_agent/actions/workflows/ci.yml/badge.svg)](https://github.com/bi0punk/langraph_financial_agent/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Financial data exploration and visualization tool. Performs EDA on bank account transaction data from CSV, generating spending pattern visualizations including bar charts, heatmaps, and trend lines.

## Tabla de contenidos

- [Características](#características)
- [Stack](#stack)
- [Estructura](#estructura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [CI](#ci)
- [Datos](#datos)
- [Limitaciones](#limitaciones)
- [Licencia](#licencia)

## Características

- EDA sobre cartola de movimientos bancarios (CSV).
- Visualizaciones: gráficos de barras, heatmaps, líneas de tendencia.
- Dos notebooks: `app.ipynb` (aplicación) y `EDA_cartola_desde_cero.ipynb` (walkthrough completo).

## Stack

- **Lenguaje**: Python 3.12+
- **Entorno**: Jupyter Notebook
- **Datos**: pandas, numpy
- **Visualización**: matplotlib
- **Calidad**: ruff (excluye `.ipynb`), pytest

## Estructura

```
langraph_financial_agent/
├── app.ipynb                          # Notebook aplicación
├── EDA_cartola_desde_cero.ipynb       # Walkthrough EDA
├── movimientos_cartola_*.csv          # Datos (NO commiteados, ver Datos)
├── requirements.txt
├── pyproject.toml                     # config pytest + ruff
├── tests/test_smoke.py
└── .github/workflows/ci.yml
```

## Requisitos

- Python 3.12+
- Jupyter

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
jupyter notebook app.ipynb
```

O abre `EDA_cartola_desde_cero.ipynb` para el walkthrough completo. Los notebooks esperan un CSV de movimientos en la raíz (ver [Datos](#datos)).

## Tests

```bash
pytest -q
```

Smoke tests (`tests/test_smoke.py`): validan estructura de ambos notebooks (JSON válido, celdas code+markdown), que el CSV de datos personales no esté commiteado y que las deps figuren en `requirements.txt`.

## CI

GitHub Actions (`.github/workflows/ci.yml`) sobre Python 3.12:

- `ruff check .` (excluye `.ipynb`)
- `pytest -q`

## Datos

El archivo `movimientos_cartola_2025-12_a_2026-01.csv` contiene **movimientos bancarios personales** y **no se commitea** (excluido vía `.gitignore` con `*.csv`). Coloca tu propio CSV con el esquema:

```csv
fecha,descripcion,canal,monto_clp,tipo,monto_abs_clp
2025-12-25,PAGO EJEMPLO,Débito nacional,-40520,cargo,40520
```

## Limitaciones

- Análisis batch en notebook; sin servicio/API.
- Los notebooks no se lintean para preservar outputs y flujo.

## Licencia

MIT — ver [LICENSE](LICENSE).
