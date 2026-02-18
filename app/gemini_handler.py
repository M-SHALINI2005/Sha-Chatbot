import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(question, books):
    prompt = f"""
User question: {question}

Book results:
{books}

Explain the answer in a friendly human tone.
"""

    response = model.generate_content(prompt)

    return response.text
