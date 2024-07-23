locals {
  data_lake_bucket = "holiday_weather"
}

variable "project" {
  description = "Your GCP Project ID"
  default = "clear-router-390022"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "us-central1"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "holiday_weather"
}

# variable "dataproc_cluster_name" {
#   description = "Name of the Dataproc cluster"
#   type        = string
#   # default     = "cluster-62de"
# }