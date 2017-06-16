import re
import pymongo
import os
import datetime
d=datetime.datetime.strptime('2017-02-06','%Y-%m-%d')
for i in range(2):
    d2 = d+ datetime.timedelta(days=i)
    date = str(d2.date())
    cmd1 = 'tar -zxvf ../../lobby.log.{0}.tar.gz'.format(date)
    print cmd1
    os.system(cmd1)
    cmd2='grep inviter_id mnt/log/lobby.log.{0} > invite.{1}'.format(date,date)
    print cmd2
    os.system(cmd2)
    print 'ok!'
    log = "invite.{0}".format(date)


    output = open('invite.text', 'a')
    output2 = open('invite.text.'+date, 'w')
    with open(log) as file:
        print "~~~~~~~~~~~~~~~~~~start lobby"
        for line in file:
            #if "lobby.PurchaseItem:27" in line and user_id in line:
            user_id = re.findall(r"user_id': (.+?),", line)
            inviter_id = re.findall(r"inviter_id': (.+?)}", line)
                #log = "{0} player({1}) buy item_id({2}) residue currency {3} ".format(
                    #line[1:20], user[0], item_id[0], currency[0])
               # print user[0]
            try:
                user = user_id[0]
                inviter = inviter_id[0]
                if 'u'in user_id[0]:
                    user = user_id[0][1:]
                if 'u' in inviter_id[0]:
                    inviter = inviter_id[0][1:]
                print int(user), int(inviter)
                user_list = [int(user),int(inviter)]
                output.write(str(user_list))
                output2.write(str(user_list))
                #set_inviter(int(user),int(inviter))
            except:
                pass
    output.close()
    cmd3='rm mnt/log/lobby.log.{0}'.format(date)
    print cmd3
    os.system(cmd3)
    os.system(cmd3)