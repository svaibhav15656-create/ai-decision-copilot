from data_loader import load_data
from data_inspector import inspect_data
from decision_engine import suggest_decision
from simulator import simulate_price_change
from explainer import explain

DATA_PATH = "../data/sample_sales.csv"

def main():
    df = load_data(DATA_PATH)

    print("Inspecting data...")
    issues = inspect_data(df)
    for issue in issues:
        print("⚠️", issue)

    df = df.fillna(df.mean(numeric_only=True))

    decision, base_profit = suggest_decision(df)

    simulated_profit = simulate_price_change(df, 0.05)

    report = explain(decision, base_profit, simulated_profit)
    print(report)

if __name__ == "__main__":
    main()
