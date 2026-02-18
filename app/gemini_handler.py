import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are an intelligent AI assistant.

Classify the user's question.

If the question is about books, authors, categories, ratings, or recommendations → return:

{
 "type": "book_query",
 "filters": {
    "title": "",
    "author": "",
    "category": ""
 },
 "sort_by": "",
 "limit": 5
}

If the question is general conversation (greetings, feelings, casual talk, life questions, etc.) → return:

{
 "type": "general"
}

Rules:
- Greetings = general
- Emotions = general
- Questions not related to books = general
- Only book-related requests = book_query

Format answer cleanly:
- short paragraphs
- bullet points for lists
- no markdown stars

Return ONLY JSON.
"""

def generate_reply(question, books):

    if not books:
        return "I couldn't find any books matching your request."

    book_text = "\n".join(
        [f"{b['title']} by {b['authors']} (Rating: {b.get('average_rating', 'N/A')})"
         for b in books]
    )

    prompt = f"""
You are a friendly AI book assistant.

User question:
{question}

Book results:
{book_text}
You are a clean-format AI assistant.

Rules for response formatting:
- NEVER use markdown symbols like *, **, #, -, etc.
- Use only plain text.
- Use numbered points when listing books.
- Each book must be on a new line.
- Keep answers short and neat.
- Do NOT add decorative characters.

If recommending books, format exactly like:

Here are some books you may like:

1. Title: <title>
   Author: <author>
   Rating: <rating>

2. Title: <title>
   Author: <author>
   Rating: <rating>

User question:
{question}

Books data:
{books}
"""

    response = model.generate_content(prompt)

    return response.text


def analyze_query(user_question):

    prompt = SYSTEM_PROMPT + f"\nUser question: {user_question}"

    try:
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )

        plan = json.loads(response.text)

    except Exception:
        # fallback if Gemini returns invalid JSON
        return {"type": "general"}

    # defaults
    if plan.get("type") == "book_query":
        plan["limit"] = plan.get("limit") or 5
        plan["filters"] = plan.get("filters") or {}

    return plan
