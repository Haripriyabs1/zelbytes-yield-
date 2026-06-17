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
