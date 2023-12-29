resource "azurerm_service_plan" "asp" {
  name                      = "${var.service_plan_name}-sp"
  location                  = var.resource_group_location
  resource_group_name       = var.resource_group_name
  os_type                   = "Linux"
  sku_name                  = "P0v3"
}

resource "azurerm_linux_web_app" "as" {
  name                      = "${var.app_service_name}-as"
  location                  = var.resource_group_location
  resource_group_name       = var.resource_group_name
  service_plan_id           = azurerm_service_plan.asp.id
  
  site_config {
    always_on = true
  }

  identity {
    type = "SystemAssigned"
  }
}
