4. Data to ML
Let's create a classification model to predict the success score of the movie based on GENRE and RUNTIME attributes. We will use the CREATE MODEL statement with the option ‘LOGISTIC_REG' to create and train a logistic regression model.

Run the below query in BigQuery console SQL Workspace QUERY EDITOR section:

```SQL
CREATE OR REPLACE MODEL
  `movie_insights.model_rating_by_runtime_genre`
OPTIONS
  ( model_type='LOGISTIC_REG',
    auto_class_weights=TRUE,
    data_split_method='NO_SPLIT',
    model_registry='vertex_ai',   
    vertex_ai_model_version_aliases=['logistic_reg', 'experimental'],
    input_label_cols=['score']
  ) AS
SELECT name, genre,runtime, score
FROM
  movie_insights.movie_score
WHERE
  data_cat = 'TRAIN';
```


Query Details:

The CREATE MODEL statement trains a model using the training data in the SELECT statement.

The OPTIONS clause specifies the model type and training options. Here, the LOGISTIC_REG option specifies a logistic regression model type. It is not necessary to specify a binary logistic regression model versus a multiclass logistic regression model: BigQuery ML can determine which to train based on the number of unique values in the label column.

data_split_method=‘NO_SPLIT' forces BQML to train on the data per the query conditions (data_cat = ‘TRAIN'), also note that it's better to use the ‘AUTO_SPLIT' in this option to allow the framework (or service in this case) to randomize the partition of train/test splits.

The input_label_cols option specifies which column in the SELECT statement to use as the label column. Here, the label column is score, so the model will learn which of the 10 values of score is most likely based on the other values present in each row.

The ‘auto_class_weights=TRUE' option balances the class labels in the training data. By default, the training data is unweighted. If the labels in the training data are imbalanced, the model may learn to predict the most popular class of labels more heavily.

The SELECT statement queries the table we loaded with the csv data. The WHERE clause filters the rows in the input table so that only the TRAIN dataset is selected in this step.

The following constructs are OPTIONAL so BigQuery ML can explicitly register it to the Vertex AI Model Registry. You can read about this more in this blog. model_registry='vertex_ai', vertex_ai_model_version_aliases=['logistic_reg', 'experimental']


After creating your model, evaluate the performance of the model using the ML.EVALUATE function. The ML.EVALUATE function evaluates the predicted values against the actual data.

You can also view the evaluation metrics of your model from the MODEL page:


## Key metrics at a glance:

- Precision - What proportion of positive identifications was actually correct? Precision = True Positive / (True Positive + False Positive) 

- Recall - What proportion of actual positives was identified correctly? Recall = True Positive / (True Positive + False Negative) 

- Accuracy - A metric for evaluating classification models, it is the fraction of predictions our model actually got right Accuracy = Number of correct predictions / Total number of predictions


5. Predicting movie score using the model
Prediction Time!!!! The following query predicts the score of each movie in the dataset that is categorized as "TEST" data.

Run the below query in BigQuery console SQL Workspace QUERY EDITOR section:

```sql
SELECT
  *
FROM
  ML.PREDICT (MODEL movie_insights.model_rating_by_runtime_genre,
    (
    SELECT
      *
    FROM
      movie_insights.movie_score
    WHERE
      data_cat= 'TEST'
     )
  );

```

The model result shows the predicted_score of the movie on a scale of 1 to 10 (classification). You must be wondering why there are several prediction rows against each movie. That is because the model has returned the possible predicted labels and the probability of occurrence of each one in the decreasing order.

Analyze predicted results and the model:

You can do two great analysis steps with the prediction to understand the results:

To understand why your model is generating these prediction results, you can use the ML.EXPLAIN_PREDICT function at https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-explain-predict

To know which features are the most important to determine the income bracket in general, you can use the ML.GLOBAL_EXPLAIN function at https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-global-explain.


6. Data to Generative AI
Let's deliver insights on the movies dataset by asking LLM (Large Language Model) the summary of factors that influence the movie score to be greater than 5, with Generative AI using Vertex AI's text-bison (latest) model using only sql queries

The table we created movie_score will be the input for this step as well.
External Connection will be created to establish the access between BigQuery ML and Vertex services.
BigQuery GENERATE_TEXT construct will be used to invoke the PaLM API remotely from Vertex AI.


7. Create an External Connection
Enable BQ Connection API if not already done and note down the Service Account id from the connection configuration details:

Click the +ADD button on the BigQuery Explorer pane (in the left of the BigQuery console) and click "Connection to external data sources" in the popular sources listed
Select Connection type as "BigLake and remote functions", provide location type as "Region" and value as "us-central1 (Iowa)" and "bq_llm_connection" as Connection ID

Once the connection is created, take a note of the Service Account generated from the connection configuration details
Grant permissions
In this step we will grant permissions to the Service Account to access the Vertex AI service:

Open IAM and add the Service Account you copied after creating the external connection as the Principal and select "Vertex AI User" Role


8. Create a remote ML model
Create the remote model that represents a hosted Vertex AI large language model:

```sql
CREATE OR REPLACE MODEL
  movie_insights.llm_model REMOTE
WITH CONNECTION `us-central1.bq_llm_connection` OPTIONS (remote_service_type = 'CLOUD_AI_LARGE_LANGUAGE_MODEL_V1');

```
It creates a model named llm_model in the dataset movie_insights which leverages the CLOUD_AI_LARGE_LANGUAGE_MODEL_V1 API of Vertex AI as a remote function. This will take several seconds to complete.


9. Generate text using the ML model
Once the model is created, use the model to generate, summarize or categorize text.

```sql
SELECT
  ml_generate_text_result['predictions'][0]['content'] AS generated_text,
  ml_generate_text_result['predictions'][0]['safetyAttributes']
    AS safety_attributes,
  * EXCEPT (ml_generate_text_result)
FROM
  ML.GENERATE_TEXT(
    MODEL `movie_insights.llm_model`,
    (
 SELECT
      CONCAT('FROM THE FOLLOWING TEXT ABOUT MOVIES, WHAT DO YOU THINK ARE THE FACTORS INFLUENCING A MOVIE SCORE TO BE GREATER THAN 5?: ', movie_data) AS prompt
    FROM (
      SELECT
        REPLACE(STRING_AGG( CONCAT('A movie named ',name, ' from the country ', country, ' with a censor rating of ',rating, ' and a budget of ', budget, ' produced by ', company, ' with a runtime of about ', runtime, ' and in the genre ', genre, ' starring ', star, ' has had a success score of ', score, '') ), ',','. ') AS movie_data
      FROM (
        SELECT
          *
        FROM
          `movie_insights.movie_score`
        WHERE
          CAST(SCORE AS INT64) > 5
        LIMIT
          50) ) AS MOVIES
    ),
    STRUCT(
      0.2 AS temperature,
      100 AS max_output_tokens));
```
**Explanation:

ml_generate_text_result** is the response from the text generation model in JSON format that contains both content and safety attributes: a. Content represents the generated text result b. Safety Attributes represent the built-in content filter with an adjustable threshold that is enabled in Vertex AI Palm API to avoid any unintended or unforeseen responses from the large language model - the response is blocked if it violates the safety threshold

ML.GENERATE_TEXT is the construct you use in BigQuery to access the Vertex AI LLM to perform text generation tasks

CONCAT appends your PROMPT statement and the database record

movie_insights is the dataset name and movie_score is the name of the table that has the data we will use in the prompt design

Temperature is the prompt parameter to control the randomness of the response - lesser the better in terms of relevance

Max_output_tokens is the number of words you want in response

10. Flatten the query result
Let's flatten the result so we don't have to decode the JSON explicitly in the query:

```sql
SELECT
  *
FROM
  ML.GENERATE_TEXT( MODEL movie_insights.llm_model,
    (
    SELECT
      CONCAT('FROM THE FOLLOWING TEXT ABOUT MOVIES, WHAT DO YOU THINK ARE THE FACTORS INFLUENCING A MOVIE SCORE TO BE GREATER THAN 5?: ', movie_data) AS prompt
    FROM (
      SELECT
        REPLACE(STRING_AGG( CONCAT('A movie named ',name, ' from the country ', country, ' with a censor rating of ',rating, ' and a budget of ', budget, ' produced by ', company, ' with a runtime of about ', runtime, ' and in the genre ', genre, ' starring ', star, ' has had a success score of ', score, '') ), ',','. ') AS movie_data
      FROM (
        SELECT
          *
        FROM
          `movie_insights.movie_score`
        WHERE
          CAST(SCORE AS INT64) > 5
        LIMIT
          50) ) AS MOVIES),
    STRUCT( 0.2 AS temperature,
      100 AS max_output_tokens,
      TRUE AS flatten_json_output));
**Explanation:
```
Flatten_json_output** represents the boolean, which if set true returns a flat understandable text extracted from the JSON response.

Congratulations! You have successfully created a BQML model and performed LLM based analytics using a Vertex AI API on your movies dataset only using SQL-queries. Check out Vertex AI LLM product documentation to learn more about available models.
