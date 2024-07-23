



GCS_BUCKET_NAME="holiday_weather-clear-router-390022"  # Replace this with your bucket name

gsutil -m cp -r airflow-pyspark/* gs://$GCS_BUCKET_NAME/
echo "Code uploaded to GCS bucket: $GCS_BUCKET_NAME"
