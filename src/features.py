import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
def prepare_features():
    df=pd.read_parquet("../data/processed/02_cleaned.parquet")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df=df.sort_values("timestamp")
    x=df[[ "temperature", "humidity", "CO2" ]]
    y=df["yield"]
    split_point = int(len(df) * 0.8)
    train_data = df.iloc[:split_point]
    test_data = df.iloc[split_point:]
    X_train = train_data[["temperature", "humidity", "CO2"]]
    y_train = train_data["yield"]
    X_test = test_data[["temperature", "humidity", "CO2"]]
    y_test = test_data["yield"]
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(
        scaler,
        "../models/scaler.joblib"
    )
    print("\n=== Split Summary ===")

    print(f"Train Rows: {len(train_data)}")
    print(
        f"Train Period: {train_data['timestamp'].min()} "
        f"to {train_data['timestamp'].max()}"
    )

    print(f"\nTest Rows: {len(test_data)}")
    print(
        f"Test Period: {test_data['timestamp'].min()} "
        f"to {test_data['timestamp'].max()}"
    )
    return X_train_scaled, X_test_scaled, y_train, y_test, X_test
if __name__ == "__main__":
    prepare_features()