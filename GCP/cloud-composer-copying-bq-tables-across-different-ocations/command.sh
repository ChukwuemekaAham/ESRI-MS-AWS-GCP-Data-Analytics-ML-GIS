DAGS_BUCKET=us-east1-composer-advanced--3598410a-bucket

gcloud composer environments run composer-advanced-lab \
--location us-east1 variables -- \
set table_list_file_path /home/airflow/gcs/dags/bq_copy_eu_to_us_sample.csv

gcloud composer environments run composer-advanced-lab \
--location us-east1 variables -- \
set gcs_source_bucket data-lake-21cb86aea6ae-us

gcloud composer environments run composer-advanced-lab \
--location us-east1 variables -- \
set gcs_dest_bucket data-lake-21cb86aea6ae-eu