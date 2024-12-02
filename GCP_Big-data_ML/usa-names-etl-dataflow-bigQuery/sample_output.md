```bash
yasn1, protobuf, pbr, numpy, idna, grpcio, google-crc32c, future, fasteners, fastavro, dill, charset-normalizer, certifi, avro-python3, rsa, requests, python-dateutil, pydot, pyasn1-modules, pyarrow, mock, grpcio-gcp, googleapis-common-protos, google-resumable-media, oauth2client, hdfs, grpcio-status, google-auth, grpc-google-iam-v1, google-apitools, google-api-core, apache-beam,google-cloud-core, google-cloud-vision, google-cloud-videointelligence, google-cloud-spanner, google-cloud-pubsub, google-cloud-language, google-cloud-dlp, google-cloud-datastore, google-cloud-bigtable, google-cloud-bigquery
Successfully installed apache-beam-2.24.0 avro-python3-1.9.2.1 cachetools-3.1.1 certifi-2022.12.7 charset-normalizer-3.1.0 crcmod-1.7 dill-0.3.1.1 docopt-0.6.2 fastavro-0.23.6 fasteners-0.18 future-0.18.3 google-api-core-2.10.2 google-apitools-0.5.31 google-auth-1.35.0 google-cloud-bigquery-1.28.3 google-cloud-bigtable-1.7.3 google-cloud-core-1.7.3 google-cloud-datastore-1.15.5 google-cloud-dlp-1.0.2 google-cloud-language-1.3.2 google-cloud-pubsub-1.7.2 google-cloud-spanner-1.19.3 google-cloud-videointelligence-1.16.3 google-cloud-vision-1.0.2 google-crc32c-1.5.0 google-resumable-media-1.3.3 googleapis-common-protos-1.59.0 grpc-google-iam-v1-0.12.6 grpcio-1.54.0 grpcio-gcp-0.2.2 grpcio-status-1.48.2 hdfs-2.7.0 httplib2-0.17.4 idna-3.4 mock-2.0.0 numpy-1.21.6 oauth2client-3.0.0 pbr-5.11.1 protobuf-3.20.3 pyarrow-0.17.1 pyasn1-0.5.0 pyasn1-modules-0.3.0 pydot-1.4.2 pymongo-3.13.0 pyparsing-3.0.9 python-dateutil-2.8.2 pytz-2023.3 requests-2.28.2 rsa-4.9 six-1.16.0 typing-extensions-3.7.4.3 urllib3-1.26.15
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 22.0.4; however, version 23.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
root@5c36e9238552:/# ls
bin  boot  dataflow  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@5c36e9238552:/# cd dataflow/
root@5c36e9238552:/dataflow# python dataflow_python_examples/data_ingestion.py \
  --project=$PROJECT --region=us-east5 \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
INFO:apache_beam.internal.gcp.auth:Setting socket default timeout to 60 seconds.
INFO:apache_beam.internal.gcp.auth:socket default timeout is 60.0 seconds.
INFO:oauth2client.transport:Attempting refresh to obtain initial access_token
dataflow_python_examples/data_ingestion.py:128: BeamDeprecationWarning: BigQuerySink is deprecated since 2.11.0. Use WriteToBigQuery instead.
  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
INFO:apache_beam.runners.portability.stager:Downloading source distribution of the SDK from PyPi
INFO:apache_beam.runners.portability.stager:Executing command: ['/usr/local/bin/python', '-m', 'pip', 'download', '--dest', '/tmp/tmp2y_d3pcu', 'apache-beam==2.24.0', '--no-deps', '--no-binary', ':all:']
WARNING: You are using pip version 22.0.4; however, version 23.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
INFO:apache_beam.runners.portability.stager:Staging SDK sources from PyPI: dataflow_python_sdk.tar
INFO:apache_beam.runners.portability.stager:Downloading binary distribution of the SDK from PyPi
INFO:apache_beam.runners.portability.stager:Executing command: ['/usr/local/bin/python', '-m', 'pip', 'download', '--dest', '/tmp/tmp2y_d3pcu', 'apache-beam==2.24.0', '--no-deps', '--only-binary', ':all:', '--python-version', '37', '--implementation', 'cp', '--abi', 'cp37m', '--platform', 'manylinux1_x86_64']
WARNING: You are using pip version 22.0.4; however, version 23.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
INFO:apache_beam.runners.portability.stager:Staging binary distribution of the SDK from PyPI: apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl
WARNING:root:Make sure that locally built Python SDK docker image has Python 3.7 interpreter.
INFO:root:Using Python SDK docker image: apache/beam_python3.7_sdk:2.24.0. If the image is not available at local, we will try to pull from hub.docker.com
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/pipeline.pb...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/pipeline.pb in 0 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/pickled_main_session...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/pickled_main_session in 0 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/dataflow_python_sdk.tar...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/dataflow_python_sdk.tar in 1 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421134835-190770.1682084915.190952/apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl in 8 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Create job: <Job
 createTime: '2023-04-21T13:48:49.407448Z'
 currentStateTime: '1970-01-01T00:00:00Z'
 id: '2023-04-21_06_48_47-17799025096338642711'
 location: 'us-east5'
 name: 'beamapp-root-0421134835-190770'
 projectId: 'qwiklabs-gcp-01-793878e53383'
 stageStates: []
 startTime: '2023-04-21T13:48:49.407448Z'
 steps: []
 tempFiles: []
 type: TypeValueValuesEnum(JOB_TYPE_BATCH, 1)>
INFO:apache_beam.runners.dataflow.internal.apiclient:Created job with id: [2023-04-21_06_48_47-17799025096338642711]
INFO:apache_beam.runners.dataflow.internal.apiclient:Submitted job: 2023-04-21_06_48_47-17799025096338642711
INFO:apache_beam.runners.dataflow.internal.apiclient:To access the Dataflow monitoring console, please navigate to https://console.cloud.google.com/dataflow/jobs/us-east5/2023-04-21_06_48_47-17799025096338642711?project=qwiklabs-gcp-01-793878e53383
INFO:apache_beam.runners.dataflow.dataflow_runner:Job 2023-04-21_06_48_47-17799025096338642711 is in state JOB_STATE_PENDING
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:49.987Z: JOB_MESSAGE_DETAILED: Autoscaling is enabled for job 2023-04-21_06_48_47-17799025096338642711. The number of workers will be between 1 and 1000.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:50.017Z: JOB_MESSAGE_DETAILED: Autoscaling was automatically enabled for job 2023-04-21_06_48_47-17799025096338642711.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:51.430Z: JOB_MESSAGE_BASIC: Worker configuration: e2-standard-2 in us-east5-a.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:52.126Z: JOB_MESSAGE_DETAILED: Expanding CoGroupByKey operations into optimizable parts.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:52.144Z: JOB_MESSAGE_DETAILED: Expanding GroupByKey operations into optimizable parts.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:52.158Z: JOB_MESSAGE_DETAILED: Lifting ValueCombiningMappingFns into MergeBucketsMappingFns
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:52.171Z: JOB_MESSAGE_DEBUG: Annotating graph with Autotuner information.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:48:52.191Z: JOB_MESSAGE_DETAILED: Fusing adjacent ParDo, Read, Write, and FlattINFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:49:46.437Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to 1 based on the rate of progress in the currently running stage(s).INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:50:19.438Z: JOB_MESSAGE_DETAILED: Workers have started successfully.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:51:56.192Z: JOB_MESSAGE_DETAILED: All workers have finished the startup processes and began to receive work requests.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:51:57.111Z: JOB_MESSAGE_BASIC: Executing BigQuery import job "dataflow_job_15181945967146262778". You can check its status with the bq tool: "bq show -j --project_id=qwiklabs-gcp-01-793878e53383 dataflow_job_15181945967146262778".INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.394Z: JOB_MESSAGE_BASIC: BigQuery import job "dataflow_job_15181945967146262778" done.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.829Z: JOB_MESSAGE_BASIC: Finished operation Read from a File/Read+StringTo BigQuery Row+Write to BigQuery/NativeWrite
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.858Z: JOB_MESSAGE_DEBUG: Executing success step success1INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.891Z: JOB_MESSAGE_DETAILED: Cleaning up.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.922Z: JOB_MESSAGE_DEBUG: Starting worker pool teardown.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:09.935Z: JOB_MESSAGE_BASIC: Stopping worker pool...
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:59.790Z: JOB_MESSAGE_DETAILED: Autoscaling: Resized worker pool from 1 to 0.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:59.814Z: JOB_MESSAGE_BASIC: Worker pool stopped.INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:52:59.830Z: JOB_MESSAGE_DEBUG: Tearing down pending resources...
INFO:apache_beam.runners.dataflow.dataflow_runner:Job 2023-04-21_06_48_47-17799025096338642711 is in state JOB_STATE_DONE
root@5c36e9238552:/dataflow#


root@5c36e9238552:/dataflow# ^C
root@5c36e9238552:/dataflow# python dataflow_python_examples/data_transformation.py \
  --project=$PROJECT \
  --region=us-east5 \
  --runner=DataflowRunner \
  --staging_location=gs://$PROJECT/test \
  --temp_location gs://$PROJECT/test \
  --input gs://$PROJECT/data_files/head_usa_names.csv \
  --save_main_session
INFO:apache_beam.internal.gcp.auth:Setting socket default timeout to 60 seconds.
INFO:apache_beam.internal.gcp.auth:socket default timeout is 60.0 seconds.
INFO:oauth2client.transport:Attempting refresh to obtain initial access_token
dataflow_python_examples/data_transformation.py:160: BeamDeprecationWarning: BigQuerySink is deprecated since 2.11.0. Use WriteToBigQuery instead.
  write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
INFO:apache_beam.runners.portability.stager:Downloading source distribution of the SDK from PyPi
INFO:apache_beam.runners.portability.stager:Executing command: ['/usr/local/bin/python', '-m', 'pip', 'download', '--dest', '/tmp/tmp99ktp3sk', 'apache-beam==2.24.0', '--no-deps', '--no-binary', ':all:']
WARNING: You are using pip version 22.0.4; however, version 23.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
INFO:apache_beam.runners.portability.stager:Staging SDK sources from PyPI: dataflow_python_sdk.tar
INFO:apache_beam.runners.portability.stager:Downloading binary distribution of the SDK from PyPi
INFO:apache_beam.runners.portability.stager:Executing command: ['/usr/local/bin/python', '-m', 'pip', 'download', '--dest', '/tmp/tmp99ktp3sk', 'apache-beam==2.24.0', '--no-deps', '--only-binary', ':all:', '--python-version', '37', '--implementation', 'cp', '--abi', 'cp37m', '--platform', 'manylinux1_x86_64']
WARNING: You are using pip version 22.0.4; however, version 23.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
INFO:apache_beam.runners.portability.stager:Staging binary distribution of the SDK from PyPI: apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl
WARNING:root:Make sure that locally built Python SDK docker image has Python 3.7 interpreter.
INFO:root:Using Python SDK docker image: apache/beam_python3.7_sdk:2.24.0. If the image is not available at local, we will try to pull from hub.docker.com
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/pipeline.pb...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/pipeline.pb in 0 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/pickled_main_session...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/pickled_main_session in 0 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/dataflow_python_sdk.tar...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/dataflow_python_sdk.tar in 1 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Starting GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl...
INFO:apache_beam.runners.dataflow.internal.apiclient:Completed GCS upload to gs://qwiklabs-gcp-01-793878e53383/test/beamapp-root-0421135630-097267.1682085390.097544/apache_beam-2.24.0-cp37-cp37m-manylinux1_x86_64.whl in 8 seconds.
INFO:apache_beam.runners.dataflow.internal.apiclient:Create job: <Job
 createTime: '2023-04-21T13:56:42.786413Z'
 currentStateTime: '1970-01-01T00:00:00Z'
 id: '2023-04-21_06_56_42-14922451689115154406'
 location: 'us-east5'
 name: 'beamapp-root-0421135630-097267'
 projectId: 'qwiklabs-gcp-01-793878e53383'
 stageStates: []
 startTime: '2023-04-21T13:56:42.786413Z'
 steps: []
 tempFiles: []
 type: TypeValueValuesEnum(JOB_TYPE_BATCH, 1)>
INFO:apache_beam.runners.dataflow.internal.apiclient:Created job with id: [2023-04-21_06_56_42-14922451689115154406]
INFO:apache_beam.runners.dataflow.internal.apiclient:Submitted job: 2023-04-21_06_56_42-14922451689115154406
INFO:apache_beam.runners.dataflow.internal.apiclient:To access the Dataflow monitoring console, please navigate to https://console.cloud.google.com/dataflow/jobs/us-east5/2023-04-21_06_56_42-14922451689115154406?project=qwiklabs-gcp-01-793878e53383
INFO:apache_beam.runners.dataflow.dataflow_runner:Job 2023-04-21_06_56_42-14922451689115154406 is in state JOB_STATE_PENDING
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:43.288Z: JOB_MESSAGE_DETAILED: Autoscaling is enabled for job 2023-04-21_06_56_42-14922451689115154406. The number of workers will be between 1 and 1000.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:43.315Z: JOB_MESSAGE_DETAILED: Autoscaling was automatically enabled for job 2023-04-21_06_56_42-14922451689115154406.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:44.698Z: JOB_MESSAGE_BASIC: Worker configuration: e2-standard-2 in us-east5-a.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.282Z: JOB_MESSAGE_DETAILED: Expanding CoGroupByKey operations into optimizable parts.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.301Z: JOB_MESSAGE_DETAILED: Expanding GroupByKey operations into optimizable parts.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.315Z: JOB_MESSAGE_DETAILED: Lifting ValueCombiningMappingFns into MergeBucketsMappingFns
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.327Z: JOB_MESSAGE_DEBUG: Annotating graph with Autotuner information.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.347Z: JOB_MESSAGE_DETAILED: Fusing adjacent ParDo, Read, Write, and Flatten operations
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.359Z: JOB_MESSAGE_DETAILED: Fusing consumer String to BigQuery Row into Read From Text/Read
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.373Z: JOB_MESSAGE_DETAILED: Fusing consumer Write to BigQuery/NativeWrite into String to BigQuery Row
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.394Z: JOB_MESSAGE_DEBUG: Workflow config is missing a default resource spec.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.407Z: JOB_MESSAGE_DEBUG: Adding StepResource setup and teardown to workflow graph.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.420Z: JOB_MESSAGE_DEBUG: Adding workflow start and stop steps.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.433Z: JOB_MESSAGE_DEBUG: Assigning stage ids.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.522Z: JOB_MESSAGE_DEBUG: Executing wait step start3
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.553Z: JOB_MESSAGE_BASIC: Executing operation Read From Text/Read+String to BigQuery Row+Write to BigQuery/NativeWrite
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.582Z: JOB_MESSAGE_DEBUG: Starting worker pool setup.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:56:45.595Z: JOB_MESSAGE_BASIC: Starting 1 workers in us-east5-a...
INFO:apache_beam.runners.dataflow.dataflow_runner:Job 2023-04-21_06_56_42-14922451689115154406 is in state JOB_STATE_RUNNING
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:57:20.859Z: JOB_MESSAGE_DETAILED: Autoscaling: Raised the number of workers to1 based on the rate of progress in the currently running stage(s).
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:57:57.098Z: JOB_MESSAGE_DETAILED: Workers have started successfully.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:25.325Z: JOB_MESSAGE_DETAILED: All workers have finished the startup processes and began to receive work requests.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:26.128Z: JOB_MESSAGE_BASIC: Executing BigQuery import job "dataflow_job_12361504263634008627". You can check its status with the bq tool: "bq show -j --project_id=qwiklabs-gcp-01-793878e53383 dataflow_job_12361504263634008627".
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:37.572Z: JOB_MESSAGE_BASIC: BigQuery import job "dataflow_job_12361504263634008627" done.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:37.971Z: JOB_MESSAGE_BASIC: Finished operation Read From Text/Read+String to BigQuery Row+Write to BigQuery/NativeWrite
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:38Z: JOB_MESSAGE_DEBUG: Executing success step success1
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:38.034Z: JOB_MESSAGE_DETAILED: Cleaning up.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:38.065Z: JOB_MESSAGE_DEBUG: Starting worker pool teardown.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T13:59:38.077Z: JOB_MESSAGE_BASIC: Stopping worker pool...
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T14:00:25.112Z: JOB_MESSAGE_DETAILED: Autoscaling: Resized worker pool from 1 to 0.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T14:00:25.138Z: JOB_MESSAGE_BASIC: Worker pool stopped.
INFO:apache_beam.runners.dataflow.dataflow_runner:2023-04-21T14:00:25.152Z: JOB_MESSAGE_DEBUG: Tearing down pending resources...
INFO:apache_beam.runners.dataflow.dataflow_runner:Job 2023-04-21_06_56_42-14922451689115154406 is in state JOB_STATE_DONE
root@5c36e9238552:/dataflow#

.
.
.
```