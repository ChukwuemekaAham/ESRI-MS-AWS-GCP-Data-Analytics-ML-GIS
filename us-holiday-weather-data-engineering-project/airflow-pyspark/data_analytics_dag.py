# [START composer_dataanalytics_dag]
import datetime

from airflow import models
from airflow.providers.google.cloud.operators import dataproc
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)
from airflow.utils.task_group import TaskGroup

PROJECT_NAME = "{{var.value.gcp_project}}"

# BigQuery configs
BQ_DESTINATION_DATASET_NAME = "holiday_weather"
BQ_DESTINATION_TABLE_NAME = "holidays_weather_joined"
BQ_NORMALIZED_TABLE_NAME = "holidays_weather_normalized"

# Dataproc configs
BUCKET_NAME = "{{var.value.gcs_bucket}}"
PROCESSING_PYTHON_FILE = f"gs://{BUCKET_NAME}/data_analytics_process.py"

BATCH_ID = "data-processing-{{ ts_nodash | lower}}"  # Dataproc serverless only allows lowercase characters
BATCH_CONFIG = {
    "runtime_config": {"version": "1.1"},
    "pyspark_batch": {
        "main_python_file_uri": PROCESSING_PYTHON_FILE,
        "args": [
            BUCKET_NAME,
            f"{BQ_DESTINATION_DATASET_NAME}.{BQ_DESTINATION_TABLE_NAME}",
            f"{BQ_DESTINATION_DATASET_NAME}.{BQ_NORMALIZED_TABLE_NAME}",
        ],
    },
    "environment_config": {
        "execution_config": {
            "service_account": "{{var.value.dataproc_service_account}}"
        }
    },
}

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1), datetime.datetime.min.time()
)

default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    "start_date": yesterday,
    # To email on failure or retry set 'email' arg to your email and enable
    # emailing here.
    "email_on_failure": False,
    "email_on_retry": False,
}

with models.DAG(
    "data_analytics_dag",
    # Continue to run DAG once per day
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args,
) as dag:
    create_batch = dataproc.DataprocCreateBatchOperator(
        task_id="create_batch",
        project_id=PROJECT_NAME,
        region="{{ var.value.gce_region }}",
        batch=BATCH_CONFIG,
        batch_id=BATCH_ID,
    )
    # This data is static and it is safe to use WRITE_TRUNCATE
    # to reduce chance of 409 duplicate errors
    load_external_dataset = GCSToBigQueryOperator(
        task_id="run_bq_external_ingestion",
        bucket=BUCKET_NAME,
        source_objects=["holidays.csv"],
        destination_project_dataset_table=f"{BQ_DESTINATION_DATASET_NAME}.holidays",
        source_format="CSV",
        schema_fields=[
            {"name": "Date", "type": "DATE"},
            {"name": "Holiday", "type": "STRING"},
        ],
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
    )

    with TaskGroup("join_bq_datasets") as bq_join_group:
        for year in range(1997, 2022):
            # BigQuery configs
            BQ_DATASET_NAME = f"bigquery-public-data.ghcn_d.ghcnd_{str(year)}"
            BQ_DESTINATION_TABLE_NAME = "holidays_weather_joined"
            # Specifically query a Chicago weather station
            WEATHER_HOLIDAYS_JOIN_QUERY = f"""
            SELECT Holidays.Date, Holiday, id, element, value
            FROM `{PROJECT_NAME}.holiday_weather.holidays` AS Holidays
            JOIN (SELECT id, date, element, value FROM {BQ_DATASET_NAME} AS Table WHERE Table.element="TMAX" AND Table.id="USW00094846") AS Weather
            ON Holidays.Date = Weather.Date;
            """

            # for demo purposes we are using WRITE_APPEND
            # but if you run the DAG repeatedly it will continue to append
            # Your use case may be different, see the Job docs
            # https://cloud.google.com/bigquery/docs/reference/rest/v2/Job
            # for alternative values for the writeDisposition
            # or consider using partitioned tables
            # https://cloud.google.com/bigquery/docs/partitioned-tables
            bq_join_holidays_weather_data = BigQueryInsertJobOperator(
                task_id=f"bq_join_holidays_weather_data_{str(year)}",
                configuration={
                    "query": {
                        "query": WEATHER_HOLIDAYS_JOIN_QUERY,
                        "useLegacySql": False,
                        "destinationTable": {
                            "projectId": PROJECT_NAME,
                            "datasetId": BQ_DESTINATION_DATASET_NAME,
                            "tableId": BQ_DESTINATION_TABLE_NAME,
                        },
                        "writeDisposition": "WRITE_APPEND",
                    }
                },
                location="US",
            )

        load_external_dataset >> bq_join_group >> create_batch
# [END composer_dataanalytics_dag]
