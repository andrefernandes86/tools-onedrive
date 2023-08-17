import os
from onedrivesdk import AuthProvider, OneDriveClient

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
file_path = os.environ.get('FILE_PATH')  # Path to the file you want to upload

# Authenticate with OneDrive
auth_provider = AuthProvider(client_id, scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'])
auth_url = auth_provider.get_auth_url('http://localhost')
code = input(f"Please visit this URL to authenticate: {auth_url}\nPaste the code here: ")
auth_provider.authenticate(code, 'http://localhost', client_secret)

# Initialize OneDrive client
client = OneDriveClient(auth_provider, max_retries=5)

def upload_to_onedrive(file_path):
    with open(file_path, "rb") as f:
        client.item(drive="me", path="/root:/"+os.path.basename(file_path)).upload(f)

# Upload the file to OneDrive
upload_to_onedrive(file_path)
print("Uploaded file to OneDrive")
