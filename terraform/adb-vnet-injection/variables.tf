variable "no_public_ip" {
  type        = bool
  default     = true
  description = "If Secure Cluster Connectivity (No Public IP) should be enabled. Default: true"
}

variable "rglocation" {
  type        = string
  default     = "southeastasia"
  description = "Location of resource group to create"
}

variable "env" {
  type        = string
  default     = "dev"
  description = "Environment prefix"
}

variable "ext_stacc_name" {
  type        = string
  default     = "ext"
}

variable "dbfs_prefix" {
  type        = string
  default     = "dbfs"
  description = "Name prefix for DBFS Root Storage account"
}

variable "data_factory_name" {
  type        = string
  description = "The name of the Azure Data Factory to deploy. Won't be created if not specified"
  default     = ""
}

variable "node_type" {
  type        = string
  default     = "Standard_DS3_v2"
  description = "Node type for created cluster"
}

variable "workspace_prefix" {
  type        = string
  default     = "adb"
  description = "Name prefix for Azure Databricks workspace"
}

variable "access_connector_name" {
  type        = string
  description = "the name of the access connector"
}


variable "global_auto_termination_minute" {
  type        = number
  default     = 30
  description = "Auto-termination time for created cluster"
}

variable "cidr" {
  type        = string
  default     = "10.179.0.0/20"
  description = "Network range for created VNet"
}

variable "tags" {
  type        = map(string)
  description = "Optional tags to add to resources"
  default     = {}
}

variable "subid" {
  type = string
  sensitive = true
}
/*
variable "account_id" {
  sensitive = true
  type        = string
  description = "Databricks Account ID"
}
*/


