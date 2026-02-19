import redis
import json


r = redis.Redis(host='localhost',port=6379,decode_responses=True)

while True:
    if r.llen('urgent_queue') > 0:
        data = r.brpop(['urgent_queue'])
        data = json.loads(data[1])
        print(data)
        print("AAAAAAAAAA")

    else:
        data = r.brpop(['normal_queue'])
        data = json.loads(data[1])
        print(data)
        print("BBBBBBBBBBBBB")
