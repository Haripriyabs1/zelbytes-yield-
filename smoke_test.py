import pandas as pd

print("--- Running Mushroom Yield Workspace Smoke Test ---")

sample_data = {
    "Temperature_C": [24.5],
    "Humidity_Pct": [88.2],
    "CO2_ppm": [950],
    "Predicted_Yield_kg": [4.2]
}

df = pd.DataFrame(sample_data)

print("\n[SUCCESS] Your tools are working! Here is a sample polyhouse row:")
print(df.to_string(index=False))