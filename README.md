# Mushroom Yield Forecasting

## Environment Setup

This repository features a fully reproducible and isolated Python virtual environment (`.venv`) to ensure dependency stability across data science workflows.

### Core Prerequisites
* Windows OS
* Python 3.11.x

### Activation & Execution Steps
Run the following steps sequentially inside your VS Code PowerShell terminal to initialize the environment and run the workspace validation check:

1. **Verify Environment Packages:**
   Check the installed dependency tree to ensure the data science stack compiled correctly:
   ```powershell
   .\.venv\Scripts\python.exe -m pip list

## Task 4: Feature Engineering & Temporal Train/Test Split

### Features and Target

* Features (X): Temperature, Humidity, CO2
* Target (y): Yield

### Temporal Train/Test Split

* Train Rows: 79

* Train Period: 2026-06-01 00:00:00 to 2026-06-04 07:00:00

* Test Rows: 20

* Test Period: 2026-06-04 08:00:00 to 2026-06-05 03:00:00

### Feature Scaling

* MinMaxScaler was used for feature scaling.
* The scaler was fitted only on the training dataset and then applied to the testing dataset.
* This prevents data leakage from the test set.

### Saved Artifact

* `models/scaler.joblib`

## Run Inference

### Test Prediction Module

Run the prediction script directly from the project root:

```powershell
python src/predict.py
```

Example output:

```text
Predicted Yield: 3.31 kg
```

### Launch Streamlit Application

Start the Streamlit app:

```powershell
streamlit run app.py
```

This will open the Mushroom Yield Forecast App in your browser, where users can enter Temperature, Humidity, and CO₂ values to obtain a mushroom yield prediction.

## Reproducibility

### Python Version

* Python 3.11

### Random Seeds

* Train/Test Split: `random_state=42`
* Random Forest Regressor: `random_state=42`

### Saved Artifacts

* `models/champion.joblib`
* `models/scaler.joblib`
* `models/features.json`

### Dependencies

All package versions used for this project are pinned in:

```text
requirements.txt
```
## Application Screenshots

### Dashboard

![Dashboard](<docs/screenshots/Screenshot 2026-06-23 120832.png>)

### Prediction Results

![Result](<docs/screenshots/Screenshot 2026-06-23 120857.png>)

### Sensitivity Analysis

![Sensitivity Analysis](<docs/screenshots/Screenshot 2026-06-23 120915.png>)