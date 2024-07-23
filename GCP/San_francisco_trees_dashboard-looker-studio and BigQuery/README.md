# How to Build a BI Dashboard Using Google Looker Studio and BigQuery

## Overview
For as long as business intelligence (BI) has been around, visualization tools have played an important role in helping analysts and decision-makers quickly get insights from data.


Here I explored how to build a BI dashboard with Looker Studio as the front end, powered by BigQuery on the back end.w

## Usecase

**Product details**
 
Street Trees
City and County of San Francisco
San Francisco Street Trees since 1955

This data includes a list of San Francisco Department of Public Works maintained street trees including: planting date, species, and location. Data includes 1955 to present.

This public dataset is hosted in Google BigQuery and is included in BigQuery's 1TB/mo of free tier processing. This means that each user receives 1TB of free BigQuery processing every month, which can be used to run queries on this public dataset. 

Additional details
•	Type: Datasets
•	Category: Science & research
•	Dataset source: DataSF 
•	Cloud service: BigQuery
•	Expected update frequency: Quarterly

As a manager of tree services for a large city. I make important decisions based on usage logs data, stored in large (multiple TBs) date-partitioned tables in a BigQuery dataset called "Trees".
To get business value out of that data as quickly as possible, build a dashboard for analysts that provides visualizations of trends and patterns in your data.


## Solution overview
Typically, a dashboard shows an aggregated view of usage — it doesn't need details all the way to the level of an order ID, for instance. So, to reduce query costs, first I aggregated the needed logs into another dataset called "Reports" then created a table of aggregated data. Queried the table from the Data Studio dashboard. This way, when the dashboard is refreshed, the reporting dataset queries process less data. Since usage logs from the past never change, it only refresh new usage data into the Reports dataset.
