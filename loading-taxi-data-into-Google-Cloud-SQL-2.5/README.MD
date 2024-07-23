# Loading Taxi Data into Google Cloud SQL 2.5

## Overview

The goal of this task was to import data from CSV text files into Cloud SQL and then carry out some basic data analysis using simple queries.

The dataset used is collected by the NYC Taxi and Limousine Commission and includes trip records from all trips completed in Yellow and Green taxis in NYC from 2009 to present, and all trips in for-hire vehicles (FHV) from 2015 to present. Records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.

This dataset can be used to demonstrate a wide range of data science concepts and techniques. 

## Objectives
• Create a Jump host for management access to the SQL instance
•	Create Cloud SQL instance
•	Create a Cloud SQL database
•	Import text data into Cloud SQL
•	Check the data for integrity

Add data from cloud storage to local instance with the following script:

```bash
./data.sh
```

See `output.md` and `query.sql` files for more information on how the objectives were achieved
