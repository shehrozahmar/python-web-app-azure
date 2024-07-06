#!/bin/bash

RESOURCE_GROUP="ResourceGroup"
LOCATION="eastus"

# Create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Deploy Vnet
az deployment group create --resource-group $RESOURCE_GROUP --template-file /Users/admin/Desktop/az/Python-webapp/python-web-app-azure/templates/vnet-template.json

# Deploy web NSG
az deployment group create --resource-group $RESOURCE_GROUP --template-file /Users/admin/Desktop/az/Python-webapp/python-web-app-azure/templates/nsg-web.json

# Deploy db NSG
az deployment group create --resource-group $RESOURCE_GROUP --template-file /Users/admin/Desktop/az/Python-webapp/python-web-app-azure/templates/nsg-db.json
# Deployment of virtual machine 

az deployment group create --resource-group $RESOURCE_GROUP --template-file /Users/admin/Desktop/az/Python-webapp/python-web-app-azure/templates/vm-template.json

#Deploy storage account

az deployment group create --resource-group $RESOURCE_GROUP --template-file /Users/admin/Desktop/az/Python-webapp/python-web-app-azure/templates/storage-template.json