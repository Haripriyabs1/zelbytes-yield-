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