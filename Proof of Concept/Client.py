import socket
import pickle
import base64
import datetime

import pandas as pd
import time

#Socket communication

# Define the IP address and port number
IP_ADDRESS = '127.0.0.1'
PORT = 8081

# Create channel with Issuer
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP_ADDRESS, PORT))


# Receive first half from issuer
Fhalf = client_socket.recv(6048)
Firsthalf=pickle.loads(Fhalf)
Firsthalf=int(Firsthalf)
def print_decorated_message(message):
    lines = message.split('\n')
    max_length = max(len(line) for line in lines)
    horizontal_border = '+' + '-' * (max_length + 4) + '+'
    empty_line = '|' + ' ' * (max_length + 4) + '|'

    print(horizontal_border)
    print(empty_line)
    for line in lines:
        print('|  ' + line + ' ' * (max_length - len(line)) + '  |')
    print(empty_line)
    print(horizontal_border)




print_decorated_message(f"The e-coupon first half is {Firsthalf}.\n Go the AmazingShoes shop in the second floor for the second half")




# Receive first half from issuer
finalcoupon = client_socket.recv(6048)
Ecoupon=pickle.loads(finalcoupon)



################################################################

import tkinter as tk
import qrcode
import os

from IPython.display import Image as IPImage
# Generate QR code and save it in file path
def generate_qr_code(data, file_path):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
 
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    
    img.save(file_path)
    


# Get the current working directory
current_dir = os.getcwd()
file_path = os.path.join(current_dir, "QR_code.png")
generate_qr_code(Ecoupon, file_path)


    
    

win = tk.Tk()
win.geometry("750x450")

photo = tk.PhotoImage(file='QR_code.png')
image = tk.Label(win, image=photo)
image.pack()

win.mainloop()





# Close the socket
client_socket.close()
