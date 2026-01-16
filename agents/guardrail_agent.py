def enforce_guardrails(response: str) -> str:
    if not response:
        return response

    # ✅ If the response is already a question, allow it
    if response.strip().endswith("?"):
        return response

    forbidden_indicators = [
        "therefore",
        "so the value",
        "final answer",
        "result is"
    ]

    if any(word in response.lower() for word in forbidden_indicators):
        return (
            "Let's pause here and check your understanding first.\n\n"
            "Can you think about how you would approach this?"
        )

    return response
