import os
import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday2 = today - datetime.timedelta(days=2)
yesterday3 = today - datetime.timedelta(days=3)
date=[yesterday,yesterday2,yesterday3]
for day in date:
    in_file = "game1.log."+str(day)
    out_file = "game_chat_"+str(day)
    command = "grep 'text|' "+in_file+' > tem_chat'
    print command
    os.system(command)
    with open('tem_chat','r') as inf, open(out_file,'w') as outf:
        for line in inf:
            s=line[61:].replace('chat','')
            outf.write(s)
    print "from tem_chat write in "+ out_file
    os.system('rm tem_chat')
    print "delete tem_chat "