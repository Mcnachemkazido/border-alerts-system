import json


def return_json_data():
    with open('data/border_alerts.json', 'r') as file:
        data = json.load(file)
        return data



def adding_and_sending_to_redis(data,conn_redis):
    for d in data:
        if d['weapons_count'] > 0 or d['distance_from_fence_m'] <= 50\
        or d['people_count'] >= 8 or d['vehicle_type'] == 'truck'\
        or (d['distance_from_fence_m'] <= 150 and d['people_count'] >= 4)\
        or (d['vehicle_type'] == 'jeep' and  d['people_count'] >= 3 ):
            d['priority'] = 'URGENT'
            conn_redis.lpush('urgent_queue', json.dumps(d))
        else:
            d['priority'] = 'NORMAL'
            conn_redis.lpush('normal_queue', json.dumps(d))






