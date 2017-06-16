import re
import pymongo
lobby_log = "3"
game_log = "game1.log.2017-02-13"
client = pymongo.MongoClient(host='127.0.0.1', port=13377)
date = "2017_02_12"
mongodb = client['card']
user_list={}
with open(lobby_log) as file:
    print "~~~~~~~~~~~~~~~~~~start lobby"
    coll = mongodb["player_login_" + date]

    for line in file:
        #if "lobby.PurchaseItem:27" in line and user_id in line:
            user = re.findall(r"user_id': (.+?),", line)
            delta = re.findall(r"delta': (.+?)}", line)
            time = re.findall(r"\[2017(.+?)\]", line)
            #log = "{0} player({1}) buy item_id({2}) residue currency {3} ".format(
                #line[1:20], user[0], item_id[0], currency[0])
           # print user[0]
            if "L" in user[0]:
                result = coll.find({'user_id': int(user[0][:-1])})
            else:
                result = coll.find({'user_id': int(user[0])})
           # print result
            for i in result:
                if i["channel"] == 'daiji_kuku' and int(delta[0])>100000:
                    user_list[user[0]] = "[2017"+time[0]
                    print user[0]+"      "+i["channel"]   +'    '+delta[0]+"     "+i["login_ip"]
for i in user_list.keys():
    print i.replace("L","")
user_list2=[]
with open(game_log) as file:
    print "~~~~~~~~~~~~~~~~~~start game"
    #coll = mongodb["player_login_" + date]
    for line in file:
        if "round_begin_trace" in line :
            for i in user_list.keys():
                if i.replace("L","") in line:
                    user = re.findall(r"users\|\[(.+?)\]", line)
                    if len(user)>0:
                        for u in user[0].split(","):
                                user_list2.append(u)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~user2"
    print user_list2
user_list3=[]
for i in user_list2:
    l2 = 0
    l = len(i)
    for u in i:
        if u in user_list.keys():
            l2=l2+1
    if l2 == l-1:
        user_list3.append(i)
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~user3"
print user_list3