import joblib


MODEL_PATH = "models/npt_model.pkl"

# Must match training features
MODEL_FEATURES = [
    "total_orders",
    "orders_last_30",
    "days_since_last_purchase",
    "total_spend",
    "avg_order_value",
    "spend_last_30"
]


def load_npt_model():
    model = joblib.load(MODEL_PATH)
    return model


def predict_npt(df, model):
    X = df[MODEL_FEATURES]
    df["predicted_npt"] = model.predict(X)
    return df
