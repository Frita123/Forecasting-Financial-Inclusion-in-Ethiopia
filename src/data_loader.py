import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file with basic error handling.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {path}")
    except pd.errors.ParserError:
        raise ValueError(f"❌ Parsing error while reading: {path}")


def load_enriched_dataset(path: str) -> pd.DataFrame:
    """
    Load the enriched Ethiopia financial inclusion dataset.
    """
    df = load_csv(path)
    required_cols = {"record_type", "observation_date", "indicator_code"}
    missing = required_cols - set(df.columns)

    if missing:
        raise ValueError(f"❌ Missing required columns: {missing}")

    return df
