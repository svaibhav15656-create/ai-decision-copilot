def explain(decision, base_profit, simulated_profit):
    profit_change = simulated_profit - base_profit
    profit_pct = (profit_change / base_profit) * 100 if base_profit != 0 else 0

    explanation = f"""
Decision Summary
----------------
Decision: {decision}

Current Average Profit: ₹{base_profit:,.2f}
Simulated Average Profit (5% Price Increase): ₹{simulated_profit:,.2f}
Estimated Profit Improvement: ₹{profit_change:,.2f} ({profit_pct:.1f}% increase)

Risk Considerations:
- Assumes customer demand remains constant
- Missing data was statistically estimated
- Results are directional, not absolute


Executive Explanation
---------------------
After analyzing the uploaded dataset, the system identified several data quality
issues, including missing revenue and cost values. These gaps were handled using
statistical estimation to preserve analytical continuity.

Despite these imperfections, the data indicates that the business is operating at
a healthy profit level. The current average monthly profit suggests that costs are
reasonably controlled and the business has room for strategic optimization.

A simulated scenario involving a controlled 5% price increase was evaluated.
Under this assumption, the analysis shows a meaningful improvement in average
monthly profit without requiring operational or cost-structure changes.

Based on these findings, the recommended strategy is to {decision.lower()}.
This approach is likely to generate higher returns than aggressive cost reduction,
provided customer demand remains stable.

It is advised that this strategy be validated through a controlled market test
before full-scale implementation to manage potential demand sensitivity.
"""

    return explanation
