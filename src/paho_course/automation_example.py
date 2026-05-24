"""Ejemplo de pipeline automatizado para el Módulo 5.

Descarga datos COVID-19 globales de la OMS, calcula un resumen por país y
guarda dos artefactos:
  - data/processed/covid_summary.csv  (resumen tabular)
  - data/processed/covid_summary.json (mismo resumen para APIs/dashboards)

Diseñado para correr sin intervención manual desde:
  - cron (Linux/macOS)
  - Task Scheduler (Windows)
  - GitHub Actions (ver .github/workflows/automation.yml)

Uso:
    python -m paho_course.automation_example
    python -m paho_course.automation_example --top 20
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import pandas as pd

WHO_URL = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = REPO_ROOT / "data"
OUT_DIR = REPO_ROOT / "data" / "processed"

logger = logging.getLogger("paho_course.automation")


def configure_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def download_who_data(dest: Path) -> Path:
    """Descarga el CSV global de COVID-19 de la OMS."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    logger.info("Descargando %s", WHO_URL)
    req = Request(WHO_URL, headers={"User-Agent": "paho-course-automation/1.0"})
    with urlopen(req, timeout=60) as resp, dest.open("wb") as f:
        f.write(resp.read())
    logger.info("Guardado: %s (%.1f KB)", dest, dest.stat().st_size / 1024)
    return dest


def summarize(csv_path: Path, top_n: int) -> pd.DataFrame:
    """Top-N países por casos acumulados, con fecha de corte."""
    logger.info("Procesando %s", csv_path)
    df = pd.read_csv(csv_path, parse_dates=["Date_reported"])

    latest = df["Date_reported"].max()
    snapshot = df[df["Date_reported"] == latest]

    summary = (
        snapshot.groupby("Country", as_index=False)
        .agg(
            cumulative_cases=("Cumulative_cases", "sum"),
            cumulative_deaths=("Cumulative_deaths", "sum"),
        )
        .sort_values("cumulative_cases", ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    summary.insert(0, "rank", summary.index + 1)
    summary["snapshot_date"] = latest.date().isoformat()
    return summary


def save_artifacts(summary: pd.DataFrame, out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "covid_summary.csv"
    json_path = out_dir / "covid_summary.json"

    summary.to_csv(csv_path, index=False)

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "snapshot_date": summary["snapshot_date"].iloc[0] if len(summary) else None,
        "rows": summary.drop(columns=["snapshot_date"]).to_dict(orient="records"),
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    logger.info("Artefactos: %s | %s", csv_path.name, json_path.name)
    return csv_path, json_path


def run(top_n: int = 10) -> int:
    raw_csv = download_who_data(RAW_DIR / "WHO-COVID-19-global-data.csv")
    summary = summarize(raw_csv, top_n)
    save_artifacts(summary, OUT_DIR)
    logger.info("Pipeline completado. Top %d países procesados.", len(summary))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--top", type=int, default=10, help="Cuántos países incluir en el resumen (default: 10)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Logging DEBUG")
    args = parser.parse_args()

    configure_logging(args.verbose)
    try:
        return run(top_n=args.top)
    except Exception:
        logger.exception("Pipeline falló")
        return 1


if __name__ == "__main__":
    sys.exit(main())
