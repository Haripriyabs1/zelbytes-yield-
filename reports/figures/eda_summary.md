# EDA Summary

## Dataset Overview

* Dataset contains 99 observations and 5 columns.
* Date range: 2026-06-01 00:00:00 to 2026-06-05 03:00:00.
* Features analyzed: temperature, humidity, CO₂ concentration, and mushroom yield.

## Data Quality Report

* No missing values were present after data cleaning.
* Humidity values were within the expected range of 0–100%.
* No negative yield values were observed.
* Temperature and CO₂ values appeared reasonable with no obvious outliers or invalid measurements.

## Summary Statistics

* Average temperature: 24.80°C
* Average humidity: 87.39%
* Average CO₂ concentration: 909.33 ppm
* Average yield: 2.65 kg

## Correlation Analysis

* Temperature showed a weak positive correlation with yield (0.056).
* Humidity showed a weak negative correlation with yield (-0.073).
* CO₂ showed a weak negative correlation with yield (-0.043).
* No strong linear relationships were observed.

## Scatter Plot Insights

* Temperature vs Yield showed no clear linear trend.
* Humidity vs Yield showed substantial variation in yield across humidity levels.
* CO₂ vs Yield showed no strong relationship with yield.

## Biological Interpretation

* Mushroom yield is influenced by environmental conditions such as humidity and CO₂ concentration.
* In this dataset, humidity and CO₂ did not exhibit strong linear relationships with yield.
* Yield may depend on interactions among multiple environmental variables rather than a single factor.

## Modeling Implications

* Weak correlations suggest that simple linear models may have limited predictive power.
* Additional features or more advanced machine learning models may be required to improve yield prediction.
