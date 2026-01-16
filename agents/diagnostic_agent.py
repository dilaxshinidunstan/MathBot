from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,  # lower for stability
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def diagnostic_agent(concept: str) -> str:
    """
    concept MUST be a short, clean math topic
    e.g., 'Area of a cylinder', 'LCM', 'Linear equations'
    """

    prompt = f"""
You are a diagnostic mathematics tutor.

Your task:
Ask EXACTLY ONE probing question that tests understanding of the SAME concept.

Concept:
{concept}

Strict rules:
- Stay strictly within the given concept
- Do NOT introduce new topics
- Do NOT explain
- Do NOT give answers
- Output ONLY the question
"""

    response = llm.invoke(prompt).content.strip()

    # Safety: ensure it is a question
    if not response.endswith("?"):
        response += "?"

    return response
