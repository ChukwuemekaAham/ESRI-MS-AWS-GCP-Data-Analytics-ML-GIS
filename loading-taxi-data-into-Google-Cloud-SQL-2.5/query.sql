-- schema for the trips table:
create database if not exists bts;
use bts;
drop table if exists trips;
create table trips (
  vendor_id VARCHAR(16),		
  pickup_datetime DATETIME,
  dropoff_datetime DATETIME,
  passenger_count INT,
  trip_distance FLOAT,
  rate_code VARCHAR(16),
  store_and_fwd_flag VARCHAR(16),
  payment_type VARCHAR(16),
  fare_amount FLOAT,
  extra FLOAT,
  mta_tax FLOAT,
  tip_amount FLOAT,
  tolls_amount FLOAT,
  imp_surcharge FLOAT,
  total_amount FLOAT,
  pickup_location_id VARCHAR(16),
  dropoff_location_id VARCHAR(16)
);


-- Query the trips table:
select distinct(pickup_location_id) from trips;

-- select the database
use bts; 

-- Load the local CSV file data using local-infile:
LOAD DATA LOCAL INFILE 'trips.csv-1' INTO TABLE trips
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,rate_code,store_and_fwd_flag,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,imp_surcharge,total_amount,pickup_location_id,dropoff_location_id);

LOAD DATA LOCAL INFILE 'trips.csv-2' INTO TABLE trips
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,rate_code,store_and_fwd_flag,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,imp_surcharge,total_amount,pickup_location_id,dropoff_location_id);


-- Checking for data integrity
-- Whenever data is imported from a source it's always important to check for data integrity. Roughly, this means making sure the data meets our expectations.

-- 1.	Query the trips table for unique pickup location regions:

select distinct(pickup_location_id) from trips;


-- 2.	Digging into the trip_distance column. 
select
  max(trip_distance),
  min(trip_distance)
from
  trips;

-- One would expect the trip distance to be greater than 0 and less than, say 1000 miles. 
-- The maximum trip distance returned of 85 miles seems reasonable but the minimum trip distance
-- of 0 seems buggy.

-- 3.	How many trips in the dataset have a trip distance of 0?
select count(*) from trips where trip_distance = 0;

-- There are 155 such trips in the database. These trips warrant further exploration. 
-- You'll find that these trips have non-zero payment amounts associated with them. 
-- Perhaps these are fraudulent transactions?

-- 4.	Checking if I can find more data that doesn't meet my expectations. I expect the fare_amount 
-- column to be positive. Enter the following query to see if this is true in the database:

select count(*) from trips where fare_amount < 0;

-- There are 14 such trips returned and these trips warrant further exploration. 
-- There may be a reasonable explanation for why the fares take on negative numbers. 
-- However, it's up to the data engineer to ensure there are no bugs in the data pipeline 
-- that would cause such a result.

-- 5.	Finally, investigated the payment_type column.
select
  payment_type,
  count(*)
from
  trips
group by
  payment_type;

-- The results of the query indicate that there are four different payment types, with:
-- •	Payment type = 1 has 13863 rows
-- •	Payment type = 2 has 6016 rows
-- •	Payment type = 3 has 113 rows
-- •	Payment type = 4 has 32 rows
-- Digging into the documentation, a payment type of 1 refers to credit card use, payment type of 2 is cash, 
-- and a payment type of 4 refers to a dispute. The figures make sense.

-- 6.	Exiting the 'mysql' interactive console:
exit

