import mlflow
import mlflow.sklearn
import joblib

# Load your trained models
model_le_10 = joblib.load("app/models/npt_model_lt_10.pkl")
model_gt_10 = joblib.load("app/models/npt_model_gt_10.pkl")




mlflow.set_experiment("NPT_Model_LE_10")

with mlflow.start_run():

    mlflow.log_param("segment", "days_since_last_purchase <= 10")

    mlflow.sklearn.log_model(
        sk_model=model_le_10,
        artifact_path="model",
        registered_model_name="NPT_Model_LE_10"
    )

    print("✅ Model LE_10 logged successfully")




mlflow.set_experiment("NPT_Model_GT_10")

with mlflow.start_run():

    mlflow.log_param("segment", "days_since_last_purchase > 10")

    mlflow.sklearn.log_model(
        sk_model=model_gt_10,
        artifact_path="model",
        registered_model_name="NPT_Model_GT_10"
    )

    print("✅ Model GT_10 logged successfully")