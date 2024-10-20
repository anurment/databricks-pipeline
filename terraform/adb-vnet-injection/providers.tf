# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
  subscription_id = var.subid
  resource_provider_registrations = "none"

}

# Azure active directory
provider "azuread" {
    # Configuration options
}

# For random naming strings
provider "random" {
}

# Configure the databricks provider
provider "databricks" {
  host = azurerm_databricks_workspace.this.workspace_url
  azure_workspace_resource_id = azurerm_databricks_workspace.this.id
}
