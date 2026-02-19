from fastapi import APIRouter
from mongo_connection import mongo_coll
from redis_connection import conn_redis
import dal
import json

route = APIRouter()


@route.get("/analytics/alerts-by-border-and-priority")
def alerts_by_border_and_priority():
    if conn_redis.get('alerts-by-border-and-priority') is not None:
        result = json.loads(conn_redis.get('alerts-by-border-and-priority'))
        print("cash hit",conn_redis.ttl('alerts-by-border-and-priority'))
    else:
        result =  list(dal.alerts_by_border_and_priority(mongo_coll))
        conn_redis.setex('alerts-by-border-and-priority',1000,json.dumps(result))
        print("cash miss")

    return result


