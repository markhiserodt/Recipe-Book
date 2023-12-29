resource "random_password" "admin_password" {
  count       = var.admin_password == null ? 1 : 0
  length      = 20
  special     = true
  min_numeric = 1
  min_upper   = 1
  min_lower   = 1
  min_special = 1
}

locals {
  admin_password = try(random_password.admin_password[0].result, var.admin_password)
}

resource "azurerm_mssql_server" "server" {
  name                         = "${var.sql_server_name}-server"
  resource_group_name          = var.resource_group_name
  location                     = var.resource_group_location
  administrator_login          = var.admin_username
  administrator_login_password = local.admin_password
  version                      = "12.0"
}

resource "azurerm_mssql_database" "db" {
  name      = "${var.sql_server_name}-db"
  server_id = azurerm_mssql_server.server.id
}

resource "azurerm_mysql_firewall_rule" "fwr" {
  name                = "home"
  resource_group_name = var.resource_group_name
  server_name         = azurerm_mysql_server.server.name
  start_ip_address    = var.ip_address
  end_ip_address      = var.ip_address
}