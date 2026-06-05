# Cleaning Log

## Null Counts Before Cleaning

| Column      | Null Count |
|-------------|------------|
| timestamp   |      0     |
| temperature |      1     |
| humidity    |      1     |
| CO2         |      1     |
| yield       |      1     |

## Imputation and Removal Rationale

### Temperature
Missing temperature values were replaced using the mean temperature. In a polyhouse environment, temperature changes gradually and the average provides a reasonable estimate.

### Humidity
Missing humidity values were replaced using the median humidity. The median is less affected by unusual sensor readings.

### CO2
Missing CO2 values were replaced using the median CO2 concentration. This provides a stable estimate when sensor readings are unavailable.

### Yield
Rows with missing yield values were removed. Yield is the final production outcome and should not be artificially estimated.

## Null Counts After Cleaning

| Column      | Null Count |
|-------------|------------|
| timestamp   |      0     |
| temperature |      0     |
| humidity    |      0     |
| CO2         |      0     |
| yield       |      0     |

## Output

Cleaned dataset saved as:

data/processed/02_cleaned.parquet