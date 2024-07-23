# Generative Insights with BigQuery SQL and Vertex AI


1. Introduction
In this codelab, I built a Movie Success Rating prediction and prescription app with BigQuery SQL queries and Vertex AI PaLM API. The model used to perform text generation is text-bison and is hosted as a remote function in BigQuery.

The list of services used are:
1.	BigQuery ML
2.	Vertex AI PaLM API
3.	Cloud Shell

## Objectives
•	A BigQuery dataset to contain the model
•	A BigQuery ML model that predicts the success score of a movie based on the GENRE and RUNTIME attributes of the movie
•	A BigQuery model that hosts the Vertex AI PaLM API as a remote function
•	An external connection to establish the connection between BigQuery and Vertex AI


2. Requirements
•	A browser, such as Chrome or Firefox
•	A Google Cloud project with billing enabled
Before you begin
1.	In the Google Cloud Console, on the project selector page, select or create a Google Cloud project
2.	Make sure that billing is enabled for your Cloud project. Learn how to check if billing is enabled on a project
3.	Make sure all the necessary APIs (BigQuery API, Vertex AI API, BigQuery Connection API) are enabled
4.	You will use Cloud Shell, a command-line environment running in Google Cloud that comes pre-loaded with bq. Refer documentation for gcloud commands and usage


The PaLM 2 for Text (text-bison) foundation model is optimized for a variety of natural language tasks such as sentiment analysis, entity extraction, and content creation. The types of content that the PaLM 2 for Text model can create include document summaries, answers to questions, and labels that classify content.
The PaLM 2 for Text model is ideal for tasks that can be completed with one API response, without the need for continuous conversation. For text tasks that require back-and-forth interactions, use the Generative AI on Vertex AI API for chat.
To explore this model in the console, select the PaLM 2 for Text model card in the Model Garden.
https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/text-bison?_ga=2.178587620.1562778417.1698064121-1412950406.1678701917 

## Use cases
•	Summarization: Create a shorter version of a document that incorporates pertinent information from the original text. For example, you might want to summarize a chapter from a textbook. Or, you could create a succinct product description from a long paragraph that describes the product in detail. Question answering: Provide answers to questions in text. For example, you might automate the creation of a Frequently Asked Questions (FAQ) document from knowledge base content.
•	Classification: Assign a label to provided text. For example, a label might be applied to text that describes how grammatically correct it is.
•	Sentiment analysis: This is a form of classification that identifies the sentiment of text. The sentiment is turned into a label that's applied to the text. For example, the sentiment of text might be polarities like positive or negative, or sentiments like anger or happiness.
•	Question answering: Provide answers to questions in text. For example, you might automate the creation of a Frequently Asked Questions (FAQ) document from knowledge base content.
•	Entity extraction: Extract a piece of information from text. For example, you can extract the name of a movie from the text of an article.
For more information on designing text prompts, see Design text prompts.


3. Preparing data
In this use case, we use the movies dataset derived from movielens source.


Your Cloud Platform project in this session is set to clear-router-390022.
Use “gcloud config set project [PROJECT_ID]” to change to a different project.
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ bq mk --location=us-central1 movie_insights
Dataset 'clear-router-390022:movie_insights' successfully created.
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ git clone https://github.com/AbiramiSukumaran/movie_score_genai_insightsCloning into 'movie_score_genai_insights'...
remote: Enumerating objects: 22, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (22/22), done.
remote: Total 22 (delta 6), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (22/22), 354.14 KiB | 3.93 MiB/s, done.
Resolving deltas: 100% (6/6), done.
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ ls
movie_score_genai_insights  README-cloudshell.txt
ahamchukwuemeka2@cloudshell:~ (clear-router-390022)$ cd movie_score_genai_insightsahamchukwuemeka2@cloudshell:~/movie_score_genai_insights (clear-router-390022)$ ls'bq cloud shell commands'   LICENSE   movies_data.csv   README.md
ahamchukwuemeka2@cloudshell:~/movie_score_genai_insights (clear-router-390022)$ bq load --source_format=CSV --skip_leading_rows=1 movie_insights.movie_score \
./movies_data.csv \ Id:numeric,name:string,rating:string,genre:string,year:numeric,released:string,score:string,director:string,writer:string,star:string,country:string,budget:numeric,company:string,runtime:numeric,data_cat:string
Upload complete.
Waiting on bqjob_r1cadc338a7f4c0d5_0000018ba39f0bf5_1 ... (0s) Current status: DONE   
ahamchukwuemeka2@cloudshell:~/movie_score_genai_insights (clear-router-390022)$ bq query --use_legacy_sql=false \
SELECT name, rating, genre, runtime FROM movie_insights.movie_score limit 3;
+------------------+-----------+--------+---------+
|       name       |  rating   | genre  | runtime |
+------------------+-----------+--------+---------+
| Love by Drowning | R         | Drama  |     121 |
| It's Just Us     | Not Rated | Drama  |     120 |
| The Robinsons    | Not Rated | Action |      90 |
+------------------+-----------+--------+---------+
ahamchukwuemeka2@cloudshell:~/movie_score_genai_insights (clear-router-390022)$


SEE: `Query.md` file for more information
