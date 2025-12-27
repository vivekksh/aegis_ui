import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

from data_processing import load_and_process_data

def detect_drift(reference_df, current_df, threshold=0.05):
    drift_report = {}

    for column in reference_df.columns:
        stat, p_value = ks_2samp(
            reference_df[column],
            current_df[column]
        )

        drift_report[column] = {
            "p_value": p_value,
            "drift_detected": p_value < threshold
        }

    return drift_report


def main():
    print("🚀 Loading processed features...")
    X, y = load_and_process_data("data/raw/energy.csv")

    # Simulate time-based split
    split_index = int(len(X) * 0.7)

    reference_data = X.iloc[:split_index]
    current_data = X.iloc[split_index:]

    print("🔍 Detecting data drift...")
    drift_results = detect_drift(reference_data, current_data)

    print("\n📊 DRIFT REPORT")
    print("-" * 40)

    for feature, result in drift_results.items():
        status = "⚠️ DRIFT" if result["drift_detected"] else "✅ STABLE"
        print(
            f"{feature:15} | {status} | p-value = {result['p_value']:.5f}"
        )


if __name__ == "__main__":
    main()
