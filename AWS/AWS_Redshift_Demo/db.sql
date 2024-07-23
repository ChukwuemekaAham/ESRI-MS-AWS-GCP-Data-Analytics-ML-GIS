CREATE SCHEMA IF NOT EXISTS stocksummary;

CREATE TABLE IF NOT EXISTS stocks (
    Trade_Date VARCHAR(15) NOT NULL,
    Ticker VARCHAR(15) NOT NULL,
    High DECIMAL(8,2) NOT NULL,
    Low DECIMAL(8,2) NOT NULL,
    Open DECIMAL(8,2) NOT NULL,
    Close DECIMAL(8,2) NOT NULL,
    Volume DECIMAL(15) NOT NULL,
    Adj_Close DECIMAL(8,2) NOT NULL
);


COPY stocksummary
FROM 's3://INSERT_DATA_BUCKET_NAME/data/stock_prices.csv'
iam_role 'INSERT_REDSHIFT_ROLE' 
CSV IGNOREHEADER 1;


SELECT * FROM stocksummary WHERE Trade_Date LIKE '2020-01-03' ORDER BY Ticker;


select a.ticker, a.trade_date, '$'||a.adj_close as highest_stock_price
from stocksummary a,
  (select ticker, max(adj_close) adj_close
  from stocksummary x
  group by ticker) b
where a.ticker = b.ticker
  and a.adj_close = b.adj_close
order by a.ticker

SELECT * FROM STL_LOAD_ERRORS

CREATE TABLE IF NOT EXISTS movies  (
        year VARCHAR(4) DEFAULT NULL,
        title VARCHAR(200) DEFAULT NULL,
        directors VARCHAR(35) DEFAULT NULL,
        rating VARCHAR(10) DEFAULT NULL,
        genres_0 VARCHAR(35) DEFAULT NULL,
        genres_1 VARCHAR(35) DEFAULT NULL,
        rank VARCHAR(10) DEFAULT NULL,
        running_time_secs VARCHAR(35) DEFAULT NULL,
        actors_0 VARCHAR(35) DEFAULT NULL,
        actors_1 VARCHAR(35) DEFAULT NULL,
        actors_2 VARCHAR(35) DEFAULT NULL,
        directors_1 VARCHAR(35) DEFAULT NULL,
        directors_2 VARCHAR(35) DEFAULT NULL
)

COPY movies
FROM 's3://INSERT_CHALLENGE_BUCKET_NAME/data/movies.csv'
iam_role 'INSERT_REDSHIFT_ROLE' 
CSV IGNOREHEADER 1;

SELECT title FROM movies WHERE actors_0='Mark Wahlberg' OR actors_1='Mark Wahlberg' OR actors_2='Mark Wahlberg';
