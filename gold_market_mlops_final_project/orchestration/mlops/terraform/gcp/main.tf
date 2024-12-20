terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      # version = "6.0.1"
    }
  }
}

# Define the required providers
provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
  zone        = var.zone
}

# Create a Cloud Storage bucket for input data
resource "google_storage_bucket" "input_bucket" {
  name     = "${local.data_bucket}_${var.project}" # Concatenating DL bucket & Project name for unique naming
  location = var.location

  # Optional, but recommended settings:
  storage_class               = var.storage_class
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    condition {
      age = 1 // days
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }

  force_destroy = true
}

# # Create a BigQuery dataset for the transformed data
# resource "google_bigquery_dataset" "output_dataset" {
#   dataset_id = var.BQ_DATASET
#   project    = var.project
#   location   = var.location
# }

# # Create a Dataproc cluster for running the Spark job
# resource "google_dataproc_cluster" "cluster" {
#   name    = var.dataproc_cluster_name
#   project = var.project
#   region  = var.region

#   cluster_config {
#     master_config {
#       num_instances = 1
#       machine_type  = "n1-standard-2"
#       disk_config {
#         boot_disk_size_gb = 30
#       }
#     }

#     worker_config {
#       num_instances = 0
#       machine_type  = "n1-standard-2"
#       disk_config {
#         boot_disk_size_gb = 30
#       }
#     }
#   }

# }

# Output the created resources
output "input_bucket_name" {
  value = google_storage_bucket.input_bucket.name
}

output "output_dataset_id" {
  value = google_bigquery_dataset.output_dataset.dataset_id
}
