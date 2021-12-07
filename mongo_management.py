import pymongo
import cfg


def insert_into_db(data):
    client = pymongo.MongoClient(cfg.mongo_link)
    db = client[cfg.db_name]
    mycol = db[cfg.col_name]
    mycol.insert_one(data)
    client.close()


def get_all_data():
    client = pymongo.MongoClient(cfg.mongo_link)
    db = client[cfg.db_name]
    mycol = db[cfg.col_name]
    list = []

    for x in mycol.find({}, {"_id": 0}):
        list.append(x)
    client.close()
    return list