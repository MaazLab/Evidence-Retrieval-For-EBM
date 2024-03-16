import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["thesis"]
collection = db['data']

def get_abstract():
    return [abstract['abstract'] for abstract in collection.find({},{'_id': 0, 'abstract':1})]

def find_from_abstract(doc_list):
    result = []
    for doc in doc_list:
        query = {"abstract": {"$exists": True, "$eq": doc}}
        result.append(collection.find(query)[0])
    return result