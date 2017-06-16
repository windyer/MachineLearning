import redis

import pymongo
#20429403
r = redis.Redis(host='localhost', port=13380,db=2)
client = pymongo.MongoClient(host = 'localhost', port = 13377)
mongodb = client['card']
dates=['2017_04_24','2017_04_25','2017_04_26','2017_04_27']
for i in dates:
    coll = mongodb["charge_statistics_" + i]
    result = coll.find()
    users={}
    for j in result:

        if j['user_id'] in users.keys():
            users[j['user_id']] = users[j['user_id']] +j['price']
        else:
            users[j['user_id']] = j['price']
        print users
    for user in users.keys():
        table = 'DailyStatisticItem:{0}:{1}:Model_Counter'.format(i.replace('_','-'), user)
        r.hset(table, "_charge_money", users[user])