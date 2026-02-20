def analyze_query(q: str):

    q = q.lower()

    if "free" in q and "rating" in q:
        return {"type": "compare_free_paid"}

    if "how many" in q and "korean" in q:
        return {"type": "count_korean"}

    if "best" in q and "after" in q:
        return {"type": "best_after_year"}

    if "price" in q:
        return {"type": "price_lookup"}

    return {"type": "unknown"}