import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are an intelligent book assistant.

Your job:
1. Understand the user question
2. Decide what they want
3. Return a JSON plan

Possible intents:
- top_books
- search_title
- search_author
- search_category
- book_details
- general_question

Return ONLY JSON:

{
 "intent": "...",
 "keywords": "...",
 "limit": number
}
"""

def analyze_query(user_question):

    prompt = SYSTEM_PROMPT + f"\nUser question: {user_question}"

    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )

    # 🔥 PARSE HERE
    plan = json.loads(response.text)

    return plan
