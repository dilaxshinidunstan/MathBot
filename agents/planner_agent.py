from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

def planner_agent(student_query: str) -> str:
    prompt = f"""
You are a mathematics curriculum planner for school students.

Student question:
{student_query}

Your tasks:
1. Identify the MAIN math concept.
2. Identify 2–3 prerequisite concepts.
3. Choose ONE prerequisite to test FIRST.
4. Estimate difficulty: EASY / MEDIUM / HARD.

Return EXACTLY in this format:
Main Concept:
Prerequisite Concepts:
First Concept to Test:
Difficulty:
"""
    return llm.invoke(prompt).content.strip()
