# Overview

Plot and visualize a hurricane's path using geospatial analytics

## Objectives
•	Use a geospatial analytics function to convert latitude and longitude columns into geographical points
•	Run a query that plots the path of a hurricane
•	Visualize your results in BigQuery Geo Viz

## Exploring the sample data

This analysis uses a dataset available through the Google Cloud Public Dataset Program. A public dataset is any dataset that is stored in BigQuery and made available to the general public. The public datasets are datasets that BigQuery hosts for you to access and integrate into your applications. Google pays for the storage of these datasets and provides public access to the data via a project. You pay only for the queries that you perform on the data (the first 1 TB per month is free, subject to query pricing details).

## The Global Hurricane Tracks (IBTrACS) dataset

The historical positions and intensities along the tracks of global tropical cyclones (TC) are provided by NOAA's International Best Track Archive for Climate Stewardship (IBTrACS). Tropical cyclones are known as hurricanes in the north Atlantic and northeast Pacific ocean basins, typhoons in the northwest Pacific ocean basin, cyclones in the north and south Indian Ocean basins, and tropical cyclones in the southwest Pacific ocean basin.

IBTrACS collects data about TCs reported by international monitoring centers who have a responsibility to forecast and report on TCs (and also includes some important historical datasets). Presently, IBTrACS includes data from 9 different countries. Historically, the data describing these systems has included best estimates of their track and intensity (hence the term, best track).

View the details of the hurricanes table:

- Global Hurricane Tracks (IBTrACS) dataset.xlsx file


# Query the path of hurricane Maria in 2017

```sql

GoogleSQL query that finds the path of hurricane Maria in the 2017 season. To plot the hurricane's path, query the hurricane's location at different points in time.

Query details
The following GoogleSQL query is used to find the path of hurricane Maria.

```sql
SELECT
  ST_GeogPoint(longitude, latitude) AS point,
  name,
  iso_time,
  dist2land,
  usa_wind,
  usa_pressure,
  usa_sshs,
  (usa_r34_ne + usa_r34_nw + usa_r34_se + usa_r34_sw)/4 AS radius_34kt,
  (usa_r50_ne + usa_r50_nw + usa_r50_se + usa_r50_sw)/4 AS radius_50kt
FROM
  `bigquery-public-data.noaa_hurricanes.hurricanes`
WHERE
  name LIKE '%MARIA%'
  AND season = '2017'
  AND ST_DWithin(ST_GeogFromText('POLYGON((-179 26, -179 48, -10 48, -10 26, -100 -10.1, -179 26))'),
    ST_GeogPoint(longitude, latitude), 10)
ORDER BY
  iso_time ASC
```
- Results: path_of_hurricane_Maria.csv


**The query clauses do the following:**

SELECT ST_GeogPoint(longitude, latitude) AS point, name, iso_time, dist2land, usa_wind, usa_pressure, usa_sshs, (usa_r34_ne + usa_r34_nw + usa_r34_se + usa_r34_sw)/4 AS radius_34kt, (usa_r50_ne + usa_r50_nw + usa_r50_se + usa_r50_sw)/4 AS radius_50kt

<!-- The SELECT clause selects all the storm's weather data and uses the ST_GeogPoint function to convert the values in the latitude and longitude columns to GEOGRAPHY types (points). -->

FROM bigquery-public-data.noaa_hurricanes.hurricanes

<!-- The FROM clause specifies the table being queried: hurricanes. -->

WHERE name LIKE '%MARIA%' AND season = '2017' AND ST_DWithin(ST_GeogFromText('POLYGON((-179 26, -179 48, -10 48, -10 26, -100 -10.1, -179 26))'), ST_GeogPoint(longitude, latitude), 10)

<!-- The WHERE clause filters the data to just the points in the Atlantic corresponding to hurricane Maria in the 2017 hurricane season. -->

ORDER BY iso_time ASC

<!-- The ORDER BY clause orders the points to form a chronological storm path. -->

Run the query in google cloud console
```sql
SELECT
  ST_GeogPoint(longitude, latitude) AS point,
  name,
  iso_time,
  dist2land,
  usa_wind,
  usa_pressure,
  usa_sshs,
  (usa_r34_ne + usa_r34_nw + usa_r34_se + usa_r34_sw)/4 AS radius_34kt,
  (usa_r50_ne + usa_r50_nw + usa_r50_se + usa_r50_sw)/4 AS radius_50kt
FROM
  `bigquery-public-data.noaa_hurricanes.hurricanes`
WHERE
  name LIKE '%MARIA%'
  AND season = '2017'
  AND ST_DWithin(ST_GeogFromText('POLYGON((-179 26, -179 48, -10 48, -10 26, -100 -10.1, -179 26))'),
    ST_GeogPoint(longitude, latitude), 10)
ORDER BY
  iso_time ASC

Result: 



Visualize the query results in Geo Viz
Next, visualize results using BigQuery Geo Viz — A web tool for visualization of geospatial data in BigQuery using Google Maps APIs.


Run your query in Geo Viz
After you authenticate and grant access, the next step is to run the query in Geo Viz.

To run the query:

For step one, Select data, enter your project ID in the Project ID field.

In the query window, enter the following GoogleSQL query.

SELECT
  ST_GeogPoint(longitude, latitude) AS point,
  name,
  iso_time,
  dist2land,
  usa_wind,
  usa_pressure,
  usa_sshs,
  (usa_r34_ne + usa_r34_nw + usa_r34_se + usa_r34_sw)/4 AS radius_34kt,
  (usa_r50_ne + usa_r50_nw + usa_r50_se + usa_r50_sw)/4 AS radius_50kt
FROM
  `bigquery-public-data.noaa_hurricanes.hurricanes`
WHERE
  name LIKE '%MARIA%'
  AND season = '2017'
  AND ST_DWithin(ST_GeogFromText('POLYGON((-179 26, -179 48, -10 48, -10 26, -100 -10.1, -179 26))'),
    ST_GeogPoint(longitude, latitude), 10)
ORDER BY
  iso_time ASC

```

