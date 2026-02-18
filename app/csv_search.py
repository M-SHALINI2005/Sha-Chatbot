import pandas as pd
import re

df = pd.read_csv("data/books.csv")

def get_books():
    return df

def clean_number(x):
    if pd.isna(x):
        return x
    return float(re.findall(r"\d+\.?\d*", str(x))[0])

df["average_rating"] = df["average_rating"].apply(clean_number)
df["num_pages"] = df["num_pages"].apply(clean_number)
df["ratings_count"] = df["ratings_count"].apply(clean_number)
df["published_year"] = df["published_year"].apply(clean_number)

def search_books(query):
    query = query.lower()
    df = get_books()

    # Top N books by rating
    if "top" in query and "rating" in query:
        n = [int(s) for s in query.split() if s.isdigit()]
        n = n[0] if n else 5

        result = df.sort_values("average_rating", ascending=False).head(n)

    # Books by author
    elif "author" in query:
        name = query.split("author")[-1].strip()
        result = df[df["authors"].str.contains(name, case=False, na=False)]

    # Books by category
    elif "category" in query or "genre" in query:
        name = query.split()[-1]
        result = df[df["categories"].str.contains(name, case=False, na=False)]

    # Default
    else:
        result = df.head(3)

    return result.to_dict(orient="records")
