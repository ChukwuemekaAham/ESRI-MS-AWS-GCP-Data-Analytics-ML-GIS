import pandas as pd
import matplotlib.pyplot as plt

def analyze_missing_values(taxi_df: pd.DataFrame):
    number_of_rows = len(taxi_df.index)
    columns_with_missing_values = []
    percentage_of_missing_values = []

    for col in taxi_df.columns:
        missing = taxi_df[col].isna().sum()
        if missing > 0:
            columns_with_missing_values.append(col)
            percentage_of_missing_values.append(100 * missing / number_of_rows)

    # Create a DataFrame for visualization
    missing_data_summary = pd.DataFrame({
        'Column': columns_with_missing_values,
        'Percentage Missing': percentage_of_missing_values
    })

    # Plotting the missing values
    plt.figure(figsize=(10, 5))
    plt.bar(missing_data_summary['Column'], missing_data_summary['Percentage Missing'])
    plt.title('Percentage of Missing Values in Taxi Data')
    plt.xlabel('Columns')
    plt.ylabel('Percentage of Missing Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage (if needed for testing)
    taxi_df = pd.DataFrame({
        'pickup_location_id': [1, None, 3, 4],
        'dropoff_location_id': [None, 2, 3, 4],
        'fare_amount': [10.5, None, 15.0, 12.0],
        'payment_type': ['Credit Card', None, 'Cash', 'Credit Card']
    })

    analyze_missing_values(taxi_df)