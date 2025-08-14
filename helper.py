import pandas as pd
import requests
from difflib import SequenceMatcher
import io
import os

from io import BytesIO

def load_file(url):
    response = requests.get(url)
    response.raise_for_status()

    if url.endswith(".xlsx") or url.endswith(".xls"):
        return pd.read_excel(BytesIO(response.content), engine="openpyxl")
    elif url.endswith(".csv"):
        return pd.read_csv(BytesIO(response.content))
    else:
        raise ValueError("Unsupported file type")

def similarity_ratio(a, b):
    """Return similarity ratio as percentage with 2 decimal places."""
    return round(SequenceMatcher(None, a, b).ratio() * 100, 2)

def normalize_series(series):
    """Normalize series name for comparison."""
    if pd.isna(series):
        return ""
    return str(series).strip().upper()
