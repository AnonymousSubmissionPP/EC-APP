import socket
import pickle
import base64
import pandas as pd
import time

import numpy as np
import qrcode
import os
import random

import hashlib




# A function to compute the full coupon from the first and second parts
def double_hash(val1, val2):
    val1_bytes = str(val1).encode()
    val2_bytes = str(val2).encode()
    l1=str(len(val1_bytes)).encode()
    l2=str(len(val2_bytes)).encode()
    
    combined_bytes =l1+ val1_bytes+l2+ val2_bytes
    hash_object = hashlib.sha256()
    hash_object.update(combined_bytes)
    
    hash_value = int(hash_object.hexdigest(), 16)
    
    return hash_value




#A function to check if a given first part is in the database, if yes, return its corresponding second part and delete the row from the database
def find_value_in_column(df,search_value):
    if search_value in df['First Half'].values:
        M=df.loc[df['First Half'] == search_value, 'Second Half'].values[0]
        df= df[df['First Half'] != search_value]
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir,'PSData.cvs')
        df.to_csv(file_path, index=False)
    else:
        M=f"Error: Value {search_value} is not a valid first half."
    return M



def double_hash2(int1, int2):
   
    int1 = int(int1)
    int2 = int(int2)
    
    # Convert to bytes
    int1_bytes = int1.to_bytes((int1.bit_length() + 7) // 8, byteorder='big')
    int2_bytes = int2.to_bytes((int2.bit_length() + 7) // 8, byteorder='big')
    l1_bytes=len(int1_bytes).to_bytes((int1.bit_length() + 7) // 8, byteorder='big')
    l2_bytes=len(int2_bytes).to_bytes((int1.bit_length() + 7) // 8, byteorder='big')
    
    # Concatenate the byte representations
    combined_bytes = l1_bytes+int1_bytes + l2_bytes+int2_bytes
    
    # Hash the combined byte string using SHA-256
    hash_object = hashlib.sha256(combined_bytes)
    
    # Return the hexadecimal digest of the hash
    return hash_object.hexdigest()