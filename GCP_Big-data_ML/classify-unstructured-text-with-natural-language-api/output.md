Using headline and description from a New York Times article in the food section:

A Smoky Lobster Salad With a Tapa Twist. This spin on the Spanish pulpo a la gallega skips the octopus, but keeps the sea salt, olive oil, pimentón and boiled potatoes.

```bash
$ curl "https://language.googleapis.com/v1/documents:classifyText?key=${API_KEY}" \
  -s -X POST -H "Content-Type: application/json" --data-binary @request.json
{
  "categories": [
    {
      "name": "/Food & Drink/Cooking & Recipes",
      "confidence": 0.85
    },
    {
      "name": "/Food & Drink/Food/Meat & Seafood",
      "confidence": 0.63
    }
  ]
}
```

To see how the classifyText method can help us understand a dataset with lots of text, you'll use this public dataset of BBC news articles. The dataset consists of 2,225 articles in five topic areas (business, entertainment, politics, sports, tech) from 2004 - 2005. A subset of these articles are in a public Google Cloud Storage bucket. Each of the articles is in a .txt file.

To examine the data and send it to the Natural Language API, you'll write a Python script to read each text file from Cloud Storage, send it to the classifyText endpoint, and store the results in a BigQuery table. BigQuery is Google Cloud's big data warehouse tool - it lets you easily store and analyze large data sets.

To see the type of text you'll be working with, run the following command to view one article:

$ gcloud storage cat gs://cloud-training-demos-text/bbc_dataset/entertainment/001.txt
Gallery unveils interactive tree

A Christmas tree that can receive text messages has been unveiled at London's Tate Britain art gallery.

The spruce has an antenna which can receive Bluetooth texts sent by visitors to the Tate. The messages will be "unwrapped" by sculptor Richard Wentworth, who is responsible for decorating the tree with broken plates and light bulbs. It is the 17th year that the gallery has invited an artist to dress their Christmas tree. Artists who have decorated the Tate tree in previous years include Tracey Emin in 2002.

The plain green Norway spruce is displayed in the gallery's foyer. Its light bulb adornments are dimmed, ordinary domestic ones joined together with string. The plates decorating the branches will be auctioned off for the children's charity ArtWorks. Wentworth worked as an assistant to sculptor Henry Moore in the late 1960s. His reputation as a sculptor grew in the 1980s, while he has been one of the most influential teachers during the last two decades. Wentworth is also known for his photography of mundane, everyday subjects such as a cigarette packet jammed under the wonky leg of a table.


```bash
gcloud iam service-accounts create my-account --display-name my-account
gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:my-account@$PROJECT.iam.gserviceaccount.com --role=roles/bigquery.admin
gcloud projects add-iam-policy-binding $PROJECT --member=serviceAccount:my-account@$PROJECT.iam.gserviceaccount.com --role=roles/serviceusage.serviceUsageConsumer
gcloud iam service-accounts keys create key.json --iam-account=my-account@$PROJECT.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS=key.json

```

output:

```bash
Created service account [my-account].
Updated IAM policy for project [qwiklabs-gcp-00-c21b23286b23].
bindings:
- members:
  - serviceAccount:my-account@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  role: roles/bigquery.admin
- members:
  - serviceAccount:service-870214937280@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com
  role: roles/bigquerydatatransfer.serviceAgent
- members:
  - serviceAccount:870214937280@cloudbuild.gserviceaccount.com
  role: roles/cloudbuild.builds.builder
- members:
  - serviceAccount:service-870214937280@gcp-sa-cloudbuild.iam.gserviceaccount.com
  role: roles/cloudbuild.serviceAgent
- members:
  - serviceAccount:service-870214937280@compute-system.iam.gserviceaccount.com
  role: roles/compute.serviceAgent
- members:
  - serviceAccount:service-870214937280@container-engine-robot.iam.gserviceaccount.com
  role: roles/container.serviceAgent
- members:
  - serviceAccount:870214937280-compute@developer.gserviceaccount.com
  - serviceAccount:870214937280@cloudservices.gserviceaccount.com
  role: roles/editor
- members:
  - serviceAccount:admiral@qwiklabs-services-prod.iam.gserviceaccount.com
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  - user:student-04-f76a49222eb3@qwiklabs.net
  role: roles/owner
- members:
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  role: roles/storage.admin
- members:
  - user:student-04-f76a49222eb3@qwiklabs.net
  role: roles/viewer
etag: BwYAnSmVV1Q=
version: 1
Updated IAM policy for project [qwiklabs-gcp-00-c21b23286b23].
bindings:
- members:
  - serviceAccount:my-account@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  role: roles/bigquery.admin
- members:
  - serviceAccount:service-870214937280@gcp-sa-bigquerydatatransfer.iam.gserviceaccount.com
  role: roles/bigquerydatatransfer.serviceAgent
- members:
  - serviceAccount:870214937280@cloudbuild.gserviceaccount.com
  role: roles/cloudbuild.builds.builder
- members:
  - serviceAccount:service-870214937280@gcp-sa-cloudbuild.iam.gserviceaccount.com
  role: roles/cloudbuild.serviceAgent
- members:
  - serviceAccount:service-870214937280@compute-system.iam.gserviceaccount.com
  role: roles/compute.serviceAgent
- members:
  - serviceAccount:service-870214937280@container-engine-robot.iam.gserviceaccount.com
  role: roles/container.serviceAgent
- members:
  - serviceAccount:870214937280-compute@developer.gserviceaccount.com
  - serviceAccount:870214937280@cloudservices.gserviceaccount.com
  role: roles/editor
- members:
  - serviceAccount:admiral@qwiklabs-services-prod.iam.gserviceaccount.com
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  - user:student-04-f76a49222eb3@qwiklabs.net
  role: roles/owner
- members:
  - serviceAccount:my-account@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  role: roles/serviceusage.serviceUsageConsumer
- members:
  - serviceAccount:qwiklabs-gcp-00-c21b23286b23@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com
  role: roles/storage.admin
- members:
  - user:student-04-f76a49222eb3@qwiklabs.net
  role: roles/viewer
etag: BwYAnSnBopQ=
version: 1
created key [38061c478eba1a2c20d2ffbf6fad5d32973fe4ca] of type [json] as [key.json] for [my-account@qwiklabs-gcp-00-c21b23286b23.iam.gserviceaccount.com]
student_04_f76a49222eb3@cloudshell:~ (qwiklabs-gcp-00-c21b23286b23)$ 


```

$ python3 classify-text.py
Got article files from GCS, sending them to the NL API (this will take ~2 minutes)...

Writing NL API article data to BigQuery...