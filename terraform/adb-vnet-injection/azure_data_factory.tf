resource "azurerm_data_factory" "adf" {

  name                = "${var.data_factory_name}${random_string.naming.result}"
  location            = azurerm_resource_group.this.location
  resource_group_name = azurerm_resource_group.this.name
  tags                = var.tags
}
