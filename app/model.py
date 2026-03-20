"""import joblib
import pandas as pd

MODEL_PATH = "app/models/npt_model.pkl"

MODEL_FEATURES = [
    "total_orders",
    "orders_last_30",
    "days_since_last_purchase",
    "total_spend",
    "avg_order_value",
    "spend_last_30"
]

# Load once (important 🚀)
model = joblib.load(MODEL_PATH)


def predict_npt(data: dict):


    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Ensure correct feature order
    X = df[MODEL_FEATURES]

    prediction = model.predict(X)[0]

    return float(prediction)
def calculate_deviation(actual_gap, predicted_gap):
    deviation = abs(actual_gap - predicted_gap) / predicted_gap
    return float(deviation)"""

import mlflow.pyfunc
import joblib
import pandas as pd

MODEL_URI = "models:/NPT_Model@production"
LOCAL_MODEL_PATH = "app/models/npt_model.pkl"

MODEL_FEATURES = [
    "total_orders",
    "orders_last_30",
    "days_since_last_purchase",
    "total_spend",
    "avg_order_value",
    "spend_last_30"
]

# Try MLflow first, fallback to local
try:
    model = mlflow.pyfunc.load_model(MODEL_URI)
    print("✅ Loaded model from MLflow")
except Exception as e:
    print("⚠️ MLflow failed, loading local model:", e)
    model = joblib.load(LOCAL_MODEL_PATH)


def predict_npt(data: dict):
    df = pd.DataFrame([data])
    X = df[MODEL_FEATURES]
    prediction = model.predict(X)[0]
    return float(prediction)


def calculate_deviation(actual_gap, predicted_gap):
    deviation = abs(actual_gap - predicted_gap) / predicted_gap
    return float(deviation)