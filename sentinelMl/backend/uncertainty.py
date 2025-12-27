import joblib
import numpy as np
import os
import pandas as pd

BASE_DIR = "models"

def load_ensemble(horizon):
    path = f"{BASE_DIR}/ensemble_{horizon}"

    if not os.path.exists(path):
        return None

    models = []
    for file in os.listdir(path):
        models.append(joblib.load(os.path.join(path, file)))

    return models


def predict_with_uncertainty(input_df, horizon):
    models = load_ensemble(horizon)

    if models is None:
        return {
            "error": f"Ensemble model for {horizon} not available"
        }

    predictions = [model.predict(input_df)[0] for model in models]

    mean_pred = np.mean(predictions)
    std_pred = np.std(predictions)

    return {
        "prediction": round(float(mean_pred), 3),
        "confidence_interval": [
            round(float(mean_pred - 1.96 * std_pred), 3),
            round(float(mean_pred + 1.96 * std_pred), 3)
        ]
    }
