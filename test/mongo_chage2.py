# -*- coding:utf-8 -*-
import pymongo
import datetime
import time


client = pymongo.MongoClient(host = 'localhost', port = 13377)
card = client['card']
#coll = card['daily_summary']

begin = datetime.datetime(2017, 3, 17, 0, 0, 0, 0).date()
end = datetime.datetime(2017, 3, 19, 0, 0, 0, 0).date()

datas = {}
"""
field_infos = {'dnu':u'新增用户(人)',
          'dlu':u'登录用户(人)',
          'dau':u'活跃用户(登录-新增)(人)',
          'dcu':u'充值用户(人)',
          'dcr':u'充值金额(元)',
          'dncu':u'新充值用户(人)',
          'dncr':u'新玩家充值金额(元)',
          'aucr':u'活跃玩家付费率(%)',
          'rr2':u'次日留存',
          }
"""
field_infos = {'dnu':u'新增用户(人)',
          'dlu':u'登录用户(人)',
          'dau':u'活跃用户(登录-新增)(人)',
          'dcu':u'充值用户(人)',
          'dcr':u'充值金额(元)',
          'dncu':u'新充值用户(人)',
          'dncr':u'新玩家充值金额(元)',
          'aucr':u'活跃玩家付费率(%)',
          'rr2':u'次日留存',
          'arpnu':u'新玩家人均充值(元)',
          'arppu':u'付费玩家人均充值(元)',
          'arpau':u'活跃玩家人均充值(元)',
          }
total_fields = ['dnu', 'dncu', 'aucr', 'rr2']
#fields = ['dnu', 'dcr', ]
fields = ['dnu', 'dlu', 'dau', 'dcu', 'dcr', 'dncu', 'dncr', 'aucr', 'arpnu', 'arppu', 'arpau', ]

start = begin
f = open("user_sj05", "w+")
while start < end:
    day = start.strftime("_%Y_%m_%d")
    print day
    coll = card['player_register' + day]
    #coll2 = card['player_register' + day]
    start += datetime.timedelta(days=1)
    result = coll.find({"channel":'lenovo_duowan'})
    ip_list =[]
    for doc in result:
        c = doc['channel']
        user = doc['user_id']
        ip = doc['login_ip']
        print user,ip
        ip_list.append(ip)
        #f.write(str(user)+'\n')

        #result2 = coll2.find({"user_id": user})
        #for doc2 in result2:
        #    c2 = doc2['channel']
        #    user2 = doc2['user_id']
    a=0
    for i in ip_list:
        print ip_list.count(i)
        if ip_list.count(i) > 1 :
            a+=1
    print "aaaa"*100,len(ip_list),a
f.close()