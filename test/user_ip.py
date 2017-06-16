import pymongo
import time
client = pymongo.MongoClient(host='localhost', port=13377)
mongodb = client['card']

def user_ip(date,user_id):
    info2 = []
    date = date.replace("-", "_")
    coll = mongodb["player_login_" + date]
    result = coll.find({'user_id': user_id})
    user_info = []
    total = 0
    for i in result:
        user={}
        x = time.localtime(i['timestamp'] / 1000)
        user['time'] = time.strftime('%Y-%m-%d %H:%M:%S', x)
        user['ip'] = i['login_ip']

        if len(user_info)>1 and user['ip'] != user_info[-1]["ip"]:
            print "{0} ip change {1} in {2}".format(user_id,user['ip'],user['time'])
        user_info.append(user)
    print user_info
with open('user_list') as file:
    for line in file:
        user_ip('2017-01-05',int(line))