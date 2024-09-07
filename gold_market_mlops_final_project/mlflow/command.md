<!-- The exampe uses AWS to host a remote server. In order to run the example you'll need an AWS account. Follow the steps described in the file `mlflow_on_aws.md` to create a new AWS account and launch the tracking server. 

Starting the MLflow server with S3: -->

```bash
#local
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000

mlflow server --backend-store-uri postgresql://postgres:postgres@postgres:5432/postgres --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000

#cloud s3 and Postgres
mlflow server \
    --backend-store-uri postgresql://postgres:postgres@postgres:5432/postgres \
    --default-artifact-root s3://mlflow-models-aham/

#postgresql://root:root@localhost:5432/magic

mlflow server --backend-store-uri postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB} --default-artifact-root s3://mlflow-models-aham/ --host 0.0.0.0 --port 5000
```

## Downloading the artifact from mlflow

```bash
os.environ["AWS_PROFILE"] = "" # fill in with your AWS profile. More info: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-credentials

TRACKING_SERVER_HOST = "" # fill in with the public DNS of the EC2 instance
mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")


export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
export MODEL_RUN_ID="6dd459b11b4e48dc862f4e1019d166f6"

mlflow artifacts download \
    --run-id ${MODEL_RUN_ID} \
    --artifact-path model \
    --dst-path .
```