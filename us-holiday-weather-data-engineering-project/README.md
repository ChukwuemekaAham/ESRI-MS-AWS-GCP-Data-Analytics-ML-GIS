# Overview

This project shows how to use Cloud Composer to create an Apache Airflow DAG (workflow). 
The DAG joins data from a BigQuery public dataset and a CSV file stored in a Cloud Storage 
bucket and then runs a Dataproc Serverless batch job to process the joined data.

The BigQuery public dataset in this project is ghcn_d, an integrated database of climate 
summaries across the globe. The CSV file contains information about the dates and names of 
US holidays from 1997 to 2021.

## The question we want to answer using the DAG is: 

- "How warm was it in Chicago on Thanksgiving for the past 25 years?"

### Objectives
•	Create a Cloud Composer environment in the default configuration
•	Create an empty BigQuery dataset
•	Create a new Cloud Storage bucket
•	Create and run a DAG that includes the following tasks:
•	Load an external dataset from Cloud Storage to BigQuery
•	Join two datasets in BigQuery
•	Run a data analytics PySpark job
•	Clean up the project

# Setup

1.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
Note: If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
Go to project selector
2.	Make sure that billing is enabled for your Google Cloud project.
3.	Enable the Dataproc, Composer, BigQuery, Storage APIs.
Enable the APIs

**Enable the Dataproc, Composer, BigQuery, Storage APIs.**

Grant the following roles to manage Cloud Composer environments and environment buckets:

- Composer > Environment and Storage Object Administrator
- IAM > Service Account User

Grant the following role to create a BigQuery dataset
- BigQuery > Data Owner

Grant the following role to create a Cloud Storage bucket:
- Storage > Admin

**Create and prepare your Cloud Composer environment**

To create a Cloud Composer environment:
- Choose a US based compute region
- Choose the latest Cloud Composer version

**Grant the following roles to the service account used in your Cloud Composer environment in order for the Airflow workers to successfully run DAG tasks**

- BigQuery User
- BigQuery Data Owner
- Service Account User
- Dataproc Editor
- Dataproc Worker

**Note:** The BigQuery portion must run in the US multiregion. It is recommended to shoose a US region for your Cloud Composer environment to reduce cost and latency, but the demo will still run if your Cloud Composer environment is in another region.

**Create related resources**
Caution: The empty BigQuery dataset must be located in the US region to satisfy colocation requirements for transferring the BigQuery public dataset ghcn_d.

Create an empty BigQuery dataset with the following parameters
- Name: holiday_weather
- Region: US

Create a new Cloud Storage bucket in the US multiregion

Run the following command to enable private Google access on the default subnet in the region where you would like to run Dataproc Serverless to fulfill networking requirements. We recommend using the same region as your Cloud Composer environment.

```bash
gcloud compute networks subnets update default \
    --region DATAPROC_SERVERLESS_REGION \
    --enable-private-ip-google-access

gcloud compute networks subnets update default \
    --region us-central1 \
    --enable-private-ip-google-access
```
Welcome to Cloud Shell! Type "help" to get started.
Your Cloud Platform project in this session is set to clear-router-390022.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ gcloud compute networks subnets update default \
    --region us-central1 \
    --enable-private-ip-google-access
API [compute.googleapis.com] not enabled on project [clear-router-390022]. Would you like to enable and retry (this will take a few minutes)? (y/N)?  y

Enabling service [compute.googleapis.com] on project [clear-router-390022]...
Operation "operations/acf.p2-583662008298-897cca60-b966-4604-8b78-700bf63a662a" finished successfully.
Updated [https://www.googleapis.com/compute/v1/projects/clear-router-390022/regions/us-central1/subnetworks/default].
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ 


# Running the DAG

**Data processing using Dataproc Serverless**

Explore the PySpark Job:

`./airflow-pyspark/data_analytics_process.py`

The PySpark job converts temperature from tenths of a degree in Celsius to degrees celsius. This job will convert temperature data from the dataset into a different format.

## Upload supporting files to Cloud Storage

**To upload the PySpark file and the dataset stored in holidays.csv:**

`./upload.sh`

OR:

1.	In the Google Cloud console go to the Cloud Storage browser page:
Go to Cloud Storage browser
2.	Click the name of the bucket you created earlier
3.	In the Objects tab for the bucket, click the Upload files button, select data_analytics_process.py and holidays.csv in the dialog that appears, and click Open

## Data analytics DAG
Explore the example workflow

`./airflow-pyspark/data_analytics_dag.py`

**The workflow uses multiple operators to transform and unify the data:**

•	The **GCSToBigQueryOperator** ingests the holidays.csv file from Cloud Storage to a new table in the BigQuery holidays_weather dataset you created earlier.
•	The **DataprocCreateBatchOperator** creates and runs a PySpark batch job using Dataproc Serverless.
•	The **BigQueryInsertJobOperator** joins the data from holidays.csv on the "Date" column with weather data from the BigQuery public dataset ghcn_d. The BigQueryInsertJobOperator tasks are dynamically generated using a for loop, and these tasks are in a TaskGroup for better readability in the Graph View of the Airflow UI.

**Important:** The DataprocCreateBatchOperator is available in the apache-airflow-providers-google package versions 6.2.0 and later. The required versions of this package are preinstalled in your environment starting from Cloud Composer versions 1.17.10 and 2.0.3.

`./airflow-pyspark/data_analytics_dag.py`

# Use the Airflow UI to add variables

In Airflow, variables are an universal way to store and retrieve arbitrary settings or configurations as a simple key value store. This DAG uses Airflow variables to store common values. To add them to your environment:

•	Access the Airflow UI from the Cloud Composer console
•	Go to Admin > Variables
•	Add the following variables:
•	gcp_project - your project ID
•	gcs_bucket - the name of the bucket you created earlier without the "gs://" prefix.
•	gce_region - the region where you want your Dataproc job that meets Dataproc Serverless networking requirements. This is the region where you enabled private Google access earlier.
•	dataproc_service_account - the service account for your Cloud Composer environment. You can find this service account on the environment configuration tab for your Cloud Composer environment.

# Upload the DAG to your environment's bucket
Cloud Composer schedules DAGs that are located in the /dags folder in your environment's bucket. To upload the DAG using the Google Cloud console:
1.	On your local machine, save data_analytics_dag.py
2.	In Google Cloud console, go to the Environments page.
Go to Environments
3.	In the list of environments, In the DAG folder column click the DAGs link. The DAGs folder of your environment opens.
4.	Click Upload files
5.	Select data_analytics_dag.py on your local machine and click Open
Trigger the DAG
1.	In your Cloud Composer environment, click the DAGs tab
2.	Click into DAG id data_analytics_dag
3.	Click Trigger DAG
4.	Wait about five to ten minutes until you see a green check indicating the tasks have been completed successfully.

**Validate the DAG's success**
1.	In Google Cloud console, go to the BigQuery page.
Go to BigQuery
2.	In the Explorer panel, click your project name.
3.	Click holidays_weather_joined.
4.	Click preview to view the resulting table. Note that the numbers in the value column are in tenths of a degree celsius.
5.	Click holidays_weather_normalized.
6.	Click preview to view the resulting table. Note that the numbers in the value column are in degree celsius.

Deep dive with Dataproc Serverless (optional)
You can try an advanced version of this workflow with more complex PySpark data processing flow. See Dataproc extension for the Data Analytics Example on GitHub.

# Clean up
To avoid incurring charges to your Google Cloud account for the resources used either delete the project that contains the resources, or keep the project and delete the individual resources.
Delete the project
