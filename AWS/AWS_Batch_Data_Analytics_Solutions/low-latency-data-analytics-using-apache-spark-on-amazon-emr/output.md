```bash
sh-4.2$ # Get EMR Cluster ID and export to the Environment.
sh-4.2$ export ID=$(aws emr list-clusters | jq '.Clusters[0].Id' | tr -d '"')
sh-4.2$
sh-4.2$ # Use the ID to get the PublicDNS name of the EMR Cluster
sh-4.2$ # and export to the Environment.
sh-4.2$ export HOST=$(aws emr describe-cluster --cluster-id $ID | jq '.Cluster.MasterPublicDnsName' | tr -d '"')
sh-4.2$
sh-4.2$ # SSH to the EMR cluster
sh-4.2$ ssh -i ~/EMRKey.pem hadoop@$HOST
The authenticity of host 'ec2-35-91-154-24.us-west-2.compute.amazonaws.com (10.0.10.20)' can't be established.
ECDSA key fingerprint is SHA256:oV/6hRiC30t4spbNfFBrlxgOQ7Kddc7+8WWQZDzJLAE.
ECDSA key fingerprint is MD5:f7:06:99:1b:36:d1:a2:c5:af:78:b3:af:50:96:ab:92.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ec2-35-91-154-24.us-west-2.compute.amazonaws.com,10.0.10.20' (ECDSA) to the list of known hosts.
Last login: Sun Aug  6 16:35:06 2023

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
91 package(s) needed for security, out of 142 available
Run "sudo yum update" to apply all updates.

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

[hadoop@ip-10-0-10-20 ~]$ pyspark
Python 3.7.16 (default, Mar 10 2023, 03:25:26)
[GCC 7.3.1 20180712 (Red Hat 7.3.1-15)] on linux
Type "help", "copyright", "credits" or "license" for more information.

Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
23/08/06 16:41:34 WARN Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.1-amzn-0
      /_/

Using Python version 3.7.16 (default, Mar 10 2023 03:25:26)
Spark context Web UI available at http://ip-10-0-10-20.us-west-2.compute.internal:4040
Spark context available as 'sc' (master = yarn, app id = application_1691339165261_0001).
SparkSession available as 'spark'.
>>>
>>> import sys
>>> import time
>>> from pyspark.sql import SparkSession
>>> from pyspark.sql.functions import *
>>> from pyspark.sql.types import *
>>> spark =  SparkSession.builder.appName("stock-summary").getOrCreate()
>>>
>>> dataBucket = 'databucket-us-west-2-165206281'
>>> df = spark.read.csv("s3://"+dataBucket+"/data/stock_prices.csv", header=True, inferSchema=True).select('Trade_Date', 'Ticker', 'Close', 'Volume')
>>> df.sort(df.Trade_Date, ascending=True).show(7)
+----------+------+------------------+----------+
|Trade_Date|Ticker|             Close|    Volume|
+----------+------+------------------+----------+
|2020-01-02|    sq| 63.83000183105469| 5264700.0|
|2020-01-02|  aapl|  75.0875015258789|1.354804E8|
|2020-01-02|  amzn| 1898.010009765625| 4029000.0|
|2020-01-02|     m|16.520000457763672| 2.63881E7|
|2020-01-02|  tsla|   86.052001953125| 4.76605E7|
|2020-01-02|  msft| 160.6199951171875| 2.26221E7|
|2020-01-02|    ge|11.930000305175781| 8.74218E7|
+----------+------+------------------+----------+
only showing top 7 rows

>>> ("Total number of stocks records: " + str(df.count()))
'Total number of stocks records: 1771'
>>> dfVol = df.filter( (df.Volume > 10000000)).sort(df.Volume, ascending=False)
>>> dfVol.show(10)
+----------+------+------------------+----------+
|Trade_Date|Ticker|             Close|    Volume|
+----------+------+------------------+----------+
|2020-02-28|  aapl| 68.33999633789062|  4.2651E8|
|2020-03-12|  aapl|62.057498931884766| 4.18474E8|
|2020-03-20|  aapl|57.310001373291016|4.016932E8|
|2020-07-31|  aapl|106.26000213623047|3.743368E8|
|2020-03-13|  aapl| 69.49250030517578| 3.70732E8|
|2020-08-24|  aapl|125.85749816894531|3.459376E8|
|2020-03-02|  aapl| 74.70249938964844|3.413972E8|
|2020-08-21|  aapl|124.37000274658203|3.380548E8|
|2020-03-23|  aapl|56.092498779296875|3.367528E8|
|2020-09-04|  aapl|120.95999908447266|3.326072E8|
+----------+------+------------------+----------+
only showing top 10 rows

>>> df.createOrReplaceTempView("stockprice")
>>> dfSql = spark.sql("SELECT Trade_Date, Ticker, round(DOUBLE(Close),2) AS Closing_Value, Volume  FROM stockprice WHERE Volume > 10000000 ORDER BY Close DESC LIMIT 10")
>>> dfSql.sort(dfSql.Volume, ascending=False).show()
+----------+------+-------------+----------+
|Trade_Date|Ticker|Closing_Value|    Volume|
+----------+------+-------------+----------+
|2020-12-18|  tsla|        695.0|2.221262E8|
|2020-12-31|  tsla|       705.67| 4.96499E7|
|2020-12-30|  tsla|       694.78|  4.2846E7|
|2020-12-28|  tsla|       663.69| 3.22786E7|
|2020-12-29|  tsla|       665.99| 2.29108E7|
|2020-01-31|  amzn|      2008.72| 1.55673E7|
|2020-04-16|  amzn|      2408.19| 1.20382E7|
|2020-03-12|  amzn|      1676.61| 1.13462E7|
|2020-03-17|  amzn|      1807.84| 1.09171E7|
|2020-03-19|  amzn|      1880.93| 1.03999E7|
+----------+------+-------------+----------+

>>>



**************CHALLENGE*************************************



>>> spark =  SparkSession.builder.appName("movie-summary").getOrCreate()
>>> df_challenge = spark.read.csv("s3://challengebucket-us-west-2-165206281/data/movies.csv", header=True, inferSchema=True).select('year','title','directors_0','rating','actors_0','actors_1','actors_2')
>>> dfJodieFoster = df_challenge.filter( (df_challenge.actors_0 == "Jodie Foster") | (df_challenge.actors_1 == "Jodie Foster") | (df_challenge.actors_2 == "Jodie Foster") ).sort(df_challenge.year, ascending=True)
>>> rows = dfJodieFoster.count()
>>> dfJodieFoster.show()
+----+--------------------+------------------+------+-----------------+-------------------+------------------+
|year|               title|       directors_0|rating|         actors_0|           actors_1|          actors_2|
+----+--------------------+------------------+------+-----------------+-------------------+------------------+
|1976|The Little Girl W...|   Nicolas Gessner|   7.0|     Jodie Foster|       Martin Sheen|      Alexis Smith|
|1976|        Bugsy Malone|       Alan Parker|   6.5|     Jodie Foster|         Scott Baio|    Florrie Dugger|
|1991|The Silence of th...|    Jonathan Demme|   8.7|     Jodie Foster|    Anthony Hopkins|Lawrence A. Bonney|
|1994|                Nell|     Michael Apted|   6.3|     Jodie Foster|        Liam Neeson|Natasha Richardson|
|1994|            Maverick|    Richard Donner|   6.9|       Mel Gibson|       Jodie Foster|      James Garner|
|1997|             Contact|   Robert Zemeckis|   7.3|     Jodie Foster|Matthew McConaughey|      Tom Skerritt|
|1999|   Anna and the King|      Andy Tennant|   6.5|     Jodie Foster|       Yun-Fat Chow|          Bai Ling|
|2002|          Panic Room|     David Fincher|   6.8|     Jodie Foster|    Kristen Stewart|   Forest Whitaker|
|2004|Un long dimanche ...|Jean-Pierre Jeunet|   7.7|    Audrey Tautou|     Gaspard Ulliel|      Jodie Foster|
|2005|          Flightplan|  Robert Schwentke|   6.1|     Jodie Foster|    Peter Sarsgaard|         Sean Bean|
|2006|          Inside Man|         Spike Lee|   7.6|Denzel Washington|         Clive Owen|      Jodie Foster|
|2007|       The Brave One|       Neil Jordan|   6.7|     Jodie Foster|    Terrence Howard|    Naveen Andrews|
|2008|        Nim's Island| Jennifer Flackett|   5.9|     Jodie Foster|      Gerard Butler|   Abigail Breslin|
|2011|             Carnage|    Roman Polanski|   7.1|     Jodie Foster|       Kate Winslet|   Christoph Waltz|
|2011|          The Beaver|      Jodie Foster|   6.6|       Mel Gibson|       Jodie Foster|     Anton Yelchin|
|2013|             Elysium|    Neill Blomkamp|   7.0|       Matt Damon|       Jodie Foster|    Sharlto Copley|
+----+--------------------+------------------+------+-----------------+-------------------+------------------+

>>> print(f"Total number of movies : {rows}")
Total number of movies : 16
>>>
>>> spark =  SparkSession.builder.appName("movies").getOrCreate()
>>> dataBucket = 'challengebucket-us-west-2-165206281'
>>> dfmovies = spark.read.csv("s3://"+dataBucket+"/data/movies.csv", header=True, inferSchema=True).select('year', 'title', 'rating', 'actors_0','actors_1','actors_2')
>>> dfmovies.show(10)
+----+--------------------+------+-----------------+---------------+------------------+
|year|               title|rating|         actors_0|       actors_1|          actors_2|
+----+--------------------+------+-----------------+---------------+------------------+
|2013|                Rush|   8.3|     Daniel Bruhl|Chris Hemsworth|      Olivia Wilde|
|2013|           Prisoners|   8.2|     Hugh Jackman|Jake Gyllenhaal|       Viola Davis|
|2013|The Hunger Games:...|  null|Jennifer Lawrence|Josh Hutcherson|    Liam Hemsworth|
|2013|Thor: The Dark World|  null|  Chris Hemsworth|Natalie Portman|    Tom Hiddleston|
|2013|     This Is the End|   7.2|     James Franco|     Jonah Hill|        Seth Rogen|
|2013|Insidious: Chapter 2|   7.1|   Patrick Wilson|     Rose Byrne|   Barbara Hershey|
|2013|         World War Z|   7.1|        Brad Pitt|  Mireille Enos|  Daniella Kertesz|
|2014|X-Men: Days of Fu...|  null|Jennifer Lawrence|   Hugh Jackman|Michael Fassbender|
|2014|Transformers: Age...|  null|    Mark Wahlberg|   Nicola Peltz|       Jack Reynor|
|2013|      Now You See Me|   7.3|  Jesse Eisenberg|         Common|      Mark Ruffalo|
+----+--------------------+------+-----------------+---------------+------------------+
only showing top 10 rows

>>> dfmovies.createOrReplaceTempView("movies_view")
>>> dfmovies = spark.sql("SELECT year, title, rating, actors_0, actors_1, actors_2 FROM movies_view WHERE actors_0 = 'Jodie Foster' OR actors_1 = 'Jodie Foster' OR actors_2 = 'Jodie Foster' ORDER BY year ASC")
>>> dfmovies.show()
+----+--------------------+------+-----------------+-------------------+------------------+
|year|               title|rating|         actors_0|           actors_1|          actors_2|
+----+--------------------+------+-----------------+-------------------+------------------+
|1976|The Little Girl W...|   7.0|     Jodie Foster|       Martin Sheen|      Alexis Smith|
|1976|        Bugsy Malone|   6.5|     Jodie Foster|         Scott Baio|    Florrie Dugger|
|1991|The Silence of th...|   8.7|     Jodie Foster|    Anthony Hopkins|Lawrence A. Bonney|
|1994|                Nell|   6.3|     Jodie Foster|        Liam Neeson|Natasha Richardson|
|1994|            Maverick|   6.9|       Mel Gibson|       Jodie Foster|      James Garner|
|1997|             Contact|   7.3|     Jodie Foster|Matthew McConaughey|      Tom Skerritt|
|1999|   Anna and the King|   6.5|     Jodie Foster|       Yun-Fat Chow|          Bai Ling|
|2002|          Panic Room|   6.8|     Jodie Foster|    Kristen Stewart|   Forest Whitaker|
|2004|Un long dimanche ...|   7.7|    Audrey Tautou|     Gaspard Ulliel|      Jodie Foster|
|2005|          Flightplan|   6.1|     Jodie Foster|    Peter Sarsgaard|         Sean Bean|
|2006|          Inside Man|   7.6|Denzel Washington|         Clive Owen|      Jodie Foster|
|2007|       The Brave One|   6.7|     Jodie Foster|    Terrence Howard|    Naveen Andrews|
|2008|        Nim's Island|   5.9|     Jodie Foster|      Gerard Butler|   Abigail Breslin|
|2011|             Carnage|   7.1|     Jodie Foster|       Kate Winslet|   Christoph Waltz|
|2011|          The Beaver|   6.6|       Mel Gibson|       Jodie Foster|     Anton Yelchin|
|2013|             Elysium|   7.0|       Matt Damon|       Jodie Foster|    Sharlto Copley|
+----+--------------------+------+-----------------+-------------------+------------------+

>>> dfmovies.count()
16
>>>

```
