from flask import Flask, render_template, request
import pandas as pd
import os

from src.data_loader import load_data
from src.data_inspector import inspect_data
from src.decision_engine import suggest_decision
from src.simulator import simulate_price_change
from src.explainer import explain

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


app = Flask(__name__, template_folder=TEMPLATE_DIR)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    issues = []

    if request.method == "POST":
        file = request.files.get("dataset")

        if file:
            df = pd.read_csv(file)

            issues = inspect_data(df)

            df = df.fillna(df.mean(numeric_only=True))

            decision, base_profit = suggest_decision(df)
            simulated_profit = simulate_price_change(df, 0.05)

            result = explain(decision, base_profit, simulated_profit)

    return render_template("index.html", issues=issues, result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
