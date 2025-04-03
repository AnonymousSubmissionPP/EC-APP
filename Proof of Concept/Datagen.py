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


import time

# Define the double hash function
def double_hash(int1, int2):
   
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

# Create DATA

#Timer
start_time=time.time()


num_rows = 40 # Number of E-Coupons (agreed between shop and issuer)
data = {
    'First Half': np.random.randint(0, 2**32, size=num_rows),
    'Second Half': np.random.randint(0, 2**32, size=num_rows)
}
df = pd.DataFrame(data)

# Apply the double hash function to each row
df["E-coupon"] = df.apply(lambda row: double_hash(row['First Half'], row['Second Half']), axis=1)





def hash_hex_string(hex_string):
    # Convert the hex string to bytes
    hex_bytes = bytes.fromhex(hex_string)
    
    # Hash the byte representation using SHA-256
    hash_object = hashlib.sha256(hex_bytes)
    
    # Return the hexadecimal digest of the hash
    return hash_object.hexdigest()

df["E-coupon Hash"] = df.apply(lambda row: hash_hex_string(row["E-coupon"]), axis=1)








df1 = df["E-coupon Hash"]
C1=['First Half','Second Half',"E-coupon"]
df=df[C1]
C2=['First Half','Second Half']
df2 = df[C2]


# Create the Issuer Data Base
current_dir = os.getcwd()
file_path = os.path.join(current_dir,'IssuerData.cvs')
df.to_csv(file_path, index=False)

# Create the Shop Data Base
file_path1 = os.path.join(current_dir,'ShopData.cvs')
df1.to_csv(file_path1, index=False)

# Create the Proximity Service Data Base
file_path2 = os.path.join(current_dir,'PSData.cvs')
df2.to_csv(file_path2, index=False)

end_time=time.time()
total_time = end_time - start_time
total_timef=round(total_time, 4)
print("Total time taken to generate the data :", total_timef, "s")