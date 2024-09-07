# 3. Orchestration and ML Pipelines

## 3.0 Introduction: ML pipelines and Mage

- What is MLOps
- Why we need to operationalize ML
- How Mage helps MLOps
- Example data pipeline

## 3.1 Data preparation: ETL and feature engineering

- Ingest raw data
- Prepare data for training
- Build training sets
- Data validations using built-in testing framework

## 3.2 Training: sklearn models and XGBoost

- Reusable training set data product
- Training pipeline for sklearn models
- Training pipeline for XGBoost
- Tracking training metrics with experiments

## 3.3 Observability: Monitoring and alerting

- Dashboard for sklearn training pipeline health
- Dashboard for XGBoost model explainability
- Dashboard for model training performance
- Alerts for pipeline runs

## 3.4 Triggering: Inference and retraining

- Automatic retraining pipeline
- No-code UI input fields to interact with models
- Inference pipeline for real-time predictions

## 3.5 Deploying: Running operations in production

- Setup AWS permissions and credentials
- Terraform setup
- Initial deployment to AWS
- Use GitHub Actions for CI/CD to automate deployment to production

## Quickstart
# Setup

1. Change directory into the cloned repo:

 ```
   git clone https://github.com/mage-ai/mlops.git

   cd mlops
 ```

- docker network create app-network
- docker-compose build


1. Launch Mage and the database service (PostgreSQL):

```bash
cat ~/.bash_profile

export SMTP_EMAIL="your_email@gmail"
export SMTP_PASSWORD="Password1@"
```

```
./scripts/start.sh

```
**after changes to docker-compose.yaml file**
- docker-compose up -d 

1. Open [`http://localhost:6789`](http://localhost:6789) in your browser.


### CLI for Postgres

Installing `pgcli`

```bash
pip install pgcli
```

If you have problems installing `pgcli` with the command above, try this:

```bash
conda install -c conda-forge pgcli
pip install -U mycli
```

Using `pgcli` to connect to Postgres

```bash
pgcli -h localhost -p 5432 -u root -d magic
```


io.config

GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/clear-router-390022-c9dc0b907401.json"

GOOGLE_LOCATION: US # Optional


dev:
  # PostgresSQL
  POSTGRES_CONNECT_TIMEOUT: 10
  POSTGRES_DB: "{{ env_var('POSTGRES_DB')}}"
  POSTGRES_SCHEMA: "{{ env_var('POSTGRES_SCHEMA')}}" # Optional
  POSTGRES_USER: "{{ env_var('POSTGRES_USER')}}"
  POSTGRES_PASSWORD: "{{ env_var('POSTGRES_PASSWORD')}}"
  POSTGRES_HOST: "{{ env_var('POSTGRES_HOST')}}"
  POSTGRES_PORT: "{{ env_var('POSTGRES_PORT')}}"

<!-- The exampe uses AWS to host a remote server. In order to run the example you'll need an AWS account. Follow the steps described in the file `mlflow_on_aws.md` to create a new AWS account and launch the tracking server. 

Starting the MLflow server with S3: -->

```bash
#local
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlruns

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000

mlflow server --backend-store-uri postgresql+psycopg2://postgres:postgres@postgres:5432/postgres --default-artifact-root ./mlruns-postgres --host 0.0.0.0 --port 5000

#cloud s3 and Postgres
mlflow server \
    --backend-store-uri postgresql://postgres:postgres@postgres:5432/postgres \
    --default-artifact-root s3://mlflow-models-aham/

#postgresql://root:root@localhost:5432/magic

mlflow server --backend-store-uri postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB} --default-artifact-root s3://mlflow-models-aham/ --host 0.0.0.0 --port 5000
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

# PRODUCTION

- Consider AWS Elastic Beanstalk to deploy the application in docker container, to take advantage of platform as a service, autoscaling and load balancing, as well as cdn

- or GCP Cloud Run or App Engine

- AWS RDS (PostgreSQL) to deploy Database
- AWS Aurora to take advantage of horizontally scaling and global availability

- or GCP Cloud SQL or Cloud Spanner

- AWS S3 to store artifacts and data lake

- or GCP Cloud Storage

