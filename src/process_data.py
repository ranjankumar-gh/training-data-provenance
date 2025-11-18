import pandas as pd
from pathlib import Path
from src.record_lineage import log_lineage
from src.hashing import record_file_hash

INP = Path(__file__).resolve().parents[1] / "data/cleaned/cleaned.csv"
OUT = Path(__file__).resolve().parents[1] / "data/processed/processed.csv"

def process_data():
    df = pd.read_csv(INP)
    if "text" in df.columns:
        df["text_length"] = df["text"].str.len()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    digest = record_file_hash(str(OUT))
    log_lineage("process_data", [str(INP)], [str(OUT)], f"sha256={digest}")

if __name__ == "__main__":
    process_data()
