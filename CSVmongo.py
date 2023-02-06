
import pymongo # importing the python-mongoDB connector library

connection_url = "mongodb+srv://pilpiddu:s1FiE3EP6NYJXKP4@cluster0.khyvpbl.mongodb.net/?retryWrites=true&w=majority" # This is the general link for connecting to the local device.

client = pymongo.MongoClient(connection_url) 

database=client["OCR"] #Connecting to existing Sales database or creating a new Sales database
collection=database["records"] #connecting to the product collection in the Sales database

import csv
with open("records.csv","r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    collection.insert_many(data)

