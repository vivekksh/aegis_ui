from data_processing import load_and_process_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import joblib
import os

N_MODELS = 5  # ensemble size

def main():
    print("🚀 Loading data...")
    X, targets = load_and_process_data("data/raw/energy.csv")
    y = targets["1h"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    os.makedirs("models/ensemble_1h", exist_ok=True)

    models = []

    print("🤖 Training ensemble models...")
    for i in range(N_MODELS):
        model = RandomForestRegressor(
            n_estimators=50,
            max_depth=8,
            random_state=42 + i,
            n_jobs=-1
        )
        model.fit(X_train, y_train)
        models.append(model)

        joblib.dump(
            model,
            f"models/ensemble_1h/model_{i}.pkl"
        )

        print(f"✅ Model {i+1}/{N_MODELS} trained")

    print("🎉 Ensemble training completed!")

if __name__ == "__main__":
    main()
