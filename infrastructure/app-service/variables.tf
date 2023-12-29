variable "resource_group_location" {
  type        = string
  default     = "westus"
  description = "Location of the resource group."
}

variable "resource_group_name" {
  type        = string
  description = "Name of the resource group."
}

variable "service_plan_name" {
  type        = string
  description = "Name of the service plan."
}

variable "app_service_name" {
  type        = string
  description = "Name of the app service."
}

variable "dns_prefix" {
  type        = string
  description = "A prefix for any dns based resources"
  default     = "tfq"
}

variable "plan_tier" {
  type        = string
  description = "The tier of app service plan to create"
  default     = "Standard"
}

variable "plan_sku" {
  type        = string
  description = "The sku of app service plan to create"
  default     = "S1"
}

variable "environment" {
  type        = string
  description = "Name of the deployment environment"
  default     = "dev"
}

variable "virtual_network_subnet_id" {
  type        = string
  description = "Id of the virtual network subnet to attach this service to."
  default     = null
}