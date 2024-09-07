locals {
  data_bucket = "mlops-proj-bucket"
}

variable "credentials" {
  description = "My Credentials"
  default     = "./clear-router-390022-6ec8275b7a76.json"
}

variable "project" {
  description = "Project"
  default     = "clear-router-390022"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-east1"
}

variable "zone" {
  description = "Zone"
  #Update the below to your desired zone
  default = "us-east1-a"
}

variable "location" {
  description = "Project Location"
  #Update the below to your desired location
  default = "US"
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that data (from GCS) will be written to"
  type        = string
  default     = "gold_market"
}

variable "dataproc_cluster_name" {
  description = "Name of the Dataproc cluster"
  type        = string
  default     = "mlops-proj-cluster"
}
