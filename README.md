# Training Data Provenance Repo

Run with:
```
pip install -r requirements.txt
dvc init
python src/clean_data.py
python src/process_data.py
```
# Source Code
## `src/clean_data.py`

`src/clean_data.py` does a simple ETL cleanup and adds provenance:

- Imports Pandas plus two internal helpers: `log_lineage` records provenance info, `record_file_hash` computes a SHA-256 hash of a file for integrity tracking.
- Defines constants for the raw input CSV (`data/raw/sample.csv`) and the cleaned output CSV (`data/cleaned/cleaned.csv`) using `Path`.
- `clean_data()` reads the raw CSV, removes duplicate rows and any rows with missing values, ensures the output folder exists, and writes the cleaned data back to CSV without the index column.
- After writing, it hashes the cleaned file and records that hash along with the transformation metadata (`clean_data`, input path, output path) via `log_lineage`.
- Running the script (`python src/clean_data.py`) simply executes `clean_data()`.