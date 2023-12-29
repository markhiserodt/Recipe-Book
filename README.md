# Recipe Book

A collection of fantastic recipes!

Development Stack

1. Client (UI) - Angular
2. Server (Backend) - Django, Django Rest Framework
3. Database - Azure SQL Server
4. Host - Azure App Service
5. Container - Docker image on Azure Container Registry

Infrastructure (DB, Host, Container) created using Terraform

## Client

Navigate to the `/client` folder and run `npm i` then `ng serve`. The client will be running on `http://localhost:4200`. All outbound requests going to `http://localhost:4200/api/*` will be proxied to port `8000` (the server)

## Server

Navigate to the `/server` folder and run `python manage.py runserver`. The server will be running on `http://localhost:8000`

## Infrastructure

To set up the cloud infrastructure for a given environment `<env>`, navigate to the `/infrastructure` folder. Set the variables for the `<env>` in a `<env>.tfvars` file. Then run

1. `az login`
2. `terraform init`
3. `terraform plan -out <env>.tfplan -var-file <env>.tfvars`
4. `terraform apply <env>.tfplan`

To set up the docker image navigate to navigate to the `/infrastructure` folder and run 

1. `docker-compose up <app name>`