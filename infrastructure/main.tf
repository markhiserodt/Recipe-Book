module "resource_group" {
  source = "./resource-group"

  resource_group_name = var.app_name
}

module "sql_server" {
  source = "./sql-server"

  resource_group_name = module.resource_group.resource_group_name
  sql_server_name = var.app_name
  sql_db_name = var.app_name
  ip_address = var.ip_address
}

module "container_registry" {
  source = "./container-registry"

  resource_group_name = module.resource_group.resource_group_name
  container_registry_name = var.app_name
}

module "app_service" {
  source = "./app-service"

  resource_group_name = module.resource_group.resource_group_name
  service_plan_name = var.app_name
  app_service_name = var.app_name
}
