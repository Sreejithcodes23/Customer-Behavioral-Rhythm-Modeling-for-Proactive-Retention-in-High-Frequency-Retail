import mlflow
import mlflow.sklearn
import joblib

model = joblib.load("app/models/npt_model.pkl")

mlflow.set_experiment("NPT_Model")

with mlflow.start_run():

    mlflow.log_param("model_type", "npt_existing_model")


    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="npt_model"
    )

    print("Model logged correctly!")