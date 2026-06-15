import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import mlflow.sklearn

# Synthetic Fraud Data Create Karna
np.random.seed(42)
data_size = 1000
data = pd.DataFrame({
    'amount': np.random.uniform(10, 10000, data_size),
    'oldBalance': np.random.uniform(0, 50000, data_size),
    'newBalance': np.random.uniform(0, 50000, data_size),
    'isFraud': np.random.choice([0, 1], size=data_size, p=[0.95, 0.05])
})

X = data[['amount', 'oldBalance', 'newBalance']]
y = data['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier Train Karna
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model local file mein save karna
joblib.dump(model, "src/fraud_model.pkl")
print(f"Model trained successfully! Test Accuracy: {model.score(X_test, y_test):.4f}")

# Local MLflow Server URL set karna
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Fraud_Detection_System")

with mlflow.start_run():
    # Logging parameters and metrics
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", model.score(X_test, y_test))
    
    # Model tracking aur registry registration
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="RandomForestFraudModel"
    )
print("Experiment successfully logged into MLflow Dashboard.")