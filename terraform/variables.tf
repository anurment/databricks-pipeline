variable "env" {
  type    = string
  default = "dev"
}

variable "databricks_wspace_scope" {
  type    = string
  default = "azdbws"
}

variable "default_location" {
  type    = string
  default = "North Europe"
}

# Change the default value for a unique name
variable "prefix" {
  type    = string
  default = ""
  
}

variable "project" {
  type = string
  default = "db-demo"
}

variable "secrets_name" {
    type = map
    default = {
        "databricksappsecret" = "databricksappsecret"
        "databricksappclientid" = "databricksappclientid"
        "tenantid" = "tenantid"
    }
}


