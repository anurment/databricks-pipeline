# Resources for the external storage

resource "azurerm_storage_account" "ext_storage" {
  name                     = "${var.ext_stacc_name}${random_string.naming.result}"
  resource_group_name      = azurerm_resource_group.this.name
  location                 = azurerm_resource_group.this.location
  account_tier             = "Standard"

  # LRS replication type copies your data synchronously three times within 
  # a single physical location in the primary region.(least expensive)
  account_replication_type = "LRS"

  # Hierarchial namespace (folders in storage) 
  is_hns_enabled           = true

  # blobs are retained 5 days if unused
  blob_properties {
    delete_retention_policy {
      days = 5
    }
    container_delete_retention_policy {
      days = 5
    }
  }

  tags = {
    environment = "${var.env}"
  }
}

resource "azurerm_storage_container" "ext" {
  name                  = "extcontainer"
  storage_account_name  = azurerm_storage_account.ext_storage.name
  container_access_type = "private"
}


resource "azurerm_databricks_access_connector" "access_connector" {
  name                = var.access_connector_name
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  identity {
    type = "SystemAssigned"
  }
}
resource "azurerm_role_assignment" "ext" {
  scope                = azurerm_storage_account.ext_storage.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_databricks_access_connector.access_connector.identity[0].principal_id
}
