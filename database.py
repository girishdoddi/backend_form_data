import pymongo


class Database:
    def database_response(self):
        client = pymongo.MongoClient("mongodb+srv://girish:7416252855aA@formdatadb.pu2acf3.mongodb.net/?retryWrites=true&w=majority")
        db = client["myDb"]
        return db