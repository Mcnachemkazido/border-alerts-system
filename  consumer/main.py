from redis_connection import conn_redis
from mongo_connection import mongo_coll
from datetime import datetime
import json


while True:
    if conn_redis.llen('urgent_queue') > 0:
        data = conn_redis.brpop(['urgent_queue'])
        data = json.loads(data[1])
        data['insertion_time'] = datetime.now().isoformat()
        mongo_coll.insert_one(data)

    else:
        data = conn_redis.brpop(['normal_queue'])
        data = json.loads(data[1])
        data['insertion_time'] = datetime.now().isoformat()
        mongo_coll.insert_one(data)
