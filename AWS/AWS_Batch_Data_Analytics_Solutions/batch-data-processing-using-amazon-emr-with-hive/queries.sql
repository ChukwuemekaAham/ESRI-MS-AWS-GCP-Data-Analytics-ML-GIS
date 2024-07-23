CREATE TABLE stockprice  (
`Trade_Date` string,
`Ticker` string,
`High` double,
`Low` double,
`Open` double,
`Close` double,
`Volume` double,
`Adj_Close` double
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS
INPUTFORMAT
  'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://databucket-us-west-2-616274231/data/'
TBLPROPERTIES (
  "s3select.format" = "csv",
  "s3select.headerInfo" = "ignore",
  "skip.header.line.count"="1"
);

OK
Time taken: 11.03 seconds


SET s3select.filter=true;
SELECT * FROM stockprice WHERE `Trade_Date` LIKE '2020-01-03' ORDER BY `Ticker`;



SELECT `Trade_Date`, `Ticker`, `Volume` FROM stockprice ORDER BY `Volume` DESC LIMIT 10;



CREATE TABLE movies  (
`year` int,
`title` string,
`directors_0` string,
`rating` string,
`genres_0` string,
`genres_1` string,
`rank` string,
`running_time_secs` string,
`actors_0` string,
`actors_1` string,
`actors_2` string,
`directors_1` string,
`directors_2` string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS
INPUTFORMAT
  'com.amazonaws.emr.s3select.hive.S3SelectableTextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://challengebucket-us-west-2-616274231/data/'
TBLPROPERTIES (
  "s3select.format" = "csv",
  "s3select.headerInfo" = "ignore",
  "skip.header.line.count"="1"
);


SELECT COUNT(title) FROM movies WHERE actors_0='Tom Hanks' OR actors_1='Tom Hanks' OR actors_2='Tom Hanks';

