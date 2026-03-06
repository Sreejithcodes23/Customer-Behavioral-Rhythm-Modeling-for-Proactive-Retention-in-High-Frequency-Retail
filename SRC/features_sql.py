from config.db import engine
import pandas as pd


SQL_FEATURE_TEMPLATE = """
WITH filtered_orders AS (
    SELECT
        "USERID",
        "DATE_",
        "TOTALBASKET"
    FROM orders_data
    WHERE "DATE_" <= '{snapshot_date}'
),

last_purchase AS (
    SELECT
        "USERID",
        MAX("DATE_") AS last_purchase_date
    FROM filtered_orders
    GROUP BY "USERID"
),

gaps AS (
    SELECT
        "USERID",
        "DATE_",
        LAG("DATE_") OVER (
            PARTITION BY "USERID"
            ORDER BY "DATE_"
        ) AS prev_order_date
    FROM filtered_orders
),

gap_days AS (
    SELECT
        "USERID",
        ("DATE_" - prev_order_date) AS gap_days
    FROM gaps
    WHERE prev_order_date IS NOT NULL
),

rhythm AS (
    SELECT
        "USERID",
        AVG(gap_days) AS mean_gap
    FROM gap_days
    GROUP BY "USERID"
),

rfm AS (
    SELECT
        "USERID",
        COUNT(*) AS total_orders,
        AVG("TOTALBASKET") AS avg_order_value,
        SUM("TOTALBASKET") AS total_spend,
        COUNT(*) FILTER (
            WHERE "DATE_" >= DATE '{snapshot_date}' - INTERVAL '30 days'
        ) AS orders_last_30,
        SUM("TOTALBASKET") FILTER (
            WHERE "DATE_" >= DATE '{snapshot_date}' - INTERVAL '30 days'
        ) AS spend_last_30
    FROM filtered_orders
    GROUP BY "USERID"
)

SELECT
    lp."USERID",
    lp.last_purchase_date,
    DATE '{snapshot_date}' - lp.last_purchase_date AS days_since_last_purchase,
    r.mean_gap,
    f.total_orders,
    f.avg_order_value,
    f.total_spend,
    f.orders_last_30,
    f.spend_last_30
FROM last_purchase lp
LEFT JOIN rhythm r ON lp."USERID" = r."USERID"
LEFT JOIN rfm f ON lp."USERID" = f."USERID";

"""


def get_customer_features(snapshot_date):
    """
    Run SQL feature query for given snapshot_date.
    """
    query = SQL_FEATURE_TEMPLATE.format(snapshot_date=snapshot_date)
    df = pd.read_sql(query, engine)
    return df
