import pandas as pd

# Read raw file
df = pd.read_csv(
    "data/raw/household_power_consumption.txt",
    sep=";",
    engine="python"
)

# Show what pandas read
print("COLUMNS FOUND:", df.columns.tolist())
print("FIRST 5 ROWS:")
print(df.head())

# Clean column names
df.columns = df.columns.str.strip()

# Combine Date + Time
df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"], errors="coerce")

# Select only required columns
df = df[["datetime", "Global_active_power"]]

# Rename
df.columns = ["datetime", "energy_consumption"]

# Drop missing values
df = df.dropna()

# Save clean CSV
df.to_csv("data/raw/energy.csv", index=False)

print("✅ energy.csv created with columns:", df.columns.tolist())
