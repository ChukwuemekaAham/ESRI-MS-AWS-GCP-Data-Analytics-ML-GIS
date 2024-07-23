# Powering Search and Log Analytics Workloads with Amazon OpenSearch Service

**REQUIRES:**
- AWS account access
- AWS console Region: (us-east-1)
- AWS CLI credentials (ACCOUNT_ID, SECRET_ACCESS_KEY)
- Encryption policy
- Network policy
- Data access policy
- Authentication method
- Creating an OpenSearch Serverless collection in AWS cloud
- Collection must have an assigned encryption key, network access settings, and a matching data access policy that grants permission to its resources
- OpenSearch Endpoint URL
- OpenSearch Dashboard URL

The goal of this project was to get hands on with Amazon OpenSearch Serverless. I walked through setting up a new Amazon OpenSearch Serverless domain in the AWS console. Explored the different types of search queries available. Designed eye-catching visualizations, learned how to secure domain and documents based on assigned user privileges.

# Goals

•	Create an OpenSearch Serverless Collection
•	Host multiple indices for search and logs use case with which the solution interacts for different use case with OpenSearch Serverless
•	Configure the solution to create data used to run search queries
•	Configure the solution to index sample log data to OpenSearch Serverless
•	Visualize the log interactions with OpenSearch Dashboards and create real time dashboards to view customer and component activities

# Introduction

## What is Amazon OpenSearch Serverless

Amazon OpenSearch Service  offers a new serverless option, Amazon OpenSearch Serverless , that makes it easy for customers to run large scale search and analytics workloads without having to configure, manage, or scale OpenSearch clusters. It automatically provisions and scales the underlying resources to deliver fast data ingestion and query responses for even the most demanding and unpredictable workloads. With OpenSearch Serverless, customers pay only for the resources consumed.

With Amazon OpenSearch Serverless, you do not need to account for factors that are hard to know in advance, such as the frequency and complexity of queries or the volume of data expected to be analyzed. Instead of managing infrastructure, you can focus on using OpenSearch for exploring and deriving insights from your data. You can also get started using familiar APIs to load and query data and use OpenSearch Dashboards for interactive data analysis and visualization.

OpenSearch Serverless also supports OpenSearch Dashboards, which provides an intuitive interface for analyzing data.

## Benefits

OpenSearch Serverless has the following benefits:
1.	Simpler to use – OpenSearch Serverless removes much of the complexity of managing OpenSearch Service domains and capacity.
2.	Easy to administer: No sizing, scaling and tuning of clusters, and no shard and index lifecycle management
3.	Ecosystem: Get started in seconds using the same OpenSearch clients, pipelines, and APIs
4.	Scalable – OpenSearch Serverless will eventually seamlessly scale compute and storage capacity as needed, with no disruption to client connections.
5.	Cost-effective – When you use OpenSearch Serverless, you only pay for the resources that you consume.
Before getting into details of OpenSearch Serverless, let's take a quick de-route and see what OpenSearch is?

### What is OpenSearch?

OpenSearch is a distributed search and analytics technology in the database family, providing a REST api to send data and query that data. Unlike other database technologies, you structure your data in indexes instead of tables. Each json object that you send to you OpenSearch index is called a 'document' (c.f. 'row' in a relational database). The JSON keys for that document are called 'fields' (c.f. columns), and the values are values.
Next you will see the architecture of OpenSearch Serverless followed by a hands-on exercise on OpenSearch Serverless.

#### How it works

Traditional OpenSearch clusters have a single set of instances that perform both indexing and search operations, and index storage is tightly coupled with compute capacity. In contrast, OpenSearch Serverless uses a cloud-native architecture that separates the indexing (ingest) components from the search (query) components, with Amazon S3 as the primary data storage for indexes. This decoupled architecture lets you scale search and indexing functions independently of each other, and independently of the indexed data in S3.

When you write data to a collection, OpenSearch Serverless distributes it to ingest compute units. Ingest compute units index the incoming data and move the indexes to S3. When you perform a search on the collection data, OpenSearch Serverless routes requests to the search compute units that hold the data being queried. The search compute units download the indexed data directly from S3 (if it's not already cached locally), run search operations, and perform aggregations.

**OpenSearch Serverless supports two primary use cases:**

1. Search:

We're all familiar with search experience - you log on to a website, maybe to buy some clothing, and your first action is to type some words in a search bar, wait a few milliseconds, and receive a collection of (hopefully) relevant search results. In fact, you're probably so used to searching for information that you look for a search bar in the real world. Has this happened to you? You go into the market, and you can't find what you're looking for. Your brain instinctively reaches for a search bar that's not there, to type that product in and find it.
What's going on behind the scenes in search? Search engines work with discreet entities, called documents. A document is a structured collection of fields with values. 

*****************

I worked with OpenSearch, which uses JSON-based, REST APIs for specifying (and indexing) documents. When document is sent to OpenSearch, it is indexed. The index allows to query against that collection of documents.

•	In case of search, all search data is stored in hot storage to ensure fast query response times.

******************

2. Time series:

This is the log analytics segment that focuses on analyzing large volumes of semi-structured, machine-generated data in real-time for operational, security, user behavior, and business insights.

•	In time-series, 12 hours of data is cached in hot storage, and seven days in warm storage.

# Collection

A collection in OpenSearch Serverless is a logical grouping of one or more indexes that represent an analytics workload. OpenSearch Service automatically manages and tunes the collection, requiring minimal manual input. Based on your use case, you can select either Time series or Search when you create a collection. A collection type can't be changed after it's created, so ensured you know the use case for your collection ahead of time.

The most important difference between search and time series collections is that for time series, you can't update by **document ID (POST index/_update/)**. This operation is reserved for search use cases only.


# OpenSearch Serverless Architecture

OpenSearch Serverless uses a cloud-native architecture that decouples compute and storage and separates the indexing (ingest) components from the search (query) components, with Amazon Simple Storage Service (Amazon S3)  as the primary data storage for indexes.
This decoupled architecture means customers can scale search and indexing functions independently of each other, and independently of the indexed data in S3. 

At a high level OpenSearch Serverless comes with following innovations:
•	Storage and compute decoupled
•	Separate ingestion and search pipelines
•	Built-in hot-warm tier
•	Active-standby data nodes
•	Serverless Dashboards

# Security with OpenSearch Serverless

To secure the data with OpenSearch Serverless, you can set up:

1. Encryption policies:

Encryption policy with OpenSearch Serverless can be setup at collection level, you have an option to either choose and manage your own AWS key to encrypt the data, or you can let AWS create the key and manage it for you. This is one of the use case for multi-tenant search, where you can have a separate key to encrypt the data for each tenant.

2. Network policies:

Network policies let you choose to define accessibility of your collection over internet from public networks, or it must be accessed through OpenSearch Serverless managed VPC endpoints. Apart from defining the access level you also have an option to define policy separately for OpenSearch Serverless collection endpoint , and OpenSearch Dashboards.

3. Data access policies:

Data access policy allows you to choose how you access the data within the collections. With these policies you can define what action can be performed by which user. For ex: a user having read only access will only be allowed to read certain indices whereas an admin user would have full access to create, read, write, manage indices and so on.

4. Authentication:

Authentication for OpenSearch Serverless collection can be setup in two ways. One way is to set up an IAM Users and IAM Roles which can be used to access the dashboards as well as through APIs. Where SAML can be setup to access the data using dashboards only.

If you want to learn more about the Security, checkout the Security Documentation for OpenSearch serverless. You will also learn how to create those policies while you create a collection.

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-security.html

https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg-serverless.html 

https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/opensearch/