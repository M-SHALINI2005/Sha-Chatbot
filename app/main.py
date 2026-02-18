from fastapi import FastAPI
from app.csv_search import search_books
from app.gemini_handler import generate_response

app = FastAPI()

@app.get("/chat")
def chat(q: str):
    books = search_books(q)
    answer = generate_response(q, books)

    return {
        "response": answer,
        "metadata": books
    }
