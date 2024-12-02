# Predicting the number of transactions each visitor would make

**[UA] Google Analytics sample dataset for BigQuery**

The sample dataset provides an obfuscated Google Analytics 360 dataset that can be accessed via BigQuery. It’s a great way to look at business data and experiment and learn the benefits of analyzing Google Analytics 360 data in BigQuery.


## What about BigQuery ML

BigQuery ML enables users to create and execute machine learning models in BigQuery using SQL queries. The goal is to democratize machine learning by enabling SQL practitioners to build models using their existing tools and to increase development speed by eliminating the need for data movement.

I used the sample [Google Analytics sample dataset for BigQuery](https://support.google.com/analytics/answer/7586738?hl=en&ref_topic=3416089) to create a model that predicts whether a website visitor will make a transaction. For information on the schema of the Analytics dataset, see [BigQuery export schema](https://support.google.com/analytics/answer/3437719) in the Google Analytics Help Center.


## Objectives
+ BigQuery ML to create a binary logistic regression model using the `CREATE MODEL` statement
+ The `ML.EVALUATE` function to evaluate the ML model
+ The `ML.PREDICT` function to make predictions using the ML model