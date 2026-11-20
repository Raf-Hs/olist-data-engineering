from pathlib import Path

import pandas as pd

def read_csv_file(file_path: str | Path) -> pd.DataFrame:
    """
    Read a CSV file and return its contents as a DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        A pandas DataFrame containing the CSV data.
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    if not path.is_file():
        raise ValueError(f"The provided path is not a file: {path}")

    return pd.read_csv(path)

