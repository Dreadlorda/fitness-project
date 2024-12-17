
#!/bin/bash

# Azure deployment script
# Log in to Azure
az login

# Set variables
RESOURCE_GROUP="FitnessResourceGroup"
APP_NAME="fitness-tracker-app"
PLAN_NAME="FitnessPlan"
LOCATION="EastUS"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create App Service Plan
az appservice plan create --name $PLAN_NAME --resource-group $RESOURCE_GROUP --sku B1 --is-linux

# Deploy App
az webapp create --resource-group $RESOURCE_GROUP --plan $PLAN_NAME --name $APP_NAME --deployment-container-image-name <your-docker-image>

# Set environment variables
az webapp config appsettings set --name $APP_NAME --resource-group $RESOURCE_GROUP --settings     DJANGO_SECRET_KEY="<your-secret-key>"     ALLOWED_HOSTS="fitness-tracker-app.azurewebsites.net"     DATABASE_URL="postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"

echo "Deployment complete. Visit: https://$APP_NAME.azurewebsites.net"
