## Local Setup for Terraform and GCP

### Pre-Requisites
1. Terraform client installation: https://www.terraform.io/downloads
2. Cloud Provider account: https://console.cloud.google.com/ 

### Terraform Concepts
[Terraform Overview](1_terraform_overview.md)

### GCP setup

1. [Setup for First-time](2_gcp_overview.md#initial-setup)
    * [Only for Windows](windows.md) - Steps 4 & 5
2. [IAM / Access specific to this course](2_gcp_overview.md#setup-for-access)

### Terraform Workshop for GCP Infra
Your setup is ready!
Now head to the [terraform](terraform) directory, and perform the execution steps to create your infrastructure.


 ### Execution
 
 ```shell
 # Refresh service-account's auth-token for this session
 gcloud auth application-default login
 
 # Initialize state file (.tfstate)
 terraform init
 
 # Check changes to new infra plan
 terraform plan -var="project=<your-gcp-project-id>"
 ```
 
 ```shell
 # Create new infra
 terraform apply -var="project=<your-gcp-project-id>"
 ```
 
 ```shell
 # Delete infra after your work, to avoid costs on any running services
 terraform destroy
 ```