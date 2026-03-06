import pandas as pd
from config.db import engine
from sqlalchemy import text


def get_next_snapshot_date():
    """
    Determine next snapshot date to process.
    """

    state = pd.read_sql(
        "SELECT last_snapshot_date FROM pipeline_state WHERE id=1",
        engine
    ).iloc[0, 0]

    # first run
    if state is None:
        query = f"""SELECT MIN("DATE_") FROM orders_data"""
    else:
        query = f"""
            SELECT MIN("DATE_")
            FROM orders_data
            WHERE "DATE_" > DATE '{state}'
        """

    next_date = pd.read_sql(query, engine).iloc[0, 0]

    return next_date


def update_pipeline_state(snapshot_date):
    with engine.begin() as conn:
        conn.execute(
            text("""
                UPDATE pipeline_state
                SET last_snapshot_date = :snapshot_date
                WHERE id = 1
            """),
            {"snapshot_date": snapshot_date},
        )

