import pandas as pd
import random

rows = []

for i in range(100):
    rows.append({
        "timestamp": pd.Timestamp("2026-06-01") + pd.Timedelta(hours=i),
        "temperature": round(random.uniform(22, 28), 1),
        "humidity": round(random.uniform(80, 95), 1),
        "CO2": random.randint(600, 1200),
        "yield": round(random.uniform(0.5, 5.0), 2)
    })

df = pd.DataFrame(rows)

# Add a few missing values for cleaning practice
df.loc[10, "temperature"] = None
df.loc[25, "humidity"] = None
df.loc[40, "CO2"] = None
df.loc[60, "yield"] = None

df.to_csv("data/raw/polyhouse_sensors.csv", index=False)

print("Dataset created successfully!")
print(df.head())