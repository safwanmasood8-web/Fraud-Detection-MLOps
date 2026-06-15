from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Real-Time Fraud Detection API")

# Prometheus Metrics ka setup
Instrumentator().instrument(app).expose(app)

# Model load karna
try:
    model = joblib.load("src/fraud_model.pkl")
except:
    model = None

class TransactionData(BaseModel):
    amount: float
    oldBalance: float
    newBalance: float

@app.get("/")
def home():
    return {"status": "Online", "message": "Fraud Detection API System is Live"}

@app.post("/predict")
def predict_fraud(data: TransactionData):
    if model is None:
        return {"error": "Model file missing"}
    
    features = np.array([[data.amount, data.oldBalance, data.newBalance]])
    prediction = model.predict(features)[0]
    
    result = "Fraudulent" if prediction == 1 else "Legitimate"
    return {"prediction": result, "status_code": 200}