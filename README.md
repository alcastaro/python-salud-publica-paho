# Curso de Python para Análisis de Datos en Salud Pública

> Material original dictado en octubre de 2022 para la **Organización Panamericana de la Salud (OPS/PAHO)**, actualizado a APIs modernas en 2026.

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-red?logo=youtube)](https://www.youtube.com/playlist?list=PL9aP5Ogcql5QxCRXeGOB0X8seldSoBQub)

🇪🇸 **Español** | [🇬🇧 English](README.en.md)

---

## Sobre el curso

Curso introductorio (~10 horas) que cubre desde fundamentos de Python hasta inferencia estadística y automatización, usando datos reales de egresos hospitalarios del Ecuador (2021) como caso práctico.

Diseñado para profesionales de salud pública, epidemiólogos y analistas de sistemas de información en salud.

📺 **Videos del curso:** [Lista de reproducción en YouTube](https://www.youtube.com/playlist?list=PL9aP5Ogcql5QxCRXeGOB0X8seldSoBQub)
El notebook original usado en los videos está en [`Módulo 4, 5, 6 y 7 - Primeros pasos con Pandas.ipynb`](Módulo%204%2C%205%2C%206%20y%207%20-%20Primeros%20pasos%20con%20Pandas.ipynb).

## Módulos

| # | Módulo | Notebook | Colab |
|---|--------|----------|-------|
| 1 | Fundamentos de Python | [`01_python_basico.ipynb`](notebooks/01_python_basico.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/01_python_basico.ipynb) |
| 2 | Procesamiento con Pandas | [`02_pandas.ipynb`](notebooks/02_pandas.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/02_pandas.ipynb) |
| 3 | Visualización de datos | [`03_visualizacion.ipynb`](notebooks/03_visualizacion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/03_visualizacion.ipynb) |
| 4 | Inferencia estadística | [`04_inferencia.ipynb`](notebooks/04_inferencia.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/04_inferencia.ipynb) |
| 5 | Automatización de procesos | [`05_automatizacion.ipynb`](notebooks/05_automatizacion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/05_automatizacion.ipynb) |

## Requisitos

- Python ≥ 3.10
- ~500 MB de espacio para datasets

## Instalación

```bash
git clone https://github.com/alcastaro/python-salud-publica-paho.git
cd Python_course_PAHO

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Descargar datos de ejemplo (egresos hospitalarios Ecuador 2021)
python data/download.py

jupyter lab
```

O usar **Google Colab** con los badges de la tabla arriba (no requiere instalación local).

## Estructura del repo

```
.
├── notebooks/         Notebooks por módulo
├── data/              Datasets (no versionados; usar download.py)
│   └── download.py    Script de descarga
├── src/paho_course/   Funciones reutilizables y ejemplos automatización
├── docs/              Recursos pedagógicos
├── legacy/            Notebook original 2022 (preservado)
└── .github/workflows/ CI
```

## Datos

Egresos hospitalarios del Ecuador, 2021 — INEC (Instituto Nacional de Estadística y Censos). Datos abiertos.

Ver [`data/README.md`](data/README.md) para fuentes y licencia de los datos.

## Cómo citar

```bibtex
@misc{castillo2022pythoncoursepaho,
  author       = {Castillo Aroca, Alberto},
  title        = {Curso de Python para Análisis de Datos en Salud Pública (PAHO)},
  year         = {2022},
  howpublished = {\url{https://github.com/alcastaro/python-salud-publica-paho}},
  note         = {Actualizado 2026}
}
```

## Licencia

Código bajo **MIT**. Contenido pedagógico (markdown, ejercicios, diapositivas) bajo **CC-BY-SA 4.0**. Ver [LICENSE](LICENSE).

## Contribuciones

PRs bienvenidos. Antes de abrir uno:
- Limpiar outputs de notebooks (`nbstripout *.ipynb`)
- Verificar que `python -m py_compile src/paho_course/*.py` pasa
- Mantener notebooks en español (es el idioma del curso original)

## Autor

**Alberto Castillo Aroca** — [@alcastaro](https://github.com/alcastaro)

Material desarrollado originalmente para la cooperación técnica OPS/PAHO en sistemas de información en salud, octubre 2022.
