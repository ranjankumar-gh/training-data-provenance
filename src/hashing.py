import hashlib, json
from pathlib import Path

HASHES_FILE = Path(__file__).resolve().parents[1] / "hashes.json"

def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def record_file_hash(file_path, output_json=None):
    output_json = output_json or str(HASHES_FILE)
    hashes = {}

    if Path(output_json).exists():
        hashes = json.load(open(output_json))

    digest = sha256sum(file_path)
    hashes[file_path] = {"sha256": digest}

    json.dump(hashes, open(output_json, "w"), indent=2)
    return digest
