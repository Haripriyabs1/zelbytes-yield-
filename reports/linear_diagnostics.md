# Linear Regression Diagnostics

## Model Performance

Train RMSE: 1.2567
Test RMSE: 1.6258

Train MAE: 1.0594
Test MAE: 1.5509

Train R²: 0.0003
Test R²: 0.0126

## Residual Analysis

Residuals were plotted against predicted yield and humidity.

The residuals appear scattered around zero with no strong systematic pattern.

Some spread is present, indicating prediction errors remain relatively high.

## Train vs Test Comparison

Test RMSE is higher than Train RMSE.

This suggests the model generalizes slightly worse on unseen data, though severe overfitting is not observed.

## Coefficient Interpretation

Temperature coefficient was slightly negative.

Humidity coefficient was positive.

CO₂ coefficient was positive and had the largest magnitude among the three features.

Since features were scaled using MinMaxScaler, coefficients should be interpreted comparatively rather than as real-world unit changes.

## Recommendation

Linear Regression provides a useful baseline but achieves very low R² values.

A more flexible model such as Random Forest Regressor is recommended for the next stage of experimentation.