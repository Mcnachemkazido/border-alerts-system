from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
USER=os.getenv("MONGO_USER")
PASS=os.getenv("MONGO_PASS")
HOST=os.getenv("MONGO_HOST")
PORT=os.getenv("MONGO_PORT")
URI = f"mongodb://{USER}:{PASS}@{HOST}:{PORT}"


def get_mongo_coll(uri):
    client = MongoClient(uri)
    db = client['analysis']
    coll = db['cameras']
    return coll



mongo_coll = get_mongo_coll(URI)



