variable "app_name" {
  type        = string
  description = "Name of the app to prefix all resources with."
}

variable "ip_address" {
  type        = string
  description = "The ip address to allow on the server firewall"
  sensitive   = true
  default     = "0"
}