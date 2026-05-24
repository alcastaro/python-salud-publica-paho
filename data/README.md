# Datasets

Los datasets no están versionados en git. Usar el script de descarga:

```bash
python data/download.py
```

## Fuentes

### 1. Egresos hospitalarios Ecuador 2021

- **Fuente:** [INEC — Instituto Nacional de Estadística y Censos del Ecuador](https://www.ecuadorencifras.gob.ec/camas-y-egresos-hospitalarios/)
- **URL directa:** [Datos_abiertos_camas_egresos_hospitalarios_2021.zip](https://www.ecuadorencifras.gob.ec/documentos/web-inec/Estadisticas_Sociales/Camas_Egresos_Hospitalarios/Cam_Egre_Hos_2021/Datos_abiertos_camas_egresos_hospitalarios_2021.zip)
- **Archivo clave:** `2. Datos_abiertos_EEH_2021/egresos_hospitalarios_2021.csv` (separador `;`)
- **Licencia:** Datos abiertos del Gobierno del Ecuador. Uso libre con atribución a INEC.

### 2. COVID-19 global data — WHO

- **Fuente:** [WHO COVID-19 Dashboard](https://covid19.who.int/)
- **URL directa:** [WHO-COVID-19-global-data.csv](https://covid19.who.int/WHO-COVID-19-global-data.csv)
- **Nota:** Snapshot diario; los valores cambian con cada descarga. Para reproducibilidad estricta, cachear localmente.

## Estructura esperada tras `python data/download.py`

```
data/
├── README.md                                                  (este archivo)
├── download.py                                                (script)
├── Datos_abiertos_camas_egresos_hospitalarios_2021.zip
├── WHO-COVID-19-global-data.csv
└── 2. Datos_abiertos_EEH_2021/
    ├── egresos_hospitalarios_2021.csv
    ├── camas_hospitalarias_2021.csv
    └── ... (diccionarios de variables, etc.)
```

## Sub-muestra para tests rápidos

Si necesita una muestra pequeña sin descargar los ~30 MB completos:

```python
import pandas as pd
df = pd.read_csv('data/2. Datos_abiertos_EEH_2021/egresos_hospitalarios_2021.csv', sep=';', nrows=1000)
df.to_csv('data/sample/egresos_sample.csv', sep=';', index=False)
```
