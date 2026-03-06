import pandas as pd
from config.db import engine


def get_date_range():
    query = """
        SELECT MIN("DATE_") AS min_date,
               MAX("DATE_") AS max_date
        FROM orders_data;
    """

    df = pd.read_sql(query, engine)

    min_date = df.loc[0, "min_date"]
    max_date = df.loc[0, "max_date"]

    date_range = pd.date_range(start=min_date, end=max_date, freq="D")

    snapshot_dates = date_range.strftime("%Y-%m-%d").tolist()

    return snapshot_dates