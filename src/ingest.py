import pandas as pd

df = pd.read_csv(
    "../data/raw/polyhouse_sensors.csv",
    parse_dates=["timestamp"]
)

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nInfo:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

df.to_csv(
    "../data/interim/01_loaded.csv",
    index=False
)

print("\n01_loaded.csv saved successfully!")