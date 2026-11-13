import json
from pathlib import Path


DATA_DIRECTORY = Path(__file__).resolve().parent / "data"


class JsonStorageError(Exception):
    pass


def append_json_record(filename, record):
    path = DATA_DIRECTORY / filename

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            records = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            records = []

        if not isinstance(records, list):
            raise JsonStorageError(f"{path} must contain a JSON array")

        records.append(record)
        path.write_text(
            json.dumps(records, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8"
        )
    except (OSError, json.JSONDecodeError) as error:
        raise JsonStorageError(f"Could not update {path}") from error
