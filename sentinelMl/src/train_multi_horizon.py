from data_processing import load_and_process_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
import os

def train_model(X, y, horizon):
    print(f"\n🤖 Training {horizon} model...")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = RandomForestRegressor(
        n_estimators=50,
        max_depth=8,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    print(f"✅ MAE ({horizon}): {mae:.4f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/energy_model_{horizon}.pkl")


def main():
    print("🚀 Loading data for multi-horizon training...")
    X, targets = load_and_process_data("data/raw/energy.csv")

    for horizon, y in targets.items():
        train_model(X, y, horizon)

    print("\n🎉 All horizon models trained successfully!")


if __name__ == "__main__":
    main()
