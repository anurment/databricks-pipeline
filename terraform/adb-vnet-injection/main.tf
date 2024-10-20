# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
    azuread = {
            source = "hashicorp/azuread"
            version = "3.0.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = "1.52.0"
    }
  }
}

resource "random_string" "naming" {
  special = false
  upper   = false
  length  = 6
}

# Main resource group

resource "azurerm_resource_group" "this" {
  name     = "${random_string.naming.result}-basic-demo-rg"
  location = var.rglocation
  tags     = local.tags
}

locals {
  prefix   = join("-", [var.workspace_prefix, "${random_string.naming.result}"])
  location = var.rglocation
  dbfsname = join("", [var.dbfs_prefix, "${random_string.naming.result}"]) // dbfs name must not have special chars

  // tags that are propagated down to all resources
  tags = merge({
    Environment = "Testing"
    Epoch       = random_string.naming.result
  }, var.tags)
}




