from mongo_connection import mongo_coll


def alerts_by_border_and_priority(coll):
    pipline_1 =  {"$group": {"_id":["$border","$priority"],"sum":{"$sum":"$priority"},
                             "total_events":{"$sum":1}}}
    res = mongo_coll.aggregate([pipline_1])
    return list(res)