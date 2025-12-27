from data_processing import load_and_process_data

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os

def main():
    print("🚀 Loading and processing data...")
    X, y = load_and_process_data("data/raw/energy.csv")

    print(f"📊 Total samples after processing: {len(X)}")

    print("✂️ Splitting data (time-aware)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    print("🤖 Training RandomForest model...")
    model = RandomForestRegressor(
        n_estimators=50,     # fast for development
        max_depth=8,
        n_jobs=-1,           # use all CPU cores
        random_state=42
    )

    model.fit(X_train, y_train)

    print("📈 Evaluating model...")
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5

    r2 = r2_score(y_test, preds)

    print(f"✅ MAE  : {mae:.4f}")
    print(f"✅ RMSE : {rmse:.4f}")
    print(f"✅ R²   : {r2:.4f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/energy_model.pkl")

    print("💾 Model saved to models/energy_model.pkl")
    print("🎉 Training completed successfully!")

if __name__ == "__main__":
    main()
