# import gdown

# # File ID from Google Drive link
# file_id = 'your_file_id_here'

# # Construct the download URL
# download_url = f"https://drive.google.com/uc?id={file_id}"

# # Path to save the file
# output_path = 'downloaded_file.ext'

# # Download the file
# gdown.download(download_url, output_path, quiet=False)

# print(f"File downloaded to {output_path}")

# import gdown
# import os
# try:
#     file_id = '1i9CKtqXW3nnCtcwdW8g3XCtNzkKNzPqc'
#     download_url = f"https://drive.google.com/uc?id={file_id}"
    
#     # Save to a different path where you have permissions
#     output_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'myfile.pdf')
#     gdown.download(download_url, output_path, quiet=False)

#     print(f"File downloaded to {output_path}")
# except:
#     print('invalid path')    


# import requests

# file_id = '1i9CKtqXW3nnCtcwdW8g3XCtNzkKNzPqc'
# download_url = f"https://drive.google.com/uc?id={file_id}"

# response = requests.get(download_url, stream=True)

# output_path = 'myfile.pdf'
# with open(output_path, 'wb') as file:
#     for chunk in response.iter_content(chunk_size=8192):
#         file.write(chunk)

# print(f"File downloaded to {output_path}")



# import requests

# file_id = '1i9CKtqXW3nnCtcwdW8g3XCtNzkKNzPqc'
# download_url = f"https://drive.google.com/uc?id={file_id}"

# response = requests.get(download_url, stream=True)

# # Specify the absolute path to save the file
# output_path = 'D:\\sami work\\myfile.pdf'

# with open(output_path, 'wb') as file:
#     for chunk in response.iter_content(chunk_size=8192):
#         file.write(chunk)

# print(f"File downloaded to {output_path}")



# import requests
# import os

# file_id = '1cRimwqcaAOtTx92SPXspmc3fxRCfMZja'
# download_url = f"https://drive.google.com/uc?id={file_id}"

# # Ensure the directory exists
# directory = 'D:/sami work'
# if not os.path.exists(directory):
#     os.makedirs(directory)

# output_path = os.path.join(directory, 'myyfile.pdf')

# # Download the file
# try:
#     response = requests.get(download_url, stream=True)
#     response.raise_for_status()  # Check for HTTP errors

#     # Write the file to disk
#     with open(output_path, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)
    
#     print(f"File downloaded to {output_path}")

# except requests.exceptions.RequestException as e:
#     print(f"Error downloading file: {e}")




# import requests
# import os

# file_id = '1cRimwqcaAOtTx92SPXspmc3fxRCfMZja'
# confirm = 't'  # This might be needed for large files to bypass the virus scan warning
# download_url = f"https://drive.google.com/uc?id={file_id}&confirm={confirm}"

# # Ensure the directory exists
# directory = 'D:/sami work'
# if not os.path.exists(directory):
#     os.makedirs(directory)

# output_path = os.path.join(directory, 'myfile.pdf')

# # Download the file
# try:
#     response = requests.get(download_url, stream=True)
#     response.raise_for_status()  # Check for HTTP errors

#     # Write the file to disk
#     with open(output_path, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=8192):
#             file.write(chunk)

#     print(f"File downloaded to {output_path}")

# except requests.exceptions.RequestException as e:
#     print(f"Error downloading file: {e}")


import requests
import os

file_id = 'enter your file id here '
confirm = 't'
download_url = f"https://drive.google.com/uc?id={file_id}&confirm={confirm}"

# Ensure the directory exists
directory = 'enter your full path where you want to download the file'
if not os.path.exists(directory):
    os.makedirs(directory)

output_path = os.path.join(directory, 'mfile.pdf')

# Download the file
try:
    response = requests.get(download_url, stream=True, allow_redirects=True)
    response.raise_for_status()

    # Write the file to disk
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print(f"File downloaded to {output_path}")

except requests.exceptions.RequestException as e:
    print(f"Error downloading file: {e}")
