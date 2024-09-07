import pandas as pd

def fill_in_missing_values(taxi_df: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values for relevant columns
    taxi_df['pickup_location_id'].fillna(0, inplace=True)  # Assuming 0 is a default value
    taxi_df['dropoff_location_id'].fillna(0, inplace=True)
    taxi_df['fare_amount'].fillna(taxi_df['fare_amount'].mean(), inplace=True)  # Use mean for fare
    taxi_df['payment_type'].fillna('Unknown', inplace=True)  # Default for payment type

    return taxi_df

if __name__ == "__main__":
    # Example usage (if needed for testing)
    taxi_df = pd.DataFrame({
        'pickup_location_id': [1, None, 3, 4],
        'dropoff_location_id': [None, 2, 3, 4],
        'fare_amount': [10.5, None, 15.0, 12.0],
        'payment_type': ['Credit Card', None, 'Cash', 'Credit Card']
    })

    cleaned_taxi_df = fill_in_missing_values(taxi_df)
    print(cleaned_taxi_df)