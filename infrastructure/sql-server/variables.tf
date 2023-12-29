variable "resource_group_location" {
  type        = string
  default     = "westus"
  description = "Location of the resource group."
}

variable "resource_group_name" {
  type        = string
  description = "Name of the resource group."
}

variable "sql_server_name" {
  type        = string
  description = "The name of the SQL Database."
}

variable "sql_db_name" {
  type        = string
  description = "The name of the SQL Database."
}

variable "admin_username" {
  type        = string
  description = "The administrator username of the SQL logical server."
  default     = "azureadmin"
}

variable "admin_password" {
  type        = string
  description = "The administrator password of the SQL logical server."
  sensitive   = true
  default     = null
}

variable "ip_address" {
  type        = string
  description = "The ip address to allow on the server firewall"
  sensitive   = true
  default     = null
}