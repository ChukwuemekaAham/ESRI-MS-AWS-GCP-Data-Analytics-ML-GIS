import io
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data(*args, **kwargs):

    # print("Current Working Directory:", os.getcwd())

    # config_path = path.join(get_repo_path(), 'io_config.yaml')
    # config_profile = 'default'

    # bucket_name = 'mlops-proj-bucket_clear-router-390022'
    # object_key = 'gold-ml-2024-09-02.csv'

    # file_content = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(
    #     bucket_name,
    #     object_key,
    # )

    # df = pd.read_csv(io.BytesIO(file_content)) 

    file = './mlops/cleaned_data/gold-ml-2024-09-02.csv'

    gold_dtypes = {
                    'Open': float,
                    'High': float,
                    'Low': float,
                    'Close': float,
                }
    # Load the data
    df = pd.read_csv(file, dtype=gold_dtypes)

    # Feature selection
    features = ['Open', 'High', 'Low']
    target = 'Close'

    # Prepare the data
    X = df[features]
    y = df[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return {
        'X_train': X_train.tolist(),
        'X_test': X_test.tolist(),
        'y_train': y_train.tolist(),
        'y_test': y_test.tolist()
    }

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'