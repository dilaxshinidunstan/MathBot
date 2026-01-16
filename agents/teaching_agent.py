from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.25,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def teaching_agent(
    student_query: str,
    retrieved_docs=None,
    *,
    mode: str = "diagnostic",
    concept: str = None
) -> str:
    """
    mode:
    - 'diagnostic' → Ask ONE prerequisite question (default, old behavior)
    - 'explain'    → Explain concept simply when student is confused

    concept:
    - Short clean concept string (e.g., 'Area of a circle')
    """

    context = ""
    if retrieved_docs:
        context = "\n".join(doc.page_content for doc in retrieved_docs)

    # ------------------ DIAGNOSTIC MODE ------------------
    if mode == "diagnostic":
        prompt = f"""
You are a Socratic mathematics tutor.

STRICT RULES:
- Ask ONLY ONE question.
- The question must test prerequisite understanding.
- Do NOT explain.
- Do NOT give formulas or answers.
- No multiple questions.

Reference material (do not quote directly):
{context}

Student question:
{student_query}

Ask ONE diagnostic question now.
"""

    # ------------------ EXPLANATION MODE ------------------
    elif mode == "explain":
        prompt = f"""
        You are a patient mathematics tutor.

The student asked:
"{student_query}"

Current mathematical concept:
"{concept}"

STRICT OUTPUT FORMAT (MUST FOLLOW):

### Title
- Short, clear title

### Concept Explanation
- 2–3 bullet points explaining the idea

### Step-by-Step Method
- Step 1:
- Step 2:
- Step 3:

### Guided Example
- Use the given values
- Show transformations step by step
- Do NOT jump directly to the final answer

### Follow-up Question
- Ask EXACTLY ONE simple question

Rules:
- Use bullet points and numbered steps only
- School-level language
- Do NOT introduce new topics
"""
    else:
    
        raise ValueError(f"Unknown mode: {mode}")
    
    return llm.invoke(prompt).content.strip()
