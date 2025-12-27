from backend.uncertainty import predict_with_uncertainty
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd



app = FastAPI(
    title="SentinelML API",
    description="Energy Consumption Prediction API",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)













# Load trained model
model = joblib.load("models/energy_model.pkl")

# Input schema
class EnergyInput(BaseModel):
    hour: int
    day_of_week: int
    month: int
    lag_1: float
    lag_24: float
    rolling_24h: float


@app.get("/")
def root():
    return {"message": "SentinelML API is running 🚀"}


@app.post("/predict/1h")
def predict_energy_1h(data: EnergyInput):
    input_df = pd.DataFrame([data.dict()])
    result = predict_with_uncertainty(input_df)
    


@app.post("/predict/multi-horizon")
def predict_multi_horizon(data: EnergyInput):
    input_df = pd.DataFrame([data.dict()])

    return {
        "1h": predict_with_uncertainty(input_df, "1h"),
        "6h": predict_with_uncertainty(input_df, "6h"),
        "24h": predict_with_uncertainty(input_df, "24h"),
    }


    

