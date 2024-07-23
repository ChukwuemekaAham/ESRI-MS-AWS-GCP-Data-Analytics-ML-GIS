
gcloud composer environments create $COMPOSER_ENV_NAME \
    --location $COMPOSER_REGION \
    --zone $COMPOSER_ZONE_ID \
    --python-version 3 \
    --image-version composer-1.20.12-airflow-2.4.3
