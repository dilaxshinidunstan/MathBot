import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")

MODEL = "@cf/leonardo/phoenix-1.0"


def generate_diagram(concept_description: str):
    """
    Generate an educational diagram using an LLM.
    Returns image bytes or None.
    """

    if not ACCOUNT_ID or not API_TOKEN:
        print("Cloudflare credentials missing!")
        return None

    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{MODEL}"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an expert educational illustrator for school-level mathematics.

Task:
- Analyze the given math concept
- Choose the MOST appropriate visual representation
- Create a clear, beginner-friendly educational diagram

Concept:
{concept_description}

Diagram rules:
- White background
- Clean black or dark-blue lines
- Large readable labels
- No decorative art
- No shading
- No extra text

Diagram selection guidance:
- Geometry → labeled shapes
- Algebra → number line or balance scale
- Equations → symbolic relations with arrows
- Graphs → x-y axes with plotted relation
- Sets → Venn diagrams
- Ratios → grouped blocks or bars

The diagram must help a student UNDERSTAND the concept visually.
"""

    try:
        response = requests.post(
            url,
            headers=headers,
            json={"prompt": prompt},
            timeout=30
        )

        if response.status_code == 200:
            return response.content  # image bytes

        print("Cloudflare error:", response.status_code, response.text)
        return None

    except Exception as e:
        print("Visualization request failed:", e)
        return None
