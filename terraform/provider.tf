terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = "~> 4.0"
        }

        databricks = {
            source = "databricks/databricks"
            version = "1.52.0"
        }

        azuread = {
            source = "hashicorp/azuread"
            version = "3.0.0"
        }

        time = {
            source = "hashicorp/time"
            version = "0.12.1"
        }
    }
}

# remember to set the environmental variable for subscription id with command:
# export TF_VAR_subid=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
variable "subid" {
  type = string
  sensitive = true
}


#Azure resource manager
provider "azurerm" {
    features {}
    subscription_id = var.subid
    resource_provider_registrations = "none"

}

#Azure active directory
provider "azuread" {
    # Configuration options
}

# Used to interact with time-based resources. In this tutorial the rotation time for app passwords
provider "time" {
    # Configuration options (no options 3.10.2024)
}

provider "databricks" {
    host = azurerm_databricks_workspace.this.workspace_url
    azure_workspace_resource_id = azurerm_databricks_workspace.this.id
}

