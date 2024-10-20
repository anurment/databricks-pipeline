terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
    databricks = {
      source  = "databricks/databricks"
      version = "1.52.0"
    }
  }
}



resource "databricks_cluster" "single_node" {
  cluster_name            = "SingleNode"
  num_workers             = 0
  spark_version           = var.spark_version
  node_type_id            = var.node_type_id
  autotermination_minutes = var.autotermination_minutes
  

   spark_conf = {
    "spark.databricks.cluster.profile" : "singleNode"
    "spark.master" : "local[*]"
   }

  custom_tags = {
    "ResourceClass" = "SingleNode"
  }
  
}
