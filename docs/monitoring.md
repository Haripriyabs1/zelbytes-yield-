# Monitoring Plan

## Prediction Logging

The application will maintain lightweight logs of prediction requests.

### Logged Fields

* Timestamp
* Temperature (°C)
* Humidity (%)
* CO₂ (ppm)
* Predicted Yield (kg)

### Sample Log Entry

timestamp,temp,humidity,co2,prediction

2026-06-23 11:30:00,25,85,700,3.31

---

## Retraining Triggers

The model should be retrained when:

1. One month has passed since the previous training cycle.
2. More than 500 new prediction records have been collected.
3. Model performance degrades significantly.
4. Environmental conditions differ substantially from the original training data.

---

## Monitoring Objectives

* Detect prediction drift.
* Track model usage.
* Identify unusual sensor values.
* Maintain prediction accuracy.
