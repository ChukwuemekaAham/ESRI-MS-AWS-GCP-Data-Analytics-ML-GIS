# Copying BigQuery Tables Across Different Locations using Cloud Composer 

# Case Study
Imagine you have datasets that live in different locations around the globe. Let's say your data is in Google Cloud Storage buckets, or in BigQuery tables. How can you organize that data so that it gets consolidated and analyzed, and give you insights on your business?

Cloud Composer can help you build workflows and move your data between regions and storage systems, with an intuitive graphical view. Among others, it has templates for easy and reliable data moving between BigQuery and Cloud Storage, both ways.

Here I explored how to create and run an Apache Airflow workflow in Cloud Composer that completes the following tasks:
•	Reads from a config file the list of tables to copy
•	Exports the list of tables from a BigQuery dataset located in US to Cloud Storage
•	Copies the exported tables from US to EU Cloud Storage buckets
•	Imports the list of tables into the target BigQuery Dataset in EU
