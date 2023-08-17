# tools-onedrive

Please make sure to replace 'CLIENT_ID', 'CLIENT_SECRET', and 'FILE_PATH' with the actual environment variable names that you'll be using to pass these values to the script when running the Docker container.



docker run -e CLIENT_ID="your_client_id" \
           -e CLIENT_SECRET="your_client_secret" \
           -e FILE_PATH="/app/path_to_your_file.txt" \
           onedrive-upload-container
