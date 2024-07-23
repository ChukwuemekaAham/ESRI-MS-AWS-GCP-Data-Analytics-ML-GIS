#!/bin/bash

set -x

export GCP_PROJECT_ID=$(gcloud config list --format 'value(core.project)')
export PROJECT_NUMBER=$(gcloud projects describe "${GCP_PROJECT_ID}" --format='get(projectNumber)')
export DATAPROC_SERVICE_ACCOUNT="de-proj-admin@clear-router-390022.iam.gserviceaccount.com"
export INPUT_BUCKET="holiday_weather-${GCP_PROJECT_ID}"
export RESULT_BUCKET="holiday_weather-${GCP_PROJECT_ID}"


export COMPOSER_REGION='us-central1'
export COMPOSER_ZONE_ID='us-central1-a'

export COMPOSER_ENV_NAME='data-pipeline-composer'

