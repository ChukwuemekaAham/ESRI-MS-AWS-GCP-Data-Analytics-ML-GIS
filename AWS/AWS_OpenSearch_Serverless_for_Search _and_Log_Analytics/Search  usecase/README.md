# Search usecase

Create a collection with type Search, which is good to power full-text search for internet-facing applications such as e-commerce/website/catalog search, and content search etc.

o	Creating a collection
o	Create Collection - Review
o	Accessing OpenSearch Dashboards
o	Uploading Data to OpenSearch Collections
o	Querying Data
	Searching Data in the Collection
	Highlighting
	Aggregations

# Create a collection using console

## Add new collection

Navigate to the Amazon OpenSearch console  and Create Collections. Provide a name and description for the collection, and choose Collection type as Search 


Create Collection - Review
Step 3 - Review and Create
1.	Review the configuration, then click on Submit to create the Collection

2.	Once you click on Submit, Collection status changes to "Creating", and it may take couple of minutes to create the collection.

3.	Once collection is created, status changes to "Active" where you can verify the name, type, encryption policy etc. And then at the bottom you also get the endpoint for OpenSearch and OpenSearch Dashbards.

Once both "OpenSearch Endpoint" and "OpenSearch Dashboard URL" are available, please continue to the next step to start exploring your new Amazon OpenSearch Serverless Collection


1.	Event dashboard
2.	Module 2 - Search usecase
3.	Accessing OpenSearch Dashboards
Accessing OpenSearch Dashboards
There are 2 ways to access the OpenSearch Dashboards. You can either use the IAM credentials with Secret Key and Access Key ID created earlier, or you can use to set up SAML authentication  for accessing the dashboard. Please note that SAML authentication is only available to access OpenSearch Dashboards, and you will still need the IAM credentials to perform any operations using CLI, API and other OpenSearch clients for indexing and searching of data.
As part of this workshop you will see how IAM user credentials can be used for accessing the data. To access the dashboard:
1.	Navigate to OpenSearch collection in AWS console, and click on the OpenSearch Dashboards URL
2.	Sign in with Access Key and Secret Key
3.	Click 'Explore on my own'

At this point, you have seen how to access the OpenSearch Dashboards. Next, you will see how to use the OpenSearch Rest APIs to ingest data and interact with the data in OpenSearch Serverless collections.


1.	Event dashboard
2.	Module 2 - Search usecase
3.	Uploading Data to OpenSearch Collections
Uploading Data to OpenSearch Collections
You can upload data to an OpenSearch Serverless collection using Postman, curl, logstash, devtools or other tools. In this workshop, you will be ingesting data in your collection using Dev Tools within the OpenSearch Dashboards console.
Go back to the OpenSearch Dashboards, Click 'Dev Tools' in the top right corner of the screen.

1.	Create an Index named movies-index
You will first create an index that will hold the movies data. Name it movies-index. Copy the query and paste it into the Dev tools input window
PUT movies-index

Click the small 'play' icon next to the query as seen in the screen. This creates an index named movies-index.
2.	Upload Data using Bulk API.
Next, you will insert data into the movies-index index via OpenSearch's bulk API . You'll be using a data set with 1500 documents.
Download and open the following file
sample-movies 
file and examine the contents of the file. The file has documents pertaining to movies and has information like title of the movie, plot, directors, actors, genre, etc.
You will now use the _bulk API to ingest this data into your serverless collection. In the console, enter the below command (POST request to the _bulk API endpoint) . In the next line, copy paste the entirety of the data file (1496 records) into the dev console, and click the 'Play' icon . The below example shows how the command will look like for 2 documents.
POST /_bulk
{"index": {"_index": "movies-index"}}
{"directors": ["Joseph Gordon-Levitt"], "release_date": "2013-01-18T00:00:00Z", "rating": 7.4, "genres": ["Comedy", "Drama"], "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQxNTc3NDM2MF5BMl5BanBnXkFtZTcwNzQ5NTQ3OQ@@._V1_SX400_.jpg", "plot": "A New Jersey guy dedicated to his family, friends, and church, develops unrealistic expectations from watching porn and works to find happiness and intimacy with his potential true love.", "title": "Don Jon", "rank": 1, "running_time_secs": 5400, "actors": ["Joseph Gordon-Levitt", "Scarlett Johansson", "Julianne Moore"], "year": 2013}
{"index": {"_index": "movies-index"}}
{"directors": ["Ron Howard"], "release_date": "2013-09-02T00:00:00Z", "rating": 8.3, "genres": ["Action", "Biography", "Drama", "Sport"], "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg", "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.", "title": "Rush", "rank": 2, "running_time_secs": 7380, "actors": ["Daniel Br\u00c3\u00bchl", "Chris Hemsworth", "Olivia Wilde"], "year": 2013}

Congratulations! You now have an index full of movie data you can search! Please proceed to the next step to learn about some different types of queries available to you in OpenSearch



1.	Event dashboard
2.	Module 2 - Search usecase
3.	Querying Data
Querying Data
In this section, you will learn how to:
a) search the data in the OpenSearch Collections using different queries
b) highlight search results and
c) perform aggregations


1.	Event dashboard
2.	Module 2 - Search usecase
3.	Querying Data
4.	Searching Data in the Collection
Searching Data in the Collection
In this section, you are going learn about different types of queries available in OpenSearch to search the data in your OpenSearch Collection.
1.	First, look up the indices available in the collection.
GET _cat/indices?v
The API returns the following response showing the movies-index index that we created in the previous section

2.	Simple Query:
If you want to list all the documents in the index, you can execute this simple search API. Because we have not mentioned any parameters or filters in the query, every document is part of the search result. Note how the search results include the entire JSON object that you pasted as part of the _bulk request in the previous section.
GET movies-index/_search

You can see all 1499 records have been retrieved.
Take a look at the response. The returned data contains operational information along with the result set:
{
  "took" : 140,           // Server-side execution time in milliseconds
  "timed_out" : false,    // If the query operation timed out
  "hits" : {                
    "total" : {
      "value" : 1499,     // Number of relevant documents found
      "relation" : "eq"   // Search relations, default operation eq
    }
  }
}
3.	Retrieve only certain Fields:
Your dataset can have a lot of valuable information but if you want to just retrieve the source from selected fields , you can use the _source option. By default, a search request retrieves the entire JSON object that was provided when indexing the document like you saw in the previous example.
GET movies-index/_search
{
  "_source": {
  "includes": [
    "title",
    "plot",
    "genres"
    ]
  }
}
You can scroll through the results and confirm how all documents are retrieved but only the three fields in the query are part of the result.

4.	Term Query:
A term query returns documents that exactly match the search term. Inspect the output and check if all returned documents have the term 'christmas' in their 'title'. Try different variations of the value (eg - 'harry' or 'cinderella')
GET movies-index/_search
{
  "query": {
    "term": { 
      "title": {
        "value": "christmas"
      }
    }
  }
}
Of all the 1500 documents in our index, only 3 movies/docs match the term in our query. Notice how all fields are retrieved as we did not add any filters to restrict the fields. 
5.	Term Query + retrieve selected fields
You can try a combination of queries 3 and 4 . If you want to only retrieve certain fields but are interested in a particular term, you can use this query.
GET movies-index/_search
{
  "_source": {
    "includes": [
      "title",
      "actors"
    ]
  },
  "query": {
    "query_string": {
      "default_field": "title",
      "query": "harry"
    }
  }
}

The above query gives all documents that has the term 'harry' in the title. However, the result only shows the fields of interest in the query.
6.	Boolean Query
Bool queries are compound queries that let you mix multiple term and match queries. If you want to search for movies that are part of “adventure” genre but also have the term “wizard” in the plot field, run this query:
GET /movies-index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "genres": "adventure"
          }
        },
        {
          "match": {
            "plot": "wizard"
          }
        }
      ]
    }
  }
}
The search result with [must] keyword returns only documents fulfilling the required condition. By using must conditions you get precise results. 
There are exactly 4 search results that fulfill the required conditions in the query. By using ‘must’ you get precise results. where at least one . A snippet of one of the documents is shown in the example above


1.	Event dashboard
2.	Module 2 - Search usecase
3.	Querying Data
4.	Highlighting
Highlighting
In the previous section, you saw how to query/search the data in your collection. In this section, you are going learn about the highlighting the search results.
Highlight:
If you want to highlight the results based on a search term in one or more fields in the results you can use the highlight query. The highlighted text will be wrapped between and by default but the tags can be modified. If you want to find the ‘title’ of the movie that has the text ‘christmas’ in the plot, run this query.
GET movies-index/_search
{
  "_source": {
   "includes": [
     "title"
     ]
  },
  "query": {
    "match": { "plot": "christmas" }
  },
  "highlight": {
    "fields": {
      "plot": {}
    }
  }
} 

Notice the highlighted text ‘christmas’ between .


1.	Event dashboard
2.	Module 2 - Search usecase
3.	Querying Data
4.	Aggregations
Aggregations
In this section, you are going learn how to summarize your search results using Aggregations.
Aggregations:
Aggregations compute summary values based on groupings of the values in a particular field. for eg) with movie dataset, we can summarize fields like ratings, genre, and year to search results based on the values of those fields. With aggregations, we can answer questions like ‘How many movies are in each genre?“
GET movies-index/_search
{
  "size":0,
  "aggs": {
    "genres": {
      "terms":{"field": "genres.keyword"}
    }
  }
}

You don't need to get search results to get aggregation results. In the query above, OpenSearch aggregates on the genres.keyword field. By using the "size": 0 directive as well, OpenSearch will omit the actual documents from the response; only the aggregation results will be returned.



1.	Event dashboard
2.	Summary
Summary
In this workshop, you created a log analytics pipeline using OpenSearch Serverless in module 01, whereas in module 2 you saw how easy it is to ingest and search data using OpenSearch Serverless. With OpenSearch Serverless, you can focus on building your application without having to worry about provisioning, tuning, and scaling the underlying infrastructure. OpenSearch Serverless supports the same ingestion pipelines and high-level clients as the open-source OpenSearch project. You can easily get started using the familiar OpenSearch indexing and query APIs to load and search your data and use OpenSearch Dashboards to visualize that data.
OpenSearch Serverless is powered by the open source OpenSearch Project. To learn more about OpenSearch Serverless, see the documentation . For details, including the roadmap of the OpenSearch Project, visit the project website .
Next you will see what steps you need to perform to clean up the stack.

1.	Event dashboard
2.	Clean Up
Clean Up
To clean up the environment, you need to delete the resources you have created.
1. Delete Collections
Navigate to the OpenSearch Service console  -> Expand Serverless in the left navigation pane -> Collections -> Select Collection -> Delete

Repeat the same step for your search collection as well

2. Delete security policies such as Data Access Policy, Network Policy, and Encryption Policy.
Additional resources from Module 1 to clean up include:
1. Cloud9 Instance

2. Firehose delivery stream

3. Bootstrap Cloud Formation Stack (skip this if you are in AWS Event)


