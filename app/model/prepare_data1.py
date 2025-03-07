# Save as explore.py
import pandas as pd

# Load the CSV (replace with your file name)
file_path = "/home/aswin/Learning/SmartEmailAgent/SmartEMail-AI-Agent/app/data/Bitext_Sample_Customer_Service_Testing_Dataset.csv"
# print(data.columns)  # Lists column names

# df= data.drop(columns =['tags'])
# df.drop_duplicates(inplace=True)
# print(df.head())

def prepare_data(file_path):
    data = pd.read_csv(file_path)
    return data
data = prepare_data(file_path)
# print(data.head())  # Shows first 5 rows
# print(data.columns)  # Lists column names

# df= data.drop(columns =['tags'])
# df.drop_duplicates(inplace=True)
# print(df.head())


