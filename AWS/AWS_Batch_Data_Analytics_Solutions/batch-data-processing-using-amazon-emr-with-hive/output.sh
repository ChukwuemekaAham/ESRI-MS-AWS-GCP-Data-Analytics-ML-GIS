sh-4.2$ ssh -i ~/EMRKey.pem hadoop@$HOST
ssh: Could not resolve hostname : Name or service not known
sh-4.2$ export ID=$(aws emr list-clusters | jq '.Clusters[0].Id' | tr -d '"')
sh-4.2$ export HOST=$(aws emr describe-cluster --cluster-id $ID | jq '.Cluster.MasterPublicDnsName' | tr -d '"')
sh-4.2$ ssh -i ~/EMRKey.pem hadoop@$HOST
Last login: Sun Jul 30 19:23:14 2023 from ip-10-0-10-61.us-west-2.compute.internal

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/

EEEEEEEEEEEEEEEEEEEE MMMMMMMM           MMMMMMMM RRRRRRRRRRRRRRR
E::::::::::::::::::E M:::::::M         M:::::::M R::::::::::::::R
EE:::::EEEEEEEEE:::E M::::::::M       M::::::::M R:::::RRRRRR:::::R
  E::::E       EEEEE M:::::::::M     M:::::::::M RR::::R      R::::R
  E::::E             M::::::M:::M   M:::M::::::M   R:::R      R::::R
  E:::::EEEEEEEEEE   M:::::M M:::M M:::M M:::::M   R:::RRRRRR:::::R
  E::::::::::::::E   M:::::M  M:::M:::M  M:::::M   R:::::::::::RR
  E:::::EEEEEEEEEE   M:::::M   M:::::M   M:::::M   R:::RRRRRR::::R
  E::::E             M:::::M    M:::M    M:::::M   R:::R      R::::R
  E::::E       EEEEE M:::::M     MMM     M:::::M   R:::R      R::::R
EE:::::EEEEEEEE::::E M:::::M             M:::::M   R:::R      R::::R
E::::::::::::::::::E M:::::M             M:::::M RR::::R      R::::R
EEEEEEEEEEEEEEEEEEEE MMMMMMM             MMMMMMM RRRRRRR      RRRRRR

[hadoop@ip-10-0-20-146 ~]$ sudo chown hadoop -R /var/log/hive
[hadoop@ip-10-0-20-146 ~]$ mkdir /var/log/hive/user/hadoop
mkdir: cannot create directory ‘/var/log/hive/user/hadoop’: File exists
[hadoop@ip-10-0-20-146 ~]$ hive
Hive Session ID = 1fc023b2-4770-4e9b-8808-b6032d137c8d

Logging initialized using configuration in file:/etc/hive/conf.dist/hive-log4j2.properties Async: true
Hive Session ID = 9a6001a4-9d0a-4c33-a096-34a87cd69724
hive> CREATE TABLE stockprice  (
    > `Trade_Date` string,
    > `Ticker` string,
    > `High` double,
    > `Low` double,
    > `Open` double,
    > `Close` double,
    > `Volume` double,
    > `Adj_Close` double
    > )
    > ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    > STORED AS
    > INPUTFORMAT
    >   'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
    > OUTPUTFORMAT
    >   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    > LOCATION 's3://databucket-us-west-2-616274231/data/'
    > TBLPROPERTIES (
    >   "s3select.format" = "csv",
    >   "s3select.headerInfo" = "ignore",
    >   "skip.header.line.count"="1"
    > );
OK
Time taken: 11.03 seconds


hive> SET s3select.filter=true;
hive> SELECT * FROM stockprice WHERE `Trade_Date` LIKE '2020-01-03' ORDER BY `Ticker`;
Query ID = hadoop_20230730200316_048204e0-43bd-4672-8366-23d9378e4785
Total jobs = 1
Launching Job 1 out of 1
Status: Running (Executing on YARN cluster with App id application_1690744128763_0004)

----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED      1          1        0        0       0       0
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 15.70 s
----------------------------------------------------------------------------------------------
OK
2020-01-03      aapl    75.1449966430664        74.125  74.2874984741211        74.35749816894531       1.463228E8      73.48602294921875
2020-01-03      amzn    1886.199951171875       1864.5  1864.5  1874.969970703125       3764400.0       1874.969970703125
2020-01-03      ge      12.0    11.529999732971191      11.569999694824219      11.970000267028809      8.58858E7       11.900788307189941
2020-01-03      m       16.610000610351562      16.209999084472656      16.31999969482422       16.530000686645508      1.20261E7    15.871587753295898
2020-01-03      msft    159.9499969482422       158.05999755859375      158.32000732421875      158.6199951171875       2.11162E7    156.23582458496094
2020-01-03      sq      63.27000045776367       62.33000183105469       62.59000015258789       63.0    5087100.0       63.0
2020-01-03      tsla    90.80000305175781       87.38400268554688       88.0999984741211        88.60199737548828       8.88925E7    88.60199737548828
Time taken: 23.083 seconds, Fetched: 7 row(s)
hive> SELECT `Trade_Date`, `Ticker`, `Volume` FROM stockprice ORDER BY `Volume` DESC LIMIT 10;
Query ID = hadoop_20230730200412_dad41c45-4457-4208-9569-e1f44fa4dc58
Total jobs = 1
Launching Job 1 out of 1
Status: Running (Executing on YARN cluster with App id application_1690744128763_0004)

----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED      1          1        0        0       0       0
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 10.08 s
----------------------------------------------------------------------------------------------
OK
2020-02-28      aapl    4.2651E8
2020-03-12      aapl    4.18474E8
2020-03-20      aapl    4.016932E8
2020-07-31      aapl    3.743368E8
2020-03-13      aapl    3.70732E8
2020-08-24      aapl    3.459376E8
2020-03-02      aapl    3.413972E8
2020-08-21      aapl    3.380548E8
2020-03-23      aapl    3.367528E8
2020-09-04      aapl    3.326072E8
Time taken: 11.443 seconds, Fetched: 10 row(s)
hive> CREATE TABLE movies  (
    > `year` int,
    > `title` string,
    > `directors_0` string,
    > `rating` string,
    > `genres_0` string,
    > `genres_1` string,
    > `rank` string,
    > `running_time_secs` string,
    > `actors_0` string,
    > `actors_1` string,
    > `actors_2` string,
    > `directors_1` string,
    > `directors_2` string
    > )
    > ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    > STORED AS
    > INPUTFORMAT
    >   'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
    > OUTPUTFORMAT
    >   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
    > LOCATION 's3://challengebucket-us-west-2-616274231/data/'
    > TBLPROPERTIES (
    >   "s3select.format" = "csv",
    >   "s3select.headerInfo" = "ignore",
    >   "skip.header.line.count"="1"
    > );
OK
Time taken: 0.939 seconds
hive> SELECT COUNT(title) FROM movies WHERE actors_0='Tom Hanks' OR actors_1='Tom Hanks' OR actors_2='Tom Hanks';
Query ID = hadoop_20230730200612_96310eac-b08c-40bf-99a9-5b255f6497b3
Total jobs = 1
Launching Job 1 out of 1
Status: Running (Executing on YARN cluster with App id application_1690744128763_0004)

----------------------------------------------------------------------------------------------
        VERTICES      MODE        STATUS  TOTAL  COMPLETED  RUNNING  PENDING  FAILED  KILLED
----------------------------------------------------------------------------------------------
Map 1 .......... container     SUCCEEDED      1          1        0        0       0       0
Reducer 2 ...... container     SUCCEEDED      1          1        0        0       0       0
----------------------------------------------------------------------------------------------
VERTICES: 02/02  [==========================>>] 100%  ELAPSED TIME: 11.61 s
----------------------------------------------------------------------------------------------
OK
30
Time taken: 13.09 seconds, Fetched: 1 row(s)
hive> [hadoop@ip-10-0-20-146 ~]$