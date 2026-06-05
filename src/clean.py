import pandas as pd

# Load data from ingestion stage
df = pd.read_csv(
    "data/interim/01_loaded.csv",
    parse_dates=["timestamp"]
)

# Count nulls before cleaning
null_before = df.isnull().sum()

print("NULLS BEFORE CLEANING")
print(null_before)

# Fill missing sensor values
df["temperature"] = df["temperature"].fillna(
    df["temperature"].mean()
)

df["humidity"] = df["humidity"].fillna(
    df["humidity"].median()
)

df["CO2"] = df["CO2"].fillna(
    df["CO2"].median()
)

# Remove rows with missing yield
df = df.dropna(subset=["yield"])

# Count nulls after cleaning
null_after = df.isnull().sum()

print("\nNULLS AFTER CLEANING")
print(null_after)

# Save cleaned dataset
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

print("\nCleaning completed successfully!")