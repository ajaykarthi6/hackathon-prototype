terraform {
  required_version = ">= 1.5.0"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Placeholder Terraform resources for deploying the service.
