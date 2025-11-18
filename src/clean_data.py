import pandas as pd
from pathlib import Path
from src.record_lineage import log_lineage
from src.hashing import record_file_hash

RAW = Path(__file__).resolve().parents[1] / "data/raw/sample.csv"
OUT = Path(__file__).resolve().parents[1] / "data/cleaned/cleaned.csv"

def clean_data():
    df = pd.read_csv(RAW)
    df = df.drop_duplicates().dropna()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    digest = record_file_hash(str(OUT))
    log_lineage("clean_data", [str(RAW)], [str(OUT)], f"sha256={digest}")

if __name__ == "__main__":
    clean_data()
