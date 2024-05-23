'''import os

# Specify the path where you want to create the folder
folder_path = './RidirectUrl/satyam'

# Use os.makedirs() to create the folder along with any necessary parent folders
os.makedirs(folder_path)

# Check if the folder was created
if os.path.exists(folder_path):
    print("Folder created successfully!")
else:
    print("Failed to create folder.")'''


'''
from pathlib import Path

# Specify the path where you want to create the folder
folder_path = Path("./RidirectUrl/Satyamm")

# Use .mkdir() to create the folder
folder_path.mkdir(parents=True, exist_ok=True)

# Check if the folder was created
if not folder_path.exists():
    print("Folder created successfully!")
else:
    print("Failed to create folder.")'''


import qrcode

def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    
    # Add data to the QR code
    qr.add_data(data)
    
    # Make the QR code
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(f'./RidirectUrl/{file_name}.png')

generate_qr_code('https://googleb.com','10')

