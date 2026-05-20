# Data extraction logic

from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/raw/smart_manufacturing_data.csv")


def load_raw_data(file_path=RAW_DATA_PATH):
    """
    Load raw smart manufacturing sensor data from CSV.
    """
    df = pd.read_csv(file_path)
    return df