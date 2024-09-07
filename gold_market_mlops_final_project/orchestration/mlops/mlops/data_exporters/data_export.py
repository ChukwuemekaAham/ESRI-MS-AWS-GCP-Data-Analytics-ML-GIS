
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import pandas as pd
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_predictions(data, *args, **kwargs):
    now = kwargs.get("execution_date")

    now = (now.strftime("%Y-%m-%d"))

    predictions = data['predictions']
    
    # Create a DataFrame from predictions
    df = pd.DataFrame(predictions, columns=['Predictions'])
    
    # Save DataFrame to a CSV file
    csv_path = f'./tmp/{now}-predictions.csv'
    
    df.to_csv(csv_path, index=False)


    # config_path = path.join(get_repo_path(), 'io_config.yaml')
    # config_profile = 'default'

    # bucket_name = 'mlops-proj-bucket_clear-router-390022'
    # object_key = 'predictions.csv'

    # GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    # )
    
    # print(f"Predictions exported to Google Cloud Storage: {object_key} in bucket {bucket_name}")
