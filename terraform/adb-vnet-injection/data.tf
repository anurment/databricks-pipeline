# Data sources

data "databricks_spark_version" "latest_lts" {
  long_term_support = true
  depends_on        = [azurerm_databricks_workspace.this]
}

data "databricks_node_type" "smallest" {
  depends_on = [ azurerm_databricks_workspace.this]
  local_disk = true
  category   = "General Purpose"
}

data "azurerm_databricks_workspace" "this" {
  name                = azurerm_databricks_workspace.this.name
  resource_group_name = azurerm_databricks_workspace.this.resource_group_name
}

data "azurerm_storage_account" "ext_storage" {
  name                = azurerm_storage_account.ext_storage.name
  resource_group_name = azurerm_resource_group.this.name
}


