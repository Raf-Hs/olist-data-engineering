from pathlib import Path
import json
from typing import Any

def read_json_file(file_path: str | Path) -> Any:
    """
    Read a JSON file and return its contents as a DataFrame.

    Args:
        file_path: Path to the JSON file.

    Returns:
        A Python object (dict, list, str, int, float, bool or None).
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")

    if not path.is_file():
        raise ValueError(f"The provided path is not a file: {path}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    return data
