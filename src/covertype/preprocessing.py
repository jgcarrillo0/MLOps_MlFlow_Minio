import pandas as pd


def validate_dataframe(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("The input dataset is empty.")

    if df.columns.duplicated().any():
        duplicated = df.columns[df.columns.duplicated()].tolist()
        raise ValueError(f"Duplicated columns found: {duplicated}")


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    validate_dataframe(df)

    processed = df.copy()

    return processed
