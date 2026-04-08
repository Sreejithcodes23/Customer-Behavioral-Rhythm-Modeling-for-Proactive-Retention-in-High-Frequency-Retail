import mlflow.pyfunc
import pandas as pd


# Load both models from MLflow


model_le_10 = mlflow.pyfunc.load_model("models:/NPT_Model_LE_10@production")
model_gt_10 = mlflow.pyfunc.load_model("models:/NPT_Model_GT_10@production")



# Features (must match training)


MODEL_FEATURES = [
    "total_orders",
    "orders_last_30",
    "days_since_last_purchase",
    "total_spend",
    "avg_order_value",
    "spend_last_30",
]

# Prediction Function (API)

def predict_npt(data: dict):
    """
    data: dictionary input from API
    """

    df = pd.DataFrame([data])
    X = df[MODEL_FEATURES]

    # Condition-based model selection
    if df["days_since_last_purchase"].iloc[0] <= 10:
        pred = model_le_10.predict(X)[0]
    else:
        pred = model_gt_10.predict(X)[0]

    return float(pred)



# Behavioral Deviation Score


def calculate_deviation(actual_gap, predicted_gap):
    deviation = abs(actual_gap - predicted_gap) / predicted_gap
    return float(deviation)