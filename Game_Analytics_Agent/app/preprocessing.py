import pandas as pd

def clean_data(game_path, ids_path, additional_path):

    # ---------- Load ----------
    games = pd.read_csv(game_path)
    ids = pd.read_csv(ids_path)
    extra = pd.read_csv(additional_path)

    # ---------- Standardize Column Names ----------
    games.columns = games.columns.str.lower().str.strip()
    ids.columns = ids.columns.str.lower().str.strip()
    extra.columns = extra.columns.str.lower().str.strip()

    # ---------- Remove duplicates ----------
    games = games.drop_duplicates()
    ids = ids.drop_duplicates()
    extra = extra.drop_duplicates()

    # ---------- Handle Missing Values ----------
    games = games.fillna(method="ffill")
    ids = ids.fillna("Unknown")
    extra = extra.fillna(0)

    # ---------- Fix Datatypes ----------
    for col in games.columns:
        if "date" in col:
            games[col] = pd.to_datetime(games[col], errors="coerce")

    # ---------- Merge datasets ----------
    df = games.merge(ids, how="left", on="game_id")
    df = df.merge(extra, how="left", on="game_id")

    return df