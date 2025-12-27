import joblib
import shap
import pandas as pd
import matplotlib

# Use non-GUI backend (VERY IMPORTANT)
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from data_processing import load_and_process_data
import os

def main():
    print("🚀 Loading model...")
    model = joblib.load("models/energy_model.pkl")

    print("📊 Loading data...")
    X, y = load_and_process_data("data/raw/energy.csv")

    # Sample for speed
    X_sample = X.sample(500, random_state=42)

    print("🔍 Initializing SHAP explainer...")
    explainer = shap.TreeExplainer(model)

    print("🧠 Computing SHAP values...")
    shap_values = explainer.shap_values(X_sample)

    os.makedirs("reports", exist_ok=True)

    print("📈 Saving global feature importance plot...")
    shap.summary_plot(shap_values, X_sample, show=False)
    plt.tight_layout()
    plt.savefig("reports/shap_summary.png")
    plt.close()

    print("🔎 Saving local explanation plot...")
    shap.force_plot(
        explainer.expected_value,
        shap_values[0],
        X_sample.iloc[0],
        matplotlib=True,
        show=False
    )
    plt.savefig("reports/shap_force.png")
    plt.close()

    print("✅ SHAP explanations saved in /reports folder")

if __name__ == "__main__":
    main()
