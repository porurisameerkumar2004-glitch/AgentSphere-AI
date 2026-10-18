
"""Department agents for AgentSphere AI."""


class FinanceAgent:
    def analyze(self, company, event):
        if event == "budget_cut":
            return {
                "agent": "Finance",
                "decision": "Reduce unnecessary expenses by 10%.",
                "reason": "Protect the company's available cash.",
                "expense_change": -company["expenses"] * 0.10,
                "demand_change": 0,
                "productivity_change": 0,
            }

        return {
            "agent": "Finance",
            "decision": "Maintain financial controls.",
            "reason": "Monitor expenses and preserve cash.",
            "expense_change": 0,
            "demand_change": 0,
            "productivity_change": 0,
        }


class DeveloperAgent:
    def analyze(self, company, event):
        if event == "server_outage":
            return {
                "agent": "Developer",
                "decision": "Prioritize restoring the service.",
                "reason": "Service recovery is more urgent than new features.",
                "expense_change": 0,
                "demand_change": 0,
                "productivity_change": -5,
            }

        return {
            "agent": "Developer",
            "decision": "Continue planned development.",
            "reason": "Maintain progress on product improvements.",
            "expense_change": 0,
            "demand_change": 0,
            "productivity_change": 3,
        }


class MarketingAgent:
    def analyze(self, company, event):
        if event == "competitor":
            return {
                "agent": "Marketing",
                "decision": "Promote the product's unique advantages.",
                "reason": "Differentiate the company from its competitor.",
                "expense_change": 0,
                "demand_change": 5,
                "productivity_change": 0,
            }

        return {
            "agent": "Marketing",
            "decision": "Continue targeted marketing campaigns.",
            "reason": "Attract relevant customers efficiently.",
            "expense_change": 0,
            "demand_change": 3,
            "productivity_change": 0,
        }


class SalesAgent:
    def analyze(self, company, event):
        if event == "demand_surge":
            return {
                "agent": "Sales",
                "decision": "Prioritize new customer enquiries.",
                "reason": "Respond to increasing customer demand.",
                "expense_change": 0,
                "demand_change": 10,
                "productivity_change": 0,
            }

        return {
            "agent": "Sales",
            "decision": "Follow up with potential customers.",
            "reason": "Improve customer conversion and retention.",
            "expense_change": 0,
            "demand_change": 2,
            "productivity_change": 0,
        }


class CEOAgent:
    def decide(self, event, recommendations):
        strategies = {
            "normal": "Continue the existing business plan.",
            "budget_cut": "Protect cash and prioritize essential work.",
            "demand_surge": "Scale operations carefully.",
            "server_outage": "Restore the service before expanding.",
            "competitor": "Differentiate the product and retain customers.",
        }

        return {
            "agent": "CEO",
            "decision": strategies.get(event, strategies["normal"]),
            "reason": (
                f"Reviewed {len(recommendations)} department "
                "recommendations before selecting a strategy."
            ),
        }
