def ask_llm(clause, query):
    # === Dummy Logic ===
    if "knee" in query.lower() and "90 days" in clause.lower():
        return {
            "decision": "Approved",
            "amount": "₹75,000",
            "justification": "Clause 4.3 confirms coverage for knee surgery after 90 days."
        }
    
    return {
        "decision": "Rejected",
        "amount": "₹0",
        "justification": "Procedure not covered or waiting period not met."
    }

