output "databricks_azure_workspace_resource_id" {
  value = azurerm_databricks_workspace.this.id
}

output "workspace_url" {
  value = "https://${azurerm_databricks_workspace.this.workspace_url}/"
}

output "module_cluster_id" {
  value = module.auto_scaling_cluster_example.cluster_id
}
