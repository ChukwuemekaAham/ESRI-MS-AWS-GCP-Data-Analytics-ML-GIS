import sys
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

bucket_name = "databucket-us-west-2-612964232"

spark =  SparkSession.builder.appName("stock-summary").getOrCreate()

stockDF =  spark.read.option("header",True).csv("s3://"+bucket_name+"/data/")

stockDF.registerTempTable("stock_data_view")

StockSummaryDF = spark.sql("SELECT `Trade_Date`, `Ticker`, `Close` FROM stock_data_view WHERE Volume > 100000 ORDER BY Close DESC")

StockSummaryDF.write.mode('overwrite').parquet("s3://"+bucket_name+"/output/")

spark.stop()
