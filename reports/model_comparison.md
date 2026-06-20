# Model Comparison Report

## Objective

The objective of this task was to compare Linear Regression, Default Random Forest, and Tuned Random Forest models for mushroom yield forecasting and select a champion model for deployment.

## Model Performance

### Linear Regression

Cross-Validation MAE: 1.1911

Test MAE: 1.5509

Test RMSE: 1.6258

Test R²: 0.0126

Interpretability: High. The model coefficients clearly indicate how each environmental variable affects mushroom yield, making the model easy to explain and understand.

### Random Forest (Default)

Cross-Validation MAE: 1.2086

Test MAE: 1.4933

Test RMSE: 1.6338

Test R²: 0.0028

Interpretability: Medium. Feature importance values provide insight into influential variables, but individual predictions are more difficult to explain compared to Linear Regression.

### Random Forest (Tuned)

Cross-Validation MAE: 1.1699

Test MAE: 1.5056

Test RMSE: 1.6141

Test R²: 0.0267

Interpretability: Medium. The model remains less transparent than Linear Regression but still provides useful feature importance information. Hyperparameter tuning improved overall generalization performance.

## Champion Model

The Tuned Random Forest model was selected as the champion model for deployment.

## Justification

The Tuned Random Forest achieved the best cross-validation MAE of 1.1699, indicating the strongest validation performance among the evaluated models. It also achieved the lowest RMSE of 1.6141 and the highest R² score of 0.0267 on the test set.

Although the Default Random Forest achieved a slightly lower Test MAE of 1.4933 compared to 1.5056 for the Tuned Random Forest, the difference was very small. The Tuned Random Forest demonstrated better overall balance between validation performance, generalization ability, and predictive accuracy. Therefore, it was selected as the champion model.

## Agritech Metric Considerations

In mushroom farming, prediction errors can affect operational planning. Underestimating yield may lead to insufficient labor allocation, harvesting preparation, and supply planning. Overestimating yield may result in unmet buyer expectations and inefficient resource management.

For this reason, the model should be used as a decision-support tool that assists growers in planning rather than as a source of exact yield forecasts.

## Known Limitations

* The dataset contains only temperature, humidity, and CO₂ measurements.
* The dataset is relatively small, which limits the model's ability to generalize.
* Additional environmental and biological factors may influence mushroom yield but are not included in the dataset.
* Model performance may decrease when applied to conditions outside the observed data range.
* Predictions should complement grower expertise rather than replace it.

## Conclusion

Three machine learning models were evaluated for mushroom yield forecasting: Linear Regression, Default Random Forest, and Tuned Random Forest. Hyperparameter tuning was performed using GridSearchCV with TimeSeriesSplit cross-validation. Based on cross-validation performance, RMSE, and R² scores, the Tuned Random Forest model provided the best overall balance between predictive performance and generalization. The model was therefore selected as the project's champion model and saved as `champion.joblib` for future deployment and integration.

