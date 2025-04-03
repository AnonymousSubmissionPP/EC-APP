import socket
import pickle
import base64
import random
import numpy as np
import pandas as pd
import json
import math
import qrcode
import os
import time



# Generate QR code and save it in file path
def generate_qr_code(data, file_path):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(file_path)
    print(f"QR code generated and saved to {file_path}")



current_dir = os.getcwd()
file_path = os.path.join(current_dir, "QR_code.png")



#Socket communication

# Create channel with the issuer
IP_ADDRESS = '127.0.0.1'
PORT = 8082
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))




import tkinter as tk
from tkinter import messagebox

def send_message():
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message to send.")
        return

    try:
        # Send a message
        Smessage = pickle.dumps(message)
        client_socket.send(Smessage)
        

        # Receive response from the server
        rFhalf = client_socket.recv(6048)
        response=pickle.loads(rFhalf)

        # Display the server response in the label
        response_label.config(text=f"Server response: {response}")

    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

# Set up the Tkinter window
root = tk.Tk()
root.title("AmazingShoes")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter E-coupon 1st half:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

send_button = tk.Button(frame, text="Accept", command=send_message)
send_button.pack(side=tk.LEFT)

response_label = tk.Label(root, text="50% discount on all items")
response_label.pack(pady=20)

root.mainloop()




# Close the socket
client_socket.close()
#client_socket3.close()
#server_socket3.close()

