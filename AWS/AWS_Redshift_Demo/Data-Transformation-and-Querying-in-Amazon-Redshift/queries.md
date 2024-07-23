```bash
producer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com

consumer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com

cd $HOME; pwd
sh-4.2$ cd $HOME; pwd
/home/ec2-user
sh-4.2$ cd ~
sh-4.2$ export PGPASSWORD='tkv$qKL)}5%OeLU'
sh-4.2$ psql -U dbadmin -h 'producer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com' -d producer_stocks -p 5439psql (9.2.24, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

producer_stocks=# CREATE EXTERNAL SCHEMA spectrum
producer_stocks-# FROM DATA CATALOG
producer_stocks-# DATABASE spectrumdb
producer_stocks-# IAM_ROLE 'arn:aws:iam::143369454710:role/RedshiftRole'
producer_stocks-# CREATE EXTERNAL DATABASE IF NOT EXISTS;
INFO:  External database "spectrumdb" created
CREATE SCHEMA
producer_stocks=# DROP TABLE IF EXISTS spectrum.stocksummary;
INFO:  External table "stocksummary" does not exist and will be skipped
DROP TABLE
producer_stocks=# CREATE EXTERNAL TABLE spectrum.stocksummary(
producer_stocks(#     Trade_Date VARCHAR(15),
producer_stocks(#     Ticker VARCHAR(5),
producer_stocks(#     High DECIMAL(8,2),
producer_stocks(#     Low DECIMAL(8,2),
producer_stocks(#     Open_value DECIMAL(8,2),
producer_stocks(#     Close DECIMAL(8,2),
producer_stocks(#     Volume DECIMAL(15),
producer_stocks(#     Adj_Close DECIMAL(8,2)
producer_stocks(# )
producer_stocks-# ROW FORMAT DELIMITED
producer_stocks-# FIELDS TERMINATED BY ','
producer_stocks-# STORED AS TEXTFILE
producer_stocks-# LOCATION 's3://labstack-29e32d98-34dc-411a-a712-8c6fb-databucket-1vhg4hnvp1t7p/data/';
CREATE EXTERNAL TABLE
producer_stocks=# SELECT * FROM spectrum.stocksummary
producer_stocks-#     WHERE trade_date = '2020-01-03'
producer_stocks-#     ORDER BY trade_date ASC, ticker ASC;
 trade_date | ticker |  high   |   low   | open_value |  close  |  volume   | adj_close
------------+--------+---------+---------+------------+---------+-----------+-----------
 2020-01-03 | aal    |   28.29 |   27.34 |      28.27 |   27.65 |  14008900 |     27.55
 2020-01-03 | aapl   |   75.14 |   74.13 |      74.29 |   74.36 | 146322800 |     73.38
 2020-01-03 | amzn   | 1886.20 | 1864.50 |    1864.50 | 1874.97 |   3764400 |   1874.97
 2020-01-03 | ba     |  334.89 |  330.30 |     330.63 |  332.76 |   3875900 |    330.79
 2020-01-03 | bac    |   35.15 |   34.76 |      34.98 |   34.90 |  50357900 |     33.51
 2020-01-03 | c      |   80.52 |   79.45 |      79.80 |   79.70 |  12437400 |     74.88
 2020-01-03 | chwy   |   29.40 |   28.53 |      29.00 |   29.34 |   2205300 |     29.34
 2020-01-03 | coke   |  287.36 |  277.48 |     279.77 |  285.76 |     37500 |    283.91
 2020-01-03 | dis    |  147.90 |  146.05 |     146.40 |  146.50 |   7320200 |    146.50
 2020-01-03 | f      |    9.37 |    9.15 |       9.31 |    9.21 |  45040800 |      9.06
 2020-01-03 | ge     |   96.00 |   92.24 |      92.56 |   95.76 |  10735725 |     95.13
 2020-01-03 | gs     |  232.61 |  230.30 |     231.60 |  231.58 |   2274500 |    223.41
 2020-01-03 | hsy    |  145.89 |  143.76 |     143.97 |  145.26 |    770900 |    140.04
 2020-01-03 | intc   |   60.70 |   59.81 |      59.81 |   60.10 |  15293900 |     57.56
 2020-01-03 | kodk   |    4.19 |    3.92 |       4.00 |    4.03 |    242900 |      4.03
 2020-01-03 | m      |   16.61 |   16.21 |      16.32 |   16.53 |  12026100 |     15.87
 2020-01-03 | ma     |  302.42 |  298.60 |     299.46 |  300.43 |   2501300 |    297.74
 2020-01-03 | msft   |  159.95 |  158.06 |     158.32 |  158.62 |  21116200 |    155.94
 2020-01-03 | nke    |  102.00 |  100.31 |     100.59 |  101.92 |   4541800 |    100.38
 2020-01-03 | pg     |  123.53 |  121.86 |     122.16 |  122.58 |   7970500 |    117.41
 2020-01-03 | pypl   |  110.42 |  108.76 |     109.49 |  108.76 |   7098300 |    108.76
 2020-01-03 | sq     |   63.27 |   62.33 |      62.59 |   63.00 |   5087100 |     63.00
 2020-01-03 | tsla   |   90.80 |   87.38 |      88.10 |   88.60 |  88892500 |     88.60
 2020-01-03 | v      |  190.96 |  187.92 |     188.41 |  189.60 |   4899700 |    187.62
 2020-01-03 | wmt    |  118.79 |  117.59 |     118.27 |  117.89 |   5399200 |    114.60
(25 rows)

producer_stocks=# DROP MATERIALIZED VIEW IF EXISTS stocks_mv;
INFO:  Materialized View "stocks_mv" does not exist and will be skipped
DROP MATERIALIZED VIEW
producer_stocks=# CREATE MATERIALIZED VIEW stocks_mv AS
producer_stocks-#     SELECT trade_date, ticker, volume FROM spectrum.stocksummary;
WARNING:  An incrementally maintained materialized view could not be created, reason: External tables other than Elastic Views are unsupported. The materialized view created, stocks_mv, will be recomputed from scratch for every REFRESH.
CREATE MATERIALIZED VIEW
producer_stocks=# SELECT * FROM stocks_mv
producer_stocks-#     WHERE trade_date = '2020-01-03'
producer_stocks-#     ORDER BY trade_date ASC, ticker ASC;
 trade_date | ticker |  volume
------------+--------+-----------
 2020-01-03 | aal    |  14008900
 2020-01-03 | aapl   | 146322800
 2020-01-03 | amzn   |   3764400
 2020-01-03 | ba     |   3875900
 2020-01-03 | bac    |  50357900
 2020-01-03 | c      |  12437400
 2020-01-03 | chwy   |   2205300
 2020-01-03 | coke   |     37500
 2020-01-03 | dis    |   7320200
 2020-01-03 | f      |  45040800
 2020-01-03 | ge     |  10735725
 2020-01-03 | gs     |   2274500
 2020-01-03 | hsy    |    770900
 2020-01-03 | intc   |  15293900
 2020-01-03 | kodk   |    242900
 2020-01-03 | m      |  12026100
 2020-01-03 | ma     |   2501300
 2020-01-03 | msft   |  21116200
 2020-01-03 | nke    |   4541800
 2020-01-03 | pg     |   7970500
 2020-01-03 | pypl   |   7098300
 2020-01-03 | sq     |   5087100
 2020-01-03 | tsla   |  88892500
 2020-01-03 | v      |   4899700
 2020-01-03 | wmt    |   5399200
(25 rows)

producer_stocks=# WITH tmp_variables AS (
producer_stocks(# SELECT
producer_stocks(#    '2020-10-03'::DATE AS StartDate
producer_stocks(# )
producer_stocks-#
producer_stocks-# SELECT
producer_stocks-#     ticker,
producer_stocks-#     SUM(volume) AS sum_volume
producer_stocks-# FROM stocks_mv
producer_stocks-# WHERE trade_date BETWEEN (SELECT StartDate FROM tmp_variables)-7 AND (SELECT StartDate FROM tmp_variables)
producer_stocks-# GROUP BY ticker
producer_stocks-# ORDER BY sum_volume DESC
producer_stocks-# LIMIT 3;
 ticker | sum_volume
--------+------------
 aapl   |  640562200
 aal    |  336705900
 tsla   |  270256000
(3 rows)

producer_stocks=#


producer_stocks=# CREATE DATASHARE stocks_share;
CREATE DATASHARE
producer_stocks=# ALTER DATASHARE stocks_share ADD SCHEMA public;
ALTER DATASHARE
producer_stocks=#
producer_stocks=# ALTER DATASHARE stocks_share ADD TABLE public.stocks_mv;
ALTER DATASHARE
producer_stocks=# GRANT USAGE ON DATASHARE stocks_share TO NAMESPACE 'consumer-cluster';
ERROR:  Invalid consumer principal ID.
producer_stocks=# GRANT USAGE ON DATASHARE stocks_share TO NAMESPACE '1fbcf1e2-c119-4651-8506-0883bf7ba3db';
GRANT
producer_stocks=# SELECT * FROM svv_datashares;
  share_name  | share_id | share_owner | source_database | consumer_database | share_type |     createdate      | is_publi
caccessible | share_acl | producer_account |                        producer_namespace                        | managed_by

--------------+----------+-------------+-----------------+-------------------+------------+---------------------+---------
------------+-----------+------------------+------------------------------------------------------------------+-----------
-
 stocks_share |   106522 |         100 | producer_stocks |                   | OUTBOUND   | 2023-08-11 04:09:25 | f
            |           | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475ef983                             |
(1 row)

producer_stocks=# SELECT * FROM svv_datashare_objects;
 share_type |  share_name  |    object_type    |   object_name    | producer_account |          producer_namespace
     | include_new
------------+--------------+-------------------+------------------+------------------+---------------------------------
-----+-------------
 OUTBOUND   | stocks_share | materialized view | public.stocks_mv | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475e
f983 |
 OUTBOUND   | stocks_share | schema            | public           | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475e
f983 | f
(2 rows)

producer_stocks=# SELECT * FROM svv_datashare_consumers;
  share_name  | consumer_account |          consumer_namespace          |     share_date
--------------+------------------+--------------------------------------+---------------------
 stocks_share |                  | 1fbcf1e2-c119-4651-8506-0883bf7ba3db | 2023-08-11 04:13:18
(1 row)

producer_stocks=# \q
sh-4.2$ psql -U dbadmin -h 'consumer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com' -d consumer_stocks -p 5439
psql (9.2.24, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

consumer_stocks=# SELECT * FROM svv_datashares;
  share_name  | share_id | share_owner | source_database | consumer_database | share_type | createdate | is_publicacces
sible | share_acl | producer_account |                        producer_namespace                        | managed_by
--------------+----------+-------------+-----------------+-------------------+------------+------------+---------------
------+-----------+------------------+------------------------------------------------------------------+------------
 stocks_share |          |             |                 |                   | INBOUND    |            | f
      |           | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475ef983                             |
(1 row)

consumer_stocks=# SELECT * FROM svv_datashare_objects;
 share_type |  share_name  |    object_type    |   object_name    | producer_account |          producer_namespace
     | include_new
------------+--------------+-------------------+------------------+------------------+---------------------------------
-----+-------------
 INBOUND    | stocks_share | materialized view | public.stocks_mv | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475e
f983 |
 INBOUND    | stocks_share | schema            | public           | 143369454710     | f3dcd5ec-96f1-4c6a-88ca-e868475e
f983 |
(2 rows)

consumer_stocks=# CREATE DATABASE stock_summary FROM DATASHARE stocks_share of NAMESPACE 'f3dcd5ec-96f1-4c6a-88ca-e868475ef983';
CREATE DATABASE
consumer_stocks=# SELECT * FROM stock_summary.public.stocks_mv
consumer_stocks-#     WHERE trade_date = '2020-01-03'
consumer_stocks-#     ORDER BY trade_date ASC, ticker ASC;
 trade_date | ticker |  volume
------------+--------+-----------
 2020-01-03 | aal    |  14008900
 2020-01-03 | aapl   | 146322800
 2020-01-03 | amzn   |   3764400
 2020-01-03 | ba     |   3875900
 2020-01-03 | bac    |  50357900
 2020-01-03 | c      |  12437400
 2020-01-03 | chwy   |   2205300
 2020-01-03 | coke   |     37500
 2020-01-03 | dis    |   7320200
 2020-01-03 | f      |  45040800
 2020-01-03 | ge     |  10735725
 2020-01-03 | gs     |   2274500
 2020-01-03 | hsy    |    770900
 2020-01-03 | intc   |  15293900
 2020-01-03 | kodk   |    242900
 2020-01-03 | m      |  12026100
 2020-01-03 | ma     |   2501300
 2020-01-03 | msft   |  21116200
 2020-01-03 | nke    |   4541800
 2020-01-03 | pg     |   7970500
 2020-01-03 | pypl   |   7098300
 2020-01-03 | sq     |   5087100
 2020-01-03 | tsla   |  88892500
 2020-01-03 | v      |   4899700
 2020-01-03 | wmt    |   5399200
(25 rows)

consumer_stocks=# \q
sh-4.2$ psql -U dbadmin -h 'producer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com' -d producer_stocks -p 5439psql (9.2.24, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

producer_stocks=# REVOKE USAGE ON DATASHARE stocks_share FROM NAMESPACE '1fbcf1e2-c119-4651-8506-0883bf7ba3db';
REVOKE
producer_stocks=# \q
sh-4.2$ psql -U dbadmin -h 'consumer-cluster.c1wkw85wyjsq.us-east-1.redshift.amazonaws.com' -d consumer_stocks -p 5439
psql (9.2.24, server 8.0.2)
WARNING: psql version 9.2, server version 8.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

consumer_stocks=# SELECT * FROM stock_summary.public.stocks_mv
consumer_stocks-#     WHERE trade_date = '2020-01-03'
consumer_stocks-#     ORDER BY trade_date ASC, ticker ASC;
ERROR:  The requested data share doesn't exist or is not accessible.
consumer_stocks=#


```