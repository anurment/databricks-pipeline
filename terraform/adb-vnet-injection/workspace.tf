# Resources for the workspace

resource "azurerm_databricks_workspace" "this" {
  name                = "${local.prefix}-workspace"
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  sku                 = "premium"
  tags                = local.tags

  custom_parameters {
    no_public_ip                                         = var.no_public_ip
    virtual_network_id                                   = azurerm_virtual_network.this.id
    private_subnet_name                                  = azurerm_subnet.private.name
    public_subnet_name                                   = azurerm_subnet.public.name
    public_subnet_network_security_group_association_id  = azurerm_subnet_network_security_group_association.public.id
    private_subnet_network_security_group_association_id = azurerm_subnet_network_security_group_association.private.id
    storage_account_name                                 = local.dbfsname
  }
  # We need this, otherwise destroy doesn't cleanup things correctly
  depends_on = [
    azurerm_subnet_network_security_group_association.public,
    azurerm_subnet_network_security_group_association.private
  ]
}

module "auto_scaling_cluster_example" {
  source                  = "./modules/autoscaling_cluster"
  spark_version           = data.databricks_spark_version.latest_lts.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = var.global_auto_termination_minute
}

resource "databricks_directory" "includes" {
  path = "/includes"
  delete_recursive = true
}

resource "databricks_directory" "ingestion" {
  path = "/ingestion"
  delete_recursive = true
}

resource "databricks_directory" "transform" {
  path = "/transform"
  delete_recursive = true
}

resource "databricks_directory" "enrichment" {
  path = "/enrichment"
  delete_recursive = true
}

resource "databricks_directory" "set-up" {
  path = "/set-up"
  delete_recursive = true
}



