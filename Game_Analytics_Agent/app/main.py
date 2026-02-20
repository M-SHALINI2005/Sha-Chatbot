from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# ---------- Load datasets ----------
game_df = pd.read_csv("game/analytics/data/game_data.csv")
add_df = pd.read_csv("game/analytics/data/additional.csv")
ids_df = pd.read_csv("game/analytics/data/data_ids.csv")


# ---------- Request Schema ----------
class QueryRequest(BaseModel):
    query: str


# ---------- Home Route ----------
@app.get("/")
def home():
    return {"message": "Game Analytics Agent is running"}


# ---------- Chat Route ----------
@app.get("/chat")
def chat(q: str):
    return {"response": f"You asked: {q}"}


@app.post("/game/analytics")
def game_analytics(request: QueryRequest):
    q = request.query.lower()

    try:
        # ---------- TOTAL GAMES ----------
        if "total games" in q or "count games" in q:
            result = len(game_df)

        # ---------- SHOW COLUMNS ----------
        elif "columns" in q or "fields" in q:
            result = list(game_df.columns)

        # ---------- MAX VALUES ----------
        elif "top score" in q or "max" in q:
            result = game_df.max(numeric_only=True).to_dict()

        # ---------- FREE VS PAID ----------
        elif "free vs paid" in q or "compare free paid" in q:
            free = game_df[game_df["price"] == 0]["rating"].mean()
            paid = game_df[game_df["price"] > 0]["rating"].mean()

            result = {
                "free_avg_rating": round(free, 2),
                "paid_avg_rating": round(paid, 2)
            }

        # ---------- SEARCH GAME ----------
        elif "price of" in q:
            name = q.replace("price of", "").strip()

            row = game_df[game_df["name"].str.lower() == name]

            if not row.empty:
                result = row.iloc[0]["price"]
            else:
                result = "Game not found"

        # ---------- DEFAULT ----------
        else:
            result = "Query not recognized yet"

        return {
            "query": request.query,
            "result": result,
            "status": "success"
        }

    except Exception as e:
        return {
            "query": request.query,
            "error": str(e),
            "status": "failed"
        }