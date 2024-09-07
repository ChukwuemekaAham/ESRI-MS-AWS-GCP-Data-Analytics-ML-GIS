import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# from mage_ai.data_preparation.decorators import data_preparation_step
# from mage_ai.data_preparation.sources.google_cloud_storage import GoogleCloudStorage
# from mage_ai.io.config import ConfigFileLoader
# from mage_ai.shared.utils import get_repo_path
# from os import path
# import io

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def train_and_log_model(data, *args, **kwargs):
    
    X_train = np.array(data['X_train'])
    X_test = np.array(data['X_test'])
    y_train = np.array(data['y_train'])
    y_test = np.array(data['y_test'])

    RAND_FRST_EXPERIMENT_NAME = "gold_price_prediction"

    MLFLOW_TRACKING_URI = "http://0.0.0.0:5000" #locally

    try:
        mlflow.set_experiment(RAND_FRST_EXPERIMENT_NAME)
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

        mlflow.start_run()

        params = dict(max_depth=20, n_estimators=100, min_samples_leaf=10, random_state=42)

        model = RandomForestRegressor(**params)

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred) #Measures how well the model explains the variance in the data.

        # Log the model and metrics
        mlflow.log_metrics({"mse": mse, "r2": r2})

        # Log model
        model_path = 'random_forest_model'
        mlflow.sklearn.log_model(model, model_path)

        # Calculate and log feature importances
        importances = model.feature_importances_  # Get feature importances
        features = ['Open', 'High', 'Low']  # Assuming these are your feature names
        for i, feature in enumerate(features):
            mlflow.log_param(f"feature_{i}_importance", importances[i])


        # # Verify if the MLmodel file exists
        # model_uri = mlflow.get_artifact_uri(model_path)
        # model_local_dir = model_uri.replace("file://", "")
        # mlmodel_file_path = os.path.join(model_local_dir, "MLmodel")
        
        # if not os.path.exists(mlmodel_file_path):
        #     raise FileNotFoundError(f"Could not find MLmodel file at {mlmodel_file_path}")

        # model_file_path = os.path.join(model_local_dir, "model.pkl")

        # # Upload to GCS
        # config_path = path.join(get_repo_path(), 'io_config.yaml')
        # config_profile = 'default'  # Adjust if you have different profiles
        # bucket_name = 'mlops-proj-bucket_clear-router-390022' 
        # object_key = 'models/random_forest_model/model.pkl' 

        # gcs = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile))
        # gcs.save(
        #     model_file_path,
        #     bucket_name,
        #     object_key,
        # )

        # print(f"Model exported to Google Cloud Storage: {object_key} in bucket {bucket_name}")

        return {
                'model_path': mlflow.get_artifact_uri(model_path)
            }
    finally:
        mlflow.end_run()

    