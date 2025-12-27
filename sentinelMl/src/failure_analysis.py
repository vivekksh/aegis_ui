import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

from data_processing import load_and_process_data

def main():
    print("🚀 Loading model...")
    model = joblib.load("models/energy_model.pkl")

    print("📊 Loading data...")
    X, y = load_and_process_data("data/raw/energy.csv")

    print("🤖 Generating predictions...")
    preds = model.predict(X)

    # Compute absolute errors
    errors = np.abs(y.values - preds)

    # Define failure threshold (top 5% errors)
    threshold = np.percentile(errors, 95)
    failure_mask = errors >= threshold

    failure_X = X[failure_mask]
    failure_errors = errors[failure_mask]

    print(f"❌ Number of failure cases: {len(failure_X)}")

    # Clustering failures
    print("🔍 Clustering failure cases...")
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(failure_X)

    failure_report = failure_X.copy()
    failure_report["error"] = failure_errors
    failure_report["cluster"] = clusters

    print("\n📊 FAILURE CLUSTER SUMMARY")
    print("-" * 50)
    print(
        failure_report
        .groupby("cluster")
        .mean()
    )

    failure_report.to_csv(
        "reports/failure_analysis.csv",
        index=False
    )

    print("✅ Failure analysis saved to reports/failure_analysis.csv")

if __name__ == "__main__":
    main()
