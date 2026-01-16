from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def evaluate_student_answer(question: str, student_answer: str) -> str:
    prompt = f"""
You are a mathematics assessment agent.

Question asked:
{question}

Student answer:
{student_answer}

Decide the student's understanding.

Return ONLY in this format:
Understanding: YES / PARTIAL / NO
Reason:
"""
    return llm.invoke(prompt).content.strip()
