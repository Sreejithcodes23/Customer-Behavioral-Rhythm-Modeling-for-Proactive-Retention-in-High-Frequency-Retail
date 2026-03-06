from src.scheduler import get_next_snapshot_date, update_pipeline_state
from src.features_sql import get_customer_features
from src.bds import compute_bds
from src.npt import load_npt_model, predict_npt
from src.priority import compute_priority
from src.save import save_scores


def run_daily_pipeline():
    model = load_npt_model()

    snapshot_date = get_next_snapshot_date()

    if snapshot_date is None:
        print("All dates processed.")
        return

    print(f"Running snapshot: {snapshot_date}")

    df = get_customer_features(snapshot_date)
    df = compute_bds(df)
    df = predict_npt(df, model)
    df = compute_priority(df)

    save_scores(df, snapshot_date)

    update_pipeline_state(snapshot_date)

    print("Completed and state updated.")


if __name__ == "__main__":
    run_daily_pipeline()