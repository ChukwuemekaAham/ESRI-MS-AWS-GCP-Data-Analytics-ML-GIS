
CREATE EXTERNAL SCHEMA spectrum
FROM DATA CATALOG
DATABASE spectrumdb
IAM_ROLE 'INSERT_REDSHIFT_ROLE'
CREATE EXTERNAL DATABASE IF NOT EXISTS;


DROP TABLE IF EXISTS spectrum.stocksummary;
CREATE EXTERNAL TABLE spectrum.stocksummary(
    Trade_Date VARCHAR(15),
    Ticker VARCHAR(5),
    High DECIMAL(8,2),
    Low DECIMAL(8,2),
    Open_value DECIMAL(8,2),
    Close DECIMAL(8,2),
    Volume DECIMAL(15),
    Adj_Close DECIMAL(8,2)
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 's3://INSERT_DATA_BUCKET/data/';


SELECT * FROM spectrum.stocksummary
    WHERE trade_date = '2020-01-03'
    ORDER BY trade_date ASC, ticker ASC;



DROP MATERIALIZED VIEW IF EXISTS stocks_mv;
CREATE MATERIALIZED VIEW stocks_mv AS
    SELECT trade_date, ticker, volume FROM spectrum.stocksummary;


SELECT * FROM stocks_mv
    WHERE trade_date = '2020-01-03'
    ORDER BY trade_date ASC, ticker ASC;


WITH tmp_variables AS (
SELECT 
   '2020-10-03'::DATE AS StartDate
)
   
SELECT
    ticker,
    SUM(volume) AS sum_volume
FROM stocks_mv
WHERE trade_date BETWEEN (SELECT StartDate FROM tmp_variables)-7 AND (SELECT StartDate FROM tmp_variables)
GROUP BY ticker
ORDER BY sum_volume DESC
LIMIT 3;



CREATE DATASHARE stocks_share;


ALTER DATASHARE stocks_share ADD SCHEMA public;
ALTER DATASHARE stocks_share ADD TABLE public.stocks_mv;


GRANT USAGE ON DATASHARE stocks_share TO NAMESPACE 'INSERT_CONSUMER_NAMESPACE_ID';


SELECT * FROM svv_datashares;


SELECT * FROM svv_datashare_objects;


SELECT * FROM svv_datashare_consumers;


SELECT * FROM svv_datashares;


CREATE DATABASE stock_summary FROM DATASHARE stocks_share of NAMESPACE 'INSERT_PRODUCER_NAMESPACE_ID';


SELECT * FROM stock_summary.public.stocks_mv
    WHERE trade_date = '2020-01-03'
    ORDER BY trade_date ASC, ticker ASC;


REVOKE USAGE ON DATASHARE stocks_share FROM NAMESPACE 'INSERT_CONSUMER_NAMESPACE_ID';



SELECT * FROM stock_summary.public.stocks_mv
    WHERE trade_date = '2020-01-03'
    ORDER BY trade_date ASC, ticker ASC;


SELECT
    ticker,
    SUM(volume) AS sum_volume
FROM stocks_mv
WHERE trade_date BETWEEN GETDATE()-7 AND GETDATE()
GROUP BY ticker
ORDER BY sum_volume DESC
LIMIT 3;