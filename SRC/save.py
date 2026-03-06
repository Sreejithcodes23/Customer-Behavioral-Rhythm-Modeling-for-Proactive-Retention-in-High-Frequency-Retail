from config.db import engine


def save_scores(df, snapshot_date):
    """
    Save customer behavior scores to DB.
    """

    df_out = df.copy()
    df_out["snapshot_date"] = snapshot_date

    df_out = df_out[
        [
            "USERID",
            "snapshot_date",
            "days_since_last_purchase",
            "mean_gap",
            "bds",
            "predicted_npt",
            "priority_score",
            "risk_bucket",
            "total_orders",
            "orders_last_30",
            "total_spend",
            "avg_order_value",
            "spend_last_30",
        ]
    ]

    df_out.to_sql(
        "customer_behavior_scores",
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )
