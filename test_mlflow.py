import mlflow

# MLflow ko batao ke database kahan hai
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Fraud_Detection_Experiment")

with mlflow.start_run():
    mlflow.log_param("test_param", 100)
    mlflow.log_metric("test_accuracy", 0.95)
    print("Experiment logged successfully!")