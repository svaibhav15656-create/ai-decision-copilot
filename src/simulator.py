import pandas as pd

def simulate_price_change(df: pd.DataFrame, price_change_pct: float):
    simulated = df.copy()

    simulated['price'] = simulated['price'] * (1 + price_change_pct)
    simulated['revenue'] = simulated['price'] * simulated['units_sold']

    avg_profit = (simulated['revenue'] - simulated['cost']).mean()

    return avg_profit
