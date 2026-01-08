import pandas as pd

def suggest_decision(df: pd.DataFrame):
    # Simple business logic (transparent & explainable)
    avg_profit = (df['revenue'] - df['cost']).mean()

    if avg_profit > 40000:
        decision = "Increase price slightly"
    else:
        decision = "Focus on cost reduction"

    return decision, avg_profit
