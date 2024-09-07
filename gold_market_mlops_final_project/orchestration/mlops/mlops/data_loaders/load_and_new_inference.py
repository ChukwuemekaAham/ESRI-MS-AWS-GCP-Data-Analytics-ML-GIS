from sklearn.preprocessing import StandardScaler
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_and_preprocess_inference_data(data, 
*args, **kwargs):
    # Load the data
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

    # Select relevant features
    features = df.drop(columns=['Close'])

    # Standardize the data
    scaler = StandardScaler()
    X_inference = scaler.fit_transform(features)

    model_path = data['model_path']

    return {
        'X_inference': X_inference.tolist(),
        'model_path': model_path
    }
