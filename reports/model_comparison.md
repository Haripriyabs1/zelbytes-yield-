# Model Comparison Report

## Objective

The objective of this task was to compare Linear Regression, Default Random Forest, and Tuned Random Forest models for mushroom yield forecasting and select a champion model for deployment.

## Model Performance

### Linear Regression

Cross-Validation MAE: 1.1911

Test MAE: 1.5509

Test RMSE: 1.6258

Test R²: 0.0126

Interpretability: High. The model coefficients clearly indicate how each environmental variable affects mushroom yield, making the model easy to understand and explain.

### Random Forest (Default)

Cross-Validation MAE: 1.2086

Test MAE: 1.4933

Test RMSE: 1.6338

Test R²: 0.0028

Interpretability: Medium. Feature importance values provide insight into influential variables, but individual predictions are more difficult to explain than Linear Regression.

### Random Forest (Tuned)

Cross-Validation MAE: 1.1699

Test MAE: 1.5056

Test RMSE: 1.6141

Test R²: 0.0267

Interpretability: Medium. Hyperparameter tuning improved model generalization while retaining the ability to analyze feature importance.

## Training Time

Tuned Random Forest (GridSearchCV): 7.4077 seconds

The additional training time was due to GridSearchCV evaluating multiple hyperparameter combinations using TimeSeriesSplit cross-validation.

## Champion Model

The Tuned Random Forest model was selected as the champion model for deployment.

## Justification

The Tuned Random Forest achieved the best cross-validation MAE (1.1699), indicating the strongest validation performance among all evaluated models. It also achieved the lowest RMSE (1.6141) and the highest R² score (0.0267) on the test set.

Although the Default Random Forest achieved a slightly lower Test MAE (1.4933), the difference was very small. The Tuned Random Forest demonstrated a better balance between validation performance and generalization ability, making it the preferred model for deployment.

The selected champion model was saved as `models/champion.joblib`.

## Predicted vs Actual Visualization

A predicted-versus-actual yield plot was generated for the champion model and saved as:

`reports/figures/champion_pred_vs_actual.png`

This visualization helps assess how closely the model predictions match the true mushroom yield values on the test set.

## Agritech Metric Considerations

In mushroom farming, prediction errors can affect operational planning and resource allocation.

- Underestimating yield may lead to insufficient labor allocation, harvesting preparation, and supply planning.
- Overestimating yield may result in unmet buyer expectations, wasted resources, and inaccurate production forecasts.

Therefore, the model should be used as a decision-support tool rather than a source of exact yield predictions.

## Known Limitations

- The dataset contains only temperature, humidity, and CO₂ measurements.
- The dataset is relatively small, limiting model generalization.
- Additional environmental and biological factors may improve predictive performance.
- The model may not generalize well to conditions outside the observed data range.
- Predictions should complement grower expertise rather than replace it.

## Conclusion

Three machine learning models were evaluated for mushroom yield forecasting: Linear Regression, Default Random Forest, and Tuned Random Forest.

Hyperparameter tuning was performed using GridSearchCV with TimeSeriesSplit cross-validation. The Tuned Random Forest achieved the best cross-validation performance, the lowest RMSE, and the highest R² score among the evaluated models.

Based on these results, the Tuned Random Forest was selected as the champion model and saved as `champion.joblib` for future deployment and integration into downstream applications such as Streamlit.

