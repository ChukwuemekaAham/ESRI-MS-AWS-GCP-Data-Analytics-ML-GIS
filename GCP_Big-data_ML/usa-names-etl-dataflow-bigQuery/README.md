# ETL Processing on Google Cloud Using Dataflow and BigQuery

Built several Data Pipelines that ingest data from a publicly available dataset into BigQuery, using these Google Cloud services:
•	Cloud Storage
•	Dataflow
•	BigQuery

Including the design considerations, as well as implementation details, to ensure that my prototype meets the requirements.

- Ensure that the Dataflow API is successfully enabled
- Create Cloud Storage Bucket

`gsutil mb -c regional -l   gs://$PROJECT`

- Copy files to bucket

```bash
gsutil cp gs://spls/gsp290/data_files/usa_names.csv gs://$PROJECT/data_files/
gsutil cp gs://spls/gsp290/data_files/head_usa_names.csv gs://$PROJECT/data_files/
```

- Create the BigQuery dataset
•	Create a dataset in BigQuery called lake where all tables will be loaded in BigQuery:

bq mk lake

- Build a Dataflow pipeline

Created an append-only Dataflow which ingests data into the BigQuery table. 

- Data ingestion
Built the Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically, it will:
•	Ingest the files from Cloud Storage.
•	Filter out the header row in the files.
•	Convert the lines read to dictionary objects.
•	Output the rows to BigQuery.

- Review pipeline python code

SEE: `./data_ingestion.py` file. Read through the comments as it explains what the code is doing. This code will populate the data in BigQuery.
 
-nRun the Apache Beam pip Python3.7. To ensure you're on the proper version, you will run the process on a Python 3.7 Docker container.

`docker run -it -e PROJECT=$PROJECT -v $(pwd)/dataflow-python-examples:/dataflow python:3.7 /bin/bash`

This command will pull a Docker container with the latest stable version of Python 3.7 and execute a command shell to run the next commands within the container. The -v flag provides the source code as a volume for the container so that we can edit in Cloud Shell editor and still access it within the container.

-            Once the container finishes pulling, run the following to install apache-beam:
pip install apache-beam[gcp]==2.24.0

- Change directories into where the source code linked the source code:

Running the Dataflow pipeline in the cloud.
```shell
The following will spin up the workers required, and shut them down when complete:
python dataflow_python_examples/data_ingestion.py \
  --project=$PROJECT --region= \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

- open console to Dataflow to view the status of the job.
- Navigate to BigQuery to confirm data has been populated.

- Data transformation
Build the Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically:
•	Ingest the files from Cloud Storage.
•	Convert the lines read to dictionary objects.
•	Transform the data which contains the year to a format BigQuery understands as a date.
•	Output the rows to BigQuery.
Review pipeline python code

SEE: `data_transformation.py` file. 
Read through the comments in the file which explain what the code is doing.

- Running the Apache Beam pipeline
Dataflow pipeline in the cloud. This will spin up the workers required, and shut them down when complete.

```bash
python dataflow_python_examples/data_transformation.py \
  --project=$PROJECT \
  --region= \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

-  Check status of the in Dataflow.

When Job Status has Succeeded in the Dataflow Job Status screen, The usa_names_transformed table under the lake dataset has been created in BigQuery.


- Data enrichment
Build a Dataflow pipeline with a TextIO source and a BigQueryIO destination to ingest data into BigQuery. More specifically, will:
•	Ingest the files from Cloud Storage.
•	Filter out the header row in the files.
•	Convert the lines read to dictionary objects.
•	Output the rows to BigQuery.

- Review pipeline python code

SEE: `data_enrichment.py` file.

This code will populate the data in BigQuery.
Line 83 currently looks like:
values = [x.decode('utf8') for x in csv_row]

3.	Edit it so it looks like the following:
values = [x for x in csv_row]

- Run the Apache Beam pipeline
Dataflow pipeline in the cloud.

- Run the following to spin up the workers required, and shut them down when complete:
```bash
python dataflow_python_examples/data_enrichment.py \
  --project=$PROJECT \
  --region= \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
```

SEE: `usa_names_enriched.xlsx` file.


- Data lake to Mart
Dataflow pipeline that reads data from 2 BigQuery data sources, and then joins the data sources. Specifically, you:
•	Ingest files from 2 BigQuery sources.
•	Join the 2 data sources.
•	Filter out the header row in the files.
•	Convert the lines read to dictionary objects.
•	Output the rows to BigQuery.

- Review pipeline python code
SEE: `data_lake_to_mart.py` file. This code populateS the data in BigQuery.

- Run the Apache Beam Pipeline in the cloud

- Run the following to spin up the workers required, and shut them down when complete:
```bash
python dataflow_python_examples/data_lake_to_mart.py \
  --worker_disk_type="compute.googleapis.com/projects//zones//diskTypes/pd-ssd" \
  --max_num_workers=4 \
  --project=$PROJECT \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --save_main_session \
  --region=
```
SEE: `orders_denormalized_sideinput.xlsx` file for output
