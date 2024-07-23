```bash

# Preparing the environment
# Create environment variables that will be used later for project ID and the storage bucket that will contain the data:

$ export PROJECT_ID=$(gcloud info --format='value(config.project)')
$ export BUCKET=${PROJECT_ID}-ml


# Create a Cloud SQL instance
# The following commands create a Cloud SQL instance:

$ gcloud sql instances create taxi \
    --tier=db-n1-standard-1 --activation-policy=ALWAYS
WARNING: Starting with release 233.0.0, you will need to specify either a region or a zone to create an instance.
Creating Cloud SQL instance for MYSQL_8_0...done.     
Created [https://sqladmin.googleapis.com/sql/v1beta4/projects/clear-router-390022/instances/taxi].
NAME: taxi
DATABASE_VERSION: MYSQL_8_0
LOCATION: us-central1-f
TIER: db-n1-standard-1
PRIMARY_ADDRESS: 34.132.38.87
PRIVATE_ADDRESS: -
STATUS: RUNNABLE

# Set a root password for the Cloud SQL instance:
$ gcloud sql users set-password root --host % --instance taxi \
 --password Passw0rd
Updating Cloud SQL user...done.   

# Create an environment variable with the IP address of the jump host instance
# and whitelist the instance for management access to the SQL instance:

$ gcloud sql instances patch taxi --authorized-networks $ADDRESS
When adding a new IP address to authorized networks, make sure to also include any IP addresses that have already been authorized. Otherwise, they
will be overwritten and de-authorized.

Do you want to continue (Y/n)?  Y

The following message will be used for the patch API method.
{"name": "taxi", "project": "clear-router-390022", "settings": {"ipConfiguration": {"authorizedNetworks": [{"value": "34.78.107.157/32"}]}}}
Patching Cloud SQL instance...done.     
Updated [https://sqladmin.googleapis.com/sql/v1beta4/projects/clear-router-390022/instances/taxi].

# Get the IP address of your Cloud SQL instance by running:
$ MYSQLIP=$(gcloud sql instances describe \
taxi --format="value(ipAddresses.ipAddress)")

# Check the variable MYSQLIP:
$ echo $MYSQLIP
34.132.38.87

# Create the taxi trips table by logging into the mysql command line interface:
$ mysql --host=$MYSQLIP --user=root \
      --password --verbose
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 34
Server version: 8.0.26-google (Google)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Reading history-file /home/aham/.mysql_history
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database if not exists bts;
--------------
create database if not exists bts
--------------

Query OK, 1 row affected (0.11 sec)

mysql> use bts;
Database changed
mysql> create table trips (
    ->   vendor_id VARCHAR(16),
    ->   pickup_datetime DATETIME,
    ->   dropoff_datetime DATETIME,
    ->   passenger_count INT,
    ->   trip_distance FLOAT,
    ->   rate_code VARCHAR(16),
    ->   store_and_fwd_flag VARCHAR(16),
    ->   payment_type VARCHAR(16),
    ->   fare_amount FLOAT,
    ->   extra FLOAT,
    ->   mta_tax FLOAT,
    ->   tip_amount FLOAT,
    ->   tolls_amount FLOAT,
    ->   imp_surcharge FLOAT,
    ->   total_amount FLOAT,
    ->   pickup_location_id VARCHAR(16),
    ->   dropoff_location_id VARCHAR(16)
    -> );
--------------
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
)
--------------

Query OK, 0 rows affected (0.14 sec)

mysql> describe trips;  # -- checking the import
--------------
describe trips
--------------

+---------------------+-------------+------+-----+---------+-------+
| Field               | Type        | Null | Key | Default | Extra |
+---------------------+-------------+------+-----+---------+-------+
| vendor_id           | varchar(16) | YES  |     | NULL    |       |
| pickup_datetime     | datetime    | YES  |     | NULL    |       |
| dropoff_datetime    | datetime    | YES  |     | NULL    |       |
| passenger_count     | int         | YES  |     | NULL    |       |
| trip_distance       | float       | YES  |     | NULL    |       |
| rate_code           | varchar(16) | YES  |     | NULL    |       |
| store_and_fwd_flag  | varchar(16) | YES  |     | NULL    |       |
| payment_type        | varchar(16) | YES  |     | NULL    |       |
| fare_amount         | float       | YES  |     | NULL    |       |
| extra               | float       | YES  |     | NULL    |       |
| mta_tax             | float       | YES  |     | NULL    |       |
| tip_amount          | float       | YES  |     | NULL    |       |
| tolls_amount        | float       | YES  |     | NULL    |       |
| imp_surcharge       | float       | YES  |     | NULL    |       |
| total_amount        | float       | YES  |     | NULL    |       |
| pickup_location_id  | varchar(16) | YES  |     | NULL    |       |
| dropoff_location_id | varchar(16) | YES  |     | NULL    |       |
+---------------------+-------------+------+-----+---------+-------+
17 rows in set (0.11 sec)

mysql> select distinct(pickup_location_id) from trips; # -- Querying the trips table. This will return an empty set as there is no data in the database yet.
--------------
select distinct(pickup_location_id) from trips
--------------

Empty set (0.11 sec)

mysql> exit
Writing history-file /home/aham/.mysql_history
Bye


$ ls
trips.csv-1  trips.csv-2

Connect to the mysql interactive console to load local infile data:
mysql --host=$MYSQLIP --user=root  --password  --local-infile

$ mysql --host=$MYSQLIP --user=root  --password  --local-infile
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 63
Server version: 8.0.26-google (Google)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use bts; # -- select the database
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> LOAD DATA LOCAL INFILE 'trips.csv-1' INTO TABLE trips # -- Load the local CSV file data using local-infile:
    -> FIELDS TERMINATED BY ','
    -> LINES TERMINATED BY '\n'
    -> IGNORE 1 LINES
    -> (vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,rate_code,store_and_fwd_flag,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,imp_surcharge,total_amount,pickup_location_id,dropoff_location_id);
Query OK, 10018 rows affected (0.96 sec)
Records: 10018  Deleted: 0  Skipped: 0  Warnings: 0

mysql> LOAD DATA LOCAL INFILE 'trips.csv-2' INTO TABLE trips
    -> FIELDS TERMINATED BY ','
    -> LINES TERMINATED BY '\n'
    -> IGNORE 1 LINES
    -> (vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,rate_code,store_and_fwd_flag,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,imp_surcharge,total_amount,pickup_location_id,dropoff_location_id);
Query OK, 10006 rows affected (0.78 sec)
Records: 10006  Deleted: 0  Skipped: 0  Warnings: 0

mysql> select distinct(pickup_location_id) from trips;
+--------------------+
| pickup_location_id |
+--------------------+
| 68                 |
| 138                |
| 261                |
| 262                |
| 100                |
| 7                  |
| 132                |
| 264                |
| 170                |
| 237                |
| 87                 |
| 161                |
| 229                |
| 186                |
| 230                |
| 224                |
| 234                |
| 233                |
| 125                |
| 79                 |
| 162                |
| 223                |
| 236                |
| 137                |
| 225                |
| 50                 |
| 76                 |
| 13                 |
| 65                 |
| 107                |
| 231                |
| 211                |
| 48                 |
| 164                |
| 90                 |
| 24                 |
| 88                 |
| 143                |
| 246                |
| 142                |
| 215                |
| 265                |
| 238                |
| 43                 |
| 239                |
| 141                |
| 148                |
| 166                |
| 163                |
| 249                |
| 74                 |
| 158                |
| 263                |
| 144                |
| 42                 |
| 151                |
| 114                |
| 70                 |
| 75                 |
| 33                 |
| 145                |
| 140                |
| 232                |
| 113                |
| 146                |
| 45                 |
| 4                  |
| 181                |
| 152                |
| 209                |
| 260                |
| 179                |
| 93                 |
| 244                |
| 256                |
| 226                |
| 112                |
| 243                |
| 255                |
| 40                 |
| 41                 |
| 49                 |
| 189                |
| 119                |
| 66                 |
| 12                 |
| 95                 |
| 25                 |
| 37                 |
| 52                 |
| 116                |
| 17                 |
| 80                 |
| 219                |
| 130                |
| 127                |
| 194                |
| 10                 |
| 31                 |
| 197                |
| 191                |
| 171                |
| 217                |
| 129                |
| 15                 |
| 157                |
| 97                 |
| 28                 |
| 193                |
| 168                |
| 29                 |
| 216                |
| 54                 |
| 139                |
| 206                |
| 167                |
| 16                 |
| 235                |
| 102                |
| 133                |
| 185                |
| 51                 |
| 8                  |
| 198                |
| 77                 |
| 69                 |
| 61                 |
| 126                |
| 247                |
| 89                 |
| 254                |
| 106                |
| 228                |
| 169                |
| 258                |
| 173                |
| 153                |
| 196                |
| 60                 |
| 147                |
| 208                |
| 53                 |
| 35                 |
| 82                 |
| 184                |
| 47                 |
| 218                |
| 203                |
| 134                |
| 178                |
| 92                 |
| 123                |
| 36                 |
| 159                |
| 56                 |
| 83                 |
| 200                |
| 259                |
| 188                |
+--------------------+
159 rows in set (0.12 sec)

mysql> select
    ->   max(trip_distance),
    ->   min(trip_distance)
    -> from
    ->   trips;
+--------------------+--------------------+
| max(trip_distance) | min(trip_distance) |
+--------------------+--------------------+
|                 85 |                  0 |
+--------------------+--------------------+
1 row in set (0.11 sec)

mysql> select count(*) from trips where trip_distance = 0;
+----------+
| count(*) |
+----------+
|      155 |
+----------+
1 row in set (0.12 sec)

mysql> select count(*) from trips where fare_amount < 0;
+----------+
| count(*) |
+----------+
|       14 |
+----------+
1 row in set (0.12 sec)

mysql> select
    ->   payment_type,
    ->   count(*)
    -> from
    ->   trips
    -> group by
    ->   payment_type;
+--------------+----------+
| payment_type | count(*) |
+--------------+----------+
| 1            |    13863 |
| 2            |     6016 |
| 3            |      113 |
| 4            |       32 |
+--------------+----------+
4 rows in set (0.13 sec)

mysql> exit
Bye
$

```