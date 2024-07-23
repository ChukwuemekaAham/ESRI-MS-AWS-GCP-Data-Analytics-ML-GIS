```bash
$ export PROJECT_ID=$(gcloud info --format='value(config.project)')    
$ gsutil cp gs://$PROJECT_ID/sparktodp/spark_analysis.py spark_analysis.py
Copying gs://qwiklabs-gcp-00-d5591cfe205a/sparktodp/spark_analysis.py...
/ [1 files][  2.7 KiB/  2.7 KiB]
Operation completed over 1 objects/2.7 KiB.
$ ls
kddcup.data_10_percent.gz  README-cloudshell.txt  spark_analysis.py  training-data-analyst
$ nano submit_onejob.sh
$ chmod +x submit_onejob.sh
$ ./submit_onejob.sh $PROJECT_ID
Job [82090e10e330426cb069245451a2a35b] submitted.
Waiting for job output...
23/05/02 12:26:13 INFO SparkEnv: Registering MapOutputTracker
23/05/02 12:26:13 INFO SparkEnv: Registering BlockManagerMaster
23/05/02 12:26:15 INFO DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at sparktodp-m.us-central1-c.c.qwiklabs-gcp-00-d5591cfe205a.internal./10.128.0.2:8032
23/05/02 12:26:15 INFO AHSProxy: Connecting to Application History server at sparktodp-m.us-central1-c.c.qwiklabs-gcp-00-d5591cfe205a.internal./10.128.0.2:10200
23/05/02 12:26:17 INFO Configuration: resource-types.xml not found23/05/02 12:26:17 INFO ResourceUtils: Unable to find 'resource-types.xml'.
23/05/02 12:26:19 INFO YarnClientImpl: Submitted application application_1683027303480_0004
23/05/02 12:26:20 INFO DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at sparktodp-m.us-central1-c.c.qwiklabs-gcp-00-d5591cfe205a.internal./10.128.0.2:8030
23/05/02 12:26:23 INFO GoogleCloudStorageImpl: Ignoring exception of type GoogleJsonResponseException; verified object already exists with desired state.
23/05/02 12:26:25 INFO FileInputFormat: Total input files to process : 1/usr/lib/spark/python/lib/pyspark.zip/pyspark/sql/context.py:112: FutureWarning: Deprecated in 3.0.0. Use SparkSession.builder.getOrCreate() instead.
+-------------+------+
|protocol_type| count|
+-------------+------+
|         icmp|283602|
|          tcp|190065|
|          udp| 20354|
+-------------+------+

/usr/lib/spark/python/lib/pyspark.zip/pyspark/sql/dataframe.py:229: FutureWarning: Deprecated in 2.0, use createOrReplaceTempView instead.
+-------------+---------+----------+--------------+--------------+-------------+-------------------+-----------------+--------------------+-------------------+------------------+
|protocol_type|    state|total_freq|mean_src_bytes|mean_dst_bytes|mean_duration|total_failed_logins|total_compromised|total_file_creations|total_root_attempts|total_root_acceses|
+-------------+---------+----------+--------------+--------------+-------------+-------------------+-----------------+--------------------+-------------------+------------------+
|         icmp|   attack|    282314|        932.14|           0.0|          0.0|                  0|                0|                   0|                0.0|                 0|
|          tcp|   attack|    113252|       9880.38|        881.41|        23.19|                 57|             2269|                  76|                1.0|               152|
|          tcp|no attack|     76813|       1439.31|       4263.97|        11.08|                 18|             2776|                 459|               17.0|              5456|
|          udp|no attack|     19177|         98.01|         89.89|      1054.63|                  0|                0|                   0|                0.0|                 0|
|         icmp|no attack|      1288|         91.47|           0.0|          0.0|                  0|                0|                   0|                0.0|                 0|
|          udp|   attack|      1177|          27.5|          0.23|          0.0|                  0|                0|                   0|                0.0|                 0|
+-------------+---------+----------+--------------+--------------+-------------+-------------------+-----------------+--------------------+-------------------+------------------+

23/05/02 12:27:24 INFO GoogleCloudStorageFileSystem: Successfully repaired 'gs://qwiklabs-gcp-00-d5591cfe205a/sparktodp/connections_by_protocol/' directory.
Job [82090e10e330426cb069245451a2a35b] finished successfully.
done: true
driverControlFilesUri: gs://dataproc-staging-us-central1-778018046420-qkuzjpxd/google-cloud-dataproc-metainfo/7c2f6c48-9268-4d0b-85b9-3d14e65e842c/jobs/82090e10e330426cb069245451a2a35b/
driverOutputResourceUri: gs://dataproc-staging-us-central1-778018046420-qkuzjpxd/google-cloud-dataproc-metainfo/7c2f6c48-9268-4d0b-85b9-3d14e65e842c/jobs/82090e10e330426cb069245451a2a35b/driveroutput
jobUuid: b3e55a44-bec1-32bb-b8fe-eba414a374d6
placement:
  clusterName: sparktodp
  clusterUuid: 7c2f6c48-9268-4d0b-85b9-3d14e65e842c
pysparkJob:
  args:
  - --bucket=qwiklabs-gcp-00-d5591cfe205a
  mainPythonFileUri: gs://dataproc-staging-us-central1-778018046420-qkuzjpxd/google-cloud-dataproc-metainfo/7c2f6c48-9268-4d0b-85b9-3d14e65e842c/jobs/82090e10e330426cb069245451a2a35b/staging/spark_analysis.py
reference:
  jobId: 82090e10e330426cb069245451a2a35b
  projectId: qwiklabs-gcp-00-d5591cfe205a
status:
  state: DONE
  stateStartTime: '2023-05-02T12:27:26.834695Z'
statusHistory:
- state: PENDING
  stateStartTime: '2023-05-02T12:26:03.616810Z'
- state: SETUP_DONE
  stateStartTime: '2023-05-02T12:26:03.655435Z'
- details: Agent reported job success
  state: RUNNING
  stateStartTime: '2023-05-02T12:26:04.039153Z'
yarnApplications:
- name: kdd
  progress: 1.0
  state: FINISHED
  trackingUrl: http://sparktodp-m.us-central1-c.c.qwiklabs-gcp-00-d5591cfe205a.internal.:8088/proxy/application_1683027303480_0004/
$

```