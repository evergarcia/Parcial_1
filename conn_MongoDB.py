import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/");
db = cliente['Libros_db']

collections = db['books']

#++++++++++++++++