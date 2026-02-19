from redis_connection import conn_redis
from priority_logic import return_json_data ,adding_and_sending_to_redis


adding_and_sending_to_redis(return_json_data(),conn_redis)
print("Data successfully sent to Redis")