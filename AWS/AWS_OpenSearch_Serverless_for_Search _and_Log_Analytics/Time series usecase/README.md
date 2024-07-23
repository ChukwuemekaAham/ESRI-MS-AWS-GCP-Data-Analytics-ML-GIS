# Time series usecase

o	Creating a collection
o	Create Collection - Review
o	Accessing OpenSearch Dashboards
o	Data ingestion & Search

Created a collection with type Time series. This type of collection can be used to analyze large volumes of semi-structured, machine generated time-series data for operational, security, and user behavior insights;

## Endpoints

- OpenSearch endpoint
https://k6g50ty16jg233yoz75e.us-east-1.aoss.amazonaws.com

- OpenSearch Dashboards URL
https://dashboards.us-east-1.aoss.amazonaws.com/_login/?collectionId=k6g50ty16jg233yoz75e


# Create a collection using console

## Add new collection
1.	Navigate to the Amazon OpenSearch console and Create Collections.

2.	Provide a name and description for the collection, and choose Collection type as Time series

3.	Under Encryption, choose an AWS KMS key to encrypt your data with. Here, you have an option to either provide your own KMS key to encrypt the data or let AWS own and manage the key for you. In this project I used an AWS managed key for encryption.

4.	Configured a private access via VPC endpoint for OpenSearch endpoint, and public access to the OpenSearch dashboards. 

## Review and Create Collection

1.	Review the configuration, then click on Submit to create the Collection

Once both **"OpenSearch Endpoint"** and **"OpenSearch Dashboard URL"** are availablee we can access the dashboard and load sample data for testing purposes.


# Accessing OpenSearch Dashboards
1.	To access your OpenSearch dashboard, with the previously configured data access policy and network policy click on the "Dashboard"

2.	Choose "Add sample data", and select Sample web logs which comes as part of OpenSearch Dashboards

3.	Once data is loaded, navigate to Dashboards screen and click [Logs] Web Traffic

4.	Now, you can explore the dashboards and data sample created by OpenSearch

At this point, you have seen how to load sample data available within OpenSearch Dashboards. 

# Data ingestion & Search (log analytics)
I explored three different ingestion pipelines which can be used to ingest data into OpenSearch Serverless collections along with some supported clients which can be used to interact with the OpenSearch APIs.

Below are the ingestion pipelines/clients:
1.	[Using Amazon Kinesis Data Firehose](./Data%20ingestion%20and%20search/Using%20Kinesis%20Data%20Firehost/)
-	Create Delivery Stream
-	Setup IAM Permission to Firehose
-	Setup data access policy
-	Send data to Kinesis Data Firehose
-	View Documents in dashboard

2.	[Using Python OpenSearch REST API client](./Data%20ingestion%20and%20search/Using%20Rest%20API/)
-   Setting up dashboards

3.	[Using Logstash](./Data%20ingestion%20and%20search/Using%20Logstash/)
-   Setup httpd log
-	Running Logstash

All three ingestion pipelines are independent of each other. The sample document generators from an Amazon EC2 instance was used.

