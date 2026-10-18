
"""Business simulation engine for AgentSphere AI."""

from agents import (
    FinanceAgent,
    DeveloperAgent,
    MarketingAgent,
    SalesAgent,
    CEOAgent,
)

VALID_EVENTS = {
    "normal",
    "budget_cut",
    "demand_surge",
    "server_outage",
    "competitor",
}


def run_simulation(event):
    # 1. Validate the selected event.
    if event not in VALID_EVENTS:
        event = "normal"

    # 2. Set the company's starting values.
    company = {
        "budget": 100000.0,
        "revenue": 50000.0,
        "expenses": 30000.0,
        "productivity": 80,
        "demand": 60,
    }

    # 3. Create the department agents.
    agents = [
        FinanceAgent(),
        DeveloperAgent(),
        MarketingAgent(),
        SalesAgent(),
    ]

    # 4. Collect recommendations.
    recommendations = [
        agent.analyze(company.copy(), event)
        for agent in agents
    ]

    # 5. Ask the CEO to choose a strategy.
    strategy = CEOAgent().decide(event, recommendations)

    # 6. Apply the selected event's effects.
    if event == "budget_cut":
        company["budget"] *= 0.80

    elif event == "demand_surge":
        company["revenue"] *= 1.20

    elif event == "server_outage":
        company["revenue"] *= 0.80
        company["productivity"] -= 10

    elif event == "competitor":
        company["revenue"] *= 0.90
        company["demand"] -= 10

    # 7. Apply department recommendations.
    for item in recommendations:
        company["expenses"] += item["expense_change"]
        company["demand"] += item["demand_change"]
        company["productivity"] += item["productivity_change"]

    # 8. Keep metrics within reasonable limits.
    company["expenses"] = max(0, company["expenses"])
    company["demand"] = max(0, min(100, company["demand"]))
    company["productivity"] = max(
        0, min(100, company["productivity"])
    )

    # 9. Calculate profit and the illustrative budget.
    company["profit"] = company["revenue"] - company["expenses"]
    company["budget"] += company["profit"]

    # 10. Return results to Flask.
    return {
        "event": event,
        "company": company,
        "recommendations": recommendations,
        "strategy": strategy,
    }
