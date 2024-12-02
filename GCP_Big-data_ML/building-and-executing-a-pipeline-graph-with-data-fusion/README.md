# Building and Executing a Pipeline Graph with Data Fusion 2.5

## Overview
This demo etl demostrates how to use the Wrangler and Data Pipeline features in Cloud Data Fusion to clean, transform, and process taxi trip data for further analysis.


## Objectives:
•	Connect Cloud Data Fusion to a couple of data sources
•	Apply basic transformations
•	Join two data sources
•	Write data to a sink

## Introduction
Often times, data needs to go through a number of pre-processing steps before analysts can leverage the data to glean insights. For example, data types may need to be adjusted, anomalies removed, and vague identifiers may need to be converted to more meaningful entries. Cloud Data Fusion is a service for efficiently building ETL/ELT data pipelines. Cloud Data Fusion uses Cloud Dataproc cluster to perform all transforms in the pipeline.
The use of Cloud Data Fusion was exemplified by using a subset of the NYC TLC Taxi Trips dataset on BigQuery.

- Creating a Cloud Data Fusion instance
- Loading the data
- Cleaning the data
- Creating the pipeline
- Adding a data source

```sql
SELECT
  zone_id,
  zone_name,
  borough
FROM
  `bigquery-public-data.new_york_taxi_trips.taxi_zone_geom`
```
- Joining two sources
- Storing the output to BigQuery
- Deploying and running the pipeline
- Viewing the results

To view the results after the pipeline runs:
Query below to see the values in the trips_pickup_name table:

```sql
	SELECT
	  *
	FROM
  `trips.trips_pickup_name`
```
 

