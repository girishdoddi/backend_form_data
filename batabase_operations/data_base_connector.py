import pymongo

client = pymongo.MongoClient("mongodb+srv://girish:7416252855aA@formdatadb.pu2acf3.mongodb.net/?retryWrites=true&w=majority")
db = client["myDb"]
collection = db["form_data"]
data = collection.find({}, {"_id" : 0})
for resp in data:
    print(resp)