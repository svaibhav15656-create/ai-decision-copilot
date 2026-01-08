import pandas as pd

def inspect_data(df: pd.DataFrame):
    issues = []

    # Missing values
    missing = df.isnull().sum()
    for col, count in missing.items():
        if count > 0:
            issues.append(f"Column '{col}' has {count} missing values.")

    # Data types
    for col in df.columns:
        if df[col].dtype == 'object':
            issues.append(f"Column '{col}' might need cleaning (string type).")

    return issues
