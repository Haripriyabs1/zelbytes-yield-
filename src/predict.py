import joblib
import json
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = ROOT / "models" / "champion.joblib"
SCALER_PATH = ROOT / "models" / "scaler.joblib"
FEATURE_PATH = ROOT / "models" / "features.json"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

with open(FEATURE_PATH, "r") as f:
    feature_columns = json.load(f)


def make_prediction(temperature, humidity, co2):

    input_df = pd.DataFrame(
        [[temperature, humidity, co2]],
        columns=feature_columns
    )

    scaled_input = pd.DataFrame(
    scaler.transform(input_df),
    columns=feature_columns
    )

    prediction = model.predict(scaled_input)

    return float(prediction[0])


if __name__ == "__main__":

    result = make_prediction(
        25,
        85,
        700
    )

    print(f"Predicted Yield: {result:.2f} kg")