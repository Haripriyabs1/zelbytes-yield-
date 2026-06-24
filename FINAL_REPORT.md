# Capstone Project Report

## 1. Problem Statement

We aim to predict agricultural yield using environmental and soil sensor data such as temperature, humidity, rainfall, and other relevant factors.

Accurate yield prediction helps in improving farm planning, reducing waste, and supporting better decision-making in agritech systems.

## 2. Data Description

The dataset contains agricultural and environmental sensor readings used for yield prediction.

Key features include:
- Temperature (°C)
- Humidity (%)
- Rainfall (mm)
- Soil-related parameters (if available)

The data was cleaned by handling missing values and ensuring consistent formatting before model training.

## 3. Data Cleaning & Exploratory Data Analysis

The dataset was preprocessed to ensure quality and consistency before model training.

### Data Cleaning:
- Handled missing values using appropriate imputation techniques
- Ensured consistent data types across all features
- Removed or treated invalid/outlier values where necessary

### Exploratory Data Analysis (EDA):
- Analyzed distribution of key features such as temperature, humidity, and rainfall
- Identified relationships between environmental factors and yield
- Observed seasonal and environmental patterns affecting crop yield
- Used visualizations to understand feature correlations and trends

## 4. Modeling Approach & Evaluation

We experimented with multiple machine learning models for yield prediction, including Linear Regression and ensemble-based methods.

To ensure realistic evaluation, we used a temporal split instead of random splitting. This prevents data leakage by making sure future data is not used to predict past outcomes.

Model performance was evaluated using Mean Absolute Error (MAE), which measures the average absolute difference between predicted and actual values in the same units as the target variable.

The final model was selected based on the lowest validation MAE and generalization performance on unseen data.

## 5. Deployment

The model is deployed using Streamlit Community Cloud.

The trained machine learning pipeline is loaded at runtime and used to generate real-time predictions based on user input.

Live Deployment URL: <https://zelbytes-yield-bsharipriya.streamlit.app/>

## 6. Monitoring & Logging

The system implements lightweight logging to track prediction requests.

Each log entry includes:
- Timestamp
- Input feature values
- Model prediction output

This helps in monitoring model behavior over time and identifying potential data drift due to environmental or seasonal changes.

Retraining is planned when a noticeable drop in performance is observed or when input data distribution shifts significantly.

## 7. Limitations

- Dataset size is limited, which may affect generalization
- Sensor readings may contain noise or calibration errors
- Model does not account for all external environmental factors
- No real-time external validation system is integrated

## 8. Future Work

- Improve model performance using advanced algorithms such as XGBoost or neural networks
- Integrate real-time sensor data for live prediction updates
- Expand dataset with more regions and seasonal variations
- Add alert systems for abnormal or high-risk predictions

## 🚀 Live Demo
Streamlit App: <https://zelbytes-yield-bsharipriya.streamlit.app/>

## 🧠 Model Info
Pipeline-based ML model trained on agricultural sensor data.

## 🧪 Run Locally
streamlit run app.py