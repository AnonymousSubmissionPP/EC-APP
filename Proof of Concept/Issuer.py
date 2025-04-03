import socket
import pickle
import base64
import pandas as pd
import time

import qrcode
import os
import random
from Ecoupon import find_value_in_column
from Ecoupon import double_hash
import hashlib

import time




## Socket communication


  
IP_ADDRESS = '127.0.0.1'
PORT1 = 8081
PORT2 = 8082
# Create the server sockets
server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket1.bind((IP_ADDRESS, PORT1))
server_socket1.listen()
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket2.bind((IP_ADDRESS, PORT2))
server_socket2.listen()




# Accept the connection with client
client_socket1, address1 = server_socket1.accept()
print(f"Connection established with client, e-coupon request from address {address1}")

# Send first half to client
#Timer
start_time1=time.time()


current_dir = os.getcwd()
file_path = os.path.join(current_dir,'IssuerData.cvs')

# Read the DataFrame from a CSV file
df1 = pd.read_csv(file_path)
# Pick a random row
random_row = df1.sample(n=1)
# Store the first/second half
FHalf=random_row['First Half'].values[0]
SHalf=random_row['Second Half'].values[0]
# Remove the random row from the DataFrame
df = df1.drop(index=random_row.index)
df.to_csv(file_path, index=False)



#Send the first half
Cmessage = pickle.dumps(FHalf)

client_socket1.send(Cmessage)

end_time1=time.time()
total_time1 = end_time1 - start_time1
total_timef1=round(total_time1, 4)

print(f"Issuer sent the first half to client is {FHalf}")
print("Total time taken to send the first half to Alice :", total_timef1, "s")




# Accept the connection with Shop
client_socket2, address2 = server_socket2.accept()
print(f"Connection established with shop proximity service, waiting for second half from address {address2}")




# Receive first half from shop (proximity service)



rFhalf = client_socket2.recv(6048)
recFhalf=pickle.loads(rFhalf)
recFhalf=int(recFhalf)

#Timer
start_time2=time.time()
# Read the DataFrame from the CSV file and search for the corresponding second half
file_path2 = os.path.join(current_dir,'PSData.cvs')

df2 = pd.read_csv(file_path2)
M=find_value_in_column(df2,recFhalf)


print(f"The received first half from PS for verification is: {recFhalf}")

print(f"The corresponding second half is {M}")





IssRep = pickle.dumps(M)
client_socket2.send(IssRep)


Ecouponf=double_hash(FHalf,M)
#Ecoupon=int(str(Ecouponf)[:4])

finalclient = pickle.dumps(Ecouponf)

client_socket1.send(finalclient)

end_time2=time.time()
total_time2 = end_time2 - start_time2
total_timef2=round(total_time2, 4)







print(f"Issuer sent the final E-coupon to client which is {Ecouponf}")
print("Total time taken to send the Final E-coupon to client:", total_timef2, "s")






# Close the sockets
client_socket1.close()
client_socket2.close()
server_socket1.close()
server_socket2.close()