import pandas as pd
import numpy as np
import json
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import (
    GridSearchCV,
    TimeSeriesSplit
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
df=pd.read_parquet("../data/processed/02_cleaned.parquet")
df["timestamp"]=pd.to_datetime(df["timestamp"])
df=df.sort_values("timestamp")
x=df[["temperature","humidity","CO2"]]
y=df["yield"]
split_point=int(len(df)*0.8)
X_train=x.iloc[:split_point]
y_train=y.iloc[:split_point]
X_test=x.iloc[split_point:]
y_test=y.iloc[split_point:]
tscv = TimeSeriesSplit(n_splits=3)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}
rf = RandomForestRegressor(
    random_state=42
)
search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)
search.fit(X_train, y_train)
print("Best Parameters:")
print(search.best_params_)

print("\nBest CV MAE:")
print(round(-search.best_score_, 4))
best_rf = search.best_estimator_
y_pred = best_rf.predict(X_test)
plt.figure(figsize=(6,4))
plt.scatter(
    y_test,
    y_pred
)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title(
    "Actual vs Predicted Yield"
)
plt.savefig(
    "../reports/figures/champion_pred_vs_actual.png"
)
plt.show()
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)
r2 = r2_score(y_test, y_pred)
print("\nTuned Random Forest Results")

print("Test MAE:", round(mae, 4))
print("Test RMSE:", round(rmse, 4))
print("Test R²:", round(r2, 4))
with open(
    "../models/rf_best_params.json",
    "w"
) as f:
    json.dump(
        search.best_params_,
        f,
        indent=4
    )
joblib.dump(
    best_rf,
    "../models/rf_tuned.joblib"
)
joblib.dump(
    best_rf,
    "../models/champion.joblib"
)
print("Champion model saved successfully!")
results = pd.DataFrame(
    search.cv_results_
)

results.to_csv(
    "../reports/gridsearch_results.csv",
    index=False
)