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

# def get_latest_entry():
#     get last entry from our returned mongo objects list

#     client = pymongo.MongoClient(cfg.mongo_link)
#     db = client[cfg.db_name]
#     mycol = db[cfg.col_name]
#     return [mycol.find().sort({"_id":-1}).limit(1)]
