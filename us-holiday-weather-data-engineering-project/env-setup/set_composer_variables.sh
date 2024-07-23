COMPOSER_VAR_FILE=composer_variables.json
if [ ! -f "${COMPOSER_VAR_FILE}" ]; then
    echo "Generate composer variable file ${COMPOSER_VAR_FILE}."
    envsubst < composer_variables.template > ${COMPOSER_VAR_FILE}
fi

gcloud composer environments storage data import \
--environment ${COMPOSER_ENV_NAME} \
--location ${COMPOSER_REGION} \
--source ${COMPOSER_VAR_FILE}

gcloud composer environments run \
${COMPOSER_ENV_NAME} \
--location ${COMPOSER_REGION} \
variables import -- /home/airflow/gcs/data/${COMPOSER_VAR_FILE}
