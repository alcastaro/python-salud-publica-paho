# Python Course for Public Health Data Analysis

> Material originally taught in 2021 for the **Pan American Health Organization (PAHO/WHO)**, updated to modern APIs in 2026.

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC--BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-red?logo=youtube)](https://www.youtube.com/playlist?list=PL9aP5Ogcql5QxCRXeGOB0X8seldSoBQub)

[🇪🇸 Español](README.md) | 🇬🇧 **English**

---

## About

~10-hour introductory course covering Python fundamentals through statistical inference and automation, using real Ecuador 2021 hospital-discharge data as the working case.

Designed for public-health professionals, epidemiologists, and health-information-system analysts. Course content is in Spanish (audience: Latin America); code and APIs are language-neutral.

📺 **Video lectures (Spanish):** [YouTube playlist](https://www.youtube.com/playlist?list=PL9aP5Ogcql5QxCRXeGOB0X8seldSoBQub)
The original notebook used in the videos is at [`Módulo 4, 5, 6 y 7 - Primeros pasos con Pandas.ipynb`](Módulo%204%2C%205%2C%206%20y%207%20-%20Primeros%20pasos%20con%20Pandas.ipynb).

## Modules

| # | Module | Notebook | Colab |
|---|--------|----------|-------|
| 1 | Python fundamentals | [`01_python_basico.ipynb`](notebooks/01_python_basico.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/01_python_basico.ipynb) |
| 2 | Pandas data processing | [`02_pandas.ipynb`](notebooks/02_pandas.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/02_pandas.ipynb) |
| 3 | Data visualization | [`03_visualizacion.ipynb`](notebooks/03_visualizacion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/03_visualizacion.ipynb) |
| 4 | Statistical inference | [`04_inferencia.ipynb`](notebooks/04_inferencia.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/04_inferencia.ipynb) |
| 5 | Process automation | [`05_automatizacion.ipynb`](notebooks/05_automatizacion.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alcastaro/python-salud-publica-paho/blob/main/notebooks/05_automatizacion.ipynb) |

## Quick start

```bash
git clone https://github.com/alcastaro/python-salud-publica-paho.git
cd Python_course_PAHO

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python data/download.py
jupyter lab
```

Or open any notebook in **Google Colab** via the badges above.

## License

Code under **MIT**. Course content under **CC-BY-SA 4.0**. See [LICENSE](LICENSE).

## Author

**Alberto Castillo Aroca** — [@alcastaro](https://github.com/alcastaro)
