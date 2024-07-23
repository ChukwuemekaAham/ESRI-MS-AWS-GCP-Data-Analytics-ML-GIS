# Adding data to Cloud SQL instance

# Copied a subset of the New York City taxi trips CSV files stored on Cloud Storage locally,?
# to keep resource usage low, you'll only be working with a subset of the data (~20,000 rows).

gsutil cp gs://data_bucket/data/nyc_tlc_yellow_trips_2018_subset_1.csv trips.csv-1
gsutil cp gs://data_bucket/data/nyc_tlc_yellow_trips_2018_subset_2.csv trips.csv-2
