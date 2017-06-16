import time
import re
import os

def info(t):
    with open('luck.txt.'+t) as file:
        total=0
        fp = open("luck.info."+t, "w")

        date_l=[]
        currency_l=[]
        for line in file:
            date = line[1:24]
            print date
            random_currency = re.findall(r"'delta': (.+?)L", line)
            if len(random_currency) >0 and "".join(random_currency) !="0":
                currency_l.append(random_currency[0])
            try:
                date_s=time.mktime(time.strptime(date[:-4], '%Y-%m-%d %H:%M:%S'))
            except:
                pass
            date_l.append(date_s)
            start_time=date_l[0]
            if float(date_s) > float(start_time)+20:
                fp.write("start_time : "+str(start_time)+ "\n")
                fp.write("currency : "+str(currency_l) + "\n")
                fp.write("currency_total : "+str(sum(int(i) for i in currency_l)) + "\n")
                fp.write("luck_count : "+str(len(currency_l))+ "\n")
                print "start_time : ", start_time
                print "currency : ",currency_l

                print "currency_total : ",sum(int(i) for i in currency_l)
                total += sum(int(i) for i in currency_l)
                print "luck_count : ",len(currency_l)
                start_time = date_s
                end_time = date_l[-2]
                date_l = []
                currency_l=[]
                fp.write("end_time : "+str(end_time) + "\n")
                fp.write("-"*100+ "\n")
                print "end_time  :", end_time
                print "-"*100
        fp.write("\ntotal : " + str(total) + "\n")
        fp.close()
date=["2017-12-31","2017-01-01","2017-01-02","2017-01-03","2017-01-04"]
for i in date:
    cmd = '''cat lobby.log.{0} | grep "'reason': 'luck_bag'" > luck.txt.{1}'''.format(i,i)
    os.system(cmd)
    info(i)

