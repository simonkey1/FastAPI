from pymongo import MongoClient


# bbdd local


# db_client = MongoClient().local

## remota 

db_client = MongoClient("mongodb+srv://test:acidosa123@cluster0.2v0keei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test


