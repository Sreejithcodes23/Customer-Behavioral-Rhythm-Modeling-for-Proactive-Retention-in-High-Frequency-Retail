from fastapi import FastAPI
from app.schema import NPTInput
from app.model import predict_npt

app = FastAPI(title="Next Purchase Timing API")


@app.get("/")
def home():
    return {"message": "NPT API is running 🚀"}


@app.post("/predict-npt")
def predict(data: NPTInput):
    input_data = data.dict()

    prediction = predict_npt(input_data)

    return {
        "predicted_next_purchase_days": round(prediction, 2)
    }
from app.model import predict_npt, calculate_deviation

@app.post("/customer-insight")
def customer_insight(data: NPTInput):
    input_data = data.dict()

    predicted_gap = predict_npt(input_data)

    actual_gap = input_data["days_since_last_purchase"]

    deviation_score = calculate_deviation(actual_gap, predicted_gap)

    # Business logic (VERY IMPORTANT 🔥)
    if deviation_score < 0.8:
        risk= "early"
    elif deviation_score <= 1.2:
        risk= "on_time"
    elif deviation_score <= 1.8:
        risk= "mild_delay"
    else:
        risk= "high_delay"

    return {
        "predicted_next_purchase_days": round(predicted_gap, 2),
        "behavioral_deviation_score": round(deviation_score, 3),
        "retention_risk": risk
    }