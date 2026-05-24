"""One-off: split monolithic 2021 notebook into 5 module notebooks.

Strips outputs, rewrites Colab Drive paths to portable local paths, modernizes
deprecated pandas APIs. Run once at restructure; not needed afterwards.

Usage: python scripts/split_notebook.py
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Módulo 4, 5, 6 y 7 - Primeros pasos con Pandas.ipynb"
OUT = ROOT / "notebooks"
LEGACY = ROOT / "legacy"

# (start_cell, end_cell_exclusive, output_filename, title)
MODULES = [
    (2, 21, "01_python_basico.ipynb", "Módulo 1 — Fundamentos de Python"),
    (21, 212, "02_pandas.ipynb", "Módulo 2 — Procesamiento con Pandas"),
    (212, 287, "03_visualizacion.ipynb", "Módulo 3 — Visualización de datos"),
    (287, 336, "04_inferencia.ipynb", "Módulo 4 — Inferencia estadística"),
    (336, 338, "05_automatizacion.ipynb", "Módulo 5 — Automatización de procesos"),
]

# Cells fully replaced (Colab-specific setup) — keyed by 0-based cell index in source
REPLACE_CELLS: dict[int, str] = {
    40: (
        "# Setup de rutas — funciona en local y en Colab.\n"
        "from pathlib import Path\n"
        "import os, sys\n"
        "\n"
        "try:\n"
        "    from google.colab import drive  # type: ignore\n"
        "    drive.mount('/content/gdrive')\n"
        "    DATA_DIR = Path('/content/gdrive/MyDrive/Curso_pandas')\n"
        "except ImportError:\n"
        "    # Local: usar el directorio data/ del repo\n"
        "    DATA_DIR = Path.cwd().parent / 'data' if Path.cwd().name == 'notebooks' else Path.cwd() / 'data'\n"
        "\n"
        "DATA_DIR.mkdir(parents=True, exist_ok=True)\n"
        "print('DATA_DIR =', DATA_DIR)\n"
    ),
    45: "# DATA_DIR ya fue creado arriba — saltar chdir global.\nos.chdir(DATA_DIR)\n",
    46: "# Carpeta de trabajo ya existe (DATA_DIR). Esta celda se conserva como referencia.\n# (DATA_DIR / 'Curso_pandas').mkdir(exist_ok=True)\n",
    47: "# Ya estamos en DATA_DIR.\n",
    173: (
        "# Importando librerías y configurando rutas\n"
        "import pandas as pd\n"
        "import numpy as np\n"
        "import os\n"
        "from pathlib import Path\n"
        "\n"
        "try:\n"
        "    from google.colab import drive  # type: ignore\n"
        "    drive.mount('/content/gdrive')\n"
        "    DATA_DIR = Path('/content/gdrive/MyDrive/Curso_pandas')\n"
        "except ImportError:\n"
        "    DATA_DIR = Path.cwd().parent / 'data' if Path.cwd().name == 'notebooks' else Path.cwd() / 'data'\n"
    ),
    175: "os.chdir(DATA_DIR)\nos.getcwd()\n",
    214: (
        "# Setup módulo de visualización\n"
        "from pathlib import Path\n"
        "import os\n"
        "import pandas as pd\n"
        "import numpy as np\n"
        "import seaborn as sns\n"
        "import matplotlib.pyplot as plt\n"
        "\n"
        "try:\n"
        "    from google.colab import drive  # type: ignore\n"
        "    drive.mount('/content/gdrive')\n"
        "    DATA_DIR = Path('/content/gdrive/MyDrive/Curso_pandas')\n"
        "except ImportError:\n"
        "    DATA_DIR = Path.cwd().parent / 'data' if Path.cwd().name == 'notebooks' else Path.cwd() / 'data'\n"
    ),
    215: "os.chdir(DATA_DIR)\nos.getcwd()\n",
}

# Path string substitutions (apply to every code cell that isn't fully replaced)
PATH_SUBS = [
    ("/content/gdrive/MyDrive/Curso_pandas/", "str(DATA_DIR) + '/'"),  # rare
    ("'/content/gdrive/MyDrive/Curso_pandas/", "f'{DATA_DIR}/"),
    ('"/content/gdrive/MyDrive/Curso_pandas/', 'f"{DATA_DIR}/'),
    ("'/content/gdrive/MyDrive/Curso_pandas'", "str(DATA_DIR)"),
    ('"/content/gdrive/MyDrive/Curso_pandas"', "str(DATA_DIR)"),
    ("/content/gdrive/MyDrive", "str(DATA_DIR.parent)"),
]

# Deprecated API modernization (regex, replacement)
API_FIXES: list[tuple[re.Pattern, str]] = [
    # DataFrame.append → pd.concat
    (
        re.compile(r"(\w+)\.append\(\s*(\w+)\s*,\s*ignore_index\s*=\s*True\s*\)"),
        r"pd.concat([\1, \2], ignore_index=True)",
    ),
    # !unzip ... -d /content/gdrive/... → portable
    (
        re.compile(r"!unzip\s+-q\s+(\S+)\s+-d\s+/content/gdrive/MyDrive/Curso_pandas"),
        r"!unzip -q \1 -d {DATA_DIR}",
    ),
]


def transform_cell(idx: int, cell: dict) -> dict:
    """Return modified cell (stripped outputs, fixed paths/APIs)."""
    c = copy.deepcopy(cell)

    # Strip outputs + execution_count for code cells
    if c["cell_type"] == "code":
        c["outputs"] = []
        c["execution_count"] = None

    if idx in REPLACE_CELLS:
        c["source"] = REPLACE_CELLS[idx]
        return c

    if c["cell_type"] != "code":
        return c

    src = "".join(c["source"]) if isinstance(c["source"], list) else c["source"]

    for needle, repl in PATH_SUBS:
        src = src.replace(needle, repl)

    for pattern, repl in API_FIXES:
        src = pattern.sub(repl, src)

    c["source"] = src
    return c


def build_notebook(template: dict, cells: list[dict], title: str) -> dict:
    nb = copy.deepcopy(template)
    nb["cells"] = []
    # Insert header markdown cell
    nb["cells"].append(
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": (
                f"# {title}\n\n"
                "> Curso de Python para Análisis de Datos en Salud Pública — OPS/PAHO\n"
                "> Material 2021, actualizado 2026.\n"
                "> Licencia: código MIT, contenido CC-BY-SA 4.0.\n"
            ),
        }
    )
    nb["cells"].extend(cells)
    # Clean kernel metadata to keep file diff-friendly
    nb["metadata"] = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    }
    return nb


def main() -> None:
    nb = json.loads(SRC.read_text(encoding="utf-8"))
    template = {"cells": [], "metadata": {}, "nbformat": nb.get("nbformat", 4), "nbformat_minor": nb.get("nbformat_minor", 0)}

    OUT.mkdir(exist_ok=True)
    LEGACY.mkdir(exist_ok=True)

    # Preserve original
    legacy_path = LEGACY / "monolithic_2021_original.ipynb"
    legacy_path.write_text(SRC.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Preserved original → {legacy_path.relative_to(ROOT)}")

    for start, end, fname, title in MODULES:
        cells = [transform_cell(i, nb["cells"][i]) for i in range(start, end)]
        new_nb = build_notebook(template, cells, title)
        out_path = OUT / fname
        out_path.write_text(json.dumps(new_nb, ensure_ascii=False, indent=1), encoding="utf-8")
        sz_kb = out_path.stat().st_size / 1024
        print(f"  wrote {out_path.relative_to(ROOT)}  ({len(cells)} cells, {sz_kb:.0f} KB)")

    print("\nDone. Review notebooks/ and delete the source .ipynb when satisfied.")


if __name__ == "__main__":
    main()
