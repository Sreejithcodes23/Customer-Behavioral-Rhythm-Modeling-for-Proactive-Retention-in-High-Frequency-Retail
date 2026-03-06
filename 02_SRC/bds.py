import numpy as np


def compute_bds(df):
    df = df.copy()

    df["mean_gap"] = df["mean_gap"].replace(0, np.nan)

    valid_gaps = df["mean_gap"].dropna()

    if len(valid_gaps) == 0:
        median_gap = 30
    else:
        median_gap = valid_gaps.median()

    df["mean_gap"] = df["mean_gap"].fillna(median_gap)

    df["bds"] = df["days_since_last_purchase"] / df["mean_gap"]

    # %%
    def bucket(x):
        if x < 0.8:
            return "early"
        elif x <= 1.2:
            return "on_time"
        elif x <= 1.8:
            return "mild_delay"
        else:
            return "high_delay"

    df["risk_bucket"] = df["bds"].apply(bucket)

    return df
