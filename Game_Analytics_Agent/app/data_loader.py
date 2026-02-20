from app.preprocessing import clean_data

df = clean_data(
    "data/game_data.csv",
    "data/game_ids.csv",
    "data/additional_data.csv"
)