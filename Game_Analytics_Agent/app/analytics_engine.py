from app.data_loader import df


def run_analysis(plan, query):

    # ---------- Compare Free vs Paid ----------
    if plan["type"] == "compare_free_paid":
        free = df[df["price"] == 0]["rating"].mean()
        paid = df[df["price"] > 0]["rating"].mean()

        return (
            f"Free games avg rating = {free:.2f}, Paid games avg rating = {paid:.2f}",
            {"free_avg": float(free), "paid_avg": float(paid)}
        )


    # ---------- Count Korean Language Games ----------
    elif plan["type"] == "count_korean":
        count = df[df["languages"].astype(str).str.contains("Korean", na=False)].shape[0]

        return (
            f"{count} games support Korean",
            {"count": int(count)}
        )


    # ---------- Price Lookup ----------
    elif plan["type"] == "price_lookup":
        for name in df["name"].dropna():
            if str(name).lower() in query.lower():
                row = df[df["name"] == name].iloc[0]

                return (
                    f"{name} costs {row['price']} USD",
                    row.to_dict()
                )

        return ("Game not found in dataset", {})


    # ---------- Default ----------
    return ("Sorry I could not understand the query", {})