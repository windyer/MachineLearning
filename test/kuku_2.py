import re
import pymongo
lobby_log = "3"
game_log = "game1.log.2017-02-13"
client = pymongo.MongoClient(host='127.0.0.1', port=13377)
date = "2017_02_12"
mongodb = client['card']
user_list=[]
with open(lobby_log) as file:
    print "~~~~~~~~~~~~~~~~~~start lobby"
    coll = mongodb["player_login_" + date]

    for line in file:
        if "[view|TurnerBegin]" in line and "'currency" in line:
            user = re.findall(r"\[user\|(.+?)\]", line)
            delta = re.findall(r"currency':(.+?)}", line)
            #log = "{0} player({1}) buy item_id({2}) residue currency {3} ".format(
                #line[1:20], user[0], item_id[0], currency[0])
            print user[0]
            print delta[0]
            if "L" in user[0]:
                result = coll.find({'user_id': int(user[0][:-1])})
            else:
                result = coll.find({'user_id': int(user[0])})
           # print result
            for i in result:
                if i["channel"] == 'daiji_kuku':
                    user_list.append(user)
                    print user+"      "+i["channel"]   +'    '+delta[0]+"     "+i["login_ip"]
for i in user_list:
    print i.replace("L","")