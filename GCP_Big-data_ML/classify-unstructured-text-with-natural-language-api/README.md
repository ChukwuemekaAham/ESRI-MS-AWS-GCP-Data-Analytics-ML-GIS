# Using the Natural Language API to classify news articles (unstructured text)

## Overview
The Cloud Natural Language API lets you extract entities from text, perform sentiment and syntactic analysis, and classify text into categories. 

The focus was on text classification. Using a database of 700+ categories, this API feature makes it easy to classify a large dataset of text.

## Objectives:
•	Create a Natural Language API request and calling the API with curl
•	Use the NL API's text classification feature
•	Use text classification to understand the dataset of news articles
•	Use the Google Cloud Python module to analyze the large news dataset
•	Import and analyze the data in BigQuery

- Enable Confirm that the Cloud Natural Language API is enabled
- Create an API key: Since I used curl to send a request to the Natural Language API, I needed to generate an API key to pass in the request URL.
- Create a service account. This will be used to authenticate to the Natural Language API and BigQuery from a Python script.

You can create a new API key doing something like this:
1.	To create an API key, from the Console, click Navigation menu > APIs & services > Credentials.
2.	Then click + CREATE CREDENTIALS.
3.	In the drop down menu, select API key:
4.	Next, copy the key you just generated. Then click CLOSE.

```bash
export API_KEY=<YOUR_API_KEY>
```

- Classifying a news article

Using the Natural Language API's classifyText method, you can sort text data into categories with a single API call. This method returns a list of content categories that apply to a text document. These categories range in specificity, from broad categories like /Computers & Electronics to highly specific categories such as /Computers & Electronics/Programming/Java (Programming Language). A full list of 700+ possible categories can be found in the Content Categories Guide.

## Classifying a single article

Headline and description from a New York Times article in the food section:

A Smoky Lobster Salad With a Tapa Twist. This spin on the Spanish pulpo a la gallega skips the octopus, but keeps the sea salt, olive oil, pimentón and boiled potatoes.

SEE: 

`request.json` file

Sending the text to the Natural Language API's classifyText method with the following curl command:
```bash
curl "https://language.googleapis.com/v1/documents:classifyText?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @request.json
Copied!
content_copy
Look at the response:
Output:
{ categories:
  [
    {
      name: '/Food & Drink/Cooking & Recipes',
      confidence: 0.85
    },
    {
      name: '/Food & Drink/Food/Meat & Seafood',
      confidence: 0.63
    }
  ]
}
```
The API returned 2 categories for this text:
•	/Food & Drink/Cooking & Recipes
•	/Food & Drink/Food/Meat & Seafood


The text doesn't explicitly mention that this is a recipe or even that it includes seafood, but the API is able to categorize it.
Classifying a single article is cool, but to really see the power of this feature, let's classify lots of text data.


## Classifying a large text dataset

Using the public dataset of **BBC news articles**. The dataset consists of 2,225 articles in five topic areas (business, entertainment, politics, sports, tech) from 2004 - 2005. A subset of these articles are in a public Google Cloud Storage bucket. Each of the articles is in a .txt file.

To examine the data and send it to the Natural Language API, a Python script was used to read each text file from Cloud Storage, send it to the classifyText endpoint, and store the results in a BigQuery table. 

SEE: `./classfy-text.py` file


- Creating a BigQuery table for our categorized text data
Before sending the text to the Natural Language API, you need a place to store the text and category for each article.

1.	In the Google Cloud console, click Navigation menu ( ) > BigQuery.
2.	Click Done for the welcome notice when launching BigQuery.
3.	In the left panel, click the View actions icon ( ) next to your project name and click Create dataset.
4.	For Dataset ID, type news_classification_dataset
5.	Click Create dataset.
6.	Click on the View actions icon next to your dataset name and click Create table. 

- Use the following settings for the new table:
•	Create table from: Empty table
•	Name your table article_data
•	Click Add Field (+) under Schema, and add the following 3 fields: article_text with type STRING, category with type STRING, and confidence with type FLOAT.
6.	Click CREATE TABLE.

The table is initially empty. Read the articles from Cloud Storage, send them to the Natural Language API for classification, and store the result in BigQuery.

- Classifying news data and storing the result in BigQuery

- Create a service account:
```bash
gcloud iam service-accounts create my-account --display-name my-account
gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:my-account@$PROJECT.iam.gserviceaccount.com --role=roles/bigquery.admin
gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:my-account@$PROJECT.iam.gserviceaccount.com --role=roles/serviceusage.serviceUsageConsumer
gcloud iam service-accounts keys create key.json --iam-account=my-account@$PROJECT.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS=key.json
```

Now ready to send the text data to the Natural Language API!
To do that, write a Python script using the Python module for Google Cloud. You can accomplish the same thing from any language, there are many different cloud client libraries.

## Start classifying articles and importing them to BigQuery.

Run script:
```bash
python3 classify-text.py
```

The google-cloud Python client library was used to access Cloud Storage, the Natural Language API, and BigQuery. 

First, a client is created for each service; then references are created to the BigQuery table. files is a reference to each of the BBC dataset files in the public bucket. We iterate through these files, download the articles as strings, and send each one to the Natural Language API in our classify_text function. For all articles where the Natural Language API returns a category, the article and its category data are saved to a rows_for_bq list. When classifying each article is done, the data is inserted into BigQuery using insert_rows().


Note: The Natural Language API can return more than one category for a document, in this case we only store the first category returned to keep things simple.

- verify that the article data was saved to BigQuery

Run query:
```sql
SELECT * FROM `news_classification_dataset.article_data`
```

The category column has the name of the first category the Natural Language API returned for the article, and confidence is a value between 0 and 1 indicating how confident the API is that it categorized the article correctly. 


- Analyzing categorized news data in BigQuery

To see which categories were most common in the dataset.
Run query:

```sql
SELECT
  category,
  COUNT(*) c
FROM
  `news_classification_dataset.article_data`
GROUP BY
  category
ORDER BY
  c DESC
```

- Find the article returned for a more obscure category like /Arts & Entertainment/Music & Audio/Classical Music.

Run query:
```sql
SELECT * FROM `news_classification_dataset.article_data`
WHERE category = "/Arts & Entertainment/Music & Audio/Classical Music"

```

- Get only the articles where the Natural language API returned a confidence score greater than 90%. 
Run query:
```sql
SELECT
  article_text,
  category
FROM `news_classification_dataset.article_data`
WHERE cast(confidence as float64) > 0.9
```

BigQuery also integrates with a number of visualization tools. To create visualizations of the categorized news data, check out the Data Studio quickstart for BigQuery.