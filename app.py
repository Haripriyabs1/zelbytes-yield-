import streamlit as st
from src.predict import make_prediction
import json
import pandas as pd
import numpy as np

@st.cache_resource
def load_predictor():
    return make_prediction

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    page_icon="🍄"
)
with open("metadata.json", "r") as f:
    metadata = json.load(f)

st.title("🍄 Mushroom Yield Forecast App")
with st.expander("Model Information"):

    st.write(
        f"Version: {metadata['model_version']}"
    )

    st.write(
        f"Last Training Date: {metadata['last_training_date']}"
    )

    st.write(
        f"Test MAE: {metadata['test_mae']:.4f}"
    )

with st.expander("How Predictions Are Generated"):

    st.markdown("""
    This forecasting model predicts mushroom yield using:

    - Temperature (°C)
    - Humidity (%)
    - CO₂ concentration (ppm)

    Historical environmental sensor data was used
    to train the machine learning model.

    The predicted value represents the expected
    mushroom yield in kilograms.
    """)

st.write(
    "Predict mushroom yield using sensor readings."
)

st.sidebar.header("Sensor Inputs")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    15.0,
    35.0,
    25.0
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    40.0,
    100.0,
    85.0
)

co2 = st.sidebar.slider(
    "CO₂ (ppm)",
    300,
    1500,
    700
)

try:
    predictor = load_predictor()

except Exception as e:
    st.error(
        f"Unable to load model artifacts: {e}"
    )
    st.stop()

if st.button("Predict Yield"):

    with st.spinner("Generating prediction..."):

        prediction = predictor(
            temperature,
            humidity,
            co2
        )

    st.metric(
    label="Predicted Yield",
    value=f"{prediction:.2f} kg"
    )

    if prediction >= 4:
        st.success("High expected yield.")

    elif prediction >= 2:
        st.info("Moderate expected yield.")

    else:
        st.error("Low expected yield.")
if temperature < 20 or temperature > 30:
    st.warning("Temperature is outside the typical training range.")

if humidity < 60 or humidity > 95:
    st.warning("Humidity is outside the typical training range.")

if co2 < 500 or co2 > 1200:
    st.warning("CO₂ is outside the typical training range.")
show_chart = st.checkbox(
    "Show Yield Sensitivity Analysis"
)
if show_chart:

    humidity_range = np.linspace(
        40,
        100,
        50
    )

    yields = []

    for h in humidity_range:

        pred = predictor(
            temperature,
            h,
            co2
        )

        yields.append(pred)

    chart_df = pd.DataFrame({
        "Humidity": humidity_range,
        "Predicted Yield": yields
    })

    st.subheader("Yield Sensitivity Analysis")
    st.caption(
        f"Temperature fixed at {temperature}°C and CO₂ fixed at {co2} ppm"
    )

    st.line_chart(
        chart_df.set_index("Humidity")
    )