def compute_priority(df):
    """
    Compute customer priority score.
    """
    df["priority_score"] = df["bds"] * (1 / df["predicted_npt"])
    return df
