import joblib
import numpy as np
import mlflow
import mlflow.sklearn

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def load_model_and_predict(data, *args, **kwargs):

    X_inference = np.array(data['X_inference'])
    
     # Get the model path from your previous step (train_and_log_model)
    model_path = data['model_path'] 

    # Extract the run ID and model artifact path from the model path
    parts = model_path.split('/') 
    run_id = parts[5]  # Run ID is at index 3
    model_artifact_path = parts[7]  # Artifact path is at index 5

    # Construct the model URI for MLflow
    model_uri = f"runs:/{run_id}/{model_artifact_path}"

    print(model_uri)

    # Load the model using MLflow
    model = mlflow.sklearn.load_model(model_uri)

    # Make predictions
    predictions = model.predict(X_inference)

    return {
        'predictions': predictions.tolist()
    }
