locals {
    data_lake_bucket = "de-project-bucket"
}

variable "project" {
    description = "Your GCP Project ID"
    default = "clear-router-390022"
    type = string
}

variable "region" {
    description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
    default = "europe-west2"
    type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "us_employment_dataset"
}

# variable "TABLE_NAME" {
#     description = "BigQuery Table"
#     type = string
#     default = "us_counties_population"
# }