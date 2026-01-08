import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print("Data loaded successfully.\n")
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")
