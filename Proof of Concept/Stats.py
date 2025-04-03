import pandas as pd
import os



current_dir1 = os.getcwd()
file_path = os.path.join(current_dir1,'IssuerData.cvs')

# Read the DataFrame from a CSV file
df1 = pd.read_csv(file_path)

L1=40-len(df1)

print(f"The number clients who received the first half is {L1}")

current_dir2 = os.getcwd()
file_path2 = os.path.join(current_dir2,'PSData.cvs')
# Read the DataFrame from a CSV file
df2 = pd.read_csv(file_path2)
L2=40-len(df2)
print(f"The number clients (with valid first half) who visited the shop is {L2}")