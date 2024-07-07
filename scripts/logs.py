from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Azure Storage Account details
storage_account_name = 'myappdatastorage'
storage_account_key = '//your own key'

# Local directory path where log files are located
local_directory_path = '/home/azureuser/myapp/logs'

# Initialize BlobServiceClient using account name and account key (or SAS token)
blob_service_client = BlobServiceClient(
    account_url=f"https://myappdatastorage.blob.core.windows.net",
    credential=storage_account_key
)

# Create a BlobServiceClient to interact with the Blob service
container_name = 'logs'  # Replace with your container name
container_client = blob_service_client.get_container_client(container_name)

# Upload log files from local directory to Azure Blob Storage
for root, dirs, files in os.walk(local_directory_path):
    for file_name in files:
        local_file_path = os.path.join(root, file_name)
        blob_client = container_client.get_blob_client(os.path.relpath(local_file_path, local_directory_path))
        
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded {file_name} to {container_name} container.")


