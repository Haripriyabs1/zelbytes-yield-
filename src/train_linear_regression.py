from features import prepare_features
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score,mean_absolute_error
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import json
X_train_scaled, X_test_scaled, y_train, y_test, X_test = prepare_features()
model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)
train_rmse = root_mean_squared_error(y_train, y_train_pred)
test_rmse = root_mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
print(f"Train RMSE: {train_rmse:.4f}")
print(f"Test RMSE: {test_rmse:.4f}")
print(f"Train R²: {train_r2:.4f}")
print(f"Test R²: {test_r2:.4f}")
print(f"Train MAE: {train_mae:.4f}")
print(f"Test MAE: {test_mae:.4f}")
joblib.dump(
    model,
    "../models/linear_regression.joblib"
)
print("\nModel saved successfully!")
coefficients = pd.DataFrame({
    "Feature": ["temperature", "humidity", "CO2"],
    "Coefficient": model.coef_
})
print("\nCoefficient Table")
print(coefficients)
residuals=y_test - y_test_pred
print("\nResiduals vs Predicted")
plt.figure(figsize=(6,4))
plt.scatter(y_test_pred, residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Predicted Yield")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted")
plt.savefig("../reports/figures/residuals_linear_predicted.png")
plt.close()
print("Saved: residuals_linear_predicted.png")
print("\nResiduals vs Humidity")
plt.figure(figsize=(6,4))
plt.scatter(X_test["humidity"], residuals)
plt.axhline(y=0, linestyle="--")
plt.xlabel("Humidity")
plt.ylabel("Residuals")
plt.title("Residuals vs Humidity")
plt.savefig("../reports/figures/residuals_linear_humidity.png")
plt.close()
print("Saved: residuals_linear_humidity.png")
metrics = {
    "train_rmse": float(train_rmse),
    "test_rmse": float(test_rmse),
    "train_mae": float(train_mae),
    "test_mae": float(test_mae),
    "train_r2": float(train_r2),
    "test_r2": float(test_r2)
}
with open("../reports/linear_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)
print("\nMetrics saved to linear_metrics.json")
print("\nAgritech Interpretation:")
for feature, coef in zip(coefficients["Feature"], coefficients["Coefficient"]):
    direction = "increases" if coef > 0 else "decreases"
    print(
        f"Higher {feature} is associated with {direction} "
        f"mushroom yield when other variables are held constant."
    )