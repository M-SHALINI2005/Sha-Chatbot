import pandas as pd

df = pd.read_csv("data/books.csv")

def search_books(plan):

    data = df.copy()

    filters = plan.get("filters", {})

    if filters.get("title"):
        data = data[data["title"].str.contains(filters["title"], case=False, na=False)]

    if filters.get("author"):
        data = data[data["authors"].str.contains(filters["author"], case=False, na=False)]

    if filters.get("category"):
        data = data[data["categories"].str.contains(filters["category"], case=False, na=False)]

    sort_by = plan.get("sort_by")
    if sort_by and sort_by in data.columns:
        data = data.sort_values(sort_by, ascending=False)

    limit = plan.get("limit", 5)

    return data.head(limit).to_dict(orient="records")
