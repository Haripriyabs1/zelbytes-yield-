import streamlit as st
from src.predict import make_prediction

@st.cache_resource
def load_predictor():
    return make_prediction

st.set_page_config(
    page_title="Mushroom Yield Forecast",
    page_icon="🍄"
)

st.title("🍄 Mushroom Yield Forecast App")

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

predictor = load_predictor()

if st.button("Predict Yield"):

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