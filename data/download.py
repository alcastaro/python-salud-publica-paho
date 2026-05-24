"""Descarga los datasets de ejemplo del curso.

Datasets:
  1. Egresos hospitalarios 2021 — INEC Ecuador (ZIP, ~30 MB)
  2. COVID-19 global data — WHO (CSV, ~5 MB)

Uso:
    python data/download.py             # descarga todo en data/
    python data/download.py --only inec # solo Ecuador
    python data/download.py --only who  # solo WHO
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen

DATA_DIR = Path(__file__).resolve().parent

SOURCES = {
    "inec": {
        "url": "https://www.ecuadorencifras.gob.ec/documentos/web-inec/Estadisticas_Sociales/Camas_Egresos_Hospitalarios/Cam_Egre_Hos_2021/Datos_abiertos_camas_egresos_hospitalarios_2021.zip",
        "filename": "Datos_abiertos_camas_egresos_hospitalarios_2021.zip",
        "unzip": True,
        "description": "INEC Ecuador — Camas y egresos hospitalarios 2021",
    },
    "who": {
        "url": "https://covid19.who.int/WHO-COVID-19-global-data.csv",
        "filename": "WHO-COVID-19-global-data.csv",
        "unzip": False,
        "description": "WHO — COVID-19 global data (snapshot del día de la descarga)",
    },
}


def _download(url: str, dest: Path) -> None:
    print(f"  → {url}")
    req = Request(url, headers={"User-Agent": "python-course-paho-downloader/1.0"})
    with urlopen(req) as resp, dest.open("wb") as f:
        total = 0
        while chunk := resp.read(1 << 16):
            f.write(chunk)
            total += len(chunk)
        print(f"  ✓ {dest.name} ({total / 1024 / 1024:.1f} MB)")


def _unzip(zip_path: Path, target_dir: Path) -> None:
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(target_dir)
    print(f"  ✓ descomprimido en {target_dir}")


def fetch(key: str) -> None:
    spec = SOURCES[key]
    dest = DATA_DIR / spec["filename"]
    print(f"\n[{key}] {spec['description']}")

    if dest.exists():
        print(f"  ✓ ya existe: {dest.name} (saltando descarga)")
    else:
        _download(spec["url"], dest)

    if spec["unzip"]:
        _unzip(dest, DATA_DIR)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", choices=list(SOURCES), help="Descargar solo este dataset")
    args = parser.parse_args()

    keys = [args.only] if args.only else list(SOURCES)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for k in keys:
        try:
            fetch(k)
        except Exception as e:
            print(f"  ✗ error descargando {k}: {e}", file=sys.stderr)
            return 1

    print("\nListo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
