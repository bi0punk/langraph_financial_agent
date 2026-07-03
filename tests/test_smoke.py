"""Smoke tests para los notebooks financieros (validan estructura sin ejecutar)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS = [
    REPO_ROOT / "app.ipynb",
    REPO_ROOT / "EDA_cartola_desde_cero.ipynb",
]


def test_notebooks_are_valid_json():
    for nb in NOTEBOOKS:
        assert nb.exists(), f"Notebook no encontrado: {nb.name}"
        data = json.loads(nb.read_text(encoding="utf-8"))
        assert "cells" in data, f"{nb.name} sin clave 'cells'"
        assert len(data["cells"]) > 0, f"{nb.name} sin celdas"


def test_notebooks_have_code_cells():
    for nb in NOTEBOOKS:
        data = json.loads(nb.read_text(encoding="utf-8"))
        kinds = {cell.get("cell_type") for cell in data["cells"]}
        assert "code" in kinds, f"{nb.name} sin celdas de código"


def test_personal_csv_not_tracked():
    """El CSV de movimientos bancarios (datos personales) no debe commitearse."""
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout
    csv_tracked = [line for line in tracked.splitlines() if line.endswith(".csv")]
    assert not csv_tracked, f"CSVs commiteados (datos personales): {csv_tracked}"


def test_requirements_listed():
    req = (REPO_ROOT / "requirements.txt").read_text()
    for dep in ("pandas", "numpy", "matplotlib"):
        assert dep in req, f"{dep} no está en requirements.txt"
