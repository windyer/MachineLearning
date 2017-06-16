import re
lobby_log = '1'
with open(lobby_log) as file:
    print "~~~~~~~~~~~~~~~~~~start"
    key_list = []
    for line in file:
        #if "lobby.PurchaseItem:27" in line and user_id in line:
            reason = re.findall(r"'reason': '(.+?)',", line)
            #delta = re.findall(r"delta': (.+?)}", line)
            #time = re.findall(r"\[2017(.+?)\]", line)
            #log = "{0} player({1}) buy item_id({2}) residue currency {3} ".format(
                #line[1:20], user[0], item_id[0], currency[0])
           # print user[0]
            print reason
            key_list.append(reason[0])
print key_list