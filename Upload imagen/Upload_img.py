from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import config
# Enter credentials
account_name = config.account_name
account_key = config.account_key
container_name = config.container_name

# Create a client to interact with blob storage
connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Use the client to connect to the container
container_client = blob_service_client.get_container_client(container_name)

# Path to the file you want to upload
file_path = "asistente.jpg"
blob_name = "asistente"  # Name to be given to the blob in the container

# Upload the file to the container
with open(file_path, "rb") as data:
    #container_client.upload_blob(name=blob_name, data=data)
    container_client.upload_blob(name=blob_name, data=data , overwrite=True) # overwrite in container

print("Finish")