from fastapi import FastAPI
from app.query_analyzer import analyze_query
from app.csv_search import search_books
from app.response_builder import build_response
from fastapi.middleware.cors import CORSMiddleware
from app.gemini_handler import analyze_query, generate_reply


app = FastAPI()

@app.get("/chat")
def chat(q: str):

    plan = analyze_query(q)

    books = search_books(plan)

    text = generate_reply(q, books)

    return {
        "response": text,
        "metadata": books
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
