import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import (
    TimeSeriesSplit,
    cross_val_score
)
from sklearn.linear_model import LinearRegression
df = pd.read_parquet("../data/processed/02_cleaned.parquet")
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")
X = df[["temperature","humidity","CO2"]]
y = df["yield"]
split_point = int(len(df) * 0.8)
X_train = X.iloc[:split_point]
X_test = X.iloc[split_point:]
y_train = y.iloc[:split_point]
y_test = y.iloc[split_point:]
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
y_train_pred = rf.predict(X_train)
y_test_pred = rf.predict(X_test)
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
train_rmse = root_mean_squared_error(y_train, y_train_pred)
test_rmse = root_mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
print(f"Train MAE: {train_mae:.4f}")
print(f"Test MAE: {test_mae:.4f}")
print(f"Train RMSE: {train_rmse:.4f}")
print(f"Test RMSE: {test_rmse:.4f}")
print(f"Train R²: {train_r2:.4f}")
print(f"Test R²: {test_r2:.4f}")
mae_gap = test_mae - train_mae
print(f"MAE Gap: {mae_gap:.4f}")
if test_mae > train_mae * 1.5:
    print("Potential overfitting detected.")
else:
    print("No strong signs of overfitting.")
print("\nFeature Importances:")
importances = rf.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"{feature}: {importance:.4f}")
most_important_feature = X.columns[
    importances.argmax()
]
print(
    f"\nMost Important Feature: "
    f"{most_important_feature}"
)
plt.figure(figsize=(6,4))
plt.bar(X.columns, importances)
plt.title("Random Forest Feature Importances")
plt.ylabel("Importance")
plt.tight_layout()
plt.savefig(
    "../reports/figures/rf_feature_importance.png"
)
plt.show()
joblib.dump(
    rf,
    "../models/random_forest.joblib"
)
print("Model saved successfully.")
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_mae = mean_absolute_error(y_test, lr_pred)
lr_rmse = root_mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)
comparison = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MAE": [lr_mae, test_mae],
    "RMSE": [lr_rmse, test_rmse],
    "R2": [lr_r2, test_r2]
})
print(comparison)
comparison.to_csv(
    "../reports/model_comparison.csv",
    index=False
)
tscv = TimeSeriesSplit(n_splits=3)
rf_cv_scores = -cross_val_score(
    rf,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error",
    n_jobs=-1
)
lr_cv_scores = -cross_val_score(
    lr,
    X_train,
    y_train,
    cv=tscv,
    scoring="neg_mean_absolute_error"
)
print(
    f"RF CV MAE: {rf_cv_scores.mean():.4f}"
)

print(
    f"LR CV MAE: {lr_cv_scores.mean():.4f}"
)
plt.figure(figsize=(6,4))
plt.bar(
    ["Linear Regression","Random Forest"],
    [
        lr_cv_scores.mean(),
        rf_cv_scores.mean()
    ]
)
plt.ylabel("CV MAE")
plt.title("Cross Validation Comparison")
plt.tight_layout()
plt.savefig(
    "../reports/figures/cv_comparison.png"
)
plt.show()
print(
        f"RF CV Std: {rf_cv_scores.std():.4f}"
    )
print(
        f"LR CV Std: {lr_cv_scores.std():.4f}"
    )
with open(
    "../reports/cv_results.md",
    "w"
) as f:
    f.write("# TimeSeriesSplit Results\n\n")
    f.write(
    f"RF Fold Scores: "
    f"{rf_cv_scores}\n\n"
    )

    f.write(
        f"LR Fold Scores: "
        f"{lr_cv_scores}\n\n"
    )

    f.write(
        f"Random Forest CV MAE: "
        f"{rf_cv_scores.mean():.4f}\n\n"
    )
    f.write(
        f"Linear Regression CV MAE: "
        f"{lr_cv_scores.mean():.4f}\n\n"
    )
    f.write(
        f"Most Important Feature: "
        f"{most_important_feature}\n\n"
    )
    f.write(
        "Interpretation: Random Forest "
        "relies most heavily on this "
        "feature when predicting "
        "mushroom yield.\n\n"
    )
    f.write(
        f"Train MAE: {train_mae:.4f}\n"
    )
    f.write(
        f"Test MAE: {test_mae:.4f}\n\n"
    )
    if test_mae > train_mae * 1.5:
        f.write(
            "Possible overfitting detected. "
            "Test MAE is significantly "
            "higher than Train MAE.\n"
        )
    else:
        f.write(
            "No major overfitting detected. "
            "Train and Test MAE are "
            "reasonably close.\n"
        )
    f.write("\nModel Comparison:\n")
    f.write(
        f"Linear Regression Test MAE: {lr_mae:.4f}\n"
    )
    f.write(
        f"Random Forest Test MAE: {test_mae:.4f}\n"
    )