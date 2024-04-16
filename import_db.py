import bson
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "test_user"
COLLECTION_NAME = "test_user"
FILE_PATH = "./sample_collection.bson"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

with open(FILE_PATH, "rb") as f:
    bson_data = f.read()
    collection.insert_many(bson.decode_all(bson_data))

print("Данные успешно импортированы в MongoDB.")
