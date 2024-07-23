# Running Apache Spark jobs on Cloud Dataproc

Overview
This is a demo of how to migrate Apache Spark code to Cloud Dataproc. Followed a sequence of steps progressively moving more of the job components over to GCP services:
•	Run original Spark code on Cloud Dataproc (Lift and Shift)
•	Replace HDFS with Cloud Storage (cloud-native)
•	Automate everything so it runs on job-specific clusters (cloud-optimized)


## Objectives:
•	Migrate existing Spark jobs to Cloud Dataproc
•	Modify Spark jobs to use Cloud Storage instead of HDFS
•	Optimize Spark jobs to run on Job specific clusters

## What was used
•	Cloud Dataproc
•	Apache Spark

## Scenario
You are migrating an existing Spark workload to Cloud Dataproc and then progressively modifying the Spark code to make use of GCP native features and services.

**Task 1. Lift and shift**
Migrate existing Spark jobs to Cloud Dataproc
Created a new Cloud Dataproc cluster and then run an imported Jupyter notebook that uses the cluster's default local Hadoop Distributed File system (HDFS) to store source data and then process that data just as you would on any Hadoop cluster using Spark. This demonstrates how many existing analytics workloads such as Jupyter notebooks containing Spark code require no changes when they are migrated to a Cloud Dataproc environment.

- Configure and start a Cloud Dataproc cluster

1.	In the GCP Console, on the Navigation menu, in the Analytics section, click Dataproc.
2.	Click Create Cluster.
3.	Click Create for the item Cluster on Compute Engine.
4.	Enter sparktodp for Cluster Name.
5.	In the Versioning section, click Change and select 2.1 (Debian 11, Hadoop 3.3, Spark 3.3).
This version includes Python3, which is required for the sample code used in this lab.
6.	Click Select.
7.	In the Components > Component gateway section, select Enable component gateway.
8.	Under Optional components, Select Jupyter Notebook.
9.	Below Set up cluster from the list on the left side, click Configure nodes (optional).
10.	Under Manager node change Series to E2 and Machine Type to e2-standard-2 (2 vCPU, 8 GB memory).
11.	Under Worker nodes change Series to E2 and Machine Type to e2-standard-2 (2 vCPU, 8 GB memory).
12.	Click Create.


**Task1: Local Hadoop file system**
SEE: `./01_spark.ipynb `

•	The first code cell fetches the source data file, which is an extract from the KDD Cup competition from the Knowledge, Discovery, and Data (KDD) conference in 1999. The data relates to computer intrusion detection events.
!wget https://storage.googleapis.com/cloud-training/dataengineering/lab_assets/sparklab/kddcup.data_10_percent.gz

•	In the second code cell, the source data is copied to the default (local) Hadoop file system.
!hadoop fs -put kddcup* /

•	In the third code cell, the command lists contents of the default directory in the cluster's HDFS file system.
!hadoop fs -ls /

 
**Task 2. Separate compute and storage**
Modify Spark jobs to use Cloud Storage instead of HDFS.
Taking the original 'Lift & Shift' notebook to create a copy that decouples the storage requirements for the job from the compute requirements. In this case, all that was done is replace the Hadoop file system calls with Cloud Storage calls by replacing hdfs:// storage references with gs:// references in the code and adjusting folder names as necessary.

SEE:    `./De-couple-storage.ipynb`

You start by using the cloud shell to place a copy of the source data in a new Cloud Storage bucket.

1.	Created a new storage bucket for your source data:
```bash
export PROJECT_ID=$(gcloud info --format='value(config.project)')
gsutil mb gs://$PROJECT_ID

2.	In the Cloud Shell copy the source data into the bucket:
wget https://storage.googleapis.com/cloud-training/dataengineering/lab_assets/sparklab/kddcup.data_10_percent.gz
gsutil cp kddcup.data_10_percent.gz gs://$PROJECT_ID/

```
No longer need the cells that download and copy the data onto the cluster's internal HDFS file system so it was remove.

Changed the code in the first cell that defines the data file source location and reads in the source data.

The only change here is create a variable to store a Cloud Storage bucket name and then to point the data_file to the bucket we used to store the source data on Cloud Storage:

```python
from pyspark.sql import SparkSession, SQLContext, Row
gcs_bucket='[Your-Bucket-Name]'
spark = SparkSession.builder.appName("kdd").getOrCreate()
sc = spark.sparkContext
data_file = "gs://"+gcs_bucket+"//kddcup.data_10_percent.gz"
raw_rdd = sc.textFile(data_file).cache()
raw_rdd.take(5)
```
Moving the source data files to Cloud Storage only requires that you repoint your storage source reference from hdfs:// to gs://.

**Task 3. Deploy Spark jobs**
Optimize Spark jobs to run on Job specific clusters
Creating a standalone Python file, that can be deployed as a Cloud Dataproc Job, that will perform the same functions as this notebook. Add magic commands to the Python cells in a copy of the notebook to write the cell contents out to a file. 

Also added an input parameter handler to set the storage bucket location when the Python script is called to make the code more portable.

SEE: `PySpark-analysis-fileS.ipynb` file

```python
%%writefile spark_analysis.py
import matplotlib
matplotlib.use('agg')
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--bucket", help="bucket for input and output")
args = parser.parse_args()
BUCKET = args.bucket
```

The %%writefile spark_analysis.py Jupyter magic command creates a new output file to contain your standalone python script. Added a variation of this to the remaining cells to append the contents of each cell to the standalone script file.

This code also imports the matplotlib module and explicitly sets the default plotting backend via matplotlib.use('agg') so that the plotting code runs outside of a Jupyter notebook.

- For the remaining cells insert %%writefile -a spark_analysis.py at the start of each Python code cell. These are the five cells labelled In [x].

%%writefile -a spark_analysis.py

For example the next cell now look as follows:

%%writefile -a spark_analysis.py

```python
from pyspark.sql import SparkSession, SQLContext, Row
spark = SparkSession.builder.appName("kdd").getOrCreate()
sc = spark.sparkContext
data_file = "gs://{}/kddcup.data_10_percent.gz".format(BUCKET)
raw_rdd = sc.textFile(data_file).cache()
#raw_rdd.take(5)
```

## Test automation
Tested that the PySpark code runs successfully as a file by calling the local copy from inside the notebook, passing in a parameter to identify the storage bucket you created earlier that stores the input data for this job. The same bucket will be used to store the report data files produced by the script.

- In the `PySpark-analysis-file` notebook added
```bash
BUCKET_list = !gcloud info --format='value(config.project)'
BUCKET=BUCKET_list[0]
print('Writing to {}'.format(BUCKET))
!/opt/conda/miniconda3/bin/python spark_analysis.py --bucket=$BUCKET
```

Creates a Cloud Storage Bucket using your Project ID as the Storage Bucket name. If you used a different name modify this code to set the BUCKET variable to the name you used.

`!gsutil ls gs://$BUCKET/sparktodp/**`

This lists the script output files that have been saved to the Cloud Storage bucket.

To save a copy of the Python file to persistent storage add

`!gsutil cp spark_analysis.py gs://$BUCKET/sparktodp/spark_analysis.py`

Run All to run all of the cells in the notebook.
If the notebook successfully creates and runs the Python file you should see output that indicates the script has run to completion saving the output to the Cloud Storage bucket created earlier
 
`Note: The most likely source of an error at this stage is that one did not remove the matplotlib directive in In [7]. Rechecked that I have modified all of the cells, and have not skipped any steps.

## Running the Analysis Job from Cloud Shell.

1.	Copy the Python script from Cloud Storage so you can run it as a Cloud Dataproc Job:
`gsutil cp gs://$PROJECT_ID/sparktodp/spark_analysis.py spark_analysis.py`

2.	launch script:

`./submit_onejob.sh`

chmod +x submit_onejob.sh

6.	Launch the PySpark Analysis job:
./submit_onejob.sh $PROJECT_ID

7.	In the Cloud Console tab navigate to the Dataproc > Clusters.
8.	Click Jobs.
9.	Click the name of the job that is listed. You can monitor progress here as well as from the Cloud shell. Wait for the Job to complete successfully.
10.	Navigate to your storage bucket and note that the output report, /sparktodp/report.png has an updated time-stamp indicating that the stand-alone job has completed successfully.
The storage bucket used by this Job for input and output data storage is the bucket that used just the Project ID as the name.


# CLEANUP
11.	Navigate back to the Dataproc > Clusters page.
12.	Select the sparktodp cluster and click Delete. You don't need it any more.
13.	Click CONFIRM.
14.	Close the Jupyter tabs in your browser.

