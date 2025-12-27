import pandas as pd

def load_and_process_data(path):
    df = pd.read_csv(path)

    df["datetime"] = pd.to_datetime(df["datetime"])

    # Force numeric
    df["energy_consumption"] = pd.to_numeric(
        df["energy_consumption"], errors="coerce"
    )

    df.dropna(inplace=True)

    # Time features
    df["hour"] = df["datetime"].dt.hour
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["month"] = df["datetime"].dt.month

    # Lag features
    df["lag_1"] = df["energy_consumption"].shift(1)
    df["lag_24"] = df["energy_consumption"].shift(24)

    # Rolling stats
    df["rolling_24h"] = df["energy_consumption"].rolling(24).mean()

    # 🔥 MULTI-HORIZON TARGETS
    df["target_1h"] = df["energy_consumption"].shift(-1)
    df["target_6h"] = df["energy_consumption"].shift(-6)
    df["target_24h"] = df["energy_consumption"].shift(-24)

    df.dropna(inplace=True)

    features = [
        "hour",
        "day_of_week",
        "month",
        "lag_1",
        "lag_24",
        "rolling_24h"
    ]

    X = df[features]

    y = {
        "1h": df["target_1h"],
        "6h": df["target_6h"],
        "24h": df["target_24h"]
    }

    return X, y
